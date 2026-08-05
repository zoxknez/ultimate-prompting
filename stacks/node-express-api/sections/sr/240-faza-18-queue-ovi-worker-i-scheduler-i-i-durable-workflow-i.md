## Faza 18 - Queue-ovi, Worker-i, Scheduler-i I Durable Workflow-i

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Inventarisi producer-e, consumer-e, topic-e, queue-ove, routing key-eve, payload scheme, header-e, DLQ-ove, rasporede i operator-e.
- Definisi delivery semantiku, acknowledgement tacku, visibility ili lease timeout, concurrency, ordering, partitioning i retry budget.
- Ucini consumer-e idempotentnim pod redelivery-jem, retry-jem, rebalance-om, crash-om, timeout-om i operator replay-jem.
- Koristi transactional outbox, inbox, CDC, saga ili reconciliation gde database i broker ne mogu atomicki da commit-uju.
- Ogranici prefetch, concurrency, payload size, retry-je, zadrzane failure podatke i uticaj poison poruke.
- Za scheduler-e spreci duplicate ownership, overlap, missed run, catch-up storm, timezone, DST i clock-skew greske.

### Obavezni Dokazi

- Proizvedi i sacuvaj producer-consumer contract matricu.
- Proizvedi i sacuvaj retry, DLQ, replay i poison-message politiku.
- Proizvedi i sacuvaj schedule ownership, overlap i shutdown dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da consumer crash pre i posle commit-a je bezbedan.
- Dokazi da poison poruka ne moze beskrajno da blokira processing.
- Dokazi da duplo scheduled izvrsavanje cuva invarijantu.

