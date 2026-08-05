## 11. Electron-specific audit

### 11.1 Framework, ugradjeni runtime-i i upgrade stanje

1. Razresi tacnu Electron verziju iz lock fajla i zapakovanog binarnog fajla, ne samo iz `package.json`. Zabelezi ugradjeni Chromium, Node.js, V8 i relevantni ABI.
2. Utvrdi da li je major unutar trenutnog podrzanog-major prozora i da li noviji stabilni patch popravlja security ili correctness probleme.
3. Pregledaj Electron breaking changes major po major. Ne preskaci vise major verzija bez medjuverzijskih compatibility dokaza i verifikacije native modula.
4. Popisi verzije Electron Forge, Electron Builder, Packager, Rebuild, Fuses, notarization, signing i updater paketa nezavisno.
5. Verifikuj native module-e prema stvarnom Electron ABI-ju i svakom podrzanom OS-u/arhitekturi. Rebuild, prebuild, fallback kompilacija i runtime loading moraju biti testirani.
6. Otkrij nepodrzane ili privatne Electron API-je, command-line switch-eve, Chromium flag-ove, monkey patch-eve, zamene remote modula i pretpostavke o internim procesima.
7. Verifikuj minimalnu OS podrsku i ponasanje ugradjenog runtime-a prema deklarisanoj support matrici proizvoda.
8. Dokumentuj patch i major upgrade ritam, vlasnika security response-a, test prozor i emergency release put.

### 11.2 Lifecycle aplikacije i single-instance ponasanje

1. Mapiraj izvrsavanje pre i posle `app.whenReady()`, dobijanje single-instance lock-a, second-instance argumente, open-file/open-url dogadjaje, activate, window-all-closed, before-quit, will-quit, quit i crash/relaunch putanje.
2. Validiraj command-line argumente i deep-link payload-e koje prima prva instanca. Ne veruj drugom procesu samo zato sto je ista aplikacija.
3. Testiraj startup sa korumpiranim preferences, zakljucanim profilom, read-only data direktorijumom, nedostajucim resursima, nedostupnom mrezom, sporim keychain-om, neuspelim migracijama i nepotpunim update-om.
4. Definisi ponasanje kada se svi prozori zatvore na svakoj platformi, kada tray ostane aktivan i kada OS zatrazi logout ili shutdown.
5. Spreci duple background job-ove, updater provere, lokalne server-e, migracije, device session-e ili obradu fajlova kroz vise instanci.
6. Verifikuj uredno gasenje session-a, socket-a, file handle-ova, worker-a, utility procesa, child procesa, crash reporter-a i telemetrije.
7. Testiraj app relaunch, update restart, crash restart, safe mode, recovery mode i background rezim bez prozora.
8. Osiguraj da fatalni startup otkazi daju upotrebljivu dijagnostiku bez curenja tajni i bez ulaska u beskrajnu restart petlju.

### 11.3 BrowserWindow, WebContentsView i WebPreferences

1. Popisi svaki `BrowserWindow`, `BaseWindow`, `WebContentsView`, offscreen renderer, skriveni prozor, print prozor, auth prozor, splash screen i privremeni webContents.
2. Zabelezi efektivne `webPreferences` za svaki: `nodeIntegration`, `nodeIntegrationInWorker`, `nodeIntegrationInSubFrames`, `contextIsolation`, `sandbox`, `preload`, `webSecurity`, `allowRunningInsecureContent`, `experimentalFeatures`, `enableBlinkFeatures`, `webviewTag`, `partition`, `spellcheck` i devtools politiku.
3. Zahtevaj `nodeIntegration: false`, `contextIsolation: true` i sandbox za nepoverljiv ili remote sadrzaj osim kada postoji usko dokazan izuzetak.
4. Tretiraj svaki `sandbox: false`, `contextIsolation: false`, `webSecurity: false`, insecure content, neograniceni webview ili remote Node integration kao prioritetan dokaz koji zahteva analizu dostiznosti.
5. Verifikuj da se preload putanja razresava na nameravani zapakovani fajl i da se ne moze zameniti kroz writable direktorijume, manipulaciju okruzenjem ili nepoverljivu navigaciju.
6. Odvoji session-e i storage partition-e za sadrzaj sa razlicitim trust, account, privacy ili lifecycle zahtevima. Utvrdi da li su partition-i persistent.
7. Audituj skrivene prozore i background webContents jer mogu da zadrze privilegije, cookie-je, mikrofone, kamere, timer-e ili IPC listener-e nakon zatvaranja vidljivog UI-ja.
8. Osiguraj da su window options, content origin, preload i privilegija vezani u jednu pregledanu putanju kreiranja umesto promenljivi kroz razbacan kod.

### 11.4 Preload i ContextBridge povrsina

