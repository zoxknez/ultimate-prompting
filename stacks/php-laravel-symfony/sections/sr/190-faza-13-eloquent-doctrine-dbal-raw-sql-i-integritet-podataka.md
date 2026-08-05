## Faza 13 - Eloquent, Doctrine, DBAL, raw SQL i integritet podataka

### Cilj

Audituj persistence mapping-e, query ponašanje, constraint-e, konkurentnost, performanse i životni ciklus podataka korišćenjem production-like dokaza.

### Zahtevi audita

- Inventariši svaku bazu, konekciju, repliku, ORM, DBAL, query builder, raw SQL putanju, stored procedure, search index i analytical sink.
- Pregledaj model ili entity identitet, equality, cast-ove, custom tipove, value object-e, nullability, default-e, timestamp-e, soft delete, inheritance i serializaciju.
- Audituj ownership relacija, cascade, orphan removal, pivot podatke, eager i lazy loading, global filtere ili scope-ove i N+1 ili Cartesian rast.
- Proveri schema constraint-e za uniqueness, foreign key, check, exclusion, tenant granice, money precision, status tranzicije i immutable činjenice.
- Testiraj query planove i index-e sa production-like cardinality, skew, selectivity, dubinom paginacije, sort redosledom, lock ponašanjem i replica lag-om.
- Audituj optimistic i pessimistic locking, stale entity-je, unit-of-work granice, identity map-e, detached object-e, retry i postupanje sa deadlock-om.

### Obavezni dokazi

- Schema-to-model mapping i matrica invarijanti sa dokazom database constraint-a.
- Reprezentativni query planovi i load merenja nad production-like podacima.
- Concurrency testovi za lost update, write skew, duplicate insertion, deadlock i replica lag.

### Kriterijumi prihvatanja

- Kritične invarijante sprovode durable constraint-i ili jednako snažni atomski mehanizmi, ne samo application callback-ovi.
- Query, locking i pool ponašanje ostaje ograničeno pod reprezentativnim scale-om i konkurentnošću.

