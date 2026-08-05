## Faza 22 - Event Loop, Worker Pool, CPU Rad, Async Context I Cancellation

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Izmeri event-loop delay, utilization, worker-pool pressure, CPU, throughput i tail latency pod reprezentativnim load-om.
- Pronadji sinhroni filesystem, crypto, compression, parsing, serialization, regex, template, image i child-process rad na request putanjama.
- Ogranici per-request computational complexity i spreci algorithmic-complexity abuse.
- Koristi worker_threads, izolovane procese, queue-ove, native servise ili streaming samo kada ih merenje opravdava.
- Spreci unbounded Promise.all, unbounded task creation, orphan promise-e, izgubljenu cancellation i slucajnu serializaciju.
- Testiraj AsyncLocalStorage propagation i isolation konteksta kroz promise-e, emitter-e, timer-e, callback-ove, worker-e i queue-ove.

### Obavezni Dokazi

- Proizvedi i sacuvaj event-loop, worker-pool i CPU profile.
- Proizvedi i sacuvaj async ownership, context i cancellation mapu.
- Proizvedi i sacuvaj load, saturation i bounded-concurrency dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da skup input ne moze da blokira sve klijente.
- Dokazi da worker failure je contain-ovan i observable.
- Dokazi da cancellation zaustavlja nepotreban downstream i CPU rad.

