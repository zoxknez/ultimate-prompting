## 38. Web-specifičan audit

Flutter web je browser aplikacija sa origin, cache, deployment, accessibility i compatibility ograničenjima.

- Zabeleži JavaScript ili Wasm režim, renderer, optimizaciju, base href, strategiju asset URL-a, compile-time define-e, browser matricu, mobile/desktop browser podršku i fallback.
- Proveri CSP uključujući nonce/hash strategiju, Trusted Types gde se koriste, COOP/COEP/CORP za cross-origin izolaciju, CORS, permissions policy, frame policy, referrer policy i HTTPS.
- Audituj service worker, verzionisanje cache-a, zastareo shell, asset hashing, CDN cache, HTML cache politiku, update prompt, rollback, offline ponašanje i parcijalni deployment.
- Proveri odvajanje origin-a, cookie-je, browser storage, obnovu sesije, logout, multi-tab ponašanje, BroadcastChannel ili worker upotrebu, private mode, kvotu i storage eviction.
- Audituj URL handling, history, refresh, server rewrite-e, deep route-ove, canonical metapodatke, SEO ograničenja gde su relevantna i error fallback.
- Testiraj accessibility sa browser semantics, screen reader-ima, keyboard-only navigacijom, fokusom, zoom-om, text scaling-om, high contrast-om, reduced motion-om i copy/paste-om.
- Meri početni download, kompresiju, keširanje, first paint, Flutter first frame, interaction readiness, frame performanse, memoriju, worker trošak i ponašanje na slabim uređajima.
- Pregledaj JavaScript interop i DOM pristup radi validacije šeme, origin provera, XSS-a, unsafe HTML-a, prototype ponašanja, callback lifetime-a i release minification razlika.
- Testiraj podržane browser-e, verzije, uređaje, zoom nivoe, mrežna stanja, cache stanja, stare/nove deployment-e i extension/privacy smetnje.

