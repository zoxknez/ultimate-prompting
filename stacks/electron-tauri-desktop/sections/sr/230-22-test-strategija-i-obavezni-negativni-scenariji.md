## 22. Test strategija i obavezni negativni scenariji

### 22.1 Slojevi testiranja

1. Unit-testiraj cistu poslovnu logiku, parser-e, validator-e, canonicalizer-e, state machine-e, authorization odluke, korake migracije i update-version politiku.
2. Contract-testiraj svaki preload bridge, Electron IPC kanal, Tauri komandu, event/channel payload, sidecar protokol, lokalni servis, update metadata i installer exit-code ugovor.
3. Integration-testiraj sa stvarnom filesystem semantikom, stvarnim embedded database engine-om, secure-storage apstrakcijom, reprezentativnim proxy/certificate setup-om i stvarnim platform WebView/runtime-om gde je primenljivo.
4. Pokreci testove zapakovane aplikacije, ne samo browser/dev-server testove. Verifikuj efektivne privilegije, resurse, potpise, putanje i OS integracije.
5. Koristi end-to-end testove za kriticne korisnicke tokove: install, first run, sign in, promenu naloga, file/device workflow, offline/online tranziciju, update, restart, rollback, export, logout i uninstall.
6. Koristi security testove za XSS-to-bridge dostiznost, IPC/command autorizaciju, path/URL validaciju, autentikaciju lokalnog servisa, update tampering, signature failure i data izolaciju.
7. Koristi concurrency i durability testove za duple radnje, vise prozora, vise instanci, background job-ove, database locking, update overlap, shutdown i crash recovery.
8. Koristi performance testove za startup, kriticne interakcije, velike podatke, burst input, mnogo prozora, idle, long-run leak-ove, malo resursa i spore dependency-je.
9. Koristi accessibility testove sa automatskim proverama plus keyboard i screen-reader verifikacijom u packaged build-ovima.
10. Koristi installation i update matrice na cistim snapshot-ovima/VM-ovima sa realnim starim verzijama i korisnickim podacima.
11. Svaka potvrdjena P0-P2 popravka mora imati fokusiran regression test koji bi pao pre popravke i prosao posle nje.
12. Zabelezi skipped, flaky, quarantined, platform-unavailable ili rucno verifikovane testove sa vlasnikom, razlogom, rizikom i exit kriterijumom.

### 22.2 Obavezni adversarial i failure scenariji

1. Kompromitovan renderer/webview pokusava svaki izlozeni Electron bridge ili Tauri komandu iz pogresnog origin-a, frame-a, prozora, label-e, naloga i lifecycle generation-a.
2. Zlonamerni IPC/command payload koristi dodatna polja, pogresne tipove, duboko ugnjezdavanje, ogromne string/binary vrednosti, traversal, symlink-ove, UNC/device putanje, alternativne scheme i enkodovane separatore.
3. Dva prozora ili instance istovremeno i posle renderer reload-a salju istu destruktivnu ili spolja vidljivu operaciju.
4. Caller navigira, logout-uje se, menja nalog, zatvara se ili se unistava dok je privilegovani rad u toku i pre isporuke rezultata.
5. Remote sadrzaj redirect-uje, otvara novi prozor, poziva eksterni protokol, preuzima active content i pokusava da zadrzi privilegije posle navigacije.
6. Lokalni nepoverljivi proces pokusava da se poveze na localhost/socket/pipe/helper interfejse, replay-uje poruke, imitira aplikaciju ili zauzme endpoint.
7. Update metadata, paket, potpis, publisher, kanal, arhitektura, verzija i endpoint se nezavisno menjaju.
8. Update se prekida tokom download-a, verifikacije, instalacije, prvog restart-a, migracije podataka, zamene sidecar-a i cleanup-a.
9. Cista instalacija, repair, upgrade sa svake podrzane stare verzije, skipped-version upgrade, downgrade pokusaj, rollback i uninstall rade sa realnim korisnickim podacima.
10. Signing sertifikat ili updater kljuc je istekao, opozvan, nedostaje, pogresan je, nedostupan ili se smatra kompromitovanim.
11. Disk postaje pun ili read-only tokom write-a, database transakcije, migracije, export-a, download-a, update-a, logovanja i crash reporting-a.
12. Aplikacija se ubija, OS se gasi, korisnik se logout-uje, masina ide u sleep ili nestaje napajanje tokom kriticnog rada.
13. Native module, sidecar, plugin, WebView runtime, codec, driver ili sistemski dependency nedostaje, pogresne je arhitekture, nekompatibilan, spor, zaglavljen ili zlonamerno zamenjen.
14. Proxy auth, captive portal, DNS failure, TLS interception, certificate error, clock skew, spor server, partial response, oversized response i retry storm se dogadjaju.
15. Korisnik menja nalog, OS korisnika, kanal ili profil dok cache, cookie-ji, prozori, background rad, notification-i i lokalni podaci jos postoje.
16. Mnogo prozora, veliki fajlovi, hotplug storm, burst IPC/event-i, spor consumer i dugotrajan idle guraju CPU, memoriju, GPU, disk, queue i listener limite.

### 22.3 Matrica platformi i arhitektura

| Dimenzija | Obavezna pokrivenost | Dokaz |
| --- | --- | --- |
| Operativni sistem | Svaki podrzani Windows, macOS i Linux baseline plus trenutne reprezentativne verzije | Cist VM/uredjaj, tacan build, install/update/runtime rezultati |
| Arhitektura | x64, ARM64 i svaki dodatni isporuceni target | Verifikacija native module-a/sidecar-a/plugin-a/paketa/potpisa/runtime-a |
| Distribucija | Direct, store, enterprise, portable, repository ili package format koji se stvarno isporucuje | Channel-specific install, update, rollback i policy dokaz |
| Izvorna verzija | Cista instalacija i svaki podrzani upgrade source, ukljucujuci realno staru verziju | Versioned snapshot-ovi sa reprezentativnim korisnickim podacima |
| Okruzenje | Online, offline, proxy, enterprise TLS interception gde je podrzan, malo diska, malo memorije | Zabelezeni uslovi, logovi, user-visible ishod, recovery |
| Ekran/unos | Jedan/vise mixed-DPI ekrana, tastatura, screen reader, IME, touch gde je podrzan | Packaged-app accessibility i window-state dokaz |

