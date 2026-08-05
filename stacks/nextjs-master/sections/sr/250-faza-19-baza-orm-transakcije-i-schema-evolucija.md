## Faza 19 - Baza, ORM, transakcije i schema evolucija

Dokazi poslovne invarijante na autoritativnom data layer-u i bezbednu evoluciju kroz concurrency i mixed verzije.

### Zahtevi audita

- Inventarisi klijente, ORM instance, pool-ove, replica routing, transaction API-je, raw SQL, migracije, seed-ove i admin skripte.
- Izrazi uniqueness, ownership, referential integrity, state transition-e, balance-e, kvote i idempotency constraint-ima.
- Pregledaj isolation, retry, lock order, optimistic versioning, lost update, write skew, deadlock, timeout i ambiguous commit.
- Detektuj N+1, Cartesian join-ove, scan-ove, nedostajuce index-e, stale statistike, overfetch, per-request klijente i pool exhaustion.
- Razdvoji expand, backfill, code rollout, constraint validaciju i contract cleanup.
- Koordiniraj database commit sa payment, email, storage, search, queue i webhook efektima koristeci durable obrasce.

### Obavezni dokazi

- Invariant-to-constraint i transaction matrica.
- Production-like query plan-ovi, cardinality, pool sizing i latency dokaz.
- Migration graph sa expand, backfill, switch, validate, contract i repair koracima.
- Outbox/inbox ili ekvivalentan atomicity i reconciliation dokaz.

### Obavezni failure i acceptance testovi

- Izvrsi konkurentne write operacije protiv svake kriticne invarijante.
- Izazovi crash pre commit-a, tokom ambiguity-ja, posle commit-a pre response-a i pre external acknowledgement-a.
- Pokreni staru i novu app verziju kroz svaku migration fazu.
- Iscrpi connection kapacitet i proveri admission, timeout, recovery i zastitu baze.

