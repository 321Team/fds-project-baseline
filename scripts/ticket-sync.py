#!/usr/bin/env python3
"""Conservative Issue metadata synchronization. No issue/body/state/catalog creation."""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / 'governance' / 'ticket-sync-map.json'
REPO = '321Team/fds-project-baseline'
API_VERSION = '2026-03-10'


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_new(path, value):
    # Refuse to overwrite an earlier plan or result.
    with Path(path).open('x', encoding='utf-8') as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write('\n')


def properties(body):
    lines = body.splitlines()
    starts = [n for n, line in enumerate(lines)
              if re.match(r'^\|\s*Property\s*\|', line)]
    if not starts:
        raise ValueError('missing Property table')
    start = starts[0]
    if start + 1 >= len(lines) or not re.match(r'^\|[\s:|-]+$', lines[start + 1]):
        raise ValueError('invalid table delimiter')
    result = {}
    for line in lines[start + 2:]:
        if not line.startswith('|'):
            break
        key, value = line[1:-1].split('|', 1)
        key, value = key.strip(), value.strip()
        if key in result:
            raise ValueError('duplicate property: ' + key)
        result[key] = value
    return result


def labels(issue):
    return sorted(x if isinstance(x, str) else x['name'] for x in issue['labels'])


def assignees(issue):
    return sorted(x if isinstance(x, str) else x['login'] for x in issue['assignees'])


def fingerprint(issue):
    return digest({
        'number': issue['number'], 'title': issue['title'], 'body': issue.get('body') or '',
        'updated_at': issue['updated_at'], 'state': issue['state'],
        'state_reason': issue.get('state_reason'), 'labels': labels(issue),
        'assignees': assignees(issue), 'type': type_ref(issue),
        'milestone': milestone_ref(issue),
    })


def type_ref(issue):
    value = issue.get('type')
    return {k: value.get(k) for k in ('id', 'name')} if isinstance(value, dict) else value


def milestone_ref(issue):
    value = issue.get('milestone')
    return {k: value.get(k) for k in ('number', 'title', 'due_on', 'state')} if value else None


def gh(method, endpoint, payload=None, pages=False):
    args = ['gh', 'api', '--hostname', 'github.com', '--method', method, endpoint,
            '-H', 'Accept: application/vnd.github+json',
            '-H', 'X-GitHub-Api-Version: ' + API_VERSION]
    if pages:
        args += ['--paginate', '--slurp']
    if payload is not None:
        args += ['--input', '-']
    result = subprocess.run(args, input=None if payload is None else json.dumps(payload),
                            capture_output=True, text=True, check=False)
    if result.returncode:
        # Do not copy authentication-related stderr into persistent results.
        raise RuntimeError('GitHub API failed: ' + method + ' ' + endpoint
                           + '. Check local gh authentication/permissions; no bypass attempted.')
    data = json.loads(result.stdout)
    return [item for page in data for item in page] if pages else data


def live_issues():
    return gh('GET', 'repos/' + REPO + '/issues?state=all&per_page=100', pages=True)


def catalog(native):
    data = {'labels': gh('GET', 'repos/' + REPO + '/labels?per_page=100', pages=True)}
    if native:
        data['types'] = gh('GET', 'orgs/321Team/issue-types?per_page=100', pages=True)
        data['milestones'] = gh('GET', 'repos/' + REPO + '/milestones?state=all&per_page=100', pages=True)
    return data


