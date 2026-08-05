## 10. Zajednicka web, content i origin bezbednost

### 10.1 Content origin-i i navigacija

1. Popisi svaki lokalni, custom-protocol, file, data, blob, extension, development-server, remote HTTPS, WebSocket i korisnicki origin.
2. Klasifikuj svaki origin kao pouzdani lokalni application sadrzaj, pouzdani remote application sadrzaj, third-party sadrzaj, user-generated sadrzaj, authentication sadrzaj, update sadrzaj ili nepoverljiv proizvoljan sadrzaj.
3. Definisi allowlist-u za top-level navigaciju, redirect-e, nove prozore, download-e, rukovanje eksternim protokolima, OAuth callback-e i ugradjene frame-ove.
4. Kanonikalizuj i validiraj URL pravim parser-om. Odbij username confusion, enkodovane separatore, mixed case, punycode/homograph zamke, alternativne scheme, lokalne adrese i redirect lance kada je relevantno.
5. Ne daj lokalne privilegije remote sadrzaju samo zato sto ga servira domen aplikacije. Account takeover, DNS/CDN kompromitacija, XSS ili supply-chain kompromitacija mogu taj sadrzaj uciniti neprijateljskim.
6. Odvoji pouzdani i nepoverljivi sadrzaj u posebne webview/prozore, session-e, storage partition-e, dozvole i bridge povrsine.
7. Blokiraj neocekivanu navigaciju i kreiranje prozora na privilegovanom sloju, ne samo u frontend click handler-ima.
8. Testiraj redirect-e, target blank, window.open, iframe, drag-and-drop, pasted HTML, markdown, SVG, PDF, media i preuzeti sadrzaj.

### 10.2 CSP, injection i browser povrsina

1. Definisi restriktivan Content Security Policy za svaku klasu sadrzaja. Izbegavaj siroke `unsafe-eval`, `unsafe-inline`, wildcard origin-e, neogranicen `connect-src` i permisivna frame/object pravila.
2. Prati svaku konstrukciju HTML-a, markdown-a, template-a, SVG-a, CSS-a, URL-a, script-a i komande od izvora do sink-a. Validiraj sanitization konfiguraciju i bypass-e.
3. Audituj DOM XSS, prototype pollution, unsafe deserialization, dynamic import, eval-like ponasanje, kreiranje worker-a, WebAssembly loading i script execution definisan plugin-om.
4. Verifikuj Trusted Types ili ekvivalentne kontrole gde je prakticno, ali ne tretiraj postojanje politike kao dokaz da unsafe sink-ovi nisu dostizni.
5. Audituj browser storage, IndexedDB, Cache Storage, service worker-e, cookie-je, localStorage, sessionStorage i deljene partition-e zbog osetljivih podataka i cross-account curenja.
6. Iskljuci ili opravdaj experimental browser feature-e, insecure content, certificate bypass-e, iskljucen web security, permisivne CORS workaround-e i debugging port-ove.
7. Verifikuj clipboard, drag/drop, paste, print, screen capture, notification, media capture, geolocation, USB, serial, HID, Bluetooth i filesystem dozvole.
8. Testiraj zlonamerni sadrzaj koji pokusava da dosegne svaki izlozeni bridge, navigira, otvori eksterne aplikacije, exfiltruje podatke, perzistira stanje i pokrene skupe operacije.

### 10.3 Authentication sadrzaj i session granice

1. Preferiraj system-browser authorization sa PKCE kada je primereno. Ako je ugradjena autentikacija neophodna, dokumentuj podrsku provajdera, izolaciju cookie/storage-a, phishing rizik i ogranicenja bridge-a.
2. Validiraj custom protocol ili app-link callback prema state-u, nonce-u, PKCE verifier-u, ocekivanom issuer-u, redirect URI-ju, nalogu i jednokratnoj upotrebi.
3. Spreci da cookie-ji, cache, lokalni storage, redovi baze, fajlovi, tokeni, pending operacije ili stanje prozora jednog naloga procure nakon logout-a ili promene naloga.
4. Cuvaj refresh token-e i dugotrajne kredencijale u storage-u zasticenom operativnim sistemom ili jasno opravdanoj alternativi; ne izlaži ih renderer-u.
5. Definisi token refresh single-flight, expiry, clock-skew, offline, revocation, promenu lozinke, uklanjanje uredjaja i server-side invalidation ponasanje.
6. Verifikuj lokalnu autorizaciju za privilegovane offline operacije; staro cache-irano UI stanje nije autorizacija.
7. Zastiti login, license, payment i account-recovery prozore od navigacije, proizvoljnog preload/command pristupa, screenshot-a gde je potrebno i injection-a eksternog sadrzaja.
8. Testiraj vise prozora, vise profila, brzo menjanje naloga, konkurentni refresh, istekle session-e, opozvane naloge i sleep/wake tranzicije.

