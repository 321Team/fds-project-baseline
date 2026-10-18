const fs=require('fs'),path=require('path'),crypto=require('crypto');
const out=__dirname,qa=path.resolve(out,'..'),current=path.resolve(qa,'..'),workspace=path.resolve(qa,'../../../../..');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>fs.readFileSync(path.resolve(out,p),'utf8');
const json=p=>JSON.parse(read(p));
const save=(p,obj)=>fs.writeFileSync(path.join(out,p),JSON.stringify(obj,null,2)+'\n');
const now=()=>new Date().toLocaleString('sv-SE',{timeZone:'Asia/Seoul'})+' KST';
const source=json('SOURCE_BINDING.json');
const roles=[
 ['explanation_original','payload/current/P1_AS_BUILT_CANDIDATE.md','PROPOSED_WITH_ADDENDUM'],
 ['render_status_addendum','RENDER_ADOPTION_ADDENDUM.md','REQUIRED_COMPANION_FOR_EXPLANATION'],
 ['logical_source','payload/current/render-validation-20261016/proposal-layout-constraints/P1_LOGICAL_LAYOUT_PROPOSAL.mmd','PROPOSED_EDITABLE_SOURCE'],
 ['physical_source','payload/current/candidate/architecture/P1_PHYSICAL_AS_BUILT_20261015.mmd','PROPOSED_EDITABLE_SOURCE'],
 ['logical_renderer','payload/current/render-validation-20261016/proposal-layout-constraints/render-proposal.cjs','REQUIRED_RENDER_CONTRACT'],
 ['renderer_config','payload/current/render-validation-20261016/proposal-layout-constraints/RENDER_CONFIG.json','REQUIRED_RENDER_CONTRACT'],
 ['logical_svg','payload/current/render-validation-20261016/proposal-layout-constraints/logical.svg','PROPOSED_DERIVATIVE'],
 ['physical_svg','payload/current/render-validation-20261016/physical.svg','PROPOSED_DERIVATIVE'],
 ['original_logical_source','payload/current/candidate/architecture/P1_LOGICAL_AS_BUILT_20261015.mmd','COMPARISON_ONLY_NOT_SELECTED'],
 ['original_logical_svg','payload/current/render-validation-20261016/logical.svg','DIAGNOSTIC_ONLY_VISUAL_FINDINGS_REMAIN'],
 ['d07_existing_row','references/D07/D07_LEDGER_ROW.md','SEPARATE_EXISTING_LEDGER_ADOPTION_DECISION']
];
save('ADOPTION_MANIFEST.json',{prepared_at_kst:now(),status:'READY_FOR_LOCAL_ADOPTION_REVIEW_NOT_ADOPTED',official_source_version:null,official_destination:null,official_distribution_format:null,adopted:false,source_requirements_baseline:'docs-v3.1.21 / 979facb98de8ca1f1e2ce22f38b27ac3366f3fc3',entries:roles.map(([role,file,status])=>({role,path:file,sha256:hash(path.join(out,file)),bytes:fs.statSync(path.join(out,file)).size,status})),render_semantics:'Reuses unchanged prior SOURCE_SEMANTICS_CHECK: 21 nodes / 22 visible edges / same labels; four invisible constraints only.',render_contract:'Mermaid 11.17.0 + exact renderer/config + PM -> MGW label translate(160,12); MMD alone does not reproduce selected SVG.',formal_approval_or_freeze:false});
save('DECISION_FIELDS.json',{status:'UNDECIDED_TEMPLATE_NOT_APPROVAL',prepared_at_kst:now(),new_approver_assigned:false,fields:[
 {id:'source_scope',value:null,recommendation:'Select manifest explanation+addendum, layout-only logical, unchanged physical, mandatory renderer/config and bound derivatives together.'},
 {id:'official_source_version_and_release_relation',value:{official_source_version:null,release_relation:null},recommendation:'Preserve requirements baseline docs-v3.1.21; explicitly decide source revision and relation to an official Release. Do not promote local date filenames to version numbers.'},
 {id:'destination',value:{repository:null,files:{explanation:null,addendum_or_integrated_explanation:null,logical_mmd:null,physical_mmd:null,renderer:null,config:null,logical_svg:null,physical_svg:null,manifest:null}},recommendation:{repository:'321Team/fds-project-baseline',directory:'architecture/',exact_filenames:'Decision required for each file; no official path assigned by this task.'}},
 {id:'distribution_format',value:{primary:null,include_png:null,include_pdf:null},recommendation:{primary:'SVG',editable_sources:'MMD + explanation/addendum',png:'QA/reference unless selected',pdf:'Not generated'}},
 {id:'adoption_review_record',value:{decision:null,decision_maker:null,recorded_at_kst:null,exact_manifest_sha256:null,record_location:null},recommendation:'Record actual decision and exact target; no new approver assigned.'},
 {id:'D07_ledger_linkage',value:{adopt_or_link:null,existing_ledger_location:null,receipt_location:null},recommendation:'Reuse existing D07_LEDGER_ROW.md exactly; connect to existing #20 ledger, no duplicate issue or new row authored.'},
 {id:'publication_and_freeze',value:{source_adoption:null,architecture_approval:null,publication:null,critical_document_defects_zero:null,DOC_O01_acceptance:null,Freeze:null},recommendation:'Keep each decision distinct. Local rendering/package integrity does not fill these fields.'}
]});
const actualOrigins=new Map();
for(const x of json('payload/current/SOURCE_BINDING.json').consumed_existing_receipts)actualOrigins.set(path.resolve(current,x.copy),path.resolve(workspace,x.source));
const linksOf=text=>[...text.matchAll(/\]\(([^)]+)\)/g)].map(x=>x[1].replace(/^<|>$/g,''));
const newDocs=['CURRENT_TASK.md','HANDOFF.md','ADOPTION_DECISION_CARD.md','RENDER_ADOPTION_ADDENDUM.md','D07_LINKAGE.md','RENDERER_DEPENDENCIES.md'];
const directSourceDocs=['payload/current/P1_AS_BUILT_CANDIDATE.md','references/D07/D07_LEDGER_ROW.md','references/D07/FINAL_HANDOFF.md'];
const activeLinks=[];
for(const file of [...newDocs,...directSourceDocs])for(const target of linksOf(read(file))){
 if(/^https?:|^#/.test(target)){activeLinks.push({from:file,target,type:'external_or_anchor_not_requeried'});continue;}
 const absolute=path.resolve(path.dirname(path.join(out,file)),target.split('#')[0]);
 const pending=['FINAL_BINDING.json','PACKAGE_CHECKS.json','SOURCE_LINK_MAP.json'].includes(path.relative(out,absolute).replaceAll('\\','/'));
 activeLinks.push({from:file,target,type:'local',resolved:absolute,exists:pending||fs.existsSync(absolute),generated_below:pending});
}
const missingActive=activeLinks.filter(x=>x.type==='local'&&!x.exists);if(missingActive.length)throw Error('Review link missing: '+JSON.stringify(missingActive));
const archiveLinks=[];
for(const x of source.copied_files.filter(x=>x.path.endsWith('.md'))){
 const origin=actualOrigins.get(x.source)||x.source;
 for(const target of linksOf(read(x.path))){
  if(/^https?:|^#/.test(target))continue;
  const canonical=path.resolve(path.dirname(origin),target.split('#')[0]);
  const packaged=path.resolve(path.dirname(path.join(out,x.path)),target.split('#')[0]);
  archiveLinks.push({snapshot:x.path,target,source_origin:origin,canonical_target:canonical,canonical_target_exists:fs.existsSync(canonical),packaged_relative_target_exists:fs.existsSync(packaged),scope:'Historical source link retained verbatim; not an instruction to re-review or republish its dependency tree.'});
 }
}
save('SOURCE_LINK_MAP.json',{at_kst:now(),scope:'Active review entry links and core-source direct links checked locally. Historical preserved source links are separately mapped to their original context; no remote fetch or recursive source re-review.',active_review_links:activeLinks,historical_snapshot_links:archiveLinks,external_links_freshness:'NOT_REQUERIED'});
const copyChecks=source.copied_files.map(x=>({path:x.path,copy_hash_matches:hash(path.join(out,x.path))===x.sha256,source_unchanged:hash(x.source)===x.sha256}));
if(copyChecks.some(x=>!x.copy_hash_matches||!x.source_unchanged))throw Error('Copied/source input hash changed');
const prior54=source.prior_54_artifacts.map(x=>({path:x.path,unchanged:hash(path.join(qa,x.path))===x.expected_sha256}));
if(prior54.some(x=>!x.unchanged))throw Error('Prior QA input changed');
const originalChecks=source.originals.map(x=>({path:x.path,sha256:hash(x.path),unchanged:hash(x.path)===x.expected_sha256}));
if(originalChecks.some(x=>!x.unchanged))throw Error('Original source or parent binding changed');
const frozenQA=hash(source.prior_qa_binding.source)===source.prior_qa_binding.sha256;if(!frozenQA)throw Error('QA binding changed');
const proof=json('payload/current/render-validation-20261016/SOURCE_SEMANTICS_CHECK.json');
if(proof.status!=='PASS'||proof.nodes!==21||proof.visible_edges!==22)throw Error('Prior semantic receipt unexpected');
const rendererDir=path.join(out,'payload/current/render-validation-20261016/proposal-layout-constraints');
const requiredRelative=['P1_LOGICAL_LAYOUT_PROPOSAL.mmd','../../candidate/architecture/P1_LOGICAL_AS_BUILT_20261015.mmd','../../candidate/architecture/P1_PHYSICAL_AS_BUILT_20261015.mmd','../../P1_AS_BUILT_CANDIDATE.md','../../FINAL_BINDING.json'].map(file=>({path:file,exists:fs.existsSync(path.resolve(rendererDir,file))}));
if(requiredRelative.some(x=>!x.exists))throw Error('Renderer relative input absent');
const checks={at_kst:now(),result:'PASS_MINIMUM_LOCAL_REVIEW_PACKAGE',copied_files:copyChecks,originals:originalChecks,prior_QA_54_unchanged:prior54,prior_QA_binding_unchanged:frozenQA,renderer_relative_inputs:requiredRelative,installed_renderer_asset_hashes_verified:source.installed_renderer_assets.length,active_local_links_checked:activeLinks.filter(x=>x.type==='local').length,missing_active_local_links:missingActive,history_link_scope:'Archive-only prior relative links may depend on their original workspace context; exact map retained, not falsely reported as a standalone publication link pass.',minimum_required_roles:roles.map(([role])=>role),existing_semantic_receipt_consumed:true,rerender_or_visual_QA_rerun:false,product_tests:0,CI_runs:0,external_writes:0,server_actions:0,official_version_or_new_approver_assigned:false};
save('PACKAGE_CHECKS.json',checks);
const currentTask=read('CURRENT_TASK.md').replace('현재 상태: 입력과 의존 파일 확인 중.','현재 상태: 검토 묶음·선택 카드·D-07 연결·렌더 의존성 준비 및 최소 구성/링크/해시 검사 완료. FINAL_BINDING/HANDOFF 고정. 채택·공식 발행·Freeze 미결정.');
fs.writeFileSync(path.join(out,'CURRENT_TASK.md'),currentTask);
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(x=>x.isDirectory()?walk(path.join(dir,x.name)):[path.join(dir,x.name)]);}
const artifacts=walk(out).filter(f=>f!==path.join(out,'FINAL_BINDING.json')).sort().map(f=>({path:path.relative(out,f).replaceAll('\\','/'),sha256:hash(f),bytes:fs.statSync(f).size}));
const final={completed_at_kst:now(),status:'DOC_ADOPTION_REVIEW_PACKAGE_READY_NOT_ADOPTED',scope:'PR87-independent local adoption preparation; no official records changed',source_binding_sha256:hash(path.join(out,'SOURCE_BINDING.json')),adoption_manifest_sha256:hash(path.join(out,'ADOPTION_MANIFEST.json')),handoff_sha256:hash(path.join(out,'HANDOFF.md')),checks_sha256:hash(path.join(out,'PACKAGE_CHECKS.json')),prior_QA_binding:source.prior_qa_binding,source_epoch:'as-built-current-facts-20261016 fixed facts; later Harbor inputs excluded',originals_preserved:originalChecks,prior_QA_54_unchanged:true,semantics:'Existing verified 21 nodes / 22 visible edges / same labels reused without rerun',decision_status:'All 7 decision units remain unfilled in DECISION_FIELDS.json',D07:{existing_file_sha256:'749468df858a8ec511d49f53a2596cf563e39a4bc5cc339ab3bf642ac6dd5957',body_row_sha256:'3f5de9224aea8d7a92108eb4f1d8b4f72ab55296db15fd9318a579dd1847d515',new_row_authored:false,official_write:false},actions:{new_files_only_in_this_folder:true,source_or_prior_QA_edits:0,renderer_execution:0,visual_QA_repeat:0,external_fetches:0,PR_or_CI_actions:0,server_actions:0,shared_STATUS_CONTROL_ROUND_edits:0,user_questions:0},artifact_files_excluding_this_binding:artifacts};
save('FINAL_BINDING.json',final);
for(const x of activeLinks.filter(x=>x.type==='local'))if(!fs.existsSync(x.resolved))throw Error('Final link absent: '+x.resolved);
console.log(JSON.stringify({status:final.status,completed_at_kst:final.completed_at_kst,copied_sources:copyChecks.length,prior_QA_unchanged:prior54.length,originals_preserved:originalChecks.length,renderer_assets_verified:source.installed_renderer_assets.length,active_local_links:checks.active_local_links_checked,bound_artifacts:artifacts.length,unfilled_decision_units:7,final_binding_sha256:hash(path.join(out,'FINAL_BINDING.json'))}));
