## Phase K - Shared Functional Correctness And Data

For each critical flow: `entry → authn → authz → validation → use case → transaction → DB/cache/broker/external service → response → telemetry`.

Check illegal state transitions, race scenarios, money/inventory rules, audit trail. Domain rules must not live only in handlers or clients.

Transactions: real boundary (not just a function name), isolation, deadlock retry, partial failure, outbox/inbox, saga/compensation. Idempotency for retryable writes: key, unique constraint, stored outcome, conflict response. Process-local/in-memory idempotency does not protect multi-replica systems.

Migrations: owner, SQL review, lock/duration, rolling compatibility, backup/restore, rollback/forward repair. Do not execute destructive migrations during the audit.

