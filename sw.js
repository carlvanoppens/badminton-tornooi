// Offline-cache: de app werkt na de eerste keer openen volledig zonder internet.
// Verhoog VERSION bij elke nieuwe versie, dan haalt de app de update op.
const VERSION='bt-v5';
const SHELL=['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png','apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(VERSION).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==VERSION).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return; // badman-zoekopdrachten (POST) gaan altijd naar het internet
  const url=new URL(r.url);
  if(url.origin===location.origin&&(r.mode==='navigate'||url.pathname.endsWith('/index.html'))){
    // pagina: eerst netwerk (voor updates), anders uit de cache
    e.respondWith(fetch(r).then(res=>{const c=res.clone();caches.open(VERSION).then(x=>x.put('index.html',c));return res}).catch(()=>caches.match('index.html')));
    return;
  }
  e.respondWith(caches.match(r).then(hit=>hit||fetch(r).then(res=>{
    if(res.ok||res.type==='opaque'){const c=res.clone();caches.open(VERSION).then(x=>x.put(r,c))}return res})));
});
