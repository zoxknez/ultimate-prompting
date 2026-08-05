## 28. Definition of Done

1. Workspace i user/signing podaci su zasticeni; stanje repozitorijuma i audit granice su zabelezeni.
2. Svi relevantni source, generated, dependency, build, package, signing, installer, updater, store i runtime resursi su popisani.
3. Stvarne Electron/Tauri i embedded/runtime/tool verzije su verifikovane; podrska i kompatibilnost su proverene prema trenutnim primarnim izvorima.
4. Cist locked restore/build, relevantne staticke provere, testovi, generisanje paketa i pregled artefakta su zabelezeni sa stvarnim komandama i exit code-ovima.
5. Arhitektonska, process, window/webview, origin, privilege, IPC/command, local service, data i update mapa su kompletne.
6. Svaka materijalna tvrdnja ima status i nivo dokaza. Sumnje su odvojene od potvrdjenih nalaza.
7. Svaki P0/P1 ima dokaz, root cause, uticaj, containment, popravku, regression dokaz, release uticaj, rollback i vlasnika.
8. Primenljivi P2 nalazi imaju ciljanu sanaciju ili prioritizovan, testabilan plan. P3 rad se ne predstavlja kao produkcioni blocker bez razloga.
9. Electron security podesavanja ili Tauri capabilities su verifikovani u zapakovanoj aplikaciji pozitivnim i negativnim testovima.
10. Authentication, resource authorization, account/tenant izolacija, session cleanup, secret storage i privilegovane radnje su verifikovani.
11. Kriticni lokalni write-ovi, migracije, sinhronizacija i eksterni side effect-i su bezbedni pod duplicate, concurrent, interrupted i crash uslovima.
12. Fajlovi, URL-ovi, protokoli, import-i, export-i, arhive, download-i, external-open, lokalni listener-i, sidecar-i i uredjaji su ograniceni i testirani.
13. Build i package supply chain, SBOM/provenance, identitet artefakta, signing, notarizacija, custody kljuceva i opoziv su verifikovani.
14. Cista instalacija, upgrade matrica, repair, prekinuti update, rollback/recovery i uninstall su testirani ili jasno blokirani sa tacnim razlozima.
15. Performance i resource tvrdnje su zasnovane na merenju; pristupacnost i lokalizacija su testirane u packaged build-ovima.
16. Observability i incident artefakti mogu identifikovati tacnu verziju/kanal/platformu/proces i dijagnostikovati kritican otkaz bez izlaganja osetljivih podataka.
17. CI/CD gate-ovi, promocija artefakta, staged rollout, abort, emergency release, rollback i compromised-key procedure su dokumentovani i vezbani gde je potrebno.
18. Finalni diff je uzak, pregledan, bez nepovezanih izmena i ukljucuje potrebne testove i dokumentaciju.
19. Finalni izvestaj sadrzi tacne komande, dokaze, artefakte, hash-eve, izmene, testove, blocker-e, preostali rizik, vlasnike i autoritativne izvore.
20. Ako bilo koji primenljivi uslov nije zadovoljen, aplikacija nije potpuno production-ready i tacan blocking uslov je naveden.

