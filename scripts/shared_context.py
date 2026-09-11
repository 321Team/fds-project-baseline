#!/usr/bin/env python3
"""Read-only GitHub context receipt. A receipt is an observation, never approval."""
import argparse
import base64
import datetime as dt
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "handoff/baseline.lock.json"
REPO = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
SHA = re.compile(r"[0-9a-f]{40}\Z")


class Blocked(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Blocked(message)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode()).hexdigest()


def utcnow():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def safe_path(value):
    require(isinstance(value, str) and value and "\\" not in value,
            "invalid relative path")
    parts = value.rstrip("/").split("/")
    require(not PurePosixPath(value).is_absolute() and
            all(x not in ("", ".", "..", ".git") for x in parts), "unsafe relative path")
    return value


def valid_repo(value):
    require(isinstance(value, str) and REPO.fullmatch(value), "invalid repository")
    return value


def validate_task(task):
    require(task.get("schema_version") == 1, "unsupported task schema")
    for key in ("record_id", "purpose"):
        require(isinstance(task.get(key), str) and task[key].strip(), "missing " + key)
    valid_repo(task["target"]["repository"])
    require(task["target"].get("base_ref") == "main", "this workflow requires main base")
    for key in ("allowed_paths", "acceptance_criteria", "checks"):
        require(isinstance(task.get(key), list) and task[key] and
                all(isinstance(x, str) and x.strip() for x in task[key]), "missing " + key)
    for path in task["allowed_paths"]:
        safe_path(path)
    for item in task.get("watch_repositories", []):
        valid_repo(item["repository"])
        require(item.get("ref") == "main", "watch repositories must use main")
    require(task.get("watch_issues"), "at least one related issue is required")
    for kind in ("watch_issues", "watch_prs"):
        require(isinstance(task.get(kind), list), "missing " + kind)
        for item in task[kind]:
            valid_repo(item["repository"])
            require(type(item["number"]) is int and item["number"] > 0, "invalid issue/PR number")
    evidence = task["evidence"]
    valid_repo(evidence["repository"])
    safe_path(evidence["path"])
    require(evidence.get("receipt_commit") == "" or
            SHA.fullmatch(evidence.get("receipt_commit", "")), "invalid evidence commit")
    require(task.get("runtime") == "NOT_AUTHORIZED_BY_THIS_HANDOFF", "runtime gate cannot be overridden")


