// Offline rendering from existing VS Code assets; no install and no remote upload.
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const crypto = require('node:crypto');
const { chromium } = require('C:/Users/soldesk/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const out = __dirname;
const parent = path.resolve(out, '..');
const vsRoot = 'C:/Users/soldesk/AppData/Local/Programs/Microsoft VS Code/7debcd0e2a/resources/app';
const assetRoot = path.join(vsRoot, 'extensions/markdown-language-features/markdown-editor-out');
const moduleName = 'mermaid.core-S5KCHHL2.js';
const chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const hash = data => crypto.createHash('sha256').update(data).digest('hex');
const hashFile = p => hash(fs.readFileSync(p));
const now = () => new Date().toLocaleString('sv-SE', { timeZone: 'Asia/Seoul' }) + ' KST';
const save = (name, data) => fs.writeFileSync(path.join(out, name), typeof data === 'string' ? data : JSON.stringify(data, null, 2) + '\n');
const inputs = [
  { name: 'logical', file: '../candidate/architecture/P1_LOGICAL_AS_BUILT_20261015.mmd' },
  { name: 'physical', file: '../candidate/architecture/P1_PHYSICAL_AS_BUILT_20261015.mmd' }
];
const preserved = [
  ...inputs.map(x => x.file), '../P1_AS_BUILT_CANDIDATE.md', '../FINAL_BINDING.json'
].map(rel => ({ path: rel, sha256: hashFile(path.resolve(out, rel)), bytes: fs.statSync(path.resolve(out, rel)).size }));
const config = {
  startOnLoad: false, securityLevel: 'strict', theme: 'default',
  fontFamily: 'Arial', fontSize: 16, deterministicIds: true,
  deterministicIDSeed: 'p1-asbuilt-current-facts-20261016-render-v1',
  flowchart: { htmlLabels: false, useMaxWidth: false, curve: 'basis', nodeSpacing: 50, rankSpacing: 50, padding: 15 }
};
save('RENDER_CONFIG.json', config);
const served = new Map();
const rejectedRequests = [];
const logs = [];
const html = '<!doctype html><html><head><meta charset="UTF-8"><title>Local As-built rendering</title><style>html,body{margin:0;background:white;}body{padding:24px;font-family:Arial;}#drawing{display:inline-block;}svg{display:block;}</style></head><body><div id="drawing"></div></body></html>';
const server = http.createServer((req, res) => {
  const requestPath = new URL(req.url, 'http://127.0.0.1').pathname;
  if (requestPath === '/') { res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'}); res.end(html); return; }
  const filename = requestPath.startsWith('/assets/') ? decodeURIComponent(requestPath.slice(8)) : '';
  if (!filename || path.basename(filename) !== filename || !filename.endsWith('.js')) { res.writeHead(404); res.end(); return; }
  const resolved = path.join(assetRoot, filename);
  if (!fs.existsSync(resolved)) { res.writeHead(404); res.end(); return; }
  const data = fs.readFileSync(resolved);
  served.set(filename, { file: resolved, bytes: data.length, sha256: hash(data) });
  res.writeHead(200, {'Content-Type':'text/javascript; charset=utf-8', 'Cache-Control':'no-store'}); res.end(data);
});
let browser;
const receipt = { started_at_kst: now(), command: [process.execPath, __filename], cwd: process.cwd(), mode: 'LOCAL_EXISTING_BUNDLE_ONLY', source_preservation_before: preserved, diagrams: [], status: 'RUNNING' };
(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const origin = `http://127.0.0.1:${server.address().port}`;
  browser = await chromium.launch({ executablePath: chrome, headless: true, args: ['--disable-background-networking', '--disable-sync', '--disable-extensions'] });
  const context = await browser.newContext({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1, locale: 'en-US', timezoneId: 'Asia/Seoul', serviceWorkers: 'block' });
  await context.route('**/*', route => {
    if (route.request().url().startsWith(origin + '/')) return route.continue();
    rejectedRequests.push(route.request().url()); return route.abort('blockedbyclient');
  });
  const page = await context.newPage();
  page.on('pageerror', e => logs.push({type:'pageerror', message:e.message}));
  page.on('console', msg => { if (['warning','error'].includes(msg.type())) logs.push({type:msg.type(), message:msg.text()}); });
  await page.goto(origin, { waitUntil: 'load' });
  await page.evaluate(async ({ moduleName }) => { window.localMermaid = (await import('/assets/' + moduleName)).default; }, { moduleName });
  const infoText = fs.readFileSync(path.join(assetRoot, 'infoDiagram-RXCK75RN-2T6V4JS2.js'), 'utf8');
  const version = infoText.match(/version:"([0-9.]+)"/)[1];
  receipt.renderer = {
    mermaid_version: version, version_source: path.join(assetRoot, 'infoDiagram-RXCK75RN-2T6V4JS2.js'),
    version_source_sha256: hash(infoText), module: path.join(assetRoot, moduleName), module_sha256: hashFile(path.join(assetRoot, moduleName)),
    vscode_version: JSON.parse(fs.readFileSync(path.join(vsRoot, 'package.json'), 'utf8')).version,
    node_version: process.version, playwright_version: require('C:/Users/soldesk/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/package.json').version,
    chromium_version: browser.version(), chromium_executable: chrome, config_path: 'RENDER_CONFIG.json', config_sha256: hashFile(path.join(out, 'RENDER_CONFIG.json'))
  };
  for (const input of inputs) {
    const source = fs.readFileSync(path.resolve(out, input.file), 'utf8');
    const result = await page.evaluate(async ({ source, config, name }) => {
      window.localMermaid.initialize(config);
      const parse = await window.localMermaid.parse(source);
      const rendered = await window.localMermaid.render('asbuilt-' + name, source);
      document.getElementById('drawing').innerHTML = rendered.svg;
      await document.fonts.ready;
      const svg = document.querySelector('#drawing > svg');
      const vb = svg.viewBox.baseVal;
      svg.setAttribute('width', String(Math.ceil(vb.width)));
      svg.setAttribute('height', String(Math.ceil(vb.height)));
      svg.style.maxWidth = 'none';
      const bbox = el => { const b=el.getBoundingClientRect(); return {x:b.x,y:b.y,width:b.width,height:b.height}; };
      const nodes = [...svg.querySelectorAll('g.node')].map(n => ({id:n.id, text:n.textContent.trim(), bounds:bbox(n), shape:n.querySelector('rect')?bbox(n.querySelector('rect')):null, label:n.querySelector('.label')?bbox(n.querySelector('.label')):null}));
      const edges = [...svg.querySelectorAll('path.flowchart-link')].map(e => ({id:e.id, d:e.getAttribute('d')}));
      const labels = [...svg.querySelectorAll('g.edgeLabel')].map(e => ({text:e.textContent.trim(),bounds:bbox(e)}));
      return {svg:svg.outerHTML, diagramType:parse.diagramType, viewBox:{x:vb.x,y:vb.y,width:vb.width,height:vb.height}, nodes, edges, labels};
    }, { source, config, name: input.name });
    save(input.name + '.svg', result.svg + '\n');
    const width = Math.ceil(result.viewBox.width), height = Math.ceil(result.viewBox.height);
    if (width > 16000 || height > 16000) throw new Error(`Native diagram dimension exceeds local screenshot limit: ${width}x${height}`);
    await page.setViewportSize({width:width+48,height:height+48});
    await page.locator('#drawing').screenshot({path:path.join(out,input.name+'.png'),animations:'disabled'});
    await page.evaluate(w => { const svg=document.querySelector('#drawing > svg'); const vb=svg.viewBox.baseVal; svg.setAttribute('width',String(w));svg.setAttribute('height',String(Math.ceil(w*vb.height/vb.width))); },Math.min(width,2200));
    await page.locator('#drawing').screenshot({path:path.join(out,input.name+'-overview.png'),animations:'disabled'});
    const expectedNodeCount = source.split('\n').filter(l=>/^\s+[A-Z][A-Z0-9]*\["/.test(l)).length;
    const expectedEdgeCount = source.split('\n').filter(l=>/^\s+[A-Z][A-Z0-9]*\s+(?:-->|---)/.test(l)).length;
    const textOverflow = result.nodes.filter(n=>n.shape&&n.label&&(n.label.x<n.shape.x-2||n.label.y<n.shape.y-2||n.label.x+n.label.width>n.shape.x+n.shape.width+2||n.label.y+n.label.height>n.shape.y+n.shape.height+2));
    const metadata = {name:input.name,source:input.file,source_sha256:hash(source),diagram_type:result.diagramType,viewBox:result.viewBox,node_count:result.nodes.length,expected_node_count:expectedNodeCount,edge_count:result.edges.length,expected_edge_count:expectedEdgeCount,label_shape_overflow:textOverflow,nodes:result.nodes,edges:result.edges,edge_labels:result.labels};
    save(input.name+'-geometry.json', metadata);
    receipt.diagrams.push({name:input.name,source:input.file,source_sha256:hash(source),width,height,node_count:result.nodes.length,expected_node_count:expectedNodeCount,edge_count:result.edges.length,expected_edge_count:expectedEdgeCount,label_shape_overflow_count:textOverflow.length,files:[input.name+'.svg',input.name+'.png',input.name+'-overview.png',input.name+'-geometry.json'].map(name=>({path:name,sha256:hashFile(path.join(out,name)),bytes:fs.statSync(path.join(out,name)).size})),parse_render:'PASS'});
  }
  receipt.status = 'RENDER_COMPLETE_VISUAL_REVIEW_PENDING';
  receipt.rc = 0;
})().catch(e => { receipt.status='RENDER_FAILED';receipt.error=e.stack;receipt.rc=1;process.exitCode=1; }).finally(async () => {
  if(browser) await browser.close();
  await new Promise(resolve=>server.close(resolve));
  receipt.finished_at_kst=now();receipt.external_requests_blocked=rejectedRequests;receipt.browser_messages=logs;
  receipt.source_preservation_after=preserved.map(x=>({...x,after_sha256:hashFile(path.resolve(out,x.path)),unchanged:hashFile(path.resolve(out,x.path))===x.sha256}));
  save('RENDERER_ASSET_MANIFEST.json',[...served.values()].sort((a,b)=>a.file.localeCompare(b.file)));
  receipt.asset_manifest_sha256=hashFile(path.join(out,'RENDERER_ASSET_MANIFEST.json'));
  save('RENDER_RECEIPT.json',receipt);
  console.log(JSON.stringify({status:receipt.status,rc:receipt.rc,renderer:receipt.renderer,diagrams:receipt.diagrams.map(x=>({name:x.name,width:x.width,height:x.height,nodes:x.node_count,edges:x.edge_count,overflow:x.label_shape_overflow_count})),error:receipt.error}));
});
