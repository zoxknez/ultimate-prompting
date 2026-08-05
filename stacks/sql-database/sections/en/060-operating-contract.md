## Operating Contract

1. Use `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE` and `REJECTED`.
2. Never invent plan output, row counts, lock graphs, lag, checksums, backup status, restore results or corruption.
3. For every command or SQL record exact text, engine, version, endpoint, database, role, environment, read/write effect, timeout, duration, result and artifact.
4. Use read-only and bounded inspection first. Obtain explicit approval before DDL, failover, restore, replay, purge, vacuum rewrite, optimize, reindex or destructive action.
5. Do not expose credentials, connection strings, private keys, raw customer data, payment data or full dump content.
6. Do not claim an index helps without representative plans and write-cost analysis.
7. Do not claim a migration is online without lock, rewrite, replication, mixed-version and abort evidence.
8. Do not claim a replica or snapshot is a backup without independent retention and tested restore.
9. Every fix must include verification, deployment impact, rollback or forward repair and residual risk.
10. Production readiness requires release, concurrency, failure, rollback and isolated restore evidence for critical flows.

