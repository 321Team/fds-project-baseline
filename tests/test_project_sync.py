import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts/project_sync"))
import core as p
import run as s

def fixture(status="In Progress"):
    values = dict(zip(p.REQUIRED, [
        "P1-CICD-01", "Phase 1", "CI/CD / Supply Chain", "Task", status, "P0",
        "2026-09-01", "2026-09-18", "18", "14", "이권욱", "이하영",
        "기존 AC", "D03", "RISK-06", "승인된 운영 기록", "계획 일정",
    ]))
    body = "<!-- fds-notion-migration:2026-09-09 record-id:P1-CICD-01 -->\n"
    body += "| Property | 입력값 |\n| --- | --- |\n"
    body += "\n".join(f"| {key} | {value} |" for key, value in values.items())
    state, reason, label = p.STATES[status]
    return {"number": 16, "node_id": "I_TEST", "title": "[P1-CICD-01] Delivery", "body": body,
            "state": state, "state_reason": reason, "labels": [{"name": label}],
            "assignees": [{"login": "GWONUK"}], "milestone": {"number": 3}, "updated_at": "2026-09-12T00:00:00Z"}

def make_fields():
    specs = {"Status": ("SINGLE_SELECT", ["Todo", "In Progress", "Done", "Cancelled"]), **p.FIELDS,
             "Title": ("TITLE", []), "Assignees": ("ASSIGNEES", []), "Milestone": ("MILESTONE", []), "Labels": ("LABELS", [])}
    return {name: {"id": index, "node_id": f"F_{index}", "kind": kind,
                   "options": {option: f"O_{index}_{j}" for j, option in enumerate(options)}}
            for index, (name, (kind, options)) in enumerate(specs.items(), 1)}

class FakeAPI:
    def __init__(self, issue):
        self.issue = copy.deepcopy(issue)
        self.fields = make_fields()
        self.project = {"id": "P_TEST", "number": 123, "title": "FDS Hybrid Cloud Delivery", "url": "https://github.com/orgs/321Team/projects/123",
                        "public": False, "closed": False, "readme": "", "viewerCanUpdate": True}
        self.item = None
        self.views = []
        self.repositories = [p.REPO]
        self.writes = []
        self.drift = False

    def rest(self, path, method="GET", body=None, paginate=False):
        if path.endswith("/fields?per_page=100"):
            return [{"id": f["id"], "node_id": f["node_id"], "name": name, "data_type": f["kind"].lower(),
                     "options": [{"id": oid, "name": {"raw": option}} for option, oid in f["options"].items()]}
                    for name, f in self.fields.items()]
        if path.startswith("repos/"):
            if method != "GET":
                raise AssertionError("Native Issue mutation is forbidden")
            issue = copy.deepcopy(self.issue)
            if self.drift:
                issue["body"] += "\nupdated source"
            return [issue] if "?" in path else issue
        if path.endswith("/views") and method == "POST":
            self.writes.append(("create_view", copy.deepcopy(body)))
            view = dict(body, id=len(self.views) + 1, number=len(self.views) + 1)
            self.views.append(view)
            return {"value": copy.deepcopy(view)}
        raise AssertionError(path)

    def run(self, args, **kwargs):
        if args[:2] == ["project", "link"]:
            self.repositories = [p.REPO]
            self.writes.append(("link_repository", list(args)))
            return ""
        raise AssertionError("All test fields already exist")

    def gql(self, query, variables=None):
        v = variables or {}
        if "createProjectV2(" in query:
            self.writes.append(("create_project", copy.deepcopy(v)))
            return {"createProjectV2": {"projectV2": copy.deepcopy(self.project)}}
        if "updateProjectV2(" in query:
            self.writes.append(("private_and_readme", copy.deepcopy(v)))
            self.project["public"] = False
            self.project["readme"] = v["r"]
            return {"updateProjectV2": {"projectV2": copy.deepcopy(self.project)}}
        if "addProjectV2ItemById" in query:
            if self.project["public"]:
                raise AssertionError("Private must be verified before adding issues")
            self.writes.append(("add_item", copy.deepcopy(v)))
            self.item = {"id": "ITEM_TEST", "isArchived": False,
                         "content": {"id": "I_TEST", "number": 16, "url": "https://github.com/321Team/fds-project-baseline/issues/16",
                                     "repository": {"nameWithOwner": p.REPO}},
                         "fieldValues": {"pageInfo": {"hasNextPage": False}, "nodes": []}}
            return {"addProjectV2ItemById": {"item": {"id": "ITEM_TEST"}}}
        if query.startswith("mutation"):
            if "updateProjectV2ItemFieldValue" not in query and "clearProjectV2ItemFieldValue" not in query:
                raise AssertionError("Unexpected mutation: " + query)
            self.writes.append(("fields", copy.deepcopy(v)))
            current = p.item_values(self.item)
            for key in [key for key in v if key.startswith("f")]:
                index = key[1:]
                name = next(name for name, field in self.fields.items() if field["node_id"] == v[key])
                value = v.get("v" + index)
                if value is None:
                    current.pop(name, None)
                elif "singleSelectOptionId" in value:
                    current[name] = next(option for option, oid in self.fields[name]["options"].items() if oid == value["singleSelectOptionId"])
                else:
                    current[name] = next(iter(value.values()))
            nodes = []
            for name, value in current.items():
                key = {"TEXT": "text", "DATE": "date", "SINGLE_SELECT": "name"}[self.fields[name]["kind"]]
                nodes.append({"field": {"name": name}, key: value})
            self.item["fieldValues"]["nodes"] = nodes
            return {}
        if "items(first:" in query:
            return {"node": {"items": {"nodes": [copy.deepcopy(self.item)] if self.item else [], "pageInfo": {"hasNextPage": False}}}}
        if "views(first:" in query:
            return {"node": {"views": {"nodes": [dict(x, layout=x["layout"].upper() + "_LAYOUT") for x in self.views],
                                        "pageInfo": {"hasNextPage": False}}}}
        if "repositories(first:" in query:
            return {"node": {"repositories": {"nodes": [{"nameWithOwner": name} for name in self.repositories],
                                               "pageInfo": {"hasNextPage": False}}}}
        if "... on ProjectV2Item" in query:
            return {"node": copy.deepcopy(self.item)}
        if "... on ProjectV2" in query:
            return {"node": copy.deepcopy(self.project)}
        raise AssertionError(query)