1. Popisi svaki preload fajl i svako svojstvo izlozeno kroz `contextBridge`. Napravi tipiziran bridge ugovor.
2. Izlozi uske funkcije i nepromenljive vrednosti, ne raw `ipcRenderer`, EventEmitter, Electron module, Node primitive, filesystem handle-ove, shell execution, neogranicene URL-ove, callback-e sa skrivenom privilegijom ili genericki `invoke(channel, payload)`.
3. Validiraj argumente i na renderer i na privilegovanom sloju. Renderer validacija poboljsava UX, ali nije security granica.
4. Freeze-uj ili bezbedno wrap-uj izlozene objekte. Izbegavaj curenje promenljivih privilegovanih referenci, prototipova, Buffer instanci, native handle-ova ili objekata sa neocekivanim metodama.
5. Definisi error ugovore koji ne izlažu stack trace, file putanje, tokene, SQL, promenljive okruzenja ili implementacione detalje nepoverljivom sadrzaju.
6. Ukloni zastarele listener-e i subscription-e pri navigaciji, reload-u, promeni naloga, zatvaranju prozora i hot update-u. Ogranici broj listener-a i stopu poruka.
7. Verifikuj preload ponasanje u sandboxed kontekstima i kroz subframe-ove. Ne pretpostavljaj da je main frame jedini pozivalac.
8. Dodaj contract testove koji pokrecu zlonamerni renderer kod protiv svake izlozene metode i verifikuju denial, validaciju, autorizaciju i ogranicen otkaz.

### 11.5 IPC autentikacija, autorizacija, validacija i backpressure

1. Popisi svaki `ipcMain.handle`, `ipcMain.on`, `webContents.send`, MessagePort, postMessage, webview message i reply put. Ukloni ili odbij nepoznate kanale.
2. Validiraj sender koristeci stvarni `webContents`, frame, origin, URL, session/partition, vlasnistvo prozora, lifecycle generation i account context. Naziv kanala nije autentikacija.
3. Sprovedi resource-level autorizaciju za svaki fajl, nalog, tenant, uredjaj, job, update, podesavanje i privilegovanu radnju.
4. Koristi stroge seme sa limitima velicine, dubine, broja, string-a, putanje, enum-a i binarnih podataka. Odbij dodatna polja kada stvaraju dvosmislenost.
5. Kanonikalizuj putanje i URL-ove pre policy provera. Brani se od traversal-a, symlink/junction izlaza, alternate data stream-ova, UNC putanja, device putanja, case trikova i enkodovanih separatora.
6. Ucini side effect-e idempotentnim gde retry, dupli klik, renderer reload, duple poruke ili restart procesa mogu da ih ponove.
7. Ogranici konkurentne zahteve, redove, stopu stream-a, velicinu payload-a, velicinu odgovora i vreme izvrsavanja. Otkazi rad kada caller nestane gde je bezbedno.
8. Ne salji privilegovane rezultate zastarelom, navigiranom, unistenom ili ponovo koriscenom webContents-u bez ponovne validacije identiteta i account context-a.
9. Odvoji read, write, destruktivne, administrativne i update kanale. Zahtevaj dodatnu potvrdu ili autorizaciju za nepovratne operacije.
10. Loguj security-relevant odluke sa correlation ID-jevima i redakcijom, ukljucujuci odbijen sender, nevalidnu semu, scope failure, dupli zahtev i rate-limit dogadjaje.
11. Testiraj cross-window, subframe, navigated-frame, remote-origin, stale-renderer, destroyed-renderer, duplicate, replay, oversized, slow i concurrent IPC scenarije.
12. Tretiraj IPC kao lokalni network API sa nepoverljivim klijentom kada je kompromitacija renderer-a u threat model-u.

### 11.6 Session-i, dozvole, download-i i protokoli

1. Popisi sve session-e i partition-e. Konfigurisi permission request/check handler-e za svaki session koji moze da ucita remote ili user-controlled sadrzaj.
2. Default-deny camera, microphone, display capture, notifications, geolocation, MIDI, USB, serial, HID, Bluetooth, clipboard i fullscreen dozvole osim kada su eksplicitno potrebne.
3. Vezi permission odluke za tacan origin, frame, korisnicku radnju, nalog, uredjaj i trajanje. Perzistiraj samo kada je opravdano i opozivo.
4. Audituj cookie-je, proxy, cache, certificate verification, auth challenge-e, client sertifikate, service worker-e, extension-e i ciscenje storage-a po session-u.
5. Definisi download politiku: dozvoljene origin-e, MIME i extension provere, izbor destinacije, overwrite ponasanje, quarantine/Mark-of-the-Web, malware scan, partial fajlove, otkazivanje i ponasanje pri otvaranju.
6. Implementiraj custom protokole kao privilegovane parser-e: normalizuj putanje, namerno definisi standard/secure/cors/fetch/stream privilegije, ograniči metode i origin-e i spreci traversal.
7. Izbegavaj `file://` za privilegovani app sadrzaj gde secure custom protokol daje jasniji origin i policy model.
8. Testiraj certificate error-e, captive portal-e, proxy auth, offline rezim, redirect-e, zlonamerna imena fajlova, archive bomb-e, partial download-e i download-to-execute lance.

