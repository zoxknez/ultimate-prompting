## Persistence, Transactions, And Data Recovery

### JPA, Hibernate, JDBC, And Mapping Correctness

- Review entity identity, equality, hash codes, mutability, ownership, cascade, orphan removal, fetch strategy, inheritance, converters, listeners, generated values, and audit fields.
- Detect N+1 queries, Cartesian products, unbounded collections, lazy access outside valid context, duplicate joins, accidental flushes, dirty-checking surprises, and serialization of entities.
- Verify optimistic and pessimistic locking, lock timeout, deadlock handling, isolation, write skew, lost update prevention, and retry scope using concurrent tests.
- Inspect actual SQL, bind values with safe redaction, query plans, indexes, cardinality estimates, row counts, sorting, pagination stability, and production-like data distributions.
- Treat ORM portability as unproven until each supported database dialect, version, collation, timezone, isolation, and migration path is tested.

### Connection Pools And Database Failure

- Record pool implementation, min/max size, acquisition timeout, validation, lifetime, idle timeout, leak detection, initialization SQL, transaction defaults, and metrics.
- Size pools against database capacity, replica count, background work, admin traffic, virtual-thread concurrency, failover behavior, and other applications.
- Test pool exhaustion, slow queries, network partition, primary failover, DNS change, stale connections, credential rotation, certificate rotation, and database restart.
- Verify timeouts and cancellation reach the driver and server where possible; abandoned client futures must not leave unlimited database work.
- Alert on saturation, wait time, timeouts, active/idle imbalance, transaction age, deadlocks, replication lag, and error classes tied to runbooks.

### Transaction Boundary Proof

- For every critical operation, record transaction manager, propagation, isolation, read-only flag, timeout, rollback rules, proxy path, participating resources, and side effects outside the transaction.
- Test checked exceptions, caught exceptions, wrapped exceptions, asynchronous boundaries, self-invocation, multiple transaction managers, savepoints, nested calls, and retries.
- Prove no remote call, message publication, cache mutation, file write, email, payment, or irreversible side effect is assumed atomic with a database transaction unless a real protocol provides it.
- Use unique constraints, compare-and-set, version columns, idempotency records, or locking to make concurrency invariants enforceable at the authoritative store.
- Record the exact crash point before, during, and after commit and define replay, reconciliation, and operator repair for each ambiguous outcome.

### Outbox, Inbox, Saga, And Idempotency

- For every command and event, define stable identity, deduplication scope, retention, canonical request hash, response replay, conflict behavior, and tenant binding.
- Verify transactional outbox insertion, publication ordering, polling or CDC ownership, retry, duplicate publication, cleanup, lag monitoring, and disaster recovery.
- Verify inbox or consumer deduplication is atomic with the local state change and survives process crash, rebalance, redelivery, and retention expiry.
- For sagas, document state machine, compensation preconditions, irreversible steps, timeout, manual intervention, and observability of stuck or partially compensated instances.
- Test duplicate requests before commit, after commit before response, after response loss, after failover, after deploy, and after idempotency-record expiry.

### Schema Migration, Backup, And Restore

- Inventory Flyway, Liquibase, Hibernate DDL, custom scripts, online schema tools, seed data, reference data, search mappings, cache schemas, and message schemas.
- Use expand-and-contract for rolling compatibility; test old code/new schema, new code/old schema where required, mixed versions, partial backfill, pause, resume, retry, and rollback limits.
- Review locks, rewrite risk, transaction size, disk growth, replication lag, statement timeout, index build strategy, validation queries, and observable progress.
- Prohibit uncontrolled automatic production migration from every application replica unless concurrency, ownership, failure, and recovery are demonstrably safe.
- Perform isolated restore and point-in-time recovery drills that verify schema, data, keys, files, queues, search indexes, object storage, application startup, reconciliation, RPO, and RTO.


