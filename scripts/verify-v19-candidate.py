#!/usr/bin/env python3
"""Read-only v19 source, Description, WBS and package-content checks."""
import collections,datetime,hashlib,json,re,sys,zipfile,xml.etree.ElementTree as E
from pathlib import Path
R=Path(__file__).resolve().parents[1];V='v3.1.19';N={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def require(ok,msg):
 if not ok:raise ValueError(msg)
def read(p):return (R/p).read_text()
def props(body,keys):
 p={}
 for l in body.splitlines():
  m=re.match(r'^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|$',l)
  if m and m[1] in keys and m[1] not in p:p[m[1]]=m[2].replace('\\|','|').replace('<br>','\n')
 return p
def serial(s):
 return (datetime.date.fromisoformat(s)-datetime.date(1899,12,30)).days if re.fullmatch(r'\d{4}-\d{2}-\d{2}',s) else ''
def workbook(path):
 with zipfile.ZipFile(path) as z:
  require(z.testzip() is None,'XLSX CRC')
  strings=[''.join(x.itertext()) for x in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',N)] if 'xl/sharedStrings.xml' in z.namelist() else []
  sheets={};formulas=0
  for i,s in enumerate(E.fromstring(z.read('xl/workbook.xml')).find('m:sheets',N),1):
   cells={}
   for c in E.fromstring(z.read(f'xl/worksheets/sheet{i}.xml')).findall('.//m:sheetData/m:row/m:c',N):
    v=c.findtext('m:v',default='',namespaces=N);t=c.attrib.get('t');f=c.findtext('m:f',namespaces=N)
    require(t!='e',f'Excel error {s.attrib["name"]}!{c.attrib["r"]}')
    if t=='s':v=strings[int(v)]
    elif t=='inlineStr':v=''.join(c.find('m:is',N).itertext())
    elif v and t not in ['str','b']:
     try:v=float(v);v=int(v) if v.is_integer() else v
     except ValueError:pass
    if f:formulas+=1;require('#REF!' not in f,'broken formula reference')
    cells[c.attrib['r']]={'v':v,'f':f}
   sheets[s.attrib['name']]=cells
  charts=len([p for p in z.namelist() if re.fullmatch(r'xl/(?:drawings/)?charts/[^/]+\.xml',p)])
 return sheets,formulas,charts
data=json.loads(read(f'tickets/{V}/canonical-records.json'));records=data['records'];byid={x['record_id']:x for x in records}
require(len(records)==len(byid)==67,'67 unique records');planned={r['record_id']:r for r in records if r['planning_record']};require(len(planned)==58,'58 planning records')
require(all(r['milestone'] for r in records),'milestone coverage')
for r in records:
 source=json.loads(read(f'tickets/{V}/sources/issue-{r["issue"]}.json'));body=source['body'];description=read(r['description']);keys=r['properties'].keys()
 require(hashlib.sha256(body.encode()).hexdigest()==r['source_body_sha256'],'source body hash')
 require(props(body,keys)==r['source_properties'],'source properties')
 require(props(description,keys)==r['properties'],'description properties '+r['record_id'])
 require(body in description,'original body retained')
 require(len(re.findall(r'- \[[xX]\]',description))==len(re.findall(r'- \[[xX]\]',body)),'new checked AC')
 require((source['state']=='closed')==(r['properties']['Status']=='Done'),'lifecycle mismatch')
 for k in keys:
  if k not in ['Source','Schedule Note']:require(r['properties'][k]==r['source_properties'][k],'unauthorized property delta')
sheets,fc,charts=workbook(R/f'wbs/FDS_{V}_WBS_and_Gantt_v1.0.xlsx')
require(list(sheets)==['Executive Summary','WBS','Phase 1 Gantt','Phase 2 Gantt','Milestones & Decisions','Risks & Assumptions','Sources & Change Log','Team Calendar','Fast Track Plan'],'original 9 sheets')
require(charts==2,'two native charts')
val=lambda sn,c:sheets[sn].get(c,{}).get('v','')
rowids={val('WBS',f'A{n}'):n for n in range(4,62)};require(set(rowids)==set(planned),'WBS IDs')
for rid,r in planned.items():
 n=rowids[rid];p=r['properties']
 for c,k in {'A':'Record ID','C':'Phase','D':'Category','E':'Type','F':'Priority','G':'Status','L':'Lead','M':'Support','N':'Related Decision IDs','O':'Related Risk IDs','P':'Exit Criteria','Q':'Schedule Note'}.items():require(val('WBS',f'{c}{n}')==p[k],f'WBS {rid} {k}')
 require(val('WBS',f'B{n}')==r['title'],'WBS title');require(val('WBS',f'R{n}')==r['source_url'],'WBS source')
 for c,k in [('H','Start'),('I','End')]:require(val('WBS',f'{c}{n}')==serial(p[k]),'WBS dates '+rid)
 for c,k in [('J','Calendar Days'),('K','Working Days')]:
  expected=int(p[k]) if p[k].isdigit() else '';require(val('WBS',f'{c}{n}')==expected,'WBS duration '+rid+' '+k)
 require(all(sheets['WBS'][f'{c}{n}']['f'] for c in ['J','K','S']),'editable calculations')
for sn,count,phase in [('Phase 1 Gantt',33,'Phase 1'),('Phase 2 Gantt',25,'Phase 2')]:
 ids=[]
 for n in range(5,count+5):
  rid=val(sn,f'A{n}');ids.append(rid);r=planned[rid];p=r['properties']
  require(r['properties']['Phase'] in ([phase,'Design'] if phase=='Phase 1' else [phase]),'Gantt phase')
  require(val(sn,f'B{n}')==r['title'] and val(sn,f'C{n}')==p['Status'] and val(sn,f'F{n}')==p['Lead'],'Gantt labels')
  require(val(sn,f'D{n}')==serial(p['Start']) and val(sn,f'E{n}')==serial(p['End']),'Gantt dates')
 require(len(ids)==len(set(ids)),'Gantt unique')
counts=collections.Counter(r['properties']['Status'] for r in planned.values())
for n in range(12,16):require(val('Executive Summary',f'B{n}')==counts[val('Executive Summary',f'A{n}')],'summary states')
require(val('Executive Summary','B6')==58,'summary planning')
require(val('Executive Summary','B4')==serial('2026-09-17'),'asof')
require(val('Executive Summary','B5')=='3.1.19 CANDIDATE','candidate label')
for r in records:
 for target in [f'tickets/FDS_{V}_Canonical_Ticket_Update_Pack_v1.0.md',f'baseline/FDS_Project_Implementation_Baseline_{V}.md','governance/GITHUB_MILESTONE_MAP.md',f'web/FDS_{V}_Canonical_Status.html']:require(r['record_id'] in read(target),'document coverage')
require('NOT PUBLISHED' not in read('CURRENT.md').split('## Historical')[0],'CURRENT actual publication')
require('2026-09-11' in read('CURRENT.md') and 'v3.1.18' in read('CURRENT.md'),'published v18 preserved')
for s in sheets.values():require(not any('KW LEE' in str(c['v']) for c in s.values()),'incorrect KW LEE found; expected GU LEE')
result={'status':'PASS','scope':'STATIC document/source/workbook consistency; no Runtime or approval','records':67,'planning_records':58,'historical_closed_records':9,'milestone_coverage':67,'source_body_hash_matches':67,'description_properties_matches':67,'new_checked_AC':0,'workbook_sheets':9,'workbook_charts':charts,'workbook_formula_cells':fc,'workbook_formula_errors':0,'states':dict(collections.Counter(r['properties']['Status'] for r in records)),'REVIEW':'PENDING','MERGE':'NOT_EXECUTED','PUBLICATION':'NOT_EXECUTED','RUNTIME':'NOT_EXECUTED_IN_THIS_REVIEW'}
print(json.dumps(result,ensure_ascii=False,indent=2))
