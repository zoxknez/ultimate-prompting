## Phases D-X - Required Deep Audit Procedure

### D. Java, JVM, And Language Correctness

Review Java `release`/bytecode target, Lombok/annotation processing, module path/classpath, reflection/proxy/generated code, serialization, classloaders, JDK-internal API use, null contracts, `Optional` boundaries, equality/hash/comparator contracts, mutability, defensive copies, exception/resource/interrupt handling, `BigDecimal`, overflow, IDs, and cryptographic randomness. Audit time zones, locale, DST, clocks, and deterministic tests. Verify records, sealed types, virtual threads, structured concurrency, foreign-function/memory APIs, and preview features against the deployment JDK and support lifecycle.

### E. Concurrency, Virtual Threads, And Reactive Flows

For executors, `CompletableFuture`, `@Async`, schedulers, and virtual threads verify bounded concurrency, queues, rejection, context/MDC/SecurityContext/trace propagation, cancellation, interrupt, observable exceptions, lifecycle, and metrics. Virtual threads do not remove database, HTTP-pool, rate, memory, or external-dependency constraints; inspect pinning and bound scarce resources. In Reactor/WebFlux find blocking calls, unmanaged `subscribe()` side effects, event-loop misuse, scheduler boundaries, backpressure, cancellation, context propagation, buffer limits, timeout/retry order, and cleanup. Do not treat imperative JPA `@Transactional` work as sharing a reactive transaction.

### F. Business Flows And State Model

For each critical flow map preconditions, command, authentication/authorization/ownership/tenant checks, validation, transactional write, external effect, event, observability, failure/compensation, retry/idempotency, and post-state. Test invalid state transitions, money/inventory/license invariants, races, audit trail, and administrator overrides. Business rules cannot live only in the client or controller.

### G. HTTP, API, And Consumer Boundaries

Audit endpoint registration, path/method conflicts, negotiation, deserialization, exception mapping, allow-listed pagination/filter/sort, ETag/cache-control, upload/download, and actual versus documented OpenAPI behavior. Separate public, partner, internal, and management APIs. For gRPC inspect interceptors, deadlines, metadata authentication, message limits, reflection exposure, and status mapping.

### H. Persistence, SQL, And Data Integrity

In addition to JPA/Hibernate, inspect JDBC templates/raw SQL, R2DBC, drivers, pools, parameter binding, pagination, query plans, indices, locks, batches, cursors/stream cleanup, and charset/collation. Require query-plan and data-volume evidence for expensive queries. Data migration must be restart-safe, measured, segmented, and use schema-expand, backfill, application-switch, and contract stages.

### I. Transactions, Outbox, And Consistency

Prove transaction boundaries by test, not annotation alone. Review isolation, propagation, timeout, rollback, transactional events, entity callbacks, lazy boundaries, and call order. For database plus message/API/email/filesystem choose and document transactional outbox, inbox/deduplication, saga/compensation, or accepted risk. Prove crash behavior before and after commit/ack boundaries.

### J. Migrations, Backup, And Recovery

Inspect migration sequence, checksums, baseline/repair policy, transactional-DDL assumptions, privileges, locks, retries, and monitoring. A backup is insufficient without a restored, verified test, RPO/RTO, integrity validation, and key access. Never edit executed migrations or run `clean`, `baseline`, `repair`, or destructive SQL against data without explicit approval, identified environment, and backup evidence.

### K. Messaging And Async Processing

Map producers/consumers, topics/queues, schema ownership, consumer groups, partitions, retention, retry/DLQ, ordering, poison-message processing, idempotency, and reprocessing. Commit/ack only after a durable outcome. For scheduled work verify distributed lock/leader election, deployment overlap, clock/time zone, and recovery after missed execution.

### L. Cache And Distributed State

Inspect Caffeine/Redis/Hazelcast and every cache adapter for key scope, authorization/tenant isolation, serialization, TTL, invalidation, stampede, outage, eviction, memory limits, metrics, and rollback. A distributed lock needs ownership, lease/renewal, failure semantics, and split-brain/timeout tests; it is not a database-constraint replacement.

### M. Identity, Sessions, And Cryptography

Beyond login/OIDC/JWT, review key rotation, JWKS cache/failure, issuer/audience/algorithm allow lists, clock skew, token disclosure in logs/URLs, session store, concurrent sessions, CSRF, and cookie domain/path. Use standard libraries and protocols rather than custom cryptography. Verify least privilege for service, database, broker, cloud, and CI identities.