def analyze(config, source, catalogs=None, native=False):
    issues = [x for x in source if not x.get('pull_request')]
    expected = {x['record_id']: x for x in config['records']}
    seen, blockers, unresolved, changes, fingerprints = {}, [], [], [], {}
    known_labels = None if catalogs is None else {x['name'] for x in catalogs['labels']}
    milestones = {x['record_id']: x for x in config['milestones']}
    for issue in issues:
        n = issue['number']
        try:
            p = properties(issue.get('body') or '')
            rid = p['Record ID']
            if rid in seen:
                raise ValueError('duplicate Record ID: ' + rid)
            seen[rid] = n
            if rid not in expected or expected[rid]['issue_number'] != n:
                raise ValueError('unmapped or moved Record ID: ' + rid)
            if not issue['title'].startswith('[' + rid + ']'):
                raise ValueError('title/Record ID mismatch')
            markers = re.findall(r'record-id:([A-Za-z0-9-]+)', issue.get('body') or '')
            if any(x != rid for x in markers):
                raise ValueError('migration marker mismatch')
            missing = [x for x in config['required_properties'] if not p.get(x)]
            if missing:
                raise ValueError('missing properties: ' + ', '.join(missing))
            if p != expected[rid]['properties']:
                raise ValueError('source property table changed; review and update map first')
            fingerprints[str(n)] = fingerprint(issue)
            unknown = [k for k, v in p.items() if '원본 속성 미확인' in v]
            if unknown:
                unresolved.append({'issue': n, 'kind': 'SOURCE_UNKNOWN', 'fields': unknown})
            want = []
            for field, mapping in config['labels'].items():
                if p[field] in mapping:
                    want.append(mapping[p[field]])
                elif '원본 속성 미확인' not in p[field]:
                    raise ValueError('invalid ' + field + ': ' + p[field])
            if p['Category'] in config['category_labels']:
                want += config['category_labels'][p['Category']]
            elif '원본 속성 미확인' not in p['Category']:
                raise ValueError('unmapped Category')
            if unknown:
                want.append(config['exception_label'])
            existing = labels(issue)
            managed = ('phase:', 'type:', 'status:', 'priority:', 'area:')
            conflict = [x for x in existing if x.startswith(managed) and x not in want]
            if conflict:
                raise ValueError('managed label conflict: ' + ', '.join(conflict))
            missing_labels = sorted(set(want) - set(existing))
            if known_labels is not None and set(missing_labels) - known_labels:
                raise ValueError('label catalog missing; creation requires separate review')
            patch = {}
            if missing_labels:
                patch['labels'] = sorted(set(existing + want))
            person = config['identities'].get(p['Lead'])
            if not person:
                raise ValueError('unverified Lead identity')
            if person not in assignees(issue):
                raise ValueError('Lead assignment drift; verify assignment eligibility separately')
            status = p['Status']
            want_state = 'closed' if status in ('Done', 'Cancelled') else 'open'
            want_reason = {'Done': 'completed', 'Cancelled': 'not_planned'}.get(status)
            if issue['state'] != want_state or (want_reason and issue.get('state_reason') != want_reason):
                raise ValueError('state/state_reason conflict; no automatic close/reopen')
            desired_type = p['Type']
            current_type = issue.get('type')
            current_type = current_type.get('name') if isinstance(current_type, dict) else current_type
            if '원본 속성 미확인' not in desired_type and current_type != desired_type:
                if current_type:
                    raise ValueError('existing native type conflict')
                hits = [t for t in (catalogs or {}).get('types', [])
                        if t['name'] == desired_type and t.get('is_enabled', True)]
                if native and len(hits) == 1:
                    patch['type'] = desired_type
                else:
                    unresolved.append({'issue': n, 'kind': 'NATIVE_TYPE_NOT_APPLIED',
                                       'fallback': config['labels']['Type'][desired_type]})
            target = expected[rid]['milestone_record_id']
            if not target:
                unresolved.append({'issue': n, 'kind': 'MILESTONE_MAPPING_HOLD',
                                   'reason': expected[rid]['milestone_basis']})
            else:
                definition = milestones[target]
                current = issue.get('milestone')
                if current and current['title'] != definition['title']:
                    raise ValueError('existing milestone conflict')
                hits = [m for m in (catalogs or {}).get('milestones', [])
                        if m['title'] == definition['title']]
                if current:
                    hits = [current]
                if len(hits) == 1:
                    due = hits[0].get('due_on')
                    if due:
                        date = dt.datetime.fromisoformat(due.replace('Z', '+00:00')).astimezone(
                            dt.timezone(dt.timedelta(hours=9))).date().isoformat()
                        if date != definition['plan_date']:
                            raise ValueError('milestone due date differs from approved plan')
                    if not current and native:
                        patch['milestone'] = hits[0]['number']
                if not current and 'milestone' not in patch:
                    unresolved.append({'issue': n, 'kind': 'MILESTONE_NOT_APPLIED', 'target': target})
            if patch:
                changes.append({'issue': n, 'record_id': rid, 'patch': patch})
        except (KeyError, ValueError, TypeError) as error:
            blockers.append({'issue': n, 'reason': str(error)})
    for rid in sorted(set(expected) - set(seen)):
        blockers.append({'record_id': rid, 'reason': 'expected Issue missing'})
    return {'repository': REPO, 'native': native, 'count': len(issues),
            'fingerprints': fingerprints, 'changes': sorted(changes, key=lambda x: x['issue']),
            'blockers': blockers, 'unresolved': unresolved,
            'status': 'STOP' if blockers else ('PARTIAL' if unresolved else 'COMPLETE')}


