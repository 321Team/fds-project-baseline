import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ticket_sync', ROOT / 'scripts/ticket-sync.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class TicketSyncTests(unittest.TestCase):
    def setUp(self):
        self.config = sync.read_json(ROOT / 'governance/ticket-sync-map.json')
        # Synthetic Issue payloads from the frozen 17-property map. No live writes.
        self.issues = []
        for row in self.config['records']:
            p = row['properties']
            body = '| Property | 입력값 |\n|---|---|\n' + '\n'.join('| ' + k + ' | ' + v + ' |' for k, v in p.items())
            want = [m[p[k]] for k, m in self.config['labels'].items() if p[k] in m]
            want += self.config['category_labels'].get(p['Category'], [])
            if any('원본 속성 미확인' in v for v in p.values()):
                want.append('metadata:needs-source')
            self.issues.append({'number': row['issue_number'], 'body': body,
                'title': '[' + row['record_id'] + '] synthetic fixture', 'updated_at': '2026-09-10T00:00:00Z',
                'state': 'closed' if p['Status'] == 'Done' else 'open',
                'state_reason': 'completed' if p['Status'] == 'Done' else None,
                'labels': want, 'assignees': [self.config['identities'][p['Lead']]],
                'type': None, 'milestone': None})

    def report(self):
        return sync.analyze(self.config, self.issues)

    def test_idempotent_metadata_still_partial(self):
        r = self.report()
        self.assertEqual([], r['blockers'])
        self.assertEqual([], r['changes'])
        self.assertEqual('PARTIAL', r['status'])

    def test_missing_labels_add_only(self):
        self.issues[0]['labels'] = ['human-note']
        r = self.report()
        self.assertIn('human-note', r['changes'][0]['patch']['labels'])
        self.assertEqual({'labels'}, set(r['changes'][0]['patch']))

    def test_duplicate_record_blocks(self):
        self.issues.append(copy.deepcopy(self.issues[0]))
        self.assertEqual('STOP', self.report()['status'])

    def test_source_drift_blocks(self):
        self.issues[0]['body'] = self.issues[0]['body'].replace('| Done |', '| In Progress |')
        self.assertEqual('STOP', self.report()['status'])

    def test_marker_mismatch_blocks(self):
        self.issues[0]['body'] += '\n<!-- record-id:WRONG-ID -->'
        self.assertEqual('STOP', self.report()['status'])

    def test_status_does_not_close_issue(self):
        self.issues[0]['state'] = 'open'
        self.assertEqual('STOP', self.report()['status'])
        self.assertFalse(any('state' in x['patch'] for x in self.report()['changes']))

    def test_unknown_source_kept(self):
        r = self.report()
        unknown = [x['issue'] for x in r['unresolved'] if x['kind'] == 'SOURCE_UNKNOWN']
        self.assertEqual([59, 61], unknown)

    def test_managed_label_conflict_blocks(self):
        self.issues[0]['labels'].append('status:in-progress')
        self.assertEqual('STOP', self.report()['status'])

    def test_assignment_conflict_blocks(self):
        self.issues[0]['assignees'] = []
        self.assertEqual('STOP', self.report()['status'])

    def test_fallback_is_not_task(self):
        cats = {'labels': [{'name': x} for i in self.issues for x in i['labels']],
                'types': [{'name': 'Task'}], 'milestones': []}
        r = sync.analyze(self.config, self.issues, cats, True)
        changes = {x['issue']: x['patch'] for x in r['changes']}
        self.assertNotIn(4, changes)
        self.assertEqual('Task', changes[9]['type'])

    def test_no_milestone_guess(self):
        r = self.report()
        self.assertEqual(20, sum(x['kind'] == 'MILESTONE_MAPPING_HOLD' for x in r['unresolved']))
        self.assertFalse(any('milestone' in x['patch'] for x in r['changes']))

    def test_protected_body_verification(self):
        before = self.issues[0]
        after = copy.deepcopy(before)
        after['body'] += '\nchanged'
        with self.assertRaises(RuntimeError):
            sync.verify_write(before, after, {})

    def test_missing_expected_issue_blocks(self):
        self.issues.pop()
        self.assertEqual('STOP', self.report()['status'])

    def test_prs_excluded(self):
        self.issues.append({'number': 999, 'pull_request': {'url': 'fixture'}})
        self.assertEqual(64, self.report()['count'])

    def test_milestone_counts_not_false_drift(self):
        before = copy.deepcopy(self.issues[0])
        before['milestone'] = {'number': 1, 'title': 'G0 Design Freeze', 'state': 'open',
                               'due_on': None, 'open_issues': 1}
        after = copy.deepcopy(before)
        after['milestone']['open_issues'] = 2
        self.assertEqual(sync.fingerprint(before), sync.fingerprint(after))

    def test_due_date_mismatch_blocks(self):
        cats = {'labels': [{'name': x} for i in self.issues for x in i['labels']],
                'types': [], 'milestones': [{'number': 1, 'title': 'G0 Design Freeze',
                                            'due_on': '2026-10-01T00:00:00Z'}]}
        r = sync.analyze(self.config, self.issues, cats, True)
        self.assertTrue(any('due date' in x['reason'] for x in r['blockers']))

    def test_milestone_uses_server_number(self):
        cats = {'labels': [{'name': x} for i in self.issues for x in i['labels']],
                'types': [], 'milestones': [{'number': 847, 'title': 'G0 Design Freeze',
                                            'due_on': '2026-09-01T14:59:59Z'}]}
        r = sync.analyze(self.config, self.issues, cats, True)
        self.assertEqual([], r['blockers'])
        changes = {x['issue']: x['patch'] for x in r['changes']}
        self.assertEqual(847, changes[8]['milestone'])

    def test_missing_label_catalog_blocks(self):
        self.issues[0]['labels'] = []
        r = sync.analyze(self.config, self.issues, {'labels': []}, False)
        self.assertEqual('STOP', r['status'])


if __name__ == '__main__':
    unittest.main()
