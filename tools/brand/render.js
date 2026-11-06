const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{ const b=await chromium.launch(); const dir=process.argv[2];
 for (const f of fs.readdirSync(dir).filter(f=>f.endsWith('.svg'))) {
  const svg=fs.readFileSync(path.join(dir,f),'utf8'); const [,w,h]=svg.match(/width="(\d+)" height="(\d+)"/);
  const p=await b.newPage({viewport:{width:+w,height:+h}});
  await p.setContent(`<html><body style="margin:0;background:#111">${svg}</body></html>`); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(300);
  await p.screenshot({path:path.join(dir,f.replace('.svg','.png'))}); await p.close(); console.log(f);
 } await b.close(); })();
