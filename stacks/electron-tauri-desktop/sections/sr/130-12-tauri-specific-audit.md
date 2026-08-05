## 12. Tauri-specific audit

### 12.1 Core, CLI, API, runtime, WebView i plugin matrica

1. Razresi tacne verzije `tauri`, `tauri-build`, `tauri-cli`, `@tauri-apps/cli`, `@tauri-apps/api`, runtime-a, Wry-ja, Tao-a, bundler-a, macro-a i svakog zvanicnog ili third-party plugin-a.
2. Ne nameci vestacku jednakost verzija nezavisno objavljenim komponentama. Umesto toga verifikuj njihovu dokumentovanu kompatibilnost i stvarno generisano/runtime ponasanje.
3. Zabelezi Rust toolchain i MSRV, Cargo feature-e, frontend package manager, generisane seme, target triple-ove, mobile overlay-e ako postoje i platform-specific podrsku plugin-a.
4. Identifikuj sistemsku WebView implementaciju i minimalnu podrzanu verziju na svakom target-u: WebView2, WKWebView/WebKit, WebKitGTK ili mobile WebView. Testiraj ponasanje na najstarijem podrzanom okruzenju.
5. Verifikuj da li je WebView2 evergreen, fixed, embedded, offline-installed, store-provided ili se pretpostavlja da postoji. Ukljuci installer i enterprise-offline ponasanje.
6. Pregledaj Tauri release notes, breaking changes, plugin changelog-e, generisane ACL seme i platform ogranicenja za razresene verzije.
7. Popisi third-party plugin-e i fork-ove. Pregledaj njihov Rust core, guest JavaScript, dozvole, scope-ove, build script-e, native kod, release proces i maintenance stanje.
8. Definisi upgrade ritam koji pokriva core, CLI, JS API, plugin-e, Rust, sistemske WebView zahteve, installer tooling i OS podrsku.

### 12.2 Capabilities, permissions, scopes i Runtime Authority

1. Popisi svaki capability fajl, inline capability, permission definiciju, scope, deny pravilo, target platformu, remote URL pattern, window label-u i webview label-u.
2. Izgradi efektivnu permission matricu nakon spajanja svih capabilities. Prozori ili webview-i navedeni u vise capabilities dobijaju uniju njihovih dozvola.
3. Koristi stabilne, jedinstvene window/webview label-e i verifikuj da dinamicko kreiranje ne moze slucajno da match-uje ili nasledi siru capability.
4. Default-deny privilegovane komande. Dodeli samo tacne komande i scope-ove potrebne odredjenom prozoru, webview-u, origin-u, ulozi i platformi.
5. Pregledaj `remote` capability grant-ove sa krajnjim oprezom. Remote origin koji dobija pristup lokalnom sistemu mora biti opravdan prema XSS-u, kompromitaciji naloga, DNS/CDN kompromitaciji i preuzimanju sadrzaja.
6. Koristi deny permissions gde daju defense in depth, ali razumi finalno merge i precedence ponasanje za razresenu verziju.
7. Verifikuj da custom scope-ove stvarno sprovodi implementacija komande ili plugin-a. Sama konfiguracija ne sprovodi application-defined scope.
8. Pregledaj generisane permission seme i plugin permission fajlove za tacnu dependency verziju. Ne kopiraj identifikatore iz nepovezanih verzija.
9. Verifikuj command registration i generisane app manifeste. Komande registrovane kroz siroke invoke handler-e i dalje moraju biti ogranicene capabilities i in-command autorizacijom.
10. Testiraj svaku privilegovanu komandu iz dozvoljenih i zabranjenih prozora, dozvoljenih i zabranjenih origin-a, subframe-ova, dinamicki kreiranih webview-a, zastarelih prozora i preimenovanih label-a.
11. Dokumentuj svaku capability bez jasnog vlasnika, svrhe, testa i uslova uklanjanja.
12. Tretiraj Runtime Authority kao jedan sloj authorization lanca, ne kao zamenu za poslovnu autorizaciju, validaciju putanje, vlasnistvo naloga ili potvrdu destruktivne radnje.

### 12.3 Commands, invoke, events, channels i managed state

