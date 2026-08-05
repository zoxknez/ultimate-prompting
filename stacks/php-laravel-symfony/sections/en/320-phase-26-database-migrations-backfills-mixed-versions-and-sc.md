## Phase 26 - Database Migrations, Backfills, Mixed Versions, and Schema Recovery

### Objective

Prove forward-compatible schema evolution, bounded data transformation, observability, repair, and recovery during real deployments.

### Audit Requirements

- Inventory Laravel, Doctrine, Phinx, custom SQL, online-schema, backfill, data-fix, trigger, view, function, and search-index changes.
- Classify additive, compatibility, destructive, long-running, locking, rewrite, backfill, and irreversible operations by engine and data scale.
- Use expand-and-contract sequencing so old and new application or worker versions can coexist through rollout and rollback windows.
- Verify defaults, nullability, indexes, constraints, generated values, trigger behavior, ORM metadata, serialization, and read or write compatibility.
- Design resumable, idempotent, rate-limited, observable backfills with checkpoints, verification queries, pause, retry, and reconciliation.
- Define rollback, forward repair, point-in-time recovery, data correction, and manual intervention for every migration failure mode.

### Required Evidence

- Migration compatibility matrix across old app, new app, old worker, new worker, and schema states.
- Production-like execution, lock, duration, backfill, pause, resume, and verification evidence.
- Restore, forward-repair, and data-reconciliation exercise evidence.

### Acceptance Criteria

- No rollout or rollback window exposes an application version to an incompatible schema.
- Long-running and irreversible data changes have bounded impact, resumability, verification, and recovery.