### N. Application Security And Supply Chain

Create a targeted threat model for browser, partner, webhook, queue, file, admin, internal service, and cloud-metadata boundaries. Review dependency/plugin provenance, checksums/signatures where available, repository allow lists, dependency confusion, CVEs with reachability, SBOM, provenance, and base-image digest. Do not label a CVE exploitable without an execution path or dismiss a reachable issue solely because of CVSS.

### O. Configuration, Secrets, And Feature Controls

Inspect `application*.yml/properties`, profiles, environment overrides, `SPRING_APPLICATION_JSON`, command arguments, config tree, external config, and feature flags. Every behavior switch needs owner, default, audit trail, rollout, and removal plan. Secrets must not exist in source, fixtures, image layers, logs, exceptions, Actuator, or CI artifacts; verify rotation and behavior when a secret is absent or changes.

### P. Resilience And External Dependencies

Build a dependency matrix with owner, SLO/deadline, timeout, retry criterion, idempotency, circuit/bulkhead/rate-limit policy, fallback, degradation, and alert. Bound timeout budgets from inbound request through database, HTTP/gRPC, and async work. Never use unbounded retries, fallbacks that hide data loss, or fail-open security behavior without an explicit decision.

### Q. Performance And Capacity

Measure or mark unverified throughput, p95/p99 latency, error rate, allocation/heap/GC, CPU, thread/connection-pool saturation, queue lag, cache hit rate, and database load for critical flows. Check payload/pagination limits, complexity, regex DoS, compression bombs, JSON depth, ORM query count, and N+1. Performance changes must not alter authorization, transaction integrity, or API semantics without tests.

### R. Observability And Incident Response

Inspect log schema, PII redaction, trace sampling, baggage propagation, metric cardinality, exemplars, dashboards, alert fatigue, and runbooks. Every alert must lead to an action. Incident flow needs correlation ID, release/commit version, configuration trace, rollout/rollback, on-call owner, and post-incident data-integrity verification.

### S. Container, Native, Kubernetes, And Deployment

Review Dockerfile/buildpacks, base image, non-root user, filesystem permissions, exposed port, signal handling, tag/digest, reproducibility, layers, OS packages, and vulnerability scan. For Kubernetes inspect requests/limits, HPA, PDB, security context, service account/RBAC, NetworkPolicy, ingress/TLS, config/secret mounts, probe timing, topology, and rolling-update parameters. For native/AOT inspect reflection/resources/proxy hints, JNI, agents, coverage, and functional differences from the JVM artifact.

### T. CI/CD, Release, Rollback, And Recovery

Map CI trigger, privileged steps, secrets, artifact promotion, test gates, image scan, SBOM, signature/provenance, approvals, migration owner, and deployment strategy. A release needs a versioned artifact, compatible configuration, documented canary/blue-green/rolling procedure, health gate, monitoring window, rollback, and data-recovery decision. Application rollback is not automatically database rollback.

### U. Test Strategy And Regression Proof

Inventory unit, slice, Spring context, integration, Testcontainers, contract, security, migration, concurrency, E2E, load, and failure tests. Use Testcontainers for actual database/broker/search integration where available with isolated data and no production endpoints. Review flaky/disabled/quarantined tests, order, parallelism, timezone/locale, random seed, and cleanup. Every implemented P0-P2 repair needs a test showing the former failure and corrected behavior.

### V. Controlled Repairs

Before a change state its finding, hypothesis, smallest change, preserved contract, risk, falsifying test, and rollback. Change the fewest files; do not perform opportunistic refactors or upgrades. After each material change run the narrowest relevant test/build step, then aggregate validation only after it passes.

### W. Production-Readiness Review

Verify supported runtime/dependencies; reproducible build; isolated tests; safe startup; authentication/authorization/ownership; database invariants/migrations; idempotency and message recovery; timeouts/retries; secrets/Actuator/supply chain; probes; observability/alerts/runbooks; resources/deployment; graceful shutdown; and rollback/restore. Mark every item `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, or `NOT_APPLICABLE` with evidence.

### X. Final Report Quality Check

Before delivery verify findings are reproducible, severity is proportional, recommendations are feasible, implemented changes link to tests, unexecuted checks are explicit, the command log is complete, secrets are redacted, and residual risk/ownership is explicit. Never turn a list of possible risks into false evidence of an executed audit.

