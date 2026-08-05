## 9. Mapa arhitekture, procesa, prozora i privilegija

### 9.1 Obavezna arhitektonska mapa

1. Nacrtaj process tree: bootstrap, Electron main ili Tauri Rust core, renderer/webview procese, GPU, utility/worker procese, sidecar-e, lokalne daemon-e, helper-e, crash reporter, updater, installer i pokrenutu decu procese.
2. Mapiraj svaki prozor i webview po stabilnoj label-i ili identifikatoru, content origin-u, lifecycle-u, vlasniku, korisnickoj ulozi, osetljivosti podataka, navigation politici, permission set-u i izlozenom bridge-u.
3. Mapiraj svaki trust boundary izmedju nepoverljivog remote sadrzaja, lokalnog zapakovanog UI-ja, privilegovanog bridge-a, native core-a, lokalnih fajlova, API-ja operativnog sistema, uredjaja i udaljenih servisa.
4. Mapiraj sve IPC mehanizme: Electron IPC, MessagePort, postMessage, webview messaging, Tauri invoke/events/channels, lokalne socket-e, named pipe-ove, HTTP, WebSocket, stdin/stdout, fajlove i custom protokole.
5. Mapiraj authentication i authorization odluke na sloju koji obavlja privilegovani rad. Sakrivanje UI-ja nije autorizacija.
6. Mapiraj vlasnistvo nad stanjem: renderer memorija, main/Rust state, lokalna baza, fajlovi, secure storage, cloud servis, updater i installer.
7. Mapiraj startup, shutdown, crash restart, sleep/wake, session lock/unlock, mreznu tranziciju, update restart i OS sign-out/shutdown putanje.
8. Oznaci svaki put koji moze da izvrsi kod, pokrene proces, otvori eksterni URL, upise fajl, pristupi kredencijalima, koristi uredjaj, promeni podesavanje, instalira update ili obrise podatke.

### 9.2 Pitanja za minimizaciju privilegija

1. Moze li renderer ili webview da radi manje? Ukloni siroke bridge-eve i izlozi uske operacije sa eksplicitnim semama.
2. Moze li privilegovana operacija da se premesti u poseban proces, scoped komandu, OS servis ili broker sa manjom attack surface povrsinom?
3. Moze li prozor da dobije jedinstvenu capability ili session umesto nasledjivanja globalnog permission set-a?
4. Moze li scope fajla, URL-a, executable-a, uredjaja ili kredencijala da se ograniči na allowlist podskup?
5. Moze li mrezni sadrzaj da se renderuje bez lokalnih privilegija i bez deljenja cookie-ja, storage-a, dozvola ili service worker-a sa pouzdanim sadrzajem?
6. Moze li updater, installer ili release job da radi sa privremenim kredencijalima i posebnim odobrenjem?
7. Moze li administrativno ponasanje da se odvoji od normalnog korisnickog procesa i ucini auditabilnim?
8. Moze li kompromitovan renderer da se zadrzi bez pristupa code execution-u, tajnama, korisnickim fajlovima, update kontrolama ili drugom tenant-u/nalogu?

