"""Read-only issue validation and Project field API helpers."""

import collections
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess

ORG = "321Team"

REPO = "321Team/fds-project-baseline"

IDENTITY = {"이권욱": "GWONUK", "이하영": "hayeounglee", "이재환": "supreme33-kr"}

REQUIRED = (
    "Record ID", "Phase", "Category", "Type", "Status", "Priority", "Start", "End",
    "Calendar Days", "Working Days", "Lead", "Support", "Exit Criteria",
    "Related Decision IDs", "Related Risk IDs", "Source", "Schedule Note",
)

STATES = {
    "To Do": ("open", None, "status:to-do"),
    "In Progress": ("open", None, "status:in-progress"),
    "In Review": ("open", None, "status:in-review"),
    "Blocked": ("open", None, "status:blocked"),
    "Done": ("closed", "completed", "status:done"),
    "Cancelled": ("closed", "not_planned", "status:cancelled"),
}

FIELDS = {
    "Record ID": ("TEXT", []),
    "Phase": ("SINGLE_SELECT", ["Design", "Phase 1", "Phase 2"]),
    "Priority": ("SINGLE_SELECT", ["P0", "P1"]),
    "Support": ("TEXT", []),
    "Plan Start": ("DATE", []),
    "Plan End": ("DATE", []),
    "Schedule Note": ("TEXT", []),
}

ITEM_BODY = """
id isArchived
content { ... on Issue { id number url repository { nameWithOwner } } }
fieldValues(first:100) { pageInfo { hasNextPage } nodes {
 ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon { name } } }
 ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } }
 ... on ProjectV2ItemFieldSingleSelectValue { name optionId field { ... on ProjectV2FieldCommon { name } } }
} }
"""

class Stop(RuntimeError):
    pass

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

def redact(value):
    return re.sub(r"(?:gh[pousr]_[A-Za-z0-9_]+|github_pat_[A-Za-z0-9_]+|Bearer\s+\S+)", "[REDACTED]", str(value))

def date_value(value):
    if value.startswith("TBD"):
        return None
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise Stop("확정 ISO 날짜/TBD가 아닌 일정: " + value)
    dt.date.fromisoformat(value)
    return value

def properties(body):
    lines = body.splitlines()
    header = next((i for i, line in enumerate(lines)
                   if re.fullmatch(r"\s*\|\s*Property\s*\|\s*입력값\s*\|\s*", line)), None)
    if header is None:
        raise Stop("본문 상단 Property/입력값 속성표 없음")
    result = {}
    for line in lines[header + 2:]:
        if not line.strip().startswith("|"):
            break
        cells = re.split(r"(?<!\\)\|", line.strip())
        if len(cells) != 4:
            raise Stop("속성표 열 구조 오류")
        key, value = cells[1].strip(), cells[2].strip().replace(r"\|", "|")
        if key in result:
            raise Stop("중복 속성: " + key)
        result[key] = value
    missing = [key for key in REQUIRED if not result.get(key)]
    if missing:
        raise Stop("필수 속성 누락: " + ", ".join(missing))
    if any("원본 속성 미확인" in result[key] for key in REQUIRED):
        raise Stop("원본 속성 미확인")
    return result

def native(issue):
    milestone = issue.get("milestone")
    if isinstance(milestone, dict):
        milestone = milestone.get("number")
    return {
        "number": issue.get("number", issue.get("issue_number")),
        "title": issue["title"], "body": issue.get("body") or "",
        "state": issue["state"], "state_reason": issue.get("state_reason"),
        "labels": sorted(x["name"] if isinstance(x, dict) else x for x in issue.get("labels") or []),
        "assignees": sorted(x["login"].lower() for x in issue.get("assignees") or []),
        "milestone": milestone,
    }