1. Popisi svaku Tauri komandu, invoke handler, plugin komandu, event, channel, global listener, window listener, menu/tray radnju i Rust-to-frontend poruku.
2. Definisi stroge request i response tipove. Odbij dvosmislene untagged enum-e, neogranicene kolekcije, duboko ugnjezdene podatke, prevelike string/binary vrednosti, nepoznata polja gde su opasna i gubitnicke numericke konverzije.
3. Autorizuj unutar komande koristeci caller window/webview/origin, nalog, ulogu, vlasnistvo resursa, trenutno stanje aplikacije i nameru operacije.
4. Validiraj i kanonikalizuj sve putanje, URL-ove, nazive komandi, device identifikatore, kljuceve baze i identifikatore eksternih servisa pre upotrebe.
5. Ne izlaži genericke filesystem, shell, process, SQL, HTTP, plugin ili command dispatcher-e frontend-u osim ako imaju usko scoped i formalno pregledanu politiku.
6. Ogranici command concurrency, trajanje, memoriju, output, channel rate, event fan-out, broj listener-a i dubinu reda. Podrzi cancellation gde je bezbedno.
7. Koristi managed state sa eksplicitnom sinhronizacijom i vlasnistvom. Audituj izbor mutex/RwLock-a, redosled lock-ova, blocking u async kontekstima, poisoning, reentrancy i shutdown ponasanje.
8. Ne drzi lock preko await-a, IPC callback-a, filesystem/network operacije ili frontend event-a bez dokazanog dizajna.
9. Ucini destruktivne i spolja vidljive komande idempotentnim ili zasticenim od duplog invoke-a, double click-a, event replay-a, renderer reload-a i restart-a procesa.
10. Definisi stabilne error kodove i redigovane poruke. Pretvori panic i library greske u kontrolisane otkaze na granici.
11. Ukloni listener-e i zatvori channel-e kada se prozor unisti, navigira, logout-uje ili zameni. Spreci zastarele poruke da stignu u novi account context.
12. Testiraj malformed serialization, nepoznate komande, odbijenu capability, nevalidan scope, stale caller, dupli poziv, concurrent poziv, cancellation, panic i shutdown.

### 12.4 Zvanicni i third-party plugin-i

1. Napravi plugin matricu: svrha, verzija, frontend API, Rust crate, podrzane platforme, dozvole, scope-ovi, native dependency-ji, storage, mrezni pristup, vlasnik update-a i testovi.
2. Pregledaj default permission set-ove pre koriscenja. Praktican `plugin:default` grant moze ukljuciti vise komandi nego sto je prozoru potrebno.
3. Preferiraj pojedinacne allow permissions i uske scope-ove za filesystem, shell, process, opener, HTTP, SQL, store, clipboard, notification, dialog, deep link, single instance, global shortcut, autostart i updater funkcionalnost.
4. Pregledaj permission-e koje plugin generise i application-added prosirenja. Osiguraj da se custom scope tipovi parsiraju i sprovode konzistentno.
5. Audituj redosled inicijalizacije plugin-a, managed state, background thread-ove, event listener-e, migration ponasanje, cleanup i error handling.
6. Verifikuj path promenljive i scope ekspanziju prema platform-specific direktorijumima, symlink-ovima, junction-ima, Unicode-u, case sensitivity-ju, removable media i network share-ovima.
7. Proveri da li plugin po default-u izlaže opasne frontend komande ili tek posle capability grant-a. Testiraj stvarnu razresenu verziju.
8. Tretiraj nezvanicne plugin-e i fork-ove kao application kod: pregledaj source, release provenance, odrzavaoce, advisory-je, build script-e, native kod i incident response.
9. Ukloni neiskoriscene plugin-e i Cargo feature-e iz finalnog binarnog fajla i capabilities.
10. Testiraj ponasanje plugin-a na nepodrzanim ili delimicno podrzanim platformama i osiguraj da UI ne nudi nefunkcionalne ili nebezbedne operacije.

### 12.5 Filesystem, shell, opener, process i sidecar-i

