## 4. EF Core, Integritet Podataka, Migracije I Cache

Pregledaj context lifetime, provider/verziju, entity konfiguraciju, migration SQL, indexes/constraints, concurrency tokens, precision, pooling, command timeout, raw SQL, N+1/cartesian, tracking, isolation, soft delete/audit, backup/restore.

Migracije: vlasnik, SQL review, backup/restore, lock/duration, rolling compatibility, backfill, forward repair, rollback/kompenzacija. Preferiraj SQL skripte ili migration bundle umesto startup `Database.Migrate()` sa svake replike.

Za kriticne upise dokumentuj i testiraj concurrency/idempotency. Process-local lock ne stiti horizontalno skalirane instance. Cache: key scope, TTL, invalidacija, stampede; privatni podaci bez shared/public kljuca.

