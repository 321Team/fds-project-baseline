from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import argparse,ast,base64,hashlib,json,subprocess
parser=argparse.ArgumentParser(description='Read pinned GitHub source and compare AST/bytes; no app execution.')
parser.add_argument('--output',required=True,help='New result JSON path; existing output is never overwritten')
out=Path(parser.parse_args().output)
if out.exists():raise SystemExit('STOP: output already exists')
base='8eac4c982076e3c219840a13686b15c46879981f';head='affbc69beef9967f7977d09a6fec14f7fb6c0e94'
paths={'fds-engine/app/main.py':['health','ready','evaluate'],'transaction-api/app/main.py':['health','ready','create_transaction'],'fds-engine/run.py':[],'transaction-api/run.py':[],'transaction-api/app/db.py':[],'transaction-api/app/fds_client.py':[]}
def fetch(pair):
 ref,path=pair;p=subprocess.run(['gh','api',f'repos/321Team/fds-msa/contents/{path}?ref={ref}'],capture_output=True,check=True,timeout=40);x=json.loads(p.stdout);b=base64.b64decode(x['content']);assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['sha'];return pair,(b,x['sha'])
with ThreadPoolExecutor(max_workers=3) as pool:data=dict(pool.map(fetch,[(ref,path) for path in paths for ref in (base,head)]))
rows=[]
for path,names in paths.items():
 old,ob=data[base,path];new,nb=data[head,path]
 funcs=[]
 if names:
  f1={x.name:ast.dump(x,include_attributes=False) for x in ast.parse(old).body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))}
  f2={x.name:ast.dump(x,include_attributes=False) for x in ast.parse(new).body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))}
  for name in names:
   assert name in f1 and name in f2
   funcs.append({'name':name,'identical_ast':f1[name]==f2[name],'base_ast_sha256':hashlib.sha256(f1[name].encode()).hexdigest(),'candidate_ast_sha256':hashlib.sha256(f2[name].encode()).hexdigest()})
  assert all(x['identical_ast'] for x in funcs)
 else:assert old==new
 rows.append({'path':path,'base_blob':ob,'candidate_blob':nb,'base_sha256':hashlib.sha256(old).hexdigest(),'candidate_sha256':hashlib.sha256(new).hexdigest(),'whole_file_identical':old==new,'functions':funcs})
result={'schema':'P1_PROBE_CANDIDATE_CHANGE_ANALYSIS_1','observed_at_utc':datetime.now(timezone.utc).isoformat(),'repository':'321Team/fds-msa','base':base,'candidate':head,'files':rows,'candidate_scope':'PR27 base to candidate only, not historical deployed binary provenance','runtime_executed':False,'existing_tests_rerun':False,'source_code_changed':False}
with out.open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({'functions_unchanged':sum(len(x['functions']) for x in rows),'support_files_unchanged':sum(not x['functions'] and x['whole_file_identical'] for x in rows),'runtime_executed':False}))
