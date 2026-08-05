## 31. Strategija testiranja, alati i quality gate-ovi

### 31.1 Obim audita

1. Inventariši unit, property, contract, integration, model/view, signal/thread, GUI, end-to-end, package, installer, update, performance, accessibility, security i recovery testove.
2. Pregledaj pytest konfiguraciju, marker-e, fixture-e, izolaciju, privremene putanje, event-loop integraciju, Qt bot tooling, timeout-e, retry-je, paralelizam, random i flaky-test politiku.
3. Mapiraj mock-ove, fake-ove, emulator-e, lokalne servise, baze, uređaje, network proxy-je, satove, keyring-e, update feed-ove i platformske VM-ove na produkciono ponašanje.
4. Identifikuj netestirane entrypoint-e, generisani kod, packaging hook-ove, frozen-only putanje, installer custom action-e, update logiku, native ekstenzije i crash recovery.
5. Definiši matrice podržane platforme, arhitekture, Python-a, Qt-a, grafičkog backend-a, locale-a, naloga, data verzije i upgrade-a.
6. Razdvoji brze presubmit gate-ove od scheduled, release, destruktivnih, hardware, store i disaster-recovery suite-ova.

### 31.2 Obavezna verifikacija

1. Pokreni determinističke fokusirane testove za svaki nalaz, zatim najširu primenljivu clean, packaged, installed i runtime matricu.
2. Koristi race/stress ponavljanje, fault injection, network shaping, disk i memory pressure, malicious corpus i kill/restart testiranje za kritične putanje.
3. Zabeleži tačnu komandu, okruženje, verzije, platformu, exit code, trajanje, logove, artefakte i zaključak za svaki prijavljeni test.
4. Quarantine-uj flaky test samo sa vlasnikom, dokazom, expiry-jem i planom zamene; ne tretiraj retry kao dokaz ispravnosti.
5. Blokiraj release kada su kritične matrice preskočene bez dokumentovanog plafona dokaza, vlasnika i acceptance plana.

