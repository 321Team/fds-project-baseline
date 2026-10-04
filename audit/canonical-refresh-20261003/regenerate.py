"""Deterministic offline candidate intake refresh; never merges or publishes."""
import json,re,hashlib,zipfile,io,difflib,datetime,shutil,sys
from pathlib import Path
R=Path(__file__).resolve().parent
O=Path(sys.argv[2]).resolve() if len(sys.argv)>2 and sys.argv[1]=='--from-snapshot' else R/'output'
A='audit/canonical-refresh-20261003'
KEYS=['Record ID','Phase','Category','Type','Status','Priority','Start','End','Calendar Days','Working Days','Lead','Support','Exit Criteria','Related Decision IDs','Related Risk IDs','Source','Schedule Note']
def read(p): return json.loads((R/p).read_text(encoding='utf-8'))
def dump(x): return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def sha(b): return hashlib.sha256(b).hexdigest()
def put(p,s):
 p=O/p;p.parent.mkdir(parents=True,exist_ok=True)
 p.write_bytes(s if isinstance(s,bytes) else s.encode('utf-8'))
def props(body):
 # Normalize CRLF for parsing only. Original source bytes are retained in snapshot.
 b=body.replace('\r\n','\n').split('## 갱신 전 원문 보관')[0]
 for table in re.findall(r'(?:^\|[^\n]*\n?)+',b,re.M):
  d=dict(re.findall(r'^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|$',table,re.M))
  if 'Record ID' in d:return {k:v for k,v in d.items() if k in KEYS}
 return {}
def days(a,b):
 try:
  x=datetime.date.fromisoformat(a);y=datetime.date.fromisoformat(b)
 except (ValueError,TypeError):return None
 return sum((x+datetime.timedelta(days=d)).weekday()<5 and str(x+datetime.timedelta(days=d)) not in ['2026-10-05','2026-10-09'] for d in range((y-x).days+1))
if len(sys.argv)>1 and sys.argv[1]=='--from-snapshot':
 with zipfile.ZipFile(R/'snapshot.zip') as z:raw=json.loads(z.read('snapshot.json'))
 writes={'writes':raw['schedule_write_evidence'],'writeComments':raw['schedule_write_comments']}
 anc=raw['ancestry']
else:
 raw=read('raw/snapshot.json');raw['repositories']['infra-dns']=read('raw/infra-dns.json')
 writes=read('raw/final-issue-writes.json');latest=read('raw/final-readback.json')
 raw['issues']=latest['issues'];raw['comments'].update(latest['comments'])
 raw['source_head_rechecks']=latest['heads']
 assert all(h['same_as_collected'] for h in latest['heads'])
 raw['schedule_write_evidence']=writes['writes'];raw['schedule_write_comments']=writes['writeComments']
 raw['initial_snapshot_serialized_at_kst']=raw['collected_at_kst']
 raw['collection_started_at_kst']=None
 raw['collection_finished_at_kst']=latest['collected_at_kst']
 anc=read('raw/ancestry.json')
 raw['previous_files']={p:(R/'before'/p).read_text(encoding='utf-8') for p in ['audit/canonical-candidate-20260927/intake.json','audit/canonical-candidate-20260927/README.md','audit/project-schedule-replan-20260930/schedule.json','releases/v3.1.21/README.md']}
