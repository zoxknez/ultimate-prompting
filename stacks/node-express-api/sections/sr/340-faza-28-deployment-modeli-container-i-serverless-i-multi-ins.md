## Faza 28 - Deployment Modeli, Container-i, Serverless I Multi-Instance Ponašanje

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Identifikuj tacan deployment model za svaki API, worker, scheduler, migrator, CLI i realtime proces.
- Proveri build i runtime image, user-a, filesystem, dozvole, init, signal-e, sertifikate, locale, DNS i native biblioteke.
- Pokreni kao non-root gde je izvodljivo, koristi read-only filesystem i uklonjene capability-je gde je kompatibilno i izoluj temp storage.
- Definisi CPU, memory, storage, file-descriptor, connection, process i concurrency limite.
- Ne oslanjaj se na warm memoriju, module global-e, lokalni disk, process lock-ove ili jednu instancu za correctness.
- Proveri serverless cold start, reuse, concurrency, timeout, payload, streaming, pool, background work i shutdown semantiku.

### Obavezni Dokazi

- Proizvedi i sacuvaj deployment i target-support matricu.
- Proizvedi i sacuvaj runtime security, limits i multi-instance dokaz.
- Proizvedi i sacuvaj graceful drain i process-replacement rezultate.

### Obavezni Failure I Acceptance Testovi

- Dokazi da non-root i read-only runtime cuva funkcionalnost.
- Dokazi da zamena instance ne gubi autoritativno stanje.
- Dokazi da serverless concurrency ne iscrpljuje deljene zavisnosti.

