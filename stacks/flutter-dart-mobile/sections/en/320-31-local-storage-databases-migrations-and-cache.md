## 31. Local Storage, Databases, Migrations, And Cache

Local persistence is a versioned data system, not an implementation detail.

- Inventory SQLite/Drift/sqflite, Isar, Hive, ObjectBox, Realm, SharedPreferences, secure storage, files, browser storage, desktop preferences, caches, and indexes.
- Classify authoritative data, replicated data, cache, derived data, secret material, draft state, queue state, telemetry state, and disposable data.
- Verify schema versioning, forward migration, rollback policy, interrupted migration, low disk, corruption, old application version, restored backup, and partial write behavior.
- Use transactions for multi-step invariants; inspect isolation, concurrent readers/writers, nested transactions, WAL/journal behavior, and native-thread access.
- Partition data by account and tenant; verify logout, account switch, tenant switch, deletion, backup, restore, and cache invalidation.
- Audit encryption claims, key lifecycle, searchable metadata, temporary files, backups, screenshots, browser DevTools exposure, and desktop filesystem permissions.
- Define cache key, freshness, stale-while-revalidate, invalidation, size, eviction, corruption, stampede protection, and offline semantics.
- Require migration fixtures from every supported historical version and test upgrade, interrupted upgrade, recovery, downgrade rejection, and data export.

