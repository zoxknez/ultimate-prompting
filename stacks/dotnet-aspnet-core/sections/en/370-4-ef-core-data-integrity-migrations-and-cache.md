## 4. EF Core, Data Integrity, Migrations, And Cache

Review context lifetime, provider/version, entity configuration, migration SQL, indexes/constraints, concurrency tokens, precision, pooling, command timeout, raw SQL, N+1/cartesian, tracking, isolation, soft delete/audit, backup/restore.

Migrations: owner, SQL review, backup/restore, lock/duration, rolling compatibility, backfill, forward repair, rollback/compensation. Prefer SQL scripts or migration bundles over startup `Database.Migrate()` from every replica.

For critical writes document and test concurrency/idempotency. A process-local lock does not protect horizontally scaled instances. Cache: key scope, TTL, invalidation, stampede; private data without shared/public keys.