T=raw['collection_finished_at_kst']
old=json.loads(raw['previous_files']['audit/canonical-candidate-20260927/intake.json'])
records=[];anomalies=[]
for i in sorted(raw['issues'],key=lambda i:i['number']):
 p=props(i['body']);record={'number':i['number'],'url':i['html_url'],'updated_at':i['updated_at'],'state':i['state'],'state_reason':i.get('state_reason'),'properties':p,'body_sha256_utf8':sha(i['body'].encode()),'body_sha256_lf':sha(i['body'].replace('\r\n','\n').encode()),'labels':[v['name'] for v in i['labels']],'assignees':[a['login'] for a in i['assignees']],'milestone':i.get('milestone'),'native_type':i.get('type')}
 record['missing_properties']=[k for k in KEYS if k not in p]
 record['blocked_by']=re.findall(r'^- \*\*(?:Blocked By|선행 차단):\*\* (.*)$',i['body'].replace('\r\n','\n').split('## 갱신 전 원문 보관')[0],re.M)
 if record['missing_properties']:anomalies.append({'number':i['number'],'kind':'MISSING_PROPERTIES','fields':record['missing_properties']})
 if p.get('Status') not in ['To Do','In Progress','In Review','Blocked','Done','Cancelled']:anomalies.append({'number':i['number'],'kind':'STATUS_VOCABULARY','value':p.get('Status')})
 if i['state']=='closed' and p.get('Status') not in ['Done','Cancelled']:anomalies.append({'number':i['number'],'kind':'STATE_BODY_DRIFT','body_status':p.get('Status'),'state':i['state'],'state_reason':i.get('state_reason')})
 records.append(record)
ids=[r['properties'].get('Record ID') for r in records]
assert None not in ids and len(ids)==len(set(ids)), 'missing or duplicate record identity'
by={r['number']:r for r in records}
repositories={};merged={};opened={};added={};non_main=[]
for name,d in sorted(raw['repositories'].items()):
 selected=sorted([p for p in d['prs'] if p['merged_at'] and p['merged_at']>raw['release']['published_at']],key=lambda p:p['number'])
 for p in selected:
  p['reachable_from_source_main']=p['merge_commit_sha'] in anc[name]['main_ancestors']
  p['reachable_from_candidate']=name=='fds-project-baseline' and p['merge_commit_sha'] in anc['candidate']['ancestors']
  assert p['reachable_from_source_main'] or p['reachable_from_candidate'],(name,p['number'])
  if not p['reachable_from_source_main']:non_main.append({'repository':name,'number':p['number'],'base_ref':p['base_ref'],'classification':'CANDIDATE_MAIN_SYNC_HISTORY'})
 merged[name]=[p['number'] for p in selected]
 added[name]=[n for n in merged[name] if n not in old['merged_inputs'].get(name,[])]
 opened[name]=sorted(p['number'] for p in d['prs'] if p['state']=='open')
 repositories[name]={'main_sha':d['main_sha'],'branch':'main','collection_pages':d['pages'],'merged_since_publication':selected,'open_unmerged':[p for p in d['prs'] if p['state']=='open'],'closed_unmerged':[p for p in d['prs'] if p['state']=='closed' and not p['merged_at']]}
