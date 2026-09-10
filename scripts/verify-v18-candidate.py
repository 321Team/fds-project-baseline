#!/usr/bin/env python3
"""Read-only consistency checks for the v3.1.18 candidate (stdlib only)."""
from pathlib import Path
import collections,datetime,hashlib,json,re,sys,xml.etree.ElementTree as E,zipfile
R=Path(__file__).resolve().parents[1];V='v3.1.18'
N={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def require(ok,message):
 if not ok:raise ValueError(message)
def props(body):
 m=re.search(r'\| Property \| 입력값 \|\n\|[-| ]+\|\n((?:\|.*\n)+)',body)
 require(m is not None,'17-field property table missing')
 return {l.strip().split('|',2)[1].strip():l.strip().split('|',2)[2].rsplit('|',1)[0].strip().replace('\\|','|') for l in m[1].splitlines()}
def excelday(t):
 if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',t):return None
 return (datetime.date.fromisoformat(t)-datetime.date(1899,12,30)).days
def workbook(path):
 with zipfile.ZipFile(path) as z:
  require(z.testzip() is None,'XLSX ZIP CRC')
  strings=[]
  if 'xl/sharedStrings.xml' in z.namelist():strings=[''.join(e.itertext()) for e in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',N)]
  wb=E.fromstring(z.read('xl/workbook.xml'));sheets={};errors=[];formula_count=0
  # The preserved workbook uses its original eight worksheet order/paths.
  for i,s in enumerate(wb.find('m:sheets',N),1):
   root=E.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'));cells={}
   for c in root.findall('.//m:sheetData/m:row/m:c',N):
    a=c.attrib['r'];v=c.findtext('m:v',default='',namespaces=N);t=c.attrib.get('t');f=c.findtext('m:f',namespaces=N)
    if t=='s':v=strings[int(v)]
    elif t=='inlineStr':v=''.join(c.find('m:is',N).itertext())
    elif t=='e':errors.append([s.attrib['name'],a,v])
    elif v!='' and t not in ('str','b'):
     try:v=float(v);v=int(v) if v.is_integer() else v
     except ValueError:pass
    if f:formula_count+=1
    cells[a]={'v':v,'f':f}
   sheets[s.attrib['name']]=cells
  require(not errors,f'Excel errors: {errors}')
  return sheets,formula_count
obj=json.loads((R/f'tickets/{V}/canonical-records.json').read_text());records=obj['records']
snapshot=json.loads((R/f'tickets/{V}/source-snapshot.json').read_text())['issues'];original={x['number']:x for x in snapshot}
require(len(records)==len(original)==64,'64 records')
require(len({x['record_id'] for x in records})==64,'unique Record IDs')
deltas=[]
for r in records:
 p=r['properties'];s=original[r['issue']];o=props(s['body']);body=(R/r['description']).read_text()
 require(len(p)==17 and set(p)==set(o),'17 properties')
 require(props(body)==p,f'Description properties: {r["record_id"]}')
 require(hashlib.sha256(s['body'].encode()).hexdigest()==r['source_body_sha256'],'original body hash')
 for k in ['Record ID','Status','Lead','Support','Start','End']:
  require(p[k]==o[k],f'Protected property {r["record_id"]}: {k}')
 require((s['state']=='closed')==(p['Status']=='Done'),'issue state / lifecycle')
 require(len(re.findall(r'- \[[xX]\]',body))<=len(re.findall(r'- \[[xX]\]',s['body'])),f'New checked AC: {r["record_id"]}')
 for k in p:
  if p[k]!=o[k]:deltas.append({'issue':r['issue'],'record_id':r['record_id'],'field':k,'before':o[k],'after':p[k]})
require(deltas==json.loads((R/f'audit/{V}/property-delta.json').read_text()),'complete delta ledger')
sheets,fc=workbook(R/f'wbs/FDS_{V}_WBS_and_Gantt_v1.0.xlsx')
require(list(sheets)==['Executive Summary','WBS','Phase 1 Gantt','Phase 2 Gantt','Milestones & Decisions','Risks & Assumptions','Sources & Change Log','Team Calendar'],'8 sheets preserved')
s=sheets['WBS'];v=lambda sh,a:sheets[sh].get(a,{}).get('v','')
planned={r['record_id']:r for r in records if r['planning_record']};require(len(planned)==55,'55 planned')
require({v('WBS',f'A{n}') for n in range(4,59)}==set(planned),'WBS IDs')
holidays={datetime.date(2026,9,24),datetime.date(2026,9,25),datetime.date(2026,10,5),datetime.date(2026,10,9)}
absence={'이하영':{datetime.date(2026,8,28),datetime.date(2026,9,8)},'이재환':{datetime.date(2026,9,4),*[datetime.date(2026,9,d) for d in range(14,18)]}}
for n in range(4,59):
 r=planned[v('WBS',f'A{n}')];p=r['properties']
 mapping={'A':'Record ID','C':'Phase','D':'Category','E':'Type','F':'Priority','G':'Status','L':'Lead','M':'Support','N':'Related Decision IDs','O':'Related Risk IDs','P':'Exit Criteria','Q':'Schedule Note','R':'Source'}
 for c,key in mapping.items():require(v('WBS',f'{c}{n}')==p[key],f'WBS {r["record_id"]} {key}')
 require(v('WBS',f'B{n}')==r['title'],'WBS title')
 for col,key in [('H','Start'),('I','End')]:require(v('WBS',f'{col}{n}')==(excelday(p[key]) or ''),'WBS plan dates')
 if excelday(p['End']):
  start=datetime.date.fromisoformat(p['Start']);end=datetime.date.fromisoformat(p['End']);days=[start+datetime.timedelta(days=d) for d in range((end-start).days+1)]
  work=sum(d.weekday()<5 and d not in holidays and d not in absence.get(p['Lead'],set()) for d in days)
  require(v('WBS',f'J{n}')==len(days)==int(p['Calendar Days']),'Calendar Days')
  require(v('WBS',f'K{n}')==work==int(p['Working Days']),f'Working Days {r["record_id"]}')
 else:require(v('WBS',f'J{n}')==v('WBS',f'K{n}')=='','TBD duration')
 require("$A$5:$A$11" in s[f'K{n}']['f'] and "$C$5:$C$11" in s[f'K{n}']['f'],'absence formula range')
for cell,expected in {'B6':55,'B7':32,'B8':13,'B12':7,'B13':9,'B14':0,'B15':39,'E12':29,'E13':14,'E14':12}.items():require(v('Executive Summary',cell)==expected,'summary '+cell)
require(v('WBS','F2')==55,'WBS header count')
for sn,count in [('Phase 1 Gantt',30),('Phase 2 Gantt',25)]:
 ids=[]
 for n in range(5,count+5):
  rid=v(sn,f'A{n}');ids.append(rid);r=planned[rid];p=r['properties']
  require(v(sn,f'B{n}')==r['title'] and v(sn,f'C{n}')==p['Status'] and v(sn,f'F{n}')==p['Lead'],'Gantt links')
  require(v(sn,f'D{n}')==(excelday(p['Start']) or '') and v(sn,f'E{n}')==(excelday(p['End']) or ''),'Gantt dates')
 require(len(set(ids))==count,'Gantt duplicate IDs')
expected={r['record_id'] for r in planned.values() if r['properties']['Type'] in ['Milestone','Decision','Change Request']}
mdids={c['v'] for a,c in sheets['Milestones & Decisions'].items() if re.fullmatch(r'A\d+',a) and int(a[1:])>=4}
require(expected<=mdids,'Milestone / Decision coverage')
require((R/'CURRENT.md').read_text().find('| Current RELEASED version | v3.1.17 |')>=0,'current release unchanged')
print(json.dumps({'status':'PASS','scope':'local candidate consistency; no runtime or release approval','records':64,'planning':55,'historical_closed':9,'states':dict(collections.Counter(r['properties']['Status'] for r in records)),'protected_property_differences':0,'property_deltas':len(deltas),'new_checked_AC':0,'workbook_sheets':len(sheets),'workbook_formulas':fc,'workbook_errors':0,'working_day_mismatches':0,'description_property_mismatches':0,'milestone_decision_coverage':len(expected),'ci':'NOT RUN','release_assets':'NOT RUN','live_issue_updates':'NOT RUN'},ensure_ascii=False,indent=2))
