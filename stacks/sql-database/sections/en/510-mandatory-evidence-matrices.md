## Mandatory Evidence Matrices

| Matrix | Required contents |
| --- | --- |
| M1 - Identity | Commit, migration checksum, engine build, package or image, endpoint, database, schema and process. |
| M2 - Topology | Primary, replicas, proxies, pools, regions, read/write routes, failover authority and owners. |
| M3 - Schema drift | Source, migration, catalog, ORM, test schema, grants, policies and divergence. |
| M4 - Invariants | Invariant, enforcement layer, concurrent test, reconciliation query and repair owner. |
| M5 - Transactions | Flow, isolation, locks, timeout, idempotency, external effects, retry and uncertainty behavior. |
| M6 - Queries | Fingerprint, parameters, plans, indexes, statistics, p50/p95/p99, rows and regression threshold. |
| M7 - Connections | Clients, pools, maximums, timeouts, session reset, failover and aggregate capacity. |
| M8 - Migration | DDL, locks, rewrite, log volume, old/new compatibility, backfill, abort and repair. |
| M9 - Security | Identity, grants, tenant controls, encryption, secrets, audit and negative tests. |
| M10 - Backup | Backup type, retention, encryption, log chain, restore result, RPO, RTO and application verification. |
| M11 - HA | Lag, durability, promotion, fencing, reconnect, failback, loss and reconciliation. |
| M12 - Release readiness | Artifact, schema, rollout, observability, capacity, rollback, forward repair and owners. |

