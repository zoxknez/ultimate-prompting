## 20. Persistence, Settings, Databases, Migrations, And Offline State

### 20.1 Audit Scope

1. Inventory QSettings, JSON/YAML/TOML/XML files, SQLite, SQLAlchemy, ORM stores, caches, key-value databases, object stores, histories, queues, and temporary files.
2. Record schema and format versions, ownership, permissions, encryption, journaling, atomic-write strategy, locking, backup, retention, and deletion.
3. Review database connection ownership per thread/process, transaction boundaries, isolation, constraints, busy timeouts, WAL, checkpoints, corruption handling, and close order.
4. Assess concurrent application instances, crash during write, disk full, read-only media, antivirus locking, network home directories, and interrupted upgrade.
5. Map offline command queues, sync cursors, conflict resolution, deduplication, tombstones, clock assumptions, and reconciliation with server authority.
6. Distinguish user preferences from security policy, credentials, authorization state, business records, derived caches, and recoverable downloads.

### 20.2 Required Verification

1. Run migration matrices from every supported historical version using representative, large, malformed, partially migrated, and corrupted datasets.
2. Inject crashes before, during, and after atomic writes, commits, schema changes, cache replacement, and sync acknowledgement.
3. Test two application instances, stale locks, concurrent updates, account switching, rollback to an older binary, and forward repair.
4. Perform isolated backup restore and, where applicable, point-in-time recovery; measure and record achieved RPO and RTO.
5. Prove that logout, user deletion, retention expiry, uninstall, and support-bundle creation handle each data class according to policy.

