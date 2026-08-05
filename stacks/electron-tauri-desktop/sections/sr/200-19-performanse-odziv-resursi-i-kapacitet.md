## 19. Performanse, odziv, resursi i kapacitet

### 19.1 Plan merenja

1. Definisi budzete za cold/warm startup, prvi upotrebljiv prozor, latenciju kriticne interakcije, IPC/command latenciju, update proveru, memoriju, CPU, GPU, disk, mrezu, bateriju, installer velicinu i package velicinu.
2. Meri na reprezentativnom minimalnom i tipicnom hardveru, podrzanim operativnim sistemima, x64/ARM64, cistim i zrelim profilima, online/offline i sa realnim volumenom podataka.
3. Odvoji frontend render vreme, framework bootstrap, native inicijalizaciju, database migraciju, credential pristup, network wait, plugin inicijalizaciju, sidecar startup i updater rad.
4. Snimi trace i profile pre optimizacije. Povezi long task-ove, main-thread blocking, Rust/Node blocking, lock contention, IPC serialization, database upite, filesystem, GPU i mrezu.
5. Testiraj idle ponasanje, hidden/tray rezim, minimizovane prozore, background timer-e, service worker-e, polling, telemetriju, device listener-e i updater ritam.
6. Ogranici cache i queue. Definisi eviction, persistence, account izolaciju, stale-data politiku i ponasanje pod memory pressure-om.
7. Meri leak ponasanje kroz otvaranje/zatvaranje prozora, navigaciju, reload, promenu naloga, otvaranje/zatvaranje dokumenta, connect/disconnect uredjaja, update i dugotrajan idle.
8. Ne tvrdi poboljsanje performansi samo na osnovu microbenchmark-a; potvrdi korisnicki tok i resource budget.

### 19.2 Odziv i containment otkaza

1. Odrzi renderer/UI thread-ove odzivnim. Premesti CPU-heavy parsing, compression, indexing, media, cryptography i database rad u odgovarajuce ogranicene worker-e ili native procese.
2. Ne blokiraj Electron main proces ili Tauri event loop sinhronim filesystem, network, crypto, database, child-process ili lock cekanjem.
3. Koristi backpressure od UI-ja kroz IPC/komande do worker-a i eksternih servisa. Odbacivanje, coalescing, pauziranje ili odbijanje rada mora biti eksplicitno.
4. Spreci jedan spor prozor, fajl, uredjaj, network zahtev, tenant/nalog ili plugin da iscrpi globalne resurse.
5. Definisi timeout-e i cancellation za operacije koje mogu da vise. Osiguraj da cancellation ne ostavlja korumpirane fajlove, poluprimenjene migracije ili duplirane side effect-e.
6. Obradi out-of-memory, GPU crash, renderer crash, sidecar crash, WebView failure, database lock i service outage sa ogranicenim recovery-jem.
7. Koristi crash restart samo sa limitima i validacijom stanja. Izbegni petlje koje ponovljeno unistavaju korisnicki rad ili bombarduju update/network servise.
8. Testiraj burst input, ogromnu istoriju, mnogo prozora, velike fajlove, spor disk, malo memorije, high DPI, vise ekrana, sleep/wake i dugotrajan offline rezim.