class GitHubAPI:
    provenance = "GH_LIVE"

    def get(self, endpoint):
        try:
            result = subprocess.run(["gh", "api", "--method", "GET", endpoint],
                                    capture_output=True, text=True, timeout=60, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise Blocked("GitHub read unavailable; use normal authenticated access") from exc
        require(result.returncode == 0, "GitHub read failed; no cached fallback")
        try:
            return json.loads(result.stdout)
        except ValueError as exc:
            raise Blocked("invalid GitHub response") from exc


class ExportAPI:
    provenance = "SNAPSHOT_ONLY"

    def __init__(self, data):
        self.responses = data["responses"]

    def get(self, endpoint):
        require(endpoint in self.responses, "incomplete API export: " + endpoint)
        return self.responses[endpoint]


def pages(api, endpoint):
    separator = "&" if "?" in endpoint else "?"
    output = []
    for page in range(1, 101):
        batch = api.get(f"{endpoint}{separator}per_page=100&page={page}")
        require(isinstance(batch, list), "expected complete GitHub list")
        output.extend(batch)
        if len(batch) < 100:
            return output
    raise Blocked("pagination limit reached; completeness not established")


def selected(item, keys):
    return {key: item.get(key) for key in keys}


def comments(items):
    return [dict(selected(item, ("id", "body", "created_at", "updated_at")),
                 author=item.get("user", {}).get("login")) for item in items]


def reviews(items):
    return [dict(selected(item, ("id", "state", "body", "commit_id", "submitted_at")),
                 author=item.get("user", {}).get("login")) for item in items]


def collect(api, lock, task):
    validate_task(task)
    repo = valid_repo(lock["repository"])
    prefix = "repos/" + repo
    release = api.get(f"{prefix}/releases/{lock['release_id']}")
    require(release["tag_name"] == lock["tag"] and not release["draft"] and
            not release["prerelease"] and release.get("published_at"), "canonical release is not published")
    releases = pages(api, f"{prefix}/releases")
    versions = []
    for item in releases:
        match = re.fullmatch(r"docs-v(\d+)\.(\d+)\.(\d+)", item["tag_name"])
        if match and not item["draft"] and not item["prerelease"] and item.get("published_at"):
            versions.append((tuple(map(int, match.groups())), item["tag_name"]))
    require(versions and max(versions)[1] == lock["tag"], "canonical lock is not latest published version")
    obj = api.get(f"{prefix}/git/ref/tags/{lock['tag']}")["object"]
    for _ in range(5):
        if obj["type"] != "tag":
            break
        obj = api.get(f"{prefix}/git/tags/{obj['sha']}")["object"]
    require(obj["type"] == "commit" and obj["sha"] == lock["tag_commit"], "canonical tag moved")
    assets = pages(api, f"{prefix}/releases/{lock['release_id']}/assets")
    for expected in lock["assets"]:
        matching = [x for x in assets if x["name"] == expected["name"]]
        require(len(matching) == 1, "missing/duplicate release asset")
        actual = matching[0]
        require(actual["id"] == expected["id"] and actual.get("state") == "uploaded" and
                actual.get("digest") == "sha256:" + expected["sha256"], "release asset identity/hash changed")
    targets = {(repo, "main"), (task["target"]["repository"], task["target"]["base_ref"]),
               (task["evidence"]["repository"], "main")}
    targets.update((x["repository"], x["ref"]) for x in task["watch_repositories"])
    heads = {}
    for target, ref in sorted(targets):
        branch = api.get(f"repos/{target}/branches/{quote(ref, safe='')}")
        require(SHA.fullmatch(branch["commit"]["sha"]), "missing base commit")
        heads[target + "@" + ref] = branch["commit"]["sha"]
    tree = api.get(f"{prefix}/git/trees/{heads[repo + '@main']}?recursive=1")
    require(not tree.get("truncated", True), "truncated canonical tree")
    blobs = {x["path"]: x for x in tree["tree"] if x["type"] == "blob"}
    for path, expected in lock["protected_files"].items():
        actual = blobs.get(path, {})
        require(actual.get("sha") == expected["git_blob"] and actual.get("mode") == expected["mode"],
                "published input changed on main: " + path)
    history = []
    for approval in lock["approval_prs"]:
        pr = api.get(f"{prefix}/pulls/{approval['number']}")
        review_list = pages(api, f"{prefix}/pulls/{approval['number']}/reviews")
        require(pr.get("merged") and pr["head"]["sha"] == approval["head"] and
                pr["merge_commit_sha"] == approval["merge"], "canonical approval PR changed")
        match = [x for x in review_list if x["id"] == approval["review_id"] and
                 x["state"] == "APPROVED" and x["commit_id"] == approval["head"] and
                 x["user"]["login"] == approval["reviewer"] and
                 x["user"]["login"] != pr["user"]["login"]]
        require(len(match) == 1, "canonical exact-head independent approval missing")
        history.append({"number": approval["number"], "reviews_sha256": digest(reviews(review_list))})
    state = {}
    for kind, field in (("issues", "watch_issues"), ("pulls", "watch_prs")):
        for target in sorted(task[field], key=lambda x: (x["repository"], x["number"])):
            endpoint = f"repos/{target['repository']}/{kind}/{target['number']}"
            item = api.get(endpoint)
            require(item["number"] == target["number"], "wrong Issue/PR response")
            normalized = selected(item, ("number", "title", "body", "state", "updated_at", "closed_at"))
            normalized["assignees"] = sorted(x["login"] for x in item.get("assignees", []))
            normalized["labels"] = sorted(x["name"] for x in item.get("labels", []))
            normalized["milestone"] = item.get("milestone")
            issue_endpoint = f"repos/{target['repository']}/issues/{target['number']}"
            normalized["comments"] = comments(pages(api, issue_endpoint + "/comments"))
            if kind == "issues":
                require("pull_request" not in item, "watch_issues contains a PR; use watch_prs")
            else:
                normalized.update(selected(item, ("draft", "merged", "merged_at", "merge_commit_sha")))
                normalized["head"] = selected(item["head"], ("sha", "ref"))
                normalized["base"] = selected(item["base"], ("sha", "ref"))
                normalized["reviews"] = reviews(pages(api, endpoint + "/reviews"))
                normalized["review_comments"] = comments(pages(api, endpoint + "/comments"))
            state[endpoint] = {"state": item["state"], "updated_at": item.get("updated_at"),
                               "content_sha256": digest(normalized)}
    evidence_commit = task["evidence"]["receipt_commit"]
    if evidence_commit:
        commit = api.get(f"repos/{task['evidence']['repository']}/git/commits/{evidence_commit}")
        require(commit["sha"] == evidence_commit, "evidence commit missing")
    return {"lock_sha256": digest(lock), "task_sha256": digest(task), "heads": heads,
            "canonical": {"tag": lock["tag"], "commit": obj["sha"],
                          "release": selected(release, ("id", "tag_name", "published_at", "updated_at", "body")),
                          "assets": [selected(x, ("id", "name", "size", "digest", "updated_at"))
                                     for x in sorted(assets, key=lambda x: x["name"])],
                          "approval_history": history},
            "watched_state": state, "evidence_commit": evidence_commit or "NOT_RECEIVED"}


def observe(api, lock, task):
    value = collect(api, lock, task)
    if api.provenance == "GH_LIVE":
        require(value == collect(api, lock, task), "state changed during observation; retry after review")
    return value


def receipt(api, lock, task):
    started = utcnow()
    context = observe(api, lock, task)
    return {"schema_version": 1, "provenance": api.provenance,
            "started_at": started, "observed_at": utcnow(),
            "context_id": digest(context), "task": task, "context": context,
            "scope": "Observed GitHub metadata, not downloaded asset bytes, runtime, or approval"}


def check_receipt(saved, api, lock):
    require(saved.get("schema_version") == 1, "unsupported receipt schema")
    require(api.provenance == "GH_LIVE" and saved.get("provenance") == "GH_LIVE",
            "SNAPSHOT_ONLY cannot satisfy a live execution recheck")
    when = dt.datetime.fromisoformat(saved["observed_at"])
    require(when.tzinfo is not None, "receipt time needs timezone")
    age = (dt.datetime.now(dt.timezone.utc) - when).total_seconds()
    require(0 <= age <= 8 * 3600, "receipt expired or timestamp is in the future")
    require(digest(saved["context"]) == saved["context_id"], "receipt content hash mismatch")
    require(digest(saved["task"]) == saved["context"]["task_sha256"], "task changed after capture")
    current = observe(api, lock, saved["task"])
    require(digest(current) == saved["context_id"], "context drift: stop and re-handoff both tools")
    return current


def check_worktree(root, saved):
    task = saved["task"]
    base = saved["context"]["heads"][task["target"]["repository"] + "@main"]
    def git(*args):
        run = subprocess.run(["git", "-C", str(root), *args], capture_output=True, check=False)
        require(run.returncode == 0, "worktree/base verification failed")
        return run.stdout.decode().strip()
    remote = git("remote", "get-url", "origin")
    match = re.fullmatch(r"(?:https://github\.com/|git@github\.com:)([\w.-]+/[\w.-]+?)(?:\.git)?", remote)
    require(match and match[1] == task["target"]["repository"], "worktree repository differs from task")
    git("merge-base", "--is-ancestor", base, "HEAD")
    paths = set(filter(None, git("diff", "--name-only", "-z", base, "--").split("\0")))
    paths.update(filter(None, git("ls-files", "--others", "--exclude-standard", "-z").split("\0")))
    for path in paths:
        safe_path(path)
        require(any(path == allowed or (allowed.endswith("/") and path.startswith(allowed))
                    for allowed in task["allowed_paths"]), "changed path outside task scope: " + path)
    return {"head": git("rev-parse", "HEAD"), "changed_paths": sorted(paths)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    capture = sub.add_parser("capture")
    capture.add_argument("--task", type=Path, required=True)
    capture.add_argument("--out", type=Path, required=True)
    capture.add_argument("--api-export", type=Path)
    check = sub.add_parser("check")
    check.add_argument("--receipt", type=Path, required=True)
    check.add_argument("--worktree", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        lock = json.loads(LOCK.read_text())
        if args.command == "capture":
            task = json.loads(args.task.read_text())
            api = ExportAPI(json.loads(args.api_export.read_text())) if args.api_export else GitHubAPI()
            output = receipt(api, lock, task)
            with args.out.open("x") as handle:
                json.dump(output, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
            print(output["provenance"], output["context_id"])
        else:
            saved = json.loads(args.receipt.read_text())
            check_receipt(saved, GitHubAPI(), lock)
            local = check_worktree(args.worktree, saved)
            print(json.dumps({"status": "MATCH_LIVE_OBSERVATION", "context_id": saved["context_id"],
                              "worktree": local, "approval": "NOT_GRANTED"}, ensure_ascii=False))
        return 0
    except (Blocked, KeyError, TypeError, ValueError, OSError) as exc:
        print("BLOCKED:", str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
