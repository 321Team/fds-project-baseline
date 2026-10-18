const fs=require('fs'),path=require('path'),crypto=require('crypto');
const out=__dirname,qa=path.resolve(out,'..'),current=path.resolve(qa,'..'),integration=path.resolve(current,'..'),workspace=path.resolve(qa,'../../../../..');
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const save=(name,obj)=>fs.writeFileSync(path.join(out,name),JSON.stringify(obj,null,2)+'\n');
const copies=[];
function copy(source,destination,role){
 source=path.resolve(source); const target=path.resolve(out,destination);
 if(!target.startsWith(out+path.sep))throw Error('Destination outside package');
 fs.mkdirSync(path.dirname(target),{recursive:true});fs.copyFileSync(source,target);
 if(hash(source)!==hash(target))throw Error('Copy mismatch: '+source);
 copies.push({path:destination,source,source_workspace_relative:path.relative(workspace,source).replaceAll('\\','/'),sha256:hash(source),bytes:fs.statSync(source).size,role});
}
const prior=JSON.parse(fs.readFileSync(path.join(qa,'FINAL_BINDING.json'),'utf8'));
const verifiedQA=prior.artifact_files_excluding_this_binding.map(x=>({path:x.path,expected_sha256:x.sha256,current_sha256:hash(path.join(qa,x.path)),unchanged:hash(path.join(qa,x.path))===x.sha256}));
if(verifiedQA.some(x=>!x.unchanged))throw Error('Frozen QA artifact changed');
const originals=prior.authoritative_originals_unchanged.map(x=>({path:path.resolve(qa,x.path),sha256:hash(path.resolve(qa,x.path)),expected_sha256:x.after_sha256,unchanged:hash(path.resolve(qa,x.path))===x.after_sha256}));
if(originals.some(x=>!x.unchanged))throw Error('Original changed');
for(const f of ['P1_AS_BUILT_CANDIDATE.md','candidate/architecture/P1_LOGICAL_AS_BUILT_20261015.mmd','candidate/architecture/P1_PHYSICAL_AS_BUILT_20261015.mmd','SOURCE_BINDING.json','FINAL_BINDING.json'])copy(path.join(current,f),'payload/current/'+f,'FROZEN_SOURCE_OR_SOURCE_BINDING');
const sourceBinding=JSON.parse(fs.readFileSync(path.join(current,'SOURCE_BINDING.json'),'utf8'));
for(const x of sourceBinding.consumed_existing_receipts){if(hash(path.join(current,x.copy))!==x.sha256)throw Error('Receipt mismatch');copy(path.join(current,x.copy),'payload/current/'+x.copy,'EXISTING_RECEIPT_SNAPSHOT');}
for(const f of ['physical.svg','physical.png','logical.svg','RENDER_RECEIPT.json','RENDERER_ASSET_MANIFEST.json','RENDER_CONFIG.json','render-local.cjs','VISUAL_REVIEW.md','SOURCE_SEMANTICS_CHECK.json','GEOMETRY_REVIEW.json','PROPOSAL_GEOMETRY_REVIEW.json','LAYOUT_ONLY_PROPOSAL.patch','RENDERER_LAYOUT_PROPOSAL.patch','FINAL_BINDING.json'])copy(path.join(qa,f),'payload/current/render-validation-20261016/'+f,'REUSED_QA_NO_RERUN');
for(const f of ['P1_LOGICAL_LAYOUT_PROPOSAL.mmd','render-proposal.cjs','RENDER_CONFIG.json','RENDER_RECEIPT.json','RENDERER_ASSET_MANIFEST.json','logical.svg','logical.png','logical-geometry.json','final-label-inspection.png','final-left-inspection.png','final-right-inspection.png','FINAL_INSPECTION_CROPS.json'])copy(path.join(qa,'proposal-layout-constraints',f),'payload/current/render-validation-20261016/proposal-layout-constraints/'+f,'SELECTED_LOGICAL_LAYOUT_PROPOSAL');
copy(path.resolve(integration,'../references/N02--README.md'),'references/ARCHITECTURE_RULE.md','EXISTING_APPROVED_SOURCE_DERIVATIVE_RULE');
const d07=path.join(integration,'defect-d07-reply-linkage-20261016');
for(const f of ['D07_LEDGER_ROW.md','FINAL_HANDOFF.md','D07_IMPACT.json','FINAL_BINDING.json','SOURCE_BINDING.json','references/COMMENT_6211817978.json'])copy(path.join(d07,f),'references/D07/'+f,'EXISTING_D07_CANDIDATE_EXACT_COPY_NO_NEW_ROW');
copy(path.join(integration,'app-contract-sections5-7-ready-20261016/references/BASE_CONTRACT.md'),'references/app-contract-sections5-7-ready-20261016/references/BASE_CONTRACT.md','EXISTING_D07_HANDOFF_DEPENDENCY');
copy(path.resolve(integration,'../SOURCE_INDEX.json'),'SOURCE_INDEX.json','EXISTING_PROVENANCE_INDEX_NO_SOURCE_REREVIEW');
copy(path.resolve(integration,'../FINAL_HEAD_READBACK.json'),'FINAL_HEAD_READBACK.json','HISTORICAL_HEAD_READBACK_NOT_LIVE');
copy(path.join(integration,'as-built-candidate/P1_AS_BUILT_CANDIDATE.md'),'payload/as-built-candidate/P1_AS_BUILT_CANDIDATE.md','HISTORICAL_COMPARISON_ONLY_NOT_SELECTED');
const external=[path.join(current,'A1_UPDATED_DECISION_CARD.md'),path.resolve(integration,'../SOURCE_INDEX.json'),path.resolve(integration,'../FINAL_HEAD_READBACK.json'),path.join(integration,'as-built-candidate/P1_AS_BUILT_CANDIDATE.md')].map(source=>({source,sha256:hash(source),bytes:fs.statSync(source).size,role:'WORKSPACE_PROVENANCE_REFERENCE_NOT_SELECTED_FOR_ADOPTION'}));
const rendererAssets=JSON.parse(fs.readFileSync(path.join(qa,'proposal-layout-constraints/RENDERER_ASSET_MANIFEST.json'),'utf8')).map(x=>({...x,current_sha256:hash(x.file),hash_matches:hash(x.file)===x.sha256}));
if(rendererAssets.some(x=>!x.hash_matches))throw Error('Renderer asset changed since QA');
save('SOURCE_BINDING.json',{at_kst:new Date().toLocaleString('sv-SE',{timeZone:'Asia/Seoul'})+' KST',scope:'WORKSPACE_BOUND_ADOPTION_REVIEW_PACKAGE; NOT A PUBLISHED OR PORTABLE SOURCE RELEASE',copied_files:copies,workspace_provenance_references:external,originals,prior_qa_binding:{source:path.join(qa,'FINAL_BINDING.json'),sha256:hash(path.join(qa,'FINAL_BINDING.json')),status:prior.status},prior_54_artifacts:verifiedQA,installed_renderer_assets:rendererAssets,render_QA_rerun:false,external_fetches:0});
console.log(JSON.stringify({copied_files:copies.length,qa_artifacts_verified:verifiedQA.length,originals_verified:originals.length,renderer_assets_verified:rendererAssets.length,workspace_references:external,adoption_root:out}));
