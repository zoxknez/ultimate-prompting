## Faza 1 - Repozitorijum, workspace i mapa vlasnistva

Mapiraj efektivnu aplikaciju, ne samo top-level folder. Ukljuci monorepo pakete, generatore, deployment projekte, shared UI, interne biblioteke, scheme, infrastrukturu i operativne alate.

### Zahtevi audita

- Identifikuj granice paketa, vlasnike, javne API-je, ciklicne zavisnosti, duplirane utility-je i cross-layer import-e.
- Mapiraj svaku aplikaciju, paket, worker, scheduled job, CLI, migration alat, Storybook, preview i deployment projekat.
- Razdvoji bezbedno shared kod od koda koji propusta server-only module, tajne ili teske zavisnosti u client bundle.
- Dokumentuj vlasnistvo za auth, autorizaciju, podatke, cache invalidaciju, deployment, rollback, restore i incident response.
- Detektuj shadow konfiguraciju, kopiranu route logiku, duple scheme, napustene pakete i nekoriscene deployment putanje.
- Mapiraj trust boundary-je izmedju browser-a, CDN-a, Proxy-ja, runtime-a, baze, queue-a, storage-a, provider-a i admin tooling-a.

### Obavezni dokazi

- Repository tree, workspace graph, mapa vlasnistva i inventar generisanog koda.
- Import graph za kriticne pakete i server/client boundary putanje.
- Route-to-owner i side-effect-to-owner matrice.
- Lista autoritativnih i dupliranih konfiguracionih ili schema izvora.

### Obavezni failure i acceptance testovi

- Izgradi cist checkout bez nedeklarisanih lokalnih fajlova.
- Isprati jedan kritican tok kroz svaki paket i runtime boundary.
- Dokazi koji config ili schema izvor je autoritativan kontrolisanom promenom ili generisanim izlazom.
- Proveri da nijedan client entry ne moze da importuje server-only kod kroz barrel export ili tranzitivnu zavisnost.

