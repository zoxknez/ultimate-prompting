## Test Strategy And Database Verification Pyramid

Build tests at the layer that can reproduce the relevant engine semantics and failure mode.

- Use unit tests for pure mapping and SQL generation, not as proof of engine behavior.
- Use integration tests on the actual production engine and supported patch family.
- Add schema, migration, rollback, seed, permission and tenant-isolation tests.
- Add concurrent transaction, deadlock, retry, idempotency and commit-uncertainty tests.
- Add representative plan, load, soak, connection-storm and resource-exhaustion tests.
- Add backup, PITR, restore, failover, failback and reconciliation game-day tests.