### 11.7 Navigacija, novi prozori, external open i webview-i

1. Koristi `will-navigate`, obradu redirect-a i window-open handler-e da sprovedes tacnu navigation i popup politiku.
2. Validiraj svaki URL prosledjen `shell.openExternal` ili OS launch API-jima. Dozvoli samo potrebne scheme i host-ove; odbij lokalne fajlove, executable protokole, script scheme, malformed URL-ove i proizvoljne custom protokole.
3. Ne koristi `<webview>` osim ako njegove prednosti izolacije i lifecycle-a nadmasuju attack surface. Preferiraj `WebContentsView` ili sistemski browser kada je primereno.
4. Ako `<webview>` postoji, validiraj `will-attach-webview` options i source, ukloni opasan preload i dozvole, odbij `allowpopups` i izoluj partition-e.
5. Verifikuj OAuth, payment, help, documentation, support i third-party content tokove pod redirect i compromised-content uslovima.
6. Spreci nepoverljivi sadrzaj da kontrolise window feature-e, izbor preload-a, partition, sandbox, devtools, download lokaciju ili eksterne aplikacije.
7. Audituj drag-and-drop i link handling zbog curenja lokalnih fajlova i izvrsavanja komandi/protokola.
8. Testiraj nested frame-ove, dinamicki kreirane webview-e, same-origin promene, history navigaciju, server redirect-e i post-authentication navigaciju.

### 11.8 Fuses, ASAR integrity i ojacavanje executable-a

1. Pregledaj fuses u stvarnom zapakovanom executable-u. Ne oslanjaj se samo na Forge ili build konfiguraciju.
2. Proceni fuses kao sto su iskljucivanje `RunAsNode`, ogranicavanje uticaja `NODE_OPTIONS` i `NODE_EXTRA_CA_CERTS` gde je primereno, iskljucivanje inspection argumenata, obavezno ASAR app ucitavanje i ukljucivanje embedded ASAR integrity validacije.
3. Promeni fuses nakon pakovanja i pre code signing-a, zatim verifikuj finalni potpisani binary. Zabelezi tacnu verziju fuse alata i opcije.
4. Razumi compatibility uticaj pre iskljucivanja ponasanja; testiraj CLI integracije, child procese, debugging, enterprise sertifikate i native module-e.
5. Ukljuci ASAR integrity samo sa kompletnom potrebnom kombinacijom fuse-ova i packaging tokom. Verifikuj da izmenjene arhive otkazuju kako je ocekivano.
6. Drzi executable kod van writable raspakovanih resursa. Opravdaj svaku `asarUnpack` putanju i zastiti njen load path.
7. Verifikuj signature i ASAR integrity ponasanje posle installer instalacije, delta update-a, full update-a, repair-a i rollback-a.
8. Tretiraj fuses i ASAR kao defense in depth, ne kao zamenu za bezbednu renderer izolaciju, IPC autorizaciju, signing i update poverenje.

### 11.9 Utility procesi, worker-i, extension-i i native module-i

1. Preferiraj utility procese nad ad hoc Node child procesima kada Electron lifecycle, sandbox i MessagePort integracija daju bezbedniji fit; opravdaj izuzetke.
2. Popisi Node child procese, fork-ovane worker-e, worker thread-ove, renderer worker-e, service worker-e, GPU task-ove, extension procese i native helper procese.
3. Validiraj konstrukciju child executable-a i argumenata; izbegavaj shell interpretaciju; koristi eksplicitne allowlist-e promenljivih okruzenja i radne direktorijume.
4. Ogranici broj procesa, CPU, memoriju, file descriptor-e, output buffer-e, ucestalost restart-a i dubinu reda. Spreci crash loop i fork bomb.
5. Autentifikuj lokalni IPC prema helper-ima i spreci drugi lokalni proces da imitira aplikaciju ili se poveze na privilegovane socket-e/pipe-ove.
6. Verifikuj putanje ucitavanja native modula, potpise gde su dostupni, ABI kompatibilnost, DLL search order, rpath, library search putanje i hijacking kroz writable direktorijume.
7. Iskljuci ili strogo kontrolisi Chrome extension-e, devtools extension-e, remote debugging, inspect port-ove i automation interfejse u produkciji.
8. Testiraj helper crash, hang, malformed output, oversized output, partial protocol poruke, version mismatch, update overlap i gasenje aplikacije.

