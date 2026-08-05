## 41. Zabranjene prečice

1. Ne proglašavaj uspeh zato što se aplikacija pokreće iz source-a, unit suite prolazi ili jedan nepotpisan paket radi na developer mašini.
2. Ne pozivaj `processEvents`, ne spavaj na GUI thread-u, ne prebacuj UI rad na proizvoljne thread-ove i ne drži objekte globalno živim samo da sakriješ lifecycle defekte.
3. Ne ažuriraj widget-e ili modele direktno iz worker-a, ne ignoriši thread affinity i ne pretpostavljaj da GIL čini Qt i poslovno stanje thread-safe.
4. Ne uključuj free-threaded režim, JIT, novi Python major ili novi Qt major bez dokaza za native zavisnosti, packaging, platformu i rollback.
5. Ne potiskuj izuzetke, Qt upozorenja, failed future-e, unhandled task-ove, type greške, linter rezultate, packaging upozorenja, signature kvarove ili migration greške bez root-cause analize.
6. Ne dodaj široke `except` blokove, prazne handler-e, proizvoljne sleep-ove, forced garbage collection, unchecked cast-ove, globalno mutable stanje ili blanket suppression kao univerzalne popravke.
7. Ne deserijalizuj nepoverljiv pickle/YAML/object sadržaj, ne izvršavaj korisnički input, ne učitavaj proizvoljne plugin-e i ne kompajliraj nepoverljiv QML/JavaScript/template.
8. Ne gradi shell komande interpoliranim inputom, ne veruj automatski localhost-u, ne otvaraj proizvoljne URL-ove i ne pretražuj writable putanje za kod i helper-e.
9. Ne isključuj TLS validaciju, ne prihvataj sve sertifikate, ne čuvaj tajne u plain settings i ne loguj tokene, credential-e, lične podatke ili kriptografski materijal.
10. Ne proširuj file, device, plugin, WebChannel, IPC, helper, service ili installer dozvole samo da bi funkcija proradila.
11. Ne tretiraj PyInstaller/Nuitka/Qt bundling, obfuscation, code signing, antivirus odobrenje ili OS sandbox kao kompletnu security granicu.
12. Ne migriraj ili resetuj podatke automatski bez backup-a i failure semantike; ne briši tiho korumpirane profile-e ili korisničke fajlove.
13. Ne objavljuj mutable ili nepotpisane artefakte, ne rebuild-uj različite bajtove po okruženju bez razloga i ne dozvoli untrusted CI-ju pristup signing-u i produkcionim kanalima.
14. Ne povećavaj thread, queue, timeout, retry, memory, disk, parser ili transfer limite bez capacity i abuse analize.
15. Ne tvrdi Windows, macOS, Linux, x64, ARM64, high DPI, accessibility, update, rollback ili restore podršku bez primenljivih packaged dokaza.
16. Ne masovno formatiraj, ne briši nepovezane fajlove, ne slabi testove, ne krij neuspele provere i ne prepisuj tuđ rad.
17. Ne nazivaj aplikaciju savršenom, potpuno bezbednom, potpuno testiranom ili production-ready bez ispunjavanja primenljivih evidence i recovery zahteva.