def record(issue):
    protected = native(issue)
    p = properties(protected["body"])
    rid = p["Record ID"]
    if not re.fullmatch(r"[A-Z0-9]+(?:-[A-Z0-9]+)+", rid):
        raise Stop("Record ID 형식 오류")
    if not protected["title"].startswith("[" + rid + "]"):
        raise Stop(f"#{protected['number']} 제목/Record ID 불일치")
    markers = re.findall(r"<!--\s*fds-notion-migration:[^>]*?record-id:([^\s>]+)\s*-->", protected["body"])
    if any(m != rid for m in markers):
        raise Stop(f"#{protected['number']} migration marker/Record ID 불일치")
    if p["Status"] not in STATES:
        raise Stop("알 수 없는 Status: " + p["Status"])
    state, reason, label = STATES[p["Status"]]
    if protected["state"] != state or (reason and protected["state_reason"] != reason):
        raise Stop(f"#{protected['number']} 본문/실제 Issue state 불일치")
    if [x for x in protected["labels"] if x.startswith("status:")] != [label]:
        raise Stop(f"#{protected['number']} 상태 라벨 불일치")
    if p["Lead"] not in IDENTITY or IDENTITY[p["Lead"]].lower() not in protected["assignees"]:
        raise Stop(f"#{protected['number']} Lead/Assignee 불일치")
    if any(name.strip() not in IDENTITY for name in p["Support"].split(",")):
        raise Stop(f"#{protected['number']} Support 실명 확인 필요")
    if not protected["milestone"]:
        raise Stop(f"#{protected['number']} 대표 Milestone 확인 필요")
    start, end = date_value(p["Start"]), date_value(p["End"])
    if start and end and start > end:
        raise Stop(f"#{protected['number']} Start > End")
    values = {"Record ID": rid, "Status": p["Status"], "Phase": p["Phase"],
              "Priority": p["Priority"], "Support": p["Support"],
              "Plan Start": start, "Plan End": end, "Schedule Note": p["Schedule Note"]}
    for name, (kind, options) in FIELDS.items():
        if kind == "SINGLE_SELECT" and values[name] not in options:
            raise Stop(f"#{protected['number']} {name} 허용값 확인 필요: {values[name]}")
    return {"record_id": rid, "number": protected["number"], "title": protected["title"],
            "url": f"https://github.com/{REPO}/issues/{protected['number']}",
            "node_id": issue.get("node_id"), "source_updated_at": issue.get("updated_at"),
            "source_fingerprint": digest(protected), "body_sha256": hashlib.sha256(protected["body"].encode()).hexdigest(),
            "lead": p["Lead"], "assignees": protected["assignees"], "milestone": protected["milestone"],
            "properties": p, "values": values}

def validate_issues(issues, known=None, live=False):
    records = []
    seen = set()
    for issue in issues:
        if "pull_request" in issue:
            continue
        r = record(issue)
        if r["record_id"] in seen:
            raise Stop("중복 Record ID: " + r["record_id"])
        seen.add(r["record_id"])
        if live and not r["node_id"]:
            raise Stop("실제 Issue node_id 누락")
        records.append(r)
    if known:
        by_id = {r["record_id"]: r["number"] for r in records}
        for rid, number in known.items():
            if by_id.get(rid) != number:
                raise Stop(f"등록된 Record ID 주소 변경/조회 누락: {rid}")
    if not records:
        raise Stop("조회된 Issue가 없음")
    return sorted(records, key=lambda r: r["number"])

def summary(records):
    return {"issues": len(records),
            "status": dict(collections.Counter(r["values"]["Status"] for r in records)),
            "phase": dict(collections.Counter(r["values"]["Phase"] for r in records)),
            "lead": dict(collections.Counter(r["lead"] for r in records)),
            "plan_end_tbd": [r["number"] for r in records if r["values"]["Plan End"] is None]}

class API:
    def __init__(self):
        if not shutil.which("gh"):
            raise Stop("GitHub CLI(gh)가 필요합니다. README의 사전 조건을 확인하세요.")

    def run(self, args, payload=None):
        env = dict(os.environ, GH_HOST="github.com", GH_PROMPT_DISABLED="1", GH_PAGER="cat")
        try:
            p = subprocess.run(["gh"] + args, input=None if payload is None else json.dumps(payload, ensure_ascii=False),
                               capture_output=True, text=True, encoding="utf-8", env=env, timeout=60)
        except subprocess.TimeoutExpired:
            raise Stop("GitHub 응답 시간 초과. 결과를 재조회한 뒤 같은 키트를 재실행하세요.")
        if p.returncode:
            raise Stop(redact(p.stderr.strip())[:2500])
        return p.stdout

    def rest(self, path, method="GET", body=None, paginate=False):
        args = ["api", "--hostname", "github.com", "--method", method,
                "-H", "Accept: application/vnd.github+json", "-H", "X-GitHub-Api-Version: 2026-03-10", path]
        if paginate:
            args.append("--paginate")
        if body is not None:
            args += ["--input", "-"]
        raw = self.run(args, body)
        if not raw.strip():
            return None
        if not paginate:
            return json.loads(raw)
        decoder, pages = json.JSONDecoder(), []
        while raw.strip():
            page, end = decoder.raw_decode(raw.lstrip())
            if not isinstance(page, list):
                raise Stop("예상하지 못한 REST pagination 응답")
            pages.extend(page)
            raw = raw.lstrip()[end:]
        return pages

    def gql(self, query, variables=None):
        result = self.rest("graphql", "POST", {"query": query, "variables": variables or {}})
        if result.get("errors"):
            raise Stop(redact(json.dumps(result["errors"], ensure_ascii=False))[:2500])
        return result["data"]

