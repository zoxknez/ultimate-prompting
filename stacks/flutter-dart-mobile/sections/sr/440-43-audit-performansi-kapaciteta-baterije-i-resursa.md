## 43. Audit performansi, kapaciteta, baterije i resursa

Profiluj release/profile build-ove na reprezentativnom hardveru pre optimizacije.

- Definiši budžete za cold/warm startup, first frame, time to interactive, route tranziciju, input latenciju, frame build/raster vreme, memoriju, CPU, bateriju, mrežu, disk i veličinu artefakta.
- Sačuvaj DevTools timeline-e, frame chart-ove, CPU profile-e, allocation profile-e, heap snapshot-e, mrežne trace-ove, shader/raster ponašanje, platformske trace-ove i backend metrike.
- Meri slabe uređaje, stare podržane uređaje, velike skupove podataka, spor storage, ograničenu memoriju, thermal pressure, battery saver, lošu mrežu i duge sesije.
- Audituj startup dependency lanac, sinhroni I/O, inicijalizaciju plugin-a, migraciju baze, remote config, obnovu autentikacije, font/image decode i rad prve rute.
- Otkrij rebuild i relayout hotspot-e, skup paint, trošak platform view-a, churn velikih objekata, image/cache leak-ove, stream/listener leak-ove, isolate overhead i background wakeup-e.
- Testiraj burst, soak, paginaciju, ogromnu listu, brzu navigaciju, ponovljen login/logout, promenu naloga, offline queue, reconnect, upload/download, medije i notification storm.
- Poveži client ponašanje sa API stopom, retry amplification-om, websocket konekcijama, push registracijom, rastom storage-a, cache hit stopom i cloud troškom.
- Zahtevaj before/after merenja, statistički kontekst, device matricu, definiciju workload-a, vizuelnu ispravnost i rollback za performance izmene.

