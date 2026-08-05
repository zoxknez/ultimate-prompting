## Faza 15 - Queue-ovi, Messenger, Horizon, scheduling, cron i background rad

### Cilj

Dokaži delivery, retry, ordering, deduplikaciju, resource, deployment i recovery ponašanje za sav asinhroni rad.

### Zahtevi audita

- Inventariši svaki queue, transport, topic, subscription, failed transport, Horizon supervisor, Messenger worker, scheduler, cron, batch i spoljni trigger.
- Proveri message schema, serializaciju, versioning, tenant i actor context, autorizaciju, idempotency ključ, correlation, trace i sensitive-data policy.
- Audituj acknowledgement timing, visibility timeout, retry raspored, max attempts, backoff, jitter, dead-letter postupanje, poison-message quarantine i replay odobrenje.
- Testiraj worker crash pre i posle side effect-a, broker redelivery, reorderovane event-e, duplikate, odložene poruke, stale poruke i schema mismatch.
- Pregledaj scheduler overlap, lock TTL, leader election, clock skew, propuštena pokretanja, catch-up, DST, duge taskove i multi-replica izvršavanje.
- Proveri bounded concurrency, prefetch, memory, pritisak na database pool, backpressure, graceful drain, zamenu worker-a i deployment kompatibilnost.

### Obavezni dokazi

- Matrica async topologije i message ugovora sa owner-om, retry-jem, DLQ-om i recovery putanjom.
- Dokaz crash, duplicate, reorder, poison, replay, shutdown i mixed-version worker testova.
- Dokaz rollout-a worker-a i scheduler-a povezan sa artifact revizijom i queue depth-om.

### Kriterijumi prihvatanja

- At-least-once delivery i retry ne krše poslovne invarijante niti cure tenant context.
- Worker-i mogu da se drain-uju, zamene, replay-uju i oporave bez tihog gubitka ili nekontrolisanog dupliranja.