def desired_values(r, fields):
    values = dict(r["values"])
    status = fields.get("Status")
    if status and values["Status"] == "To Do" and "To Do" not in status["options"] and "Todo" in status["options"]:
        values["Status"] = "Todo"
    # Project display only: preserve Cancelled in the issue and source summary.
    # Prefer the dedicated option when the board provides it.
    if status and values["Status"] == "Cancelled" and "Cancelled" not in status["options"]:
        values["Status"] = "Done"
    return values

def validate_fields(fields, records, allow_missing=False):
    expected = dict(FIELDS, Status=("SINGLE_SELECT", []))
    for name, (kind, options) in expected.items():
        if name not in fields:
            if allow_missing:
                continue
            raise Stop("Project 필드 없음: " + name)
        f = fields[name]
        if f["kind"] != kind:
            raise Stop("기존 필드 타입 불일치: " + name)
        if kind == "SINGLE_SELECT":
            needed = {desired_values(r, fields)[name] for r in records}
            if not needed.issubset(f["options"]):
                raise Stop("기존 선택 필드에 필요한 값 없음: " + name)

def item_values(item):
    connection = item["fieldValues"]
    if connection["pageInfo"]["hasNextPage"]:
        raise Stop("Project item fieldValues pagination 필요")
    result = {}
    for value in connection["nodes"]:
        if not value or "field" not in value:
            continue
        field = value["field"]
        if not field or "name" not in field:
            continue
        result[field["name"]] = value.get("text", value.get("date", value.get("name")))
    return result

def list_items(api, pid):
    items, after = {}, None
    while True:
        q = "query($id:ID!,$after:String){node(id:$id){... on ProjectV2{items(first:50,after:$after){nodes{" + ITEM_BODY + "}pageInfo{hasNextPage endCursor}}}}}"
        conn = api.gql(q, {"id": pid, "after": after})["node"]["items"]
        for item in conn["nodes"]:
            content = item.get("content")
            if not content or content.get("repository", {}).get("nameWithOwner") != REPO:
                continue
            if content["id"] in items:
                raise Stop("Project 안의 중복 Issue 연결")
            items[content["id"]] = item
        if not conn["pageInfo"]["hasNextPage"]:
            return items
        after = conn["pageInfo"]["endCursor"]

def get_item(api, iid):
    return api.gql("query($id:ID!){node(id:$id){... on ProjectV2Item{" + ITEM_BODY + "}}}", {"id": iid})["node"]

def item_changes(item, expected):
    actual = item_values(item) if item else {}
    return {k: v for k, v in expected.items() if actual.get(k) != v}

def update_fields(api, pid, iid, changes, fields):
    declarations, parts = ["$p:ID!", "$i:ID!"], []
    variables = {"p": pid, "i": iid}
    for index, (name, value) in enumerate(changes.items()):
        declarations.append(f"$f{index}:ID!")
        variables[f"f{index}"] = fields[name]["node_id"]
        if value is None:
            parts.append(f"m{index}:clearProjectV2ItemFieldValue(input:{{projectId:$p,itemId:$i,fieldId:$f{index}}}){{projectV2Item{{id}}}}")
        else:
            declarations.append(f"$v{index}:ProjectV2FieldValue!")
            kind = fields[name]["kind"]
            key = {"TEXT": "text", "DATE": "date", "SINGLE_SELECT": "singleSelectOptionId"}[kind]
            variables[f"v{index}"] = {key: fields[name]["options"][value] if kind == "SINGLE_SELECT" else value}
            parts.append(f"m{index}:updateProjectV2ItemFieldValue(input:{{projectId:$p,itemId:$i,fieldId:$f{index},value:$v{index}}}){{projectV2Item{{id}}}}")
    if parts:
        api.gql("mutation(" + ",".join(declarations) + "){" + " ".join(parts) + "}", variables)
