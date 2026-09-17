#!/usr/bin/env python3
"""One-way synchronization into 321Team Project 1; default is read-only."""
import argparse
import json
import os
from pathlib import Path
from core import (API, Stop, ORG, REPO, FIELDS, validate_issues, summary,
                  validate_fields, desired_values, list_items, get_item,
                  item_values, item_changes, update_fields, digest, native)

PROJECT_NUMBER = 1
PROJECT_URL = 'https://github.com/orgs/321Team/projects/1'


def project(api):
    p = api.gql('query($o:String!,$n:Int!){organization(login:$o){projectV2(number:$n){id url public closed viewerCanUpdate}}}',
                {'o': ORG, 'n': PROJECT_NUMBER})['organization']['projectV2']
    if not p or p['url'].rstrip('/') != PROJECT_URL or p['public'] or p['closed'] or not p['viewerCanUpdate']:
        raise Stop('Project 1 identity/private/open/write permission check failed')
    return p


def fields(api, pid):
    result, after = {}, None
    while True:
        conn = api.gql('''query($p:ID!,$a:String){node(id:$p){... on ProjectV2{
          fields(first:100,after:$a){nodes{
            ... on ProjectV2Field{id name dataType}
            ... on ProjectV2SingleSelectField{id name dataType options{id name}}
            ... on ProjectV2IterationField{id name dataType}
          }pageInfo{hasNextPage endCursor}}
        }}}''', {'p': pid, 'a': after})['node']['fields']
        for f in conn['nodes']:
            if not f or 'name' not in f:
                raise Stop('Unsupported project field response')
            if f['name'] in result:
                raise Stop('Duplicate field: ' + f['name'])
            options = {o['name']: o['id'] for o in f.get('options', [])}
            if len(options) != len(f.get('options', [])):
                raise Stop('Duplicate field options')
            result[f['name']] = {'node_id': f['id'], 'kind': f['dataType'], 'options': options}
        if not conn['pageInfo']['hasNextPage']:
            return result
        after = conn['pageInfo']['endCursor']


def sources(api):
    raw = api.rest(f'repos/{REPO}/issues?state=all&per_page=100', paginate=True)
    return validate_issues(raw, live=True)


def assert_source(api, r):
    fresh = api.rest(f"repos/{REPO}/issues/{r['number']}")
    if digest(native(fresh)) != r['source_fingerprint'] or fresh.get('updated_at') != r['source_updated_at']:
        raise Stop(f"Stale source #{r['number']}; rerun against latest source")


def sync(api, apply, report, emit):
    p = project(api)
    records = sources(api)  # Validate every source before any project mutation.
    fs = fields(api, p['id'])
    if 'Status' not in fs:
        raise Stop('Existing Status field required')
    validate_fields(fs, records, allow_missing=True)
    items = list_items(api, p['id'])
    for r in records:
        item = items.get(r['node_id'])
        if item and item['isArchived']:
            raise Stop(f"Archived target #{r['number']}; no automatic restore")
    missing = [name for name in FIELDS if name not in fs]
    report.update(source_summary=summary(records), missing_fields=missing,
                  plan=[{'issue': r['number'], 'add_item': r['node_id'] not in items,
                         'changes': item_changes(items.get(r['node_id']), desired_values(r, fs))}
                        for r in records])
    emit()
    if not apply:
        report['status'] = 'CHECK_READY'
        return

    def write(action, payload, fn):
        entry = dict(action=action, status='REQUESTED', **payload)
        report['journal'].append(entry)
        report['remote_write_state'] = 'PARTIAL_OR_UNKNOWN'
        emit()  # Ambiguous API failures remain visible.
        result = fn()
        entry['status'] = 'API_RETURNED'
        emit()
        return result

    for name in missing:
        kind, options = FIELDS[name]
        args = ['project', 'field-create', str(PROJECT_NUMBER), '--owner', ORG,
                '--name', name, '--data-type', kind, '--format', 'json']
        if options:
            args += ['--single-select-options', ','.join(options)]
        write('create_field', {'field': name}, lambda: api.run(args))
    fs = fields(api, p['id'])
    validate_fields(fs, records)
    for r in records:
        expected = desired_values(r, fs)
        item = items.get(r['node_id'])
        if item and not item_changes(item, expected):
            continue
        assert_source(api, r)
        if item:
            fresh = get_item(api, item['id'])
            if fresh['isArchived'] or item_values(fresh) != item_values(item):
                raise Stop(f"Concurrent project edit #{r['number']}")
        else:
            added = write('add_item', {'issue': r['number']}, lambda: api.gql(
                'mutation($p:ID!,$c:ID!){addProjectV2ItemById(input:{projectId:$p,contentId:$c}){item{id}}}',
                {'p': p['id'], 'c': r['node_id']}))
            item = get_item(api, added['addProjectV2ItemById']['item']['id'])
            if item['isArchived']:
                raise Stop('Archived added item')
        changes = item_changes(item, expected)
        if changes:
            write('set_fields', {'issue': r['number'], 'before': item_values(item), 'changes': changes},
                  lambda: update_fields(api, p['id'], item['id'], changes, fs))
        fresh = get_item(api, item['id'])
        if fresh['isArchived'] or item_changes(fresh, expected):
            raise Stop(f"Post-write verification failed #{r['number']}")
        assert_source(api, r)
        report['verified_issues'].append(r['number'])
        emit()
    # No implicit success after partial writes or source edits during the run.
    latest = sources(api)
    if [(r['number'], r['source_fingerprint'], r['source_updated_at']) for r in latest] != [
            (r['number'], r['source_fingerprint'], r['source_updated_at']) for r in records]:
        raise Stop('Sources changed during synchronization; rerun')
    project(api)
    latest_items = list_items(api, p['id'])
    for r in records:
        item = latest_items.get(r['node_id'])
        if not item or item['isArchived'] or item_changes(item, desired_values(r, fs)):
            raise Stop(f"Final verification failed #{r['number']}")
    report.update(status='SYNC_VERIFIED', remote_write_state='VERIFIED')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    report = {'status': 'STARTED', 'project_url': PROJECT_URL,
              'remote_write_state': 'NOT_ATTEMPTED', 'journal': [], 'verified_issues': []}
    out = Path('project-sync-result.json')
    def emit():
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    code = 0
    try:
        sync(API(), args.apply, report, emit)
    except Exception as exc:
        # Do not copy API response bodies or untrusted source content into logs.
        report.update(status='STOP', error_type=type(exc).__name__)
        if isinstance(exc, Stop):
            # Operator details stay in the private artifact; credential strings are redacted.
            from core import redact
            report['error'] = redact(str(exc))
        code = 1
    finally:
        emit()
        print('PROJECT_SYNC_STATUS=' + report['status'])
        if os.environ.get('GITHUB_STEP_SUMMARY'):
            with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as f:
                f.write('Project #1: **' + report['status'] + '**\n\n'
                        'Remote write state: ' + report['remote_write_state'] + '\n')
    return code


if __name__ == '__main__':
    raise SystemExit(main())
