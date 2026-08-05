## Definition Of Done

Rad je zavrsen samo kada je svih 23 uslova ispod obelezeno dokazom ili `NIJE_PRIMENJIVO` uz obrazlozenje:

1. Repo snapshot i status tudjih izmena su zabelezeni.
2. Stvarni build sistem i JDK/toolchain su identifikovani.
3. Support/lifecycle status je proveravan na aktuelnim primarnim izvorima.
4. Arhitektura i kriticni tokovi su mapirani.
5. Baseline komande i prvi neuspeh su sacuvani.
6. Svi P0/P1 nalazi imaju dokaz, uzrok, uticaj i vlasnika.
7. Potencijalni rizici su odvojeni od potvrdjenih nalaza.
8. Autentikacija, autorizacija, ownership i tenant izolacija su provereni.
9. Javni i management security chainovi su provereni.
10. Kriticni write tokovi imaju transakcioni i idempotency dokaz.
11. Concurrency i failure scenariji su testirani ili jasno blokirani.
12. Migracije, backup/restore i rollback ogranicenja su dokumentovani.
13. Message/job retry, ack, deduplication i shutdown ponasanje su provereni.
14. Secrets, konfiguracija, Actuator i dependency supply chain su auditirani.
15. Timeout, retry, rate limit i resource limiti su razumno bounded.
16. Health, observability, alerti i runbook imaju stvarne dokaze.
17. Container/deployment/native razlike su proverene kada postoje.
18. Graceful shutdown je testiran ili oznacen `NEPROVERENO` sa razlogom.
19. Implementirane izmene su minimalne, reviewable i povezane sa nalazima.
20. Svaka popravka P0-P2 ima ciljani regresioni test.
21. Relevantni test/build opseg je izvrsen posle izmena.
22. Komandni dnevnik sadrzi okruzenje, exit status i rezultat.
23. Zavrsna presuda, blokatori, preostali rizik, rollback/recovery i sledeci vlasnici su jasni.