total=sum(map(len,merged.values()));delta=sum(map(len,added.values()))
source={'collected_at_kst':T,'collection_is_atomic':False,'collection_started_at_kst':raw['collection_started_at_kst'],'base_publication_utc':raw['release']['published_at'],'candidate_input_head':raw['candidate_head'],'baseline_main':raw['main_sha'],'candidate_main_comparison':raw['comparison'],'repositories':repositories,'scope_rule':'Previous intake repository set + infra-terraform/infra-rosa + infra-dns identified by repository responsibility inventory. Organization-wide discovery not claimed.','merged_window_rule':'merged_at > v3.1.20 Release published_at; paginate until short page; preserve destination branch; verify merge SHA reachable from captured main or candidate for candidate sync PRs.','candidate_sync_history':non_main,'total_merged':total,'main_reachable_merged':total-len(non_main),'added_vs_old_intake':delta,'added_inputs':added,'ancestry_evidence':'snapshot.zip contains ancestor SHA sets and exact captured records'}
source['source_head_rechecks']=raw['source_head_rechecks']
raw['ancestry']=anc
snapshot=dump(raw).encode();buf=io.BytesIO()
with zipfile.ZipFile(buf,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 info=zipfile.ZipInfo('snapshot.json',date_time=(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.create_system=3;info.external_attr=0o100644<<16
 z.writestr(info,snapshot,compresslevel=9)
compressed=buf.getvalue()
put(A+'/snapshot.zip',compressed)
put(A+'/snapshot-integrity.json',dump({'compressed_sha256':sha(compressed),'decompressed_sha256':sha(snapshot),'encoding':'UTF-8 JSON','zip_entry_timestamp':'2026-01-01T00:00:00','contains':'78 issue original bodies + selected decision comment collections + PR metadata + repository ancestors + exact issue write before/after','limitations':'Not all 78 issue comment threads were collected; Runtime logs were not re-executed or independently revalidated.'}))
put(A+'/repository-source-heads.json',dump(source))
put(A+'/issue-index.json',dump({'collected_at_kst':T,'records':records,'source_anomalies':anomalies}))
intake=old.copy();intake.update({'generated_at_kst':T,'source_main':raw['main_sha'],'merged_inputs':merged,'open_excluded':opened,'repository_source_heads':A+'/repository-source-heads.json','source_snapshot':A+'/snapshot.zip','issue_index':A+'/issue-index.json','collection_status':'REFRESHED_AT_CAPTURE_TIME','merged_input_count':total,'added_merged_inputs':delta,'missing_merged_inputs_at_capture':0,'candidate_main_sync':{'verified_at_kst':T,'candidate_input_head':raw['candidate_head'],'base_main':raw['main_sha'],'ahead':raw['comparison']['ahead'],'behind':raw['comparison']['behind'],'scope':'Pre-change candidate HEAD; resulting refresh commit inherits this HEAD.'},'previous_collection':{'generated_at_kst':old['generated_at_kst'],'source_main':old['source_main'],'merged_input_count':sum(map(len,old['merged_inputs'].values()))}})
i110=by[110]
intake['current_planning_inputs']=[{'record_id':i110['properties']['Record ID'],'issue':110,'status':i110['properties']['Status'],'state':i110['state'],'start':i110['properties'].get('Start'),'end':i110['properties'].get('End'),'lead':i110['properties'].get('Lead'),'native_issue_type':i110['native_type'],'source_updated_at':i110['updated_at'],'source_body_sha256':i110['body_sha256_utf8'],'decision_approval':'APPROVED_DECISION_ONLY','delivery_runtime':'NOT_REVALIDATED_IN_THIS_COLLECTION','source_url':i110['url']}]
intake['change_dispositions']=[{'issue':n,'disposition':disp,'effective_ac_change':effective,'state':by[n]['state'],'state_reason':by[n]['state_reason'],'source_comments':f'{A}/snapshot.zip#comments/{n}'} for n,disp,effective in [(125,'ACCEPTED_CR_COMPLETED',True),(126,'WITHDRAWN_NO_CHANGE',False),(127,'REJECTED_NO_CHANGE',False),(128,'WITHDRAWN_NO_AC_CHANGE',False),(130,'CHG01_CHG02_ACCEPTED_CR_COMPLETED',True)]]
intake['release_gates']={'P1_CLOSE':'HOLD','D21':'OPEN','P2_ARCH_FREEZE':'HOLD','P2_IAC_STAGE_A':'NOT_READY','WBS':'STALE_REGENERATION_REQUIRED','FULL_RELEASE_SET':'NOT_GENERATED','PUBLICATION':'NOT_READY','RUNTIME':'NOT_EXECUTED_BY_THIS_TASK'}
intake['schedule_replan_20260930']['latest_refresh']=A+'/dependency-schedule.json'
put('audit/canonical-candidate-20260927/intake.json',dump(intake))
s=json.loads(raw['previous_files']['audit/project-schedule-replan-20260930/schedule.json']);s['generated_at_kst']=T
s['p0_schedule']={str(n):[by[n]['properties'].get('Start'),by[n]['properties'].get('End'),days(by[n]['properties'].get('Start'),by[n]['properties'].get('End'))] for n in map(int,s['p0_schedule'])}
s['p1_decision_windows']={};s['p1_unscheduled']=[]
for n in [25,26,27,40,41,44,48,51,95,120,121]:
 p=by[n]['properties'];wd=days(p.get('Start'),p.get('End'))
 if wd is None:s['p1_unscheduled'].append(n)
 else:s['p1_decision_windows'][str(n)]=[p['Start'],p['End'],wd]
s['phase2_available_workdays']=days(s['phase2_start'],s['project_end'])
s['source_index']=A+'/issue-index.json';s['dependency_contract']=A+'/dependency-schedule.json'
s['schedule_rule']='Inclusive weekday count, exclude 2026-10-05 and 2026-10-09; dates are planning targets, never actual execution/acceptance.'
put('audit/project-schedule-replan-20260930/schedule.json',dump(s))
dep={'generated_at_kst':T,'sequence':[{'step':1,'issue':36,'checkpoint':'D21 transport decision','target':'2026-10-08','status':'OPEN','requires':['Education-site UDP500/4500 packet path observed','Return/NAT-T/IKE result reviewed','Security exposure, return-route and SPOF disposition']},{'step':2,'issue':34,'checkpoint':'Final Architecture Freeze','target':'2026-10-08','status':'HOLD','requires':['D21 selected transport','remaining subnet/AZ/topology/state/security contracts frozen']},{'step':3,'issue':35,'checkpoint':'Stage-A handoff','target':'2026-10-08','status':'NOT_READY','requires':['Final Architecture Freeze','exact source/schema + reviewed plan + handoff evidence']},{'step':4,'issue':37,'checkpoint':'VPN start','target':'2026-10-12','status':'CONDITIONAL','requires':['D21 decision','Stage-A accepted handoff']}],'same_day_capacity':'UNVERIFIED: D21 -> Freeze -> Stage-A on 10-08 is ordered, not proof of sufficient work time; replan #37/G4 if any gate or handoff slips.','wip_rule':'10-07 preliminary architecture input is precheck. D21 decision and final Freeze are serialized for Lead 이권욱; do not claim workload feasibility from date arithmetic.','resource_mutations':'NOT_AUTHORIZED_BY_THIS_CHANGE','issue_body_dependency_sections':'Unchanged; subordinate same-day checkpoint ordering added to permitted Schedule Note metadata and audit.','issue_metadata_applied':[34,35,36]}
put(A+'/dependency-schedule.json',dump(dep))
e=[]
for w in writes['writes']:
 assert w['body_exact_match'] and w['unrelated_metadata_unchanged']
 before=w['before_body'];after=w['after_body'];n=w['number']
 diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=f'issue-{n}-before',tofile=f'issue-{n}-after'))
 put(A+f'/issue-diffs/issue-{n}.diff',diff)
 e.append({k:v for k,v in w.items() if k not in ['before_body','after_body']}|{'before_sha256':sha(before.encode()),'after_sha256':sha(after.encode()),'diff':f'issue-diffs/issue-{n}.diff'})
put(A+'/issue-write-verification.json',dump(e))
close={'target_date_kst':'2026-10-06','status':'PENDING_ACTUAL_CLOSE_RESULT','required_source_issues':[30,31,32],'allowed_dispositions':['MET','NOT MET-RISK ACCEPTED','KNOWN ISSUE','APPROVED DEFERRED'],'records':[],'required_per_record':['record_id','acceptance_owner','disposition','decision_url','evidence_repository','evidence_commit','evidence_path','runtime_timestamp_kst','source_sha','remaining_action','owner','due_or_approved_deferred_reason'],'rule':'No fabricated records. Populate only from Lead Close decision plus original evidence; null/empty input never means MET. Recollect all changed source heads and issue bodies before final generation.'}
put(A+'/phase1-close-input.json',dump(close))
regen={'status':'PREPARATION_EXECUTED_FULL_RELEASE_NOT_GENERATED','source_index':'issue-index.json','source_snapshot':'snapshot.zip','input_record_count':len(records),'previous_wbs_record_count':58,'required_outputs':['Baseline','WBS/Gantt with all current applicable records','Ticket Pack','78 Description snapshots','Release Notes','Manifest','SHA256SUMS','WEB snapshot','Distribution ZIP + sidecar'],'blocking_inputs':['10/6 Phase 1 Close disposition not available','D21 and Architecture/Stage-A contract unresolved','Source metadata anomalies require explicit resolution; preserve absent values as unknown'],'metadata_anomalies':anomalies,'generation_order':['Refresh source heads and issues/comments, revalidate source ancestry','Apply approved dispositions and resolve source metadata anomalies without inventing AC/status','Populate phase1-close-input.json with original evidence references','Generate complete Baseline, Ticket Pack/Descriptions, WBS from one Record ID registry','Recalculate working days and individual absences; verify checkpoint dependencies and owner WIP','Render workbook and verify formulas, all sheet ranges and record coverage','Generate Manifest/SHA256SUMS/WEB/ZIP from exact candidate bytes','Run canonical-integrity and record exact-head review; merge/publication require separate authorization'],'boundaries':{'STATIC':'Executed for intake/metadata/date/dependency/ancestry','MOCK':'NOT_RUN','CI':'NOT_RUN_FOR_THIS_GENERATOR','RUNTIME':'NOT_RUN','REVIEW':'NOT_APPROVED','MERGE':'NOT_DONE','PUBLICATION':'NOT_DONE'}}
put(A+'/regeneration-plan.json',dump(regen))
# Regenerate a complete metadata index, not a falsely complete release Ticket Pack.
lines=['# v3.1.21 Ticket Pack 재생성 입력','',f'수집: {T}. 78개 이슈의 현행 속성. 원문과 AC는 snapshot.zip에 바이트 보존.','', '이 파일은 입력 인덱스이며 최종 Canonical Ticket Pack이 아니다. 상태를 임의 보정하지 않는다.','', '| Issue | Record ID | Phase | Priority | Body Status | GitHub state | Start | End | Lead |','|---|---|---|---|---|---|---|---|---|']
for r in records:
 p=r['properties'];vals=[f"[#{r['number']}]({r['url']})",p.get('Record ID'),p.get('Phase'),p.get('Priority'),p.get('Status'),r['state']+'/'+str(r['state_reason'] or ''),p.get('Start'),p.get('End'),p.get('Lead')]
 lines.append('| '+' | '.join(str(v or '미확인').replace('|','/') for v in vals)+' |')
put(A+'/proposed/Ticket-Pack-input.md','\n'.join(lines)+'\n')
put(A+'/proposed/Baseline-change-input.md',f'''# v3.1.21 Baseline 재생성 변경 입력

기준: docs-v3.1.20 RELEASED. 수집 {T}. 이 문서는 변경 입력이며 전체 Baseline을 대체하지 않는다.

- 발행 이후 14개 저장소 병합 입력 {total}건( main 계보 {total-len(non_main)}건, 후보 동기화 {len(non_main)}건). 기존 intake 대비 {delta}건 추가.
- #110: Done/closed(completed) Decision 완료를 반영. Delivery Runtime 완료와 분리.
- #125: accepted/completed; encryption·backup·rollback P1 유지, preventive rotation NOT MET/RISK ACCEPTED.
- #126: withdrawn/no change; 원 AC 유지.
- #127: rejected/no change; source-preservation 필수 유지.
- #128: withdrawn/no AC change. MTU/identity 수용은 기존 #10 evidence interpretation. Body Status Todo drift는 미해소.
- #130: CHG01/02 accepted/completed; #14 OID-02 추적 및 #13 AC05A/05B 생산·인수 분리, HBR end-to-end gate 유지.
- 일정: D21 10-08 → #34 최종 Freeze 10-08 → #35 Stage-A 10-08(조건부) → #37 10-12. 잔여 사양/당일 작업창은 미검증.
- D21 preferred AWS EC2/EIP Relay는 후보이며 확정 사양 아님. UDP 경로 관측, security/return-route/SPOF 결정 전 임의 승격 금지.
- Phase 1 Close 10-06 결과는 아직 없음. phase1-close-input.json에 실제 판정/원본 증적 수신 후 반영.
- 기존 v3.1.20 정본/Tag/Assets 및 CURRENT.md 불변. WBS 58행은 78개 Issue 입력과 전량 대조 필요.

상세 원문은 snapshot.zip, 해시는 issue-index.json, 다음 생성 규칙은 regeneration-plan.json 참조.
''')
readme=f'''# v3.1.21 정본 수집 최신화 — 2026-10-03

최종 수집 시각: {T}. 최초 스냅샷 기록: {raw['initial_snapshot_serialized_at_kst']}. 최초 원격조회 시작 시각은 별도 계측하지 않았다. 비원자적 스냅샷이며 각 Issue updated_at과 source HEAD 재조회 시작/종료시각을 별도 보존한다.

- 기준 정본: docs-v3.1.20 / RELEASED (Release API 확인)
- 입력 candidate HEAD: `{raw['candidate_head']}`
- baseline main: `{raw['main_sha']}`; candidate behind=0 / ahead={raw['comparison']['ahead']}
- 14개 저장소 / Issue 78건 / 발행 이후 merged {total}건 / 기존 대비 추가 {delta}건
- main 계보 입력 {total-len(non_main)}건, 후보 브랜치 동기화 #131/#133 2건을 구분한다.
- 수집 목록 누락 0은 이 조회 범위/시점 기준이며 Runtime 또는 AC PASS가 아니다.

## 실제 반영

intake.json, 두 candidate README, schedule.json을 갱신했다. repository-source-heads.json에 main/PR head/merge SHA/대상 브랜치/계보 검증을 고정했다. #34 Start/End를 10-08로, #34/#35/#36 Schedule Note를 순서와 HOLD 조건으로 정정하고 반영 후 본문 정확 일치 및 다른 메타데이터 불변을 확인했다.

## 검증·한계

STATIC: 병합 목록의 전체 페이지, merge SHA 계보, Record ID 유일성, 근무일 계산, 이슈 쓰기 전후 차이 검증. snapshot ZIP SHA256은 무결성만 확인한다. CI/Runtime은 이 작업에서 실행하지 않았다. 원본 Runtime의 성공을 재인수하지 않는다.

원본 메타데이터 이상 {len(anomalies)}건은 issue-index.json과 regeneration-plan.json에 남겼다. 부족한 값이나 closed/not_planned의 해석을 임의 Done/Cancelled로 고치지 않았다. 기존 workbook은 read-only 검사로 9개 시트·WBS 58개 레코드 및 stale 정본 표기를 확인했다. Workbook 수정·계산·시각 QA는 미실행이다.

## 재현

`snapshot.zip`를 UTF-8 JSON으로 풀면 원문 이슈/선택 댓글/PR/HEAD/계보/쓰기 전후 기록이 복원된다. `snapshot-integrity.json`의 압축/해제 해시를 검증한다. 이 감사 디렉터리에서 `python regenerate.py --from-snapshot <새 출력 디렉터리>`를 실행하면 네트워크 없이 동일 수집 산출물을 재생성한다(Python 3.12.14 검증). 출력 루트 기준 `SHA256SUMS`를 대조한다. 이 checksum은 audit 무결성용이며 Release SHA256SUMS가 아니다. 생성 규칙은 `regeneration-plan.json`, 전체 78건 입력 인덱스는 `proposed/Ticket-Pack-input.md`, Baseline 변경 입력은 `proposed/Baseline-change-input.md`다.

## 남은 HOLD

P1_CLOSE=HOLD / D21=OPEN / P2_ARCH_FREEZE=HOLD / P2_IAC_STAGE_A=NOT_READY. 10-08 연속 인계 시간은 미검증이다. 10-06 실제 Close와 미결 metadata/사양을 반영한 뒤 WBS/Baseline/Ticket Pack/Description 전체 재생성, Workbook QA, Manifest/SHA256SUMS/WEB/ZIP 검증이 필요하다. FULL_RELEASE_SET=NOT_GENERATED / MERGE=NOT_DONE / PUBLICATION=NOT_READY.
'''
put(A+'/README.md',readme)
for path in ['audit/canonical-candidate-20260927/README.md','releases/v3.1.21/README.md']:
 history=raw['previous_files'][path]
 prefix=f'''# v3.1.21 Candidate — 최신 수집 2026-10-03

**CANDIDATE / COLLECTING / NOT RELEASED**

- Source main: `{raw['main_sha']}`
- Candidate 입력 HEAD: `{raw['candidate_head']}` / behind=0
- 수집 시각(KST): {T}
- 14개 저장소 merged {total}건, 기존 대비 {delta}건 추가. infra-dns 신규 수집 포함.
- 상세·HEAD·원문·diff·생성 규칙: `{A}/README.md`
- #110=Done Decision; #125/#130=CR completed; #126/#127/#128=no-change 이력. Runtime 완료와 분리.
- #34 최종 Freeze 목표=10-08 D21 이후; #35 Stage-A=동일일 조건부 handoff. source schedule.json 최신 이슈에서 재생성.
- P1 Close HOLD / D21 OPEN / Architecture HOLD / Stage-A NOT_READY.
- 기존 WBS STALE; 78개 Record 입력 인덱스/Baseline 변경 입력/10-06 Close 수신 구조 생성. 전체 Release Set은 NOT_GENERATED.

아래는 이전 수집 당시 원문이다. 오래된 source HEAD/날짜/#110 To Do/CR 미결 표기는 현행 판정으로 사용하지 않는다. 현재 상태는 위 스냅샷과 intake.json이 기준이다.

<details>
<summary>이전 수집 기록 — 역사적 원문</summary>

'''
 put(path,prefix+history+'\n</details>\n')
for path in ['audit/canonical-candidate-20260927/intake.json','audit/canonical-candidate-20260927/README.md','audit/project-schedule-replan-20260930/schedule.json','releases/v3.1.21/README.md']:
 before=raw['previous_files'][path];after=(O/path).read_text(encoding='utf-8')
 put(A+'/file-diffs/'+path.replace('/','__')+'.diff',''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+path,tofile='b/'+path)))
validation={'STATIC':'PASS_FOR_INTAKE_SCOPE','source_record_count':len(records),'unique_record_ids':len(set(ids)),'repository_count':len(repositories),'merged_count':total,'main_merged_count':total-len(non_main),'candidate_sync_count':len(non_main),'new_inputs':delta,'ancestry_verified':True,'missing_inputs_at_capture':0,'baseline_behind':raw['comparison']['behind'],'phase2_workdays':s['phase2_available_workdays'],'issue_write_exact_match':all(w['body_exact_match'] and w['unrelated_metadata_unchanged'] for w in writes['writes']),'metadata_anomalies':anomalies,'full_release_status':'NOT_GENERATED'}
put(A+'/validation.json',dump(validation))
put(A+'/regenerate.py',Path(__file__).read_bytes())
put(A+'/SHA256SUMS',''.join(f'{sha(p.read_bytes())}  {p.relative_to(O).as_posix()}\n' for p in sorted(O.rglob('*')) if p.is_file() and p.name!='SHA256SUMS'))
print(dump(validation))