def verify_write(before, after, patch):
    for key in ('number', 'title', 'body', 'state', 'state_reason'):
        if before.get(key) != after.get(key):
            raise RuntimeError('protected field changed: ' + key)
    if labels(after) != patch.get('labels', labels(before)):
        raise RuntimeError('labels verification failed')
    if assignees(after) != patch.get('assignees', assignees(before)):
        raise RuntimeError('assignees verification failed')
    if 'type' in patch:
        if (after.get('type') or {}).get('name') != patch['type']:
            raise RuntimeError('native type verification failed')
    elif type_ref(before) != type_ref(after):
        raise RuntimeError('unrequested native type change')
    if 'milestone' in patch:
        if (after.get('milestone') or {}).get('number') != patch['milestone']:
            raise RuntimeError('milestone verification failed')
    elif milestone_ref(before) != milestone_ref(after):
        raise RuntimeError('unrequested milestone change')


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    audit = sub.add_parser('audit')
    audit.add_argument('--snapshot', required=True)
    plan = sub.add_parser('plan')
    plan.add_argument('--native', action='store_true')
    plan.add_argument('--output', required=True)
    apply = sub.add_parser('apply')
    apply.add_argument('--plan', required=True)
    apply.add_argument('--expect-sha256', required=True)
    apply.add_argument('--confirm-repo', required=True)
    apply.add_argument('--output', required=True)
    args = parser.parse_args()
    config = read_json(MAP)
    if config['repository'] != REPO:
        raise RuntimeError('repository mismatch')
    if args.action == 'audit':
        report = analyze(config, read_json(args.snapshot))
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1 if report['blockers'] else 0
    if args.action == 'plan':
        if Path(args.output).exists():
            raise RuntimeError('output already exists')
        report = analyze(config, live_issues(), catalog(args.native), args.native)
        report['map_sha256'] = digest(config)
        report['created_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
        write_new(args.output, report)
        print(json.dumps({'status': report['status'], 'changes': len(report['changes']),
                          'blockers': len(report['blockers']), 'unresolved': len(report['unresolved'])}))
        return 1 if report['blockers'] else 0
    if args.confirm_repo != REPO or Path(args.output).exists():
        raise RuntimeError('repository confirmation mismatch or output already exists')
    raw = Path(args.plan).read_bytes()
    if hashlib.sha256(raw).hexdigest() != args.expect_sha256:
        raise RuntimeError('plan SHA-256 mismatch')
    plan_data = json.loads(raw)
    if plan_data['repository'] != REPO or plan_data['map_sha256'] != digest(config) or plan_data['blockers']:
        raise RuntimeError('invalid or blocked plan')
    age = dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(plan_data['created_at'])
    if age.total_seconds() < 0 or age.total_seconds() > 86400:
        raise RuntimeError('plan expired or future timestamp')
    current_catalog = catalog(plan_data['native'])
    fresh = analyze(config, live_issues(), current_catalog, plan_data['native'])
    for key in ('fingerprints', 'changes', 'blockers', 'unresolved'):
        if fresh[key] != plan_data[key]:
            raise RuntimeError('stale plan: ' + key)
    result = {'repository': REPO, 'plan_sha256': args.expect_sha256, 'applied': [],
              'status': 'IN_PROGRESS', 'unresolved': fresh['unresolved']}
    # Create the output before writes and flush after each applied Issue.
    with Path(args.output).open('x', encoding='utf-8') as output:
        def save():
            output.seek(0)
            json.dump(result, output, ensure_ascii=False, indent=2)
            output.truncate()
            output.flush()
        save()
        try:
            for change in fresh['changes']:
                n, patch = change['issue'], change['patch']
                if set(patch) - {'labels', 'type', 'milestone'}:
                    raise RuntimeError('forbidden patch field')
                before = gh('GET', 'repos/' + REPO + '/issues/' + str(n))
                if fingerprint(before) != fresh['fingerprints'][str(n)]:
                    raise RuntimeError('Issue changed immediately before write: ' + str(n))
                entry = {'issue': n, 'patch': patch, 'before_sha256': fingerprint(before), 'status': 'REQUESTING'}
                result['applied'].append(entry)
                save()
                if 'labels' in patch:
                    # Add only; never overwrite labels added concurrently by a human.
                    added = sorted(set(patch['labels']) - set(labels(before)))
                    if added:
                        gh('POST', 'repos/' + REPO + '/issues/' + str(n) + '/labels', {'labels': added})
                native_patch = {k: v for k, v in patch.items() if k != 'labels'}
                if native_patch:
                    gh('PATCH', 'repos/' + REPO + '/issues/' + str(n), native_patch)
                after = gh('GET', 'repos/' + REPO + '/issues/' + str(n))
                verify_write(before, after, patch)
                entry.update({'status': 'VERIFIED', 'after_sha256': fingerprint(after)})
                save()
            final = analyze(config, live_issues(), current_catalog, plan_data['native'])
            if final['changes'] or final['blockers']:
                raise RuntimeError('final requery detected drift')
            result['status'] = final['status']
            result['unresolved'] = final['unresolved']
            save()
        except Exception as error:
            result.update({'status': 'STOP', 'error': str(error)})
            save()
            raise
    print(json.dumps({'status': result['status'], 'applied': len(result['applied']),
                      'unresolved': len(result['unresolved'])}))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        print('STOP: ' + str(exc), file=sys.stderr)
        sys.exit(1)
