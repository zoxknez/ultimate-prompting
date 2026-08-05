## Faza 1 - Repozitorijum, Workspace, Executable I Ownership Mapa

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Mapiraj monorepo workspace-e, pakete, aplikacije, interne biblioteke, deljene scheme, infrastrukturu, migracije i operativne alate.
- Identifikuj svaki API, worker, cron, CLI, migration runner, webhook receiver, realtime gateway i one-off skriptu.
- Dodeli owner-e za autentikaciju, autorizaciju, tenant izolaciju, podatke, cache, queue, release, rollback, restore i incident response.
- Detektuj ciklicne zavisnosti, cross-layer import-e, duplirane scheme, shadow konfiguraciju, mrtve skripte i napustene deployment putanje.
- Mapiraj trust boundary-je od klijenta preko CDN-a i proxy-ja do servisa, database-a, broker-a, storage-a, provider-a i admin tooling-a.
- Razlikuj autoritativnu poslovnu logiku od adapter-a, generisanog koda, framework glue-a i test-only implementacija.

### Obavezni Dokazi

- Proizvedi i sacuvaj workspace i executable graf.
- Proizvedi i sacuvaj route-to-owner i side-effect-to-owner matrice.
- Proizvedi i sacuvaj trust-boundary i mapu autoritativnih izvora.

### Obavezni Failure I Acceptance Testovi

- Dokazi da svaki produkcioni executable je moguce pronaci.
- Dokazi da kriticna ruta ima identifikovanog owner-a.
- Dokazi da nedokumentovane admin i maintenance putanje su otkrivene.

