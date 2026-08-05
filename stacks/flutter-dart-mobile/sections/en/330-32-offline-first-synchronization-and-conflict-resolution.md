## 32. Offline-First, Synchronization, And Conflict Resolution

Offline behavior must define authority, ordering, identity, and conflict semantics.

- Document which reads and writes are allowed offline, their user promise, durability, expiration, cancellation, and server acceptance conditions.
- Assign stable operation IDs and idempotency keys; persist queue state transactionally with payload version, actor, tenant, dependency, retry count, and status.
- Define ordering, dependency, compaction, deduplication, retry, backoff, expiry, poison operation, cancellation, and manual intervention.
- Choose conflict policy per entity and field: server authority, client authority, version check, merge, append-only, CRDT, or explicit user resolution.
- Prevent stale offline operations from acting after logout, role change, tenant change, deletion, quota change, price change, or business-rule change.
- Test long offline periods, clock skew, reordered operations, duplicated operations, partial synchronization, server reset, schema change, token expiry, and multiple devices.
- Provide truthful UI for pending, synced, conflicted, failed, canceled, expired, and rejected operations.
- Measure queue age, conflict rate, retry count, poison rate, duplicate suppression, reconciliation lag, and user-visible data loss.