1. Ogranici filesystem pristup po komandi i kanonickom scope-u. Razlikuj fajlove koje je korisnik izabrao od application-controlled putanja i sirokih grant-ova direktorijuma.
2. Spreci traversal i izlaz kroz symlink-ove, junction-e, alias-e, hard link-ove, UNC/device putanje, promene case-a, Unicode normalizaciju, alternate data stream-ove i race condition izmedju provere i upotrebe.
3. Koristi bezbedne create/write/replace obrasce, dozvole privremenih fajlova, atomic rename gde je podrzan, fsync zahteve, conflict handling i oporavak od partial write-a.
4. Nikada ne izlaži proizvoljne shell string-ove. Koristi allowlisted programe ili bundled sidecar-e, strukturisane argumente, bez shell interpretacije, eksplicitno okruzenje, eksplicitni radni direktorijum i ogranicen output.
5. Verifikuj razresavanje sidecar putanje, bundled target-triple naming, executable dozvole, potpis/hash, version handshake, update coupling i hijacking kroz writable putanju.
6. Autentifikuj lokalnu komunikaciju sa sidecar-ima ili servisima. Koristi zasticene socket-e/pipe-ove, random tajne ili OS kredencijale, peer verifikaciju i usku kontrolu pristupa.
7. Validiraj URL-ove i scheme prosledjene opener API-jima. Odvoji otvaranje HTTPS dokumentacije od pozivanja proizvoljnih application protokola.
8. Definisi child-process timeout, cancellation, graceful stop, forced termination, ciscenje potomaka, output backpressure, crash retry i quarantine ponasanje.
9. Audituj elevation i administrator/root helper-e. Koristi platform-approved privilege separation i autentifikuj zahteve; nikada ne pokreci ceo UI privilegovano radi pogodnosti.
10. Testiraj zlonamerna imena fajlova, executable substitution, argument injection, environment injection, lokalnu impersonation, sidecar version mismatch, partial output, hang, crash i gasenje aplikacije.

### 12.6 Asset protocol, CSP, isolation i remote sadrzaj

1. Popisi asset/custom protocol konfiguraciju, dozvoljene putanje, scope, CSP, dev URL, frontend distribution direktorijum, remote URL-ove i sve asset conversion helper-e.
2. Verifikuj da produkcioni build ne moze da ucita development server ili nepoverljiv URL zbog environment drift-a ili fallback ponasanja.
3. Koristi restriktivan CSP i isolation podesavanja koja podrzava razresena Tauri/WebView verzija. Testiraj na svakom sistemskom WebView-u jer se enforcement i feature podrska mogu razlikovati.
4. Tretiraj `convertFileSrc` i asset protocol pristup kao privilegovano otkrivanje fajla. Ogranici koji fajlovi i direktorijumi mogu da se konvertuju i renderuju.
5. Ne dodeljuj remote URL-ovima capabilities osim ako je kompletan compromise scenario prihvacen i ublazen. Preferiraj remote webview bez privilegija ili sistemski browser.
6. Verifikuj navigation, popup, download, external-open, clipboard, media, permission i devtools ponasanje u svakom webview-u.
7. Audituj frontend dependency-je i XSS sink-ove istom strogoscu kao kod Electron-a; manji native core ne cini kompromitovan web sadrzaj bezopasnim kada su komande izlozene.
8. Testiraj malformed asset URL-ove, encoded traversal, local-file probing, remote redirect-e, kompromitovan frontend bundle, CSP bypass pokusaje i zastarelu capability dodelu.

### 12.7 Unsafe Rust, FFI, mobile overlay i platform kod

1. Pregledaj svaki `unsafe` blok sa dokumentovanim invariantama, ownership, lifetime, thread, alignment, aliasing, initialization i error pretpostavkama.
2. Audituj FFI granice za ABI, layout strukture, encoding string-a, duzinu buffer-a, lifetime callback-a, prelazak exception-a/panic-a, cancellation i library version mismatch.
3. Verifikuj da platform moduli i conditional compilation proizvode ekvivalentne security odluke; odsutan kod na jednom target-u ne sme tiho da prosiri ponasanje.
4. Pregledaj Objective-C/Swift, C/C++, Java/Kotlin, PowerShell, shell i installer custom action-e istom disciplinom nalaza kao Rust i TypeScript.
5. Ako postoje mobile target-i, posebno audituj generisane Android/iOS projekte, dozvole, intent-e/URL scheme, WebView podesavanja, signing, prodavnice, background ponasanje i plugin hook-ove.
6. Testiraj odsustvo native biblioteke, pogresnu arhitekturu, signature failure, odbijenu dozvolu, OS API deprecation, callback posle shutdown-a i malformed native podatke.
7. Koristi sanitizer-e, Miri, fuzzing, clippy, compiler upozorenja i platform diagnostics gde je primenljivo, ali povezi nalaze sa isporucenim kodom i runtime dostiznoscu.
8. Ne prepisuj bezbedan funkcionalan kod u `unsafe` ili custom FFI samo radi performansi bez merenja i odrzavane test strategije.

