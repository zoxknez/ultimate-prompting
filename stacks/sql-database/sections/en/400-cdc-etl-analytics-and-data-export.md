## CDC, ETL, Analytics, And Data Export

- Map snapshot, log position, schema version, ordering, duplicate and delete semantics for every pipeline.
- Test schema evolution, backfill overlap, replay, consumer lag and poison records.
- Verify analytics or search stores are not treated as authoritative for writes or authorization.
- Protect exports with authorization, tenant scope, row limits, encryption, expiry and audit.
- Reconcile source and destination counts, aggregates, checksums where meaningful and critical invariants.
- Define cutover and rollback behavior when a pipeline is part of a migration.

