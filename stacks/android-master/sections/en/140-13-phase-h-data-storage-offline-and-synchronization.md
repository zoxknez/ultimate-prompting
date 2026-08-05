## 13. Phase H - Data, Storage, Offline And Synchronization

### 13.1 Room And Database Correctness

1. Inspect entities, primary keys, foreign keys, indices, uniqueness, nullability, defaults, converters, views, FTS, and embedded models.
2. Verify queries use indices and return only required data for hot paths.
3. Detect main-thread access, N+1 patterns, unbounded reads, cursor leaks, and large object loading.
4. Verify multi-step writes use transactions and preserve invariants.
5. Verify conflict strategies match business semantics and do not silently discard data.
6. Review migration graph from every supported production version.
7. Test migrations with real historical schemas and representative data.
8. Verify destructive fallback is never used for user data without explicit product approval and recovery design.
9. Verify downgrade, backup, restore, prepackaged database, WAL, multi-process, and encryption behavior where applicable.
10. Verify schema export and migration tests are version-controlled.

### 13.2 DataStore, Files, Cache And Content

1. Verify preferences and typed DataStore ownership, corruption handling, migrations, and concurrency.
2. Do not store relational or large mutable data in preferences.
3. Verify files use appropriate internal, external, media, or shared storage APIs.
4. Verify scoped storage, FileProvider paths, URI permissions, MIME types, and lifetime.
5. Prevent path traversal, arbitrary file overwrite, unsafe archive extraction, and exposure through exported providers.
6. Verify caches have bounds, eviction, ownership, privacy, invalidation, and low-storage behavior.
7. Verify backup and restore rules exclude secrets, ephemeral data, tokens, and device-bound encrypted material.
8. Test reinstall, clear data, restore, device transfer, account change, and logout behavior.

### 13.3 Offline-First, Sync And Conflict Resolution

1. Define the authoritative source for each data type.
2. Verify offline reads, queued writes, retry, ordering, idempotency, deduplication, and conflict policy.
3. Verify timestamps and version vectors are not treated as reliable without clock and server semantics.
4. Test reconnect after partial writes, duplicate delivery, process death, app update, token refresh, and server conflict.
5. Verify the UI communicates pending, synced, failed, stale, and conflicted states.
6. Prevent infinite sync loops, battery drain, unbounded queues, and silent data loss.
7. Verify WorkManager constraints and backoff reflect business urgency and device health.
8. Test multi-device and multi-account behavior where applicable.

