## 27. Production readiness checklist

1. Podrzane framework/runtime/toolchain verzije su verifikovane iz source-a, lock fajlova, zapakovanog artefakta i runtime-a. Nema neodobrenog preview-a ili nepodrzanog major-a.
2. Repozitorijum, generisana konfiguracija, dependency graf, build script-i, native kod, plugin-i i supply-chain trust su popisani i imaju vlasnike.
3. Source-to-installed-runtime identity lanac je dokazan ili je svaki prekid eksplicitan blocker/preostali rizik.
4. Svaki prozor/webview ima dokumentovan origin, lifecycle, session, privilegiju, bridge/capability, navigation politiku, vlasnika podataka i negativne testove.
5. Electron webPreferences/preload/IPC ili Tauri capabilities/permissions/scopes/commands sprovode least privilege u stvarnoj zapakovanoj aplikaciji.
6. Remote i user-controlled sadrzaj ne moze da dosegne lokalni kod, tajne, fajlove, uredjaje, updater, installer ili druge naloge bez eksplicitne autorizacije.
7. Path, URL, deep-link, external-open, file import/export, archive i local-service granice su kanonikalizovane, scoped, autentifikovane i testirane.
8. Lokalni podaci imaju ownership, dozvole, semu/migraciju, backup/restore, corruption recovery, account izolaciju, retention i uninstall politiku.
9. Kriticni write-ovi i eksterni side effect-i imaju constraint-e, transakcije ili durable state tranzicije, concurrency kontrolu, idempotency i crash recovery.
10. Network klijenti i lokalni listener-i imaju TLS/peer trust, autentikaciju, timeout-e, ogranicen retry, cancellation, backpressure, redakciju i failure testove.
11. Native module-i, FFI, sidecar-i, codec-i, sistemski dependency-ji i WebView runtime-i su verifikovani na svakoj podrzanoj platformi/arhitekturi.
12. Sadrzaj paketa nema nenamerne tajne, debug povrsine, writable executable kod, nepodrzane binary fajlove ili neobjasnjene dodatke.
13. Svaki distribuirani artefakt je vezan za source, pregledan, hash-ovan, potpisan gde je potrebno, timestamp-ovan/notarizovan gde je primenljivo i verifikovan posle instalacije.
14. Install, repair, upgrade sa svakog podrzanog source-a, skipped-version update, prekinuti update, rollback/recovery i uninstall su testirani sa reprezentativnim podacima.
15. Update metadata, potpisi, custody kljuceva, channel politika, staged rollout, abort, downgrade, rollback, revocation i compromised-key response su dokazani.
16. Startup, odziv, memorija, CPU, GPU, disk, mreza, idle, long-run i failure-containment budzeti su izmereni na reprezentativnim sistemima.
17. Pristupacnost, lokalizacija, high DPI, vise ekrana, tastatura, screen reader, IME, dozvole i native dialog-i su verifikovani u packaged build-ovima.
18. Logovi, metrike, trace-ovi, crash-evi, simboli/source map-e, alert-i, privacy redakcija, diagnostic export i runbook-ovi podrzavaju dijagnostiku incidenta.
19. CI/CD odvaja nepoverljiv i privilegovan rad, promovise nepromenljive artefakte, stiti signing/publishing, zadrzava dokaze i vezba emergency release.
20. Svi P0/P1 nalazi su popravljeni ili imaju eksplicitan containment i recovery; P2/P3 imaju vlasnike, acceptance kriterijume i prioritete.
21. Komande, okruzenja, izlazi, skipped provere, evidence ceiling, izmenjeni fajlovi, testovi, hash-evi artefakta i eksterni izvori su zabelezeni.
22. Finalni zakljucak je `ready`, `ready-with-conditions` ili `not-ready`, sa tacnim blocker-ima i preostalim rizikom.

