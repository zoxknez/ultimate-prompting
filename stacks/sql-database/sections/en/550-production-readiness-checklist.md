## Production Readiness Checklist

- All critical datasets, topologies, owners and trust boundaries are inventoried.
- Actual engine, patch, edition, extensions, drivers and support status are verified.
- Schema source of truth and drift controls are defined.
- Critical invariants are enforced atomically and have reconciliation queries.
- Transaction, isolation, locking, timeout, idempotency and uncertainty behavior are tested.
- Representative plans, indexes, statistics and capacity evidence exist.
- Connection pools and proxies are bounded and safe during failover.
- Migrations and backfills are rehearsed with mixed versions and abort gates.
- Authentication, privilege, tenancy, encryption, secrets and audit controls are verified.
- Backup, PITR, restore, application verification, RPO and RTO are proven.
- Failover, stale-primary fencing, reconnect, failback and reconciliation are tested.
- Observability, SLOs, alerts, runbooks, capacity and cost guardrails are operational.
- Rollout, rollback, forward repair and incident trusted-recovery plans are owned and tested.

