## Faza 20 - Queue-evi, job-ovi, cron i asinhroni rad

Auditiraj asinhrono izvrsavanje kao durable state machine sa eksplicitnim ownership-om, delivery-jem, idempotency-jem i recovery-jem.

### Zahtevi audita

- Inventarisi cron, queue-eve, workflow-e, worker-e, email, export, media i retry sisteme.
- Definisi producer-a, consumer-a, schemu, delivery, ordering, partition, acknowledgement, retry, DLQ, retention i replay.
- Ucini consumer-e idempotentnim kroz duplikate, timeout, crash, retry, rebalance i manuelni replay.
- Zastiti tenant context, auth-derived odluke, tajne i PII u payload-ima i telemetry-ju.
- Ogranici concurrency, batch, prefetch, payload, memoriju, duration, cost i downstream pritisak.
- Definisi pause, drain, resume, kill, replay, reconciliation i poison-message procedure.

### Obavezni dokazi

- Async flow i state-machine inventar.
- Producer/consumer ugovor i idempotency matrica.
- Backlog, age, failure, retry, DLQ, saturation i cost telemetry.
- Pause, drain, replay i reconciliation runbook-ovi.

### Obavezni failure i acceptance testovi

- Isporuci istu poruku vise puta pre i posle efekata.
- Izazovi crash pre commit-a, posle commit-a, pre acknowledgement-a i tokom external poziva.
- Napravi backlog i downstream slowdown i proveri bounded recovery.
- Replay-uj stari DLQ item posle schema, permission i deployment promena.

