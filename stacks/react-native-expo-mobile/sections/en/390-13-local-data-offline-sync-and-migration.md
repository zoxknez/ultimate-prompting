## 13. Local Data, Offline, Sync, And Migration

### 13.1 Storage Inventory And Schema
- Inventory AsyncStorage, MMKV, SQLite, Realm, WatermelonDB, filesystem, SecureStore, Keychain, Keystore, native SDK stores, and caches.
- For each store record schema version, owner, transaction model, thread model, encryption, backup, corruption recovery, quota, and deletion behavior.
- Use atomic writes or database transactions for durable state and prove crash behavior at each commit boundary.
- Test old data with new binary, old data with OTA update, partially migrated data, interrupted migration, low storage, and read-only state.
- Never allow an OTA update to require an irreversible local schema change unless runtime compatibility, fallback, and forward repair are proven.
- Define backup, restore, export, deletion, reinstall, account-switch, and device-transfer semantics.

### 13.2 Offline Queue And Conflict Resolution
- Model every queued command with stable ID, actor, tenant, resource, precondition, payload version, idempotency key, attempt count, and terminal state.
- Define ordering, dependency, cancellation, replacement, compaction, expiration, priority, and user-visible pending state.
- Resolve conflicts with explicit domain rules rather than generic last-write-wins unless the business accepts data loss.
- Test duplicate delivery, reordered delivery, partial batch success, stale precondition, server rejection, token expiry, app upgrade, and account switch.
- Provide reconciliation and manual recovery when neither client nor server can determine the final state safely.
- Measure queue age, depth, retries, conflicts, dead letters, bytes, and time to convergence.