class SyncAPI(FakeAPI):
    def __init__(self, issue=None):
        super().__init__(issue or fixture())
        self.project.update(number=1, url=s.PROJECT_URL)
    def gql(self, query, variables=None):
        if 'projectV2(number:' in query:
            return {'organization': {'projectV2': copy.deepcopy(self.project)}}
        if 'fields(first:' in query:
            nodes = [{'id': f['node_id'], 'name': name, 'dataType': f['kind'],
                      'options': [{'id': oid, 'name': opt} for opt, oid in f['options'].items()]}
                     for name, f in self.fields.items()]
            return {'node': {'fields': {'nodes': nodes, 'pageInfo': {'hasNextPage': False}}}}
        if query.startswith('mutation') and not any(x in query for x in (
                'addProjectV2ItemById', 'updateProjectV2ItemFieldValue', 'clearProjectV2ItemFieldValue')):
            raise AssertionError('Forbidden mutation')
        return super().gql(query, variables)
    def run(self, args, **kwargs):
        assert args[:3] == ['project', 'field-create', '1']
        name = args[args.index('--name') + 1]
        self.fields[name] = make_fields()[name]
        self.writes.append(('create_field', name))
        return '{}'


def execute(api, apply=True):
    report = {'journal': [], 'verified_issues': [], 'remote_write_state': 'NOT_ATTEMPTED'}
    s.sync(api, apply, report, lambda: None)
    return report


class SyncTests(unittest.TestCase):
    def test_first_table_not_history(self):
        issue = fixture()
        issue['body'] += '\n\nHistory\n' + fixture('Done')['body']
        self.assertEqual(p.record(issue)['values']['Status'], 'In Progress')

    def test_duplicate_and_state_conflicts_stop(self):
        with self.assertRaises(p.Stop):
            p.validate_issues([fixture(), fixture()])
        api = SyncAPI()
        api.issue['state'] = 'closed'
        with self.assertRaises(p.Stop): execute(api)
        self.assertEqual(api.writes, [])

    def test_read_only_plan_includes_missing_fields(self):
        api = SyncAPI()
        del api.fields['Support']
        result = execute(api, False)
        self.assertEqual(result['missing_fields'], ['Support'])
        self.assertEqual(result['status'], 'CHECK_READY')
        self.assertEqual(api.writes, [])

    def test_apply_creates_field_and_rerun_is_idempotent(self):
        api = SyncAPI()
        del api.fields['Support']
        original = copy.deepcopy(api.issue)
        self.assertEqual(execute(api)['status'], 'SYNC_VERIFIED')
        writes = copy.deepcopy(api.writes)
        self.assertEqual(execute(api)['status'], 'SYNC_VERIFIED')
        self.assertEqual(api.writes, writes)
        self.assertEqual(api.issue, original)

    def test_tbd_clears_previous_date(self):
        api = SyncAPI()
        execute(api)
        api.issue['body'] = api.issue['body'].replace('| End | 2026-09-18 |', '| End | TBD |')
        execute(api)
        self.assertNotIn('Plan End', p.item_values(api.item))

    def test_cancelled_is_not_done(self):
        api = SyncAPI(fixture('Cancelled'))
        execute(api)
        self.assertEqual(p.item_values(api.item)['Status'], 'Cancelled')

    def test_stale_source_stops_before_item_add(self):
        api = SyncAPI()
        with patch.object(s, 'assert_source', side_effect=p.Stop('stale')):
            with self.assertRaises(p.Stop): execute(api)
        self.assertEqual(api.writes, [])

    def test_partial_failure_keeps_requested_journal(self):
        api = SyncAPI()
        report = {'journal': [], 'verified_issues': [], 'remote_write_state': 'NOT_ATTEMPTED'}
        with patch.object(s, 'update_fields', side_effect=p.Stop('API failure')):
            with self.assertRaises(p.Stop): s.sync(api, True, report, lambda: None)
        self.assertIsNotNone(api.item)
        self.assertEqual(report['journal'][-1]['status'], 'REQUESTED')
        self.assertEqual(report['remote_write_state'], 'PARTIAL_OR_UNKNOWN')

    def test_archived_source_does_not_restore(self):
        api = SyncAPI()
        execute(api)
        api.item['isArchived'] = True
        writes = copy.deepcopy(api.writes)
        with self.assertRaises(p.Stop): execute(api)
        self.assertEqual(api.writes, writes)

    def test_wrong_project_or_public_stops(self):
        for key, value in [('url', 'https://github.com/orgs/321Team/projects/2'), ('public', True)]:
            api = SyncAPI()
            api.project[key] = value
            with self.assertRaises(p.Stop): execute(api)
            self.assertEqual(api.writes, [])

    def test_unsupported_status_option_stops_before_write(self):
        api = SyncAPI()
        del api.fields['Status']['options']['In Progress']
        with self.assertRaises(p.Stop): execute(api)
        self.assertEqual(api.writes, [])

if __name__ == '__main__':
    unittest.main()

