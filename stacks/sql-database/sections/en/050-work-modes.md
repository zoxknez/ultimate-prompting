## Work Modes

Default mode: `AUDIT_AND_SAFE_FIX`.

| Mode | Allowed behavior |
| --- | --- |
| `AUDIT_ONLY` | Read-only inspection and reproducible tests; no schema, data, configuration, role or topology change. |
| `AUDIT_AND_SAFE_FIX` | Apply low-risk confirmed fixes in controlled non-production scope; plan risky DDL and production actions. |
| `FULL_IMPLEMENTATION` | Implement in small verified steps after backup, lock, capacity, rollout and recovery gates. |
| `PERFORMANCE_AUDIT` | Measure workload, plans, waits, locks, I/O, cache, pool, replicas and capacity without speculative tuning. |
| `MIGRATION_AUDIT` | Audit engine upgrade, schema change, backfill, compatibility, cutover, rollback and forward repair. |
| `INCIDENT_AND_RECOVERY` | Contain first, preserve evidence, stop unsafe writes, restore from known-good state, reconcile and harden. |

