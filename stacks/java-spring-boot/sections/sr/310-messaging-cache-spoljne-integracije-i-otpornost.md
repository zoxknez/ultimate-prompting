## Messaging, Cache, Spoljne Integracije I Otpornost

### Broker I Consumer Semantika

- Inventariši Kafka, RabbitMQ, JMS, Pulsar, SQS, Pub/Sub, stream-ove, exchange-e, topic-e, queue-eve, particije, consumer group-e, listener-e, serializer-e i retry infrastrukturu.
- Definiši delivery semantiku, ordering key, partitioning, acknowledgement tačku, visibility timeout, retry ownership, dead-letter policy, poison-message obradu, retention i replay proceduru.
- Testiraj crash pre i posle lokalnog commit-a, gubitak acknowledgement-a, duplu isporuku, rebalance, gubitak particije, broker failover, schema mismatch, spor consumer i retry storm.
- Ograniči konkurentnost, prefetch, in-flight zapise, batch size, memoriju, retry rate i downstream pozive; očuvaj backpressure kroz svaki adapter.
- Zaštiti tenant identitet, authorization, osetljive podatke, trace context i schema kompatibilnost kroz production, replay, dead-letter i repair putanje.

### Caching I Distribuirana Koordinacija

- Inventariši local, distributed, HTTP, query, Hibernate, method, result, session, token, metadata i negative cache-eve sa autoritativnim izvorima i ownership-om.
- Definiši konstrukciju key-a, tenant i authorization dimenzije, value schema-u, TTL, refresh, invalidaciju, versioning, očekivanje konzistentnosti i ponašanje tokom cache outage-a.
- Testiraj stampede, hot key-eve, eviction, stale read, parcijalnu invalidaciju, deployment schema promenu, serialization promenu, clock skew, failover i cache poisoning.
- Za distributed lock i lease zahtevaj owner identitet, TTL, renewal, fencing token gde stale owner može napraviti štetu, failure detection i cleanup.
- Nikada ne koristi prisustvo cache-a, lock bez fencing-a ili best-effort invalidaciju kao jedinu zaštitu za novac, inventory, kvotu, uniqueness ili authorization invarijantu.

### Outbound Klijenti I Resilience Pravila

- Inventariši HTTP, gRPC, database, broker, DNS, SMTP, object storage, payment, identity, search i custom klijente sa destination allow listama i ownership-om.
- Definiši connect, handshake, request, read, write, idle, total i pool-acquisition timeout plus deadline propagation i maksimalne veličine odgovora.
- Primeni retry samo na klasifikovane prolazne failure-e i replay-safe operacije; uključi limit pokušaja, elapsed-time budget, jitter, `Retry-After` i sprečavanje nested retry-ja.
- Pregledaj circuit breaker, bulkhead, rate limiter, concurrency limiter, hedging, fallback i degraded mode za state ispravnost i observability.
- Testiraj DNS promene, stale pooled konekcije, rotaciju sertifikata i kredencijala, parcijalne odgovore, malformed odgovore, redirect zloupotrebu, SSRF, dependency brownout i potpuni outage.

### Search, Object Storage, Email I Plaćanja

- Tretiraj search index-e, object store-ove, mail sisteme, payment provider-e i third-party API-je kao odvojene domene konzistentnosti, identiteta, authorization-a i oporavka.
- Definiši source of truth, sinhronizaciju, idempotency, ordering, reconciliation, deletion, retention i ponašanje kada callback ili acknowledgement kasni ili se duplira.
- Za object storage proveri bucket/container policy-je, path i tenant vezivanje, scope i expiry signed URL-a, validaciju sadržaja, encryption, versioning, lifecycle i delete semantiku.
- Za email i notification spreči header/template injection, recipient confusion, curenje osetljivih podataka, duplo slanje i neograničen fan-out.
- Za plaćanja i druge nepovratne operacije dokaži provider idempotency, webhook verifikaciju, amount/currency precision, ledger reconciliation, refund/chargeback obradu i manuelni oporavak.


