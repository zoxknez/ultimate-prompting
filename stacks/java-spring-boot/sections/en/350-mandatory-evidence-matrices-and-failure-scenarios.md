## Mandatory Evidence Matrices And Failure Scenarios

### Required Evidence Matrices

- M1 - Source, JDK, build tool, dependency graph, generated code, artifact, deployment, and runtime identity.
- M2 - Modules, application contexts, effective beans, proxies, conditions, profiles, configuration sources, and secret ownership.
- M3 - Endpoints, protocols, authentication, authorization, tenant rules, validation, idempotency, limits, and transaction boundaries.
- M4 - Executors, virtual threads, event loops, Reactor schedulers, queues, context propagation, cancellation, and shutdown ownership.
- M5 - Databases, entities, queries, pools, transactions, migrations, outbox/inbox, backups, restore, RPO, and RTO.
- M6 - Brokers, consumers, ordering, retries, dead letters, replay, schema compatibility, backpressure, and reconciliation.
- M7 - Caches, locks, leases, fencing, authoritative stores, invalidation, tenant dimensions, and outage behavior.
- M8 - External clients, destinations, credentials, TLS, timeouts, retries, circuit breakers, quotas, and degraded modes.
- M9 - Sensitive data, cryptographic material, retention, deletion, export, logs, metrics, traces, dumps, and support access.
- M10 - JVM memory, GC, native resources, startup, latency, throughput, saturation, load shedding, and capacity headroom.
- M11 - CI/CD identities, runners, plugins, caches, artifact trust, SBOM, provenance, signatures, promotion, and revocation.
- M12 - Rollout, compatibility window, migration, rollback, forward repair, incident controls, restore evidence, and owners.

### Mandatory Adversarial And Failure Scenarios

- S1 - Two authorized actors concurrently update the same invariant-bearing resource.
- S2 - The same command is replayed before commit, after commit before response, after failover, and after deploy.
- S3 - A client disconnects or cancels while database, broker, file, payment, or remote work continues.
- S4 - Thread pool, virtual-thread downstream limit, database pool, queue, heap, disk, file descriptor, or connection capacity is exhausted.
- S5 - A dependency becomes slow, partially responsive, malformed, certificate-invalid, DNS-stale, or fully unavailable.
- S6 - Nested retries across gateway, service, client, broker, and consumer create amplification or duplicate effects.
- S7 - The process crashes before commit, after commit, before acknowledgement, during publication, and during shutdown.
- S8 - Old and new application versions overlap with changing database, event, cache, token, session, and API schemas.
- S9 - A stale lock or lease holder continues work after ownership has moved.
- S10 - Broker redelivery, rebalance, dead-letter replay, and out-of-order events occur together.
- S11 - A user substitutes another object, parent, tenant, export, batch item, file path, or indirect identifier.
- S12 - Authentication signing keys, TLS certificates, database credentials, and application secrets rotate during traffic.
- S13 - Configuration refresh or feature-flag change applies partially across instances or mid-operation.
- S14 - A migration pauses, partially commits, locks production data, fills disk, or must be forward repaired.
- S15 - A cache is stale, poisoned, evicted, unavailable, or contains values from an incompatible release.
- S16 - A restore is performed in isolation and the application must prove data, schema, keys, files, queues, indexes, and invariants.
- S17 - A compromised dependency, plugin, runner, signing key, or artifact requires revocation and trusted rebuild.
- S18 - Rollback follows partial rollout, irreversible side effects, changed schema, and queued work from the newer version.


