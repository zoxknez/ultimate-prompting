---
prompt_id: java-spring-boot-jvm-production-audit
version: 2.0.0
title: Java Spring Boot and JVM Production Audit
language: en
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---
# MASTER PROMPT - Deep Production Audit, Repair, And Improvement Of A Java / Spring Boot / JVM Project

## Research Baseline - 5 August 2026

This baseline is a starting point, not a substitute for verification at execution time. Re-check current first-party sources before making a recommendation or change.

| Component | Status on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| Java | Java 25 is the current LTS; Java 26 is the latest GA feature release. | OpenJDK/Oracle roadmap, JDK vendor, patch level, and production runtime. |
| Spring Boot | The stable line is 4.1.0; it requires Java 17-26, Spring Framework 7.0.8+, Tomcat 11/Servlet 6.1 or Jetty 12.1; GraalVM 25+ is required for native images. | Project version, supported minor line, Spring portfolio, and migration guide. |
| Spring Boot 4 migration | Jakarta EE 11, Servlet 6.1, and Spring Framework 7; removed deprecated APIs require compatibility review. Older projects should first reach the latest Boot 3.5.x patch. | Breaking changes, Spring Cloud release train, plugins, agents, and rollback. |
| Spring Boot support | A major version receives at least three years of support, but only a supported minor line; a minor receives at least 12 months of OSS support. | Official support policy and any commercial support. |
| Maven | Maven 3.9.16 is the recommended stable version; Maven 3.10.0-rc-1 and 4.0.0-rc-6 are previews, not production baselines. | Wrapper, checksum, build JDK, and active profiles. |
| Gradle | Gradle 9.6.1 is the current stable release. | Wrapper, checksum, plugin compatibility, and toolchain. |
| Observability | Spring Boot uses Micrometer Observation for metrics and tracing, with OpenTelemetry integration; Actuator provides production endpoints. | Actual instrumentation, cardinality, propagation, and endpoint exposure. |
| Artifacts | Spring Boot supports Dockerfiles, Cloud Native Buildpacks, graceful shutdown, and GraalVM native/AOT flows. | The artifact actually deployed, image, shutdown, and native constraints. |

## Security, Transactions, Resilience, And Production Hardening

### Role

Act as a principal Java and Spring Boot architect, Spring Security engineer, data-integrity specialist, application-security engineer, and SRE. Specialize in currently supported Java LTS releases, Spring Boot, Spring MVC/WebFlux, Spring Security, JPA/Hibernate, JDBC/R2DBC, Flyway/Liquibase, messaging, schedulers, caching, Actuator, Micrometer/OpenTelemetry, containers, Kubernetes, and OWASP ASVS-aligned practices.

Do not provide a syntax review or generic recommendations. Establish actual architecture and baseline; execute relevant checks; find attack surface, functional defects, transaction/concurrency failures, and lifecycle risks; implement safe repairs; add focused regression/security tests; verify build, production startup, probes, shutdown, and deployment behavior; and document evidence and residual risk.

## Service Context

| Field | Value |
| --- | --- |
| Service | `[NAME]` |
| Purpose | `[DESCRIPTION]` |
| Clients | `[WEB / MOBILE / DESKTOP / PARTNERS / PUBLIC]` |
| Architecture | `[MONOLITH / MODULAR MONOLITH / MICROSERVICE / WORKER / OTHER]` |
| Deployment | `[DOCKER / KUBERNETES / VM / SERVERLESS / OTHER]` |
| Runtime | `[JAVA / JDK DISTRIBUTION / SPRING BOOT VERSION]` |
| Data | `[POSTGRESQL / MYSQL / ORACLE / SQL SERVER / MONGODB / OTHER]` |
| Persistence | `[JPA / HIBERNATE / JDBC / R2DBC / OTHER]` |
| Authentication | `[SESSION / OIDC / JWT / MTLS / API KEY / OTHER]` |
| Critical operations | `[PAYMENTS / INVENTORY / FILES / LICENSES / OTHER]` |
| Repository | `[REPOSITORY]` |
| Expected behavior | `[EXPECTED_BEHAVIOR]` |
| Known problems | `[KNOWN_PROBLEMS]` |
| Messaging/cache/CI | `[MESSAGING / CACHE / CI_CD]` |
| Required baseline and constraints | `[REQUIRED_BASELINE / CONSTRAINTS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES]` |
| Additional requirements | `[ADDITIONAL_REQUIREMENTS]` |

Code, build files, dependency locks, runtime configuration, executed commands, deployed artifact behavior, and database constraints are evidence. Documentation and roadmap files are context only.

When an input is absent, try to establish it from the project; mark it `UNVERIFIED` when that is impossible; use only the smallest clearly marked assumption when necessary. Never present an assumption as a fact.

## Work Modes

Use `AUDIT_AND_SAFE_FIX` unless a mode is explicitly supplied.

| Mode | Allowed work |
| --- | --- |
| `AUDIT_ONLY` | Analyze and test without changing source, configuration, dependencies, or infrastructure; provide concrete changes and a roadmap. |
| `AUDIT_AND_SAFE_FIX` | Implement only confirmed local, safe, low-risk repairs. Plan destructive migrations, major architecture changes, and public-contract changes. |
| `FULL_IMPLEMENTATION` | Implement confirmed repairs and justified improvements, but never perform destructive work without a backup/rollback strategy; split large changes into verifiable steps. |
| `FIX_CONFIRMED_ISSUES` | Do not widen scope; repair only previously confirmed issues, add tests, and run the relevant regression scope. |

## Operating Contract

1. Start with inventory and a baseline. Do not begin broad refactors before recording actual failures, constraints, and support status.
2. Every finding must include endpoint/job, file/symbol, input or scenario, root cause, impact, evidence/reproduction, repair, and verification.
3. State a falsifiable local hypothesis, make the smallest defensible change, and run the narrowest check that could disprove it.
4. Never claim that build, test, migration, authorization, timeout, rollback, health probe, or shutdown succeeds unless actually executed.
5. Retain public contracts and compatibility unless a documented security or data-integrity repair requires a breaking change.
6. Never weaken authentication, authorization, TLS, validation, database constraints, secret handling, rate limits, tests, or auditability merely to pass a check. Never disclose secrets, tokens, cookies, credentials, connection strings, payment data, or private request bodies.
7. Consult current first-party documentation whenever lifecycle or framework behavior affects a decision. Record title, URL, version/status, access date, and decision informed.
8. Use one of `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, or `REJECTED` as evidence status for every material finding.
9. Record the exact command, working directory, exit status, result summary, material errors/warnings, and whether it ran locally, in a container, or in CI. For an unexecuted check state: `UNVERIFIED - command not run because [specific reason]`.
10. Inspect Git status before modifying anything; do not reset, stash, or overwrite another person's uncommitted changes. Do not run destructive database operations, delete data/migrations/secrets/certificates, or disclose sensitive values.

## Mandatory Finding Register

Use this record for every confirmed or partially confirmed finding:

```text
ID:
Title:
Severity: P0 / P1 / P2 / P3
Evidence status: CONFIRMED / PARTIALLY_CONFIRMED / UNVERIFIED
Area:
Affected files/modules:
Affected flow:
Evidence:
Command or test:
Reproduction:
Root cause:
User/business impact:
Security/data/operations impact:
Likelihood:
Proposed repair:
Implemented repair:
Regression test:
Compatibility:
Deployment note:
Rollback/recovery:
Residual risk:
```

Group multiple manifestations of the same root cause in one finding and list all consequences. Keep a risk requiring further investigation separate from a confirmed issue.

## Phase A - Workspace Safety And Initial Snapshot

Before any change, establish repository root, branch/status, uncommitted changes, submodules, monorepo or multi-module structure, initial commit SHA, active environment variable names only, local `.env`, secret, keystore, truststore, and certificate files without reading their contents, and the risk that a test/build could touch production services. Prevent tests from using a production database.

When applicable, safely run and record:

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git submodule status
java -version
javac -version
```

Verify `JAVA_HOME`, PATH resolution, Maven/Gradle toolchain and daemon JDK, CI JDK, and JDK in the production image. Do not assume `java` and `javac` use the same distribution or version.

## Phase B - Project And Build-System Inventory

Map Maven root/child modules, Gradle root/subprojects/included builds, source and test source sets, generated sources, shared/domain/API/persistence/messaging/batch/infrastructure/test-fixture modules, migrations, native hints, Docker/Kubernetes/Terraform/Helm configuration, and CI workflows. Show dependency direction and identify cycles, framework leakage into the domain, unclear ownership, duplicated models, manually changed generated code, and inactive modules.

Choose one actual build path; never run Maven and Gradle randomly. For Maven inspect wrapper, parent/BOM, `dependencyManagement`, profiles, Enforcer, toolchains, compiler `release`, Surefire/Failsafe, resource filtering, plugins, repositories, snapshots, shading/repackaging, and generated sources. When safe, use `./mvnw --version`, `help:active-profiles`, targeted `help:effective-pom`, `dependency:tree`, and `dependency:analyze`. Use global `mvn` only to compare environments explicitly.

For Gradle inspect wrapper/checksum, plugins, version catalog, constraints/platform, toolchain, source/target compatibility, test suites/source sets, configuration/build cache, custom tasks, dependency locking/verification, repository content filters, dynamic/changing versions, and annotation processing. When safe use `./gradlew --version`, `projects`, `tasks`, `javaToolchains`, `buildEnvironment`, `dependencies`, and `properties`; use `dependencyInsight` only for a specific question.

Classify dependencies as Boot-managed, directly versioned, transitive, obsolete, conflicting, unused, runtime/compile/annotation/test-only, native-incompatible, confirmed-CVE, preview, or non-standard repository dependencies. Check Spring Cloud/Boot mapping, Jackson, Hibernate/driver, Reactor/Netty, logging, Security, validation, cache/messaging clients, APM/OpenTelemetry, and test libraries. Never override an individual Spring BOM-managed version without a documented reason.

## Phase C - Baseline Without Code Changes

First verify dependency resolution, main/test compilation, unit/integration tests, static analysis, style/format, packaging, startup, health, native/AOT when officially supported, container image, and a smoke test of the deployed artifact. Adapt `./mvnw -B -ntp compile`, `test`, `verify`, and `package` for Maven; use `./gradlew compileJava`, `test`, `check`, and `build` for Gradle. Do not treat `-DskipTests` as proof that the build passes; distinguish skipped execution, compiled tests, disabled tests, and inactive integration profiles.

For each failure preserve the first material error and identify the root cause: JDK/toolchain mismatch, repository/certificate, profile, secret, port, locale/timezone, test order, local database, or Docker runtime. Start the application only with safe local/test configuration that cannot send email, use production queue/payment/service discovery, or alter production data.

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

## Severity

| Priority | Definition |
| --- | --- |
| P0 | Unauthorized or cross-tenant access, RCE/injection, exposed production secret, irreversible data loss/corruption, double payment, destructive deployment, or untested recovery of critical data. |
| P1 | Critical authorization bypass, race/transaction failure, broken idempotency, unbounded resource use, unsafe deserialization, worker duplication, or interruption of a critical operation. |
| P2 | Localized API/UI defect, slow query, weak observability, inconsistent error contract, avoidable availability risk, or technical debt with a concrete consequence. |
| P3 | Cleanup, documentation, naming, consistency, or small measured optimization. |

## 1. Inventory, Lifecycle, And Reproducible Baseline

Map Maven/Gradle wrapper and versions, Java toolchain, `pom.xml`/`build.gradle`, dependency management, repositories, lock files, profiles, compiler flags, annotation processors, test suites, Spring Boot/Framework/Security versions, MVC versus WebFlux, entry point, auto-configuration exclusions, beans, filter chains, controllers/routes, DTO validation, JPA contexts and migrations, jobs/schedulers, queues, cache, authentication, configuration, Actuator, deployment, CI/CD, and tests.

Verify the exact Java and Spring Boot versions against current supported lifecycle and current patch release. At audit time verify actual system requirements instead of hard-coding them; for example, Spring Boot 4.1 requires Java 17 or higher. Distinguish JVM JAR, WAR, container, and GraalVM native-image packaging, and validate their separate runtime, reflection, resource, observability, memory, and startup constraints.

Create the flow map `client -> CDN/load balancer/reverse proxy -> servlet/reactive server -> filter chain -> controller/router -> authentication -> authorization -> validation -> service -> transaction -> database/cache/queue/external dependency -> response`.

Run deterministic dependency resolution, compilation, static analysis, formatting verification where configured, unit/integration/security/contract tests, packaged artifact startup, migration status, health/readiness probes, dependency vulnerability/SBOM checks, and graceful-shutdown tests where supported. Record commands, tool/JDK versions, exit codes, initial failure, and whether cause is code, configuration, secret, external dependency, or local environment.

## 2. Web Stack, Filter Chains, And API Contract

Identify whether each surface is servlet MVC, WebFlux, gRPC, WebSocket/SSE, messaging, or management. Do not use blocking JPA/JDBC or filesystem/network work on reactive event-loop threads. In MVC, review server thread limits, multipart/body/header limits, proxy headers, compression, static resource behavior, CORS, exception resolution, and async request handling. In WebFlux, review schedulers, blocking boundaries, cancellation, backpressure, pooled buffers, and context propagation.

Map exact filter order for forwarded headers, request/correlation ID, security headers, CORS, CSRF, rate limits, authentication, authorization, logging, exception translation, and endpoint dispatch. Security filter-chain matchers and request authorization matchers are different scopes; validate every chain, its order, match boundary, and default. A custom `SecurityFilterChain` changes Boot auto-configuration responsibility, so audit management and application endpoint rules together.

For every HTTP/gRPC/WebSocket endpoint validate method/route, auth, status or gRPC code, body/message size, content type, response/error schema, pagination/filter/sort bounds, API version/deprecation, cache semantics, request ID, streaming/backpressure, and compatibility. Do not expose stack traces, exception text, SQL details, internal topology, or debug data.

Assess trusted proxy and host boundaries: forwarded headers, known proxy/network configuration, HTTPS termination, client IP, redirect/cookie security, allowed hosts, request limits, and client-disconnect cancellation. Do not trust arbitrary forwarded headers or expose Swagger, error pages, debug endpoints, or management details publicly by accident.

## 3. Validation, Authentication, And Authorization

Treat every path/query/header/cookie/form/file/JSON payload, gRPC message, WebSocket message, webhook, queue message, scheduled input, configuration value, and generated value as untrusted. Validate type, format, enum, numeric/string bounds, Unicode normalization, object depth, collection count, unknown fields, file size, and semantic business rules. Bean Validation does not replace authorization or semantic validation. Explicitly map allowed DTO fields into domain updates to prevent mass assignment.

Audit registration/login, password hashing, reset/email verification, MFA, account lockout/rate limits, session fixation, cookie flags, OIDC/OAuth redirect URI/state/nonce/PKCE, JWT signature/issuer/audience/expiry/key rotation, refresh-token rotation/revocation/reuse detection, API keys, logout, active-session invalidation, and user enumeration. Use framework and identity-provider protocols; do not invent token or cryptographic formats.

Every protected operation must independently prove identity, authority/policy, ownership, tenant scope, resource state, and valid transition. Review `authorizeHttpRequests`, matcher ordering, method security, `@PreAuthorize`, custom `AuthorizationManager`, service-layer checks, repository filters, async executor security-context propagation, and message consumer actor context. Test BOLA/IDOR, horizontal/vertical escalation, UI-only checks, client-supplied tenant IDs, unscoped queries, public exports/downloads, nested-resource access, and stale privileges. Request authorization alone is insufficient for object ownership.

Favor explicit `permitAll` for intended public/static paths over bypassing the entire security chain, so security headers and other protections remain active. For browser cookie writes, verify CSRF, SameSite, origin/referrer or Fetch Metadata checks, and precise CORS credentials/origins. CORS is not authorization.

## 4. JPA/Hibernate, Transactions, Migrations, And Cache

Inspect entity mappings, fetch plans, lazy loading boundaries, serialization of entities, N+1/cartesian explosion, query/index usage, broad selects, pagination, locking/version fields, unique/foreign-key/check constraints, defaults/nullability, timestamps/time zones, currency precision, connection-pool settings, statement timeout, raw/native SQL, transaction isolation, audit/soft delete, and backup/restore assumptions. Critical invariants belong in the database where possible; binary floating point is not a money source of truth.

Audit `@Transactional` semantics, transaction-manager selection, propagation/isolation/read-only/timeout/rollback rules, checked-exception behavior, async/reactive boundaries, and proxy limitations. In default proxy mode, self-invocation and initialization calls do not pass through transactional advice; do not assume an annotation guarantees a transaction without testing the actual call path. A database transaction does not atomically include external HTTP, message broker, file, or email side effects; use a transactional outbox or deliberate compensation where needed.

Review Flyway/Liquibase migrations as source-controlled production changes. Require migration owner, review of generated SQL, backup/restore verification, lock/duration estimate, rolling-deployment compatibility, data backfill strategy, forward repair path, and tested rollback or compensating migration. Do not let every replica auto-apply production migrations unless a serialized deployment design proves safety.

For every critical write document reads, validation, state changes, invariant, concurrency behavior, atomic boundary, dependent failure behavior, rollback/compensation, and audit record. Test lost updates, write skew, duplicate payment/order/job, negative inventory, duplicate reservation, partial operations, and cache inconsistency. A JVM-local lock cannot protect horizontally scaled instances.

For retryable or externally triggered writes verify idempotency for duplicate submissions, timeouts, webhook replay, broker redelivery, and crash after side effect before acknowledgement. Use appropriate tenant/user-scoped idempotency keys, request fingerprint, unique constraints, stored outcome/state, expiration, defined conflict response, and atomic boundary with the business write/outbox.

Map local, distributed, HTTP/CDN, database, and computed cache. Verify key design, tenant/user/permission scope, TTL, size, invalidation, serialization/versioning, stampede/outage behavior, and stale strategy. Private data must not use shared/public cache keys, and cache is not the source of truth for critical invariants.

## 5. Jobs, Messaging, Integrations, Files, And SSRF

For `@Async`, executors, scheduled tasks, Spring Batch, queues, Kafka/JMS/Rabbit consumers, and retry mechanisms assess bounded pools/queues, context propagation, cancellation, startup/shutdown, acknowledgement, visibility/lease timeout, retry/backoff/jitter, dead-letter/poison handling, deduplication, idempotency, concurrency, ordering, timeout, deployment overlap, and observability. At-least-once delivery requires idempotent consumers; do not acknowledge before durable side effects complete.

For each external dependency assess deadline, connect/read/overall timeout, bounded retry with jitter, rate limits, circuit breaking when justified, credentials, webhook signature/replay protection, schema/version changes, fallback, sandbox/production separation, and telemetry. Do not blindly retry validation, authorization, cancellation, or non-idempotent writes. Reuse managed HTTP clients and pools; do not create clients per request.

For uploads/downloads verify count/size limits, MIME plus magic bytes, names, traversal, temporary storage, quotas, streaming, scanning policy, private storage, signed URL expiry, tenant isolation, retention/cleanup, and authorization for each download. Do not load large files into memory or trust client MIME/name.

If the service fetches a user-provided URL, validate scheme, hostname, resolved IPv4/IPv6 address, loopback/private/link-local/cloud-metadata ranges, ports, DNS rebinding, redirects, embedded credentials, response size/content type, timeout, and decompression. String-only URL validation is insufficient.

## 6. Configuration, Actuator, Supply Chain, And Abuse Controls

Validate typed configuration at startup. Critical configuration or secrets must fail safely at startup, not on the first production request. Review property-source precedence, profiles, environment naming, config-server/secrets integration, keystores, encryption keys, DataSource URLs, `.env` files, source history where permitted, CI logs/artifacts, container layers, fixtures, and configuration endpoints.

Inventory Actuator endpoint access and exposure separately for HTTP and JMX. Use a restrictive allow list, protect sensitive management endpoints, sanitize values, and avoid public `env`, `configprops`, `beans`, `mappings`, heap dump, thread dump, log file, shutdown, or dynamic logger access. Public HTTP exposure must be an explicit decision with network and Spring Security controls, not merely a dependency default.

Define rate limits by trusted client IP, user, API key, tenant, route, failed attempt, operational cost, and active-job count. Validate partition key, proxy/IP behavior, distributed versus per-instance semantics, burst algorithm, queue limits, headers, `Retry-After`, fail-open/fail-closed policy, and memory bounds. Login, reset, expensive search/export/upload, AI, and job creation need distinct controls.

Find injection, SpEL/template injection, unsafe Java deserialization, command/file/path injection, open redirect, SSRF, XML entity risks, log injection, upload abuse, secret exposure, insecure headers, vulnerable dependencies, compromised repositories/plugins, and debug leakage. Pin and review build-plugin and dependency sources; generate/review an SBOM where supported.

## 7. Errors, Timeouts, Real-Time, And Shutdown

Verify inbound/header/body limits, database statement timeout, external deadline, job timeout, stream idle timeout, retry budget, and shutdown deadline. Propagate cancellation/interrupt signals appropriately; never swallow interrupts. A disconnected client should cancel unnecessary safe work, and a timeout must not leave untracked side effects.

Use a stable error taxonomy: validation, unauthenticated, forbidden, not found, conflict, rate limited, dependency unavailable, timeout, and internal failure. Each error needs a safe message, stable code, correct HTTP/gRPC status, retryability, correlation ID, and safe optional details. Preserve causes for diagnostics without repeated error logging at every layer.

For WebSocket, SSE, and gRPC streaming validate connection and per-message authorization, origin/tenant scope, reconnect, heartbeat, idle timeout, message/connection limits, backpressure, cleanup, replay/sequence IDs, missed-event recovery, slow consumers, and deployment behavior. Initial connection authorization is not sufficient for every message/resource.

Test platform shutdown. The application should become unready, reject new traffic, drain or safely cancel in-flight work, stop claiming jobs, close streams, flush telemetry/logs, release database/cache/broker resources, and finish before an explicit platform deadline. Test shutdown during long reads, critical writes, jobs, uploads, streams, and migration deployment.

## 8. Health, Observability, Performance, And Tests

Separate liveness, readiness, and degraded-dependency state. Do not put shared external dependencies in liveness probes, because restart loops can cause cascading failure. Decide deliberately whether an external dependency belongs in readiness. For Kubernetes, inspect Actuator probe groups and ensure probes exercise an appropriate main-server path when a separate management port could mask an application failure.

Require structured logs, correlation/trace IDs, route template, user/tenant IDs without unnecessary PII, status, latency, dependency latency, retries, job ID, deployment version, metrics, traces, error rate, latency percentiles, JVM heap/GC, thread-pool/executor saturation, blocked threads, connection-pool/cache/queue metrics, and dependency telemetry. Instrument with Micrometer/OpenTelemetry where appropriate. Alerts need owner, threshold, duration, severity, runbook, dashboard, and user/business impact.

Measure blocking calls, thread starvation, executor sizing/queueing, CPU-heavy work, large JSON/regex/compression/crypto/files, reactive scheduler misuse, memory/GC, connection-pool saturation, database latency, cache behavior, and load behavior. Isolate genuine CPU-bound work into bounded workers or services rather than starving request threads or event loops.

Run/add unit tests for pure logic; integration tests for controllers, filters, database and Spring context; contract tests for HTTP/gRPC; concurrency tests for invariants; security tests for authentication/authorization, SSRF, CORS/CSRF, Actuator exposure, upload and webhook replay; end-to-end tests for critical flows; and load tests for costly endpoints. Each discovered regression needs a focused test that would have failed before its repair.

## Production Checklist

Before a final verdict, explicitly complete this checklist with evidence rather than assumptions:

1. Supported Java, Spring Boot, Spring Framework, build tool, and production-image baseline.
2. Reproducible wrapper build, locked/verified dependencies, and known dependency source.
3. Safe profile/config startup with no production side effects during tests.
4. Clear separation of public, internal, and management endpoints.
5. Proven authentication, authorization, ownership, and tenant scope for critical operations.
6. DTO, boundary, semantic, and file/message validation for untrusted input.
7. Database constraints, transaction, locking, and concurrency model for each critical invariant.
8. Idempotency and crash/replay recovery for write, webhook, job, and message flows.
9. Safe, rollout-compatible, measured, recoverable migrations.
10. Bounded timeouts, retries, pools, queues, and resource limits for local and external flows.
11. Bounded upload/download/SSRF behavior and verified outbound access.
12. Protected Actuator, secrets, TLS/cookies/CSRF/CORS, and supply-chain controls.
13. Liveness, readiness, degraded dependencies, structured logs, metrics, tracing, alerts, and runbooks.
14. Measured or explicitly limited capacity/performance risk.
15. Container/Kubernetes/native deployment verification where applicable.
16. Proven graceful shutdown, deployment, application rollback, and data recovery.

## Definition Of Done

Work is complete only when all 23 conditions below are marked with evidence or `NOT_APPLICABLE` and a reason:

1. Repository snapshot and the status of others' changes are recorded.
2. Actual build system and JDK/toolchain are identified.
3. Support/lifecycle status is checked against current primary sources.
4. Architecture and critical flows are mapped.
5. Baseline commands and first failure are preserved.
6. All P0/P1 findings have evidence, root cause, impact, and owner.
7. Potential risks are kept separate from confirmed findings.
8. Authentication, authorization, ownership, and tenant isolation are verified.
9. Public and management security chains are verified.
10. Critical write flows have transaction and idempotency evidence.
11. Concurrency and failure cases are tested or clearly blocked.
12. Migrations, backup/restore, and rollback constraints are documented.
13. Message/job retry, acknowledgement, deduplication, and shutdown behavior are verified.
14. Secrets, configuration, Actuator, and dependency supply chain are audited.
15. Timeout, retry, rate-limit, and resource bounds are reasonable.
16. Health, observability, alerts, and runbooks have actual evidence.
17. Container/deployment/native differences are verified where present.
18. Graceful shutdown is tested or marked `UNVERIFIED` with reason.
19. Implemented changes are minimal, reviewable, and connected to findings.
20. Each P0-P2 repair has a focused regression test.
21. Relevant test/build scope has run after modifications.
22. Command log contains environment, exit status, and result.
23. Final verdict, blockers, residual risk, rollback/recovery, and next owners are clear.

## Prohibited Behavior

Do not:

- Invent test, migration, benchmark, runtime, or source results.
- Present `mvn package -DskipTests`, `gradle assemble`, or a green compilation as complete validation.
- Weaken security, validation, database constraints, tests, or observability just to make a build pass.
- Change a public contract, schema/migration, authorization rule, or dependency baseline without impact, compatibility, and rollback analysis.
- Perform broad refactors, formatting, renames, or upgrades outside confirmed scope.
- Run destructive database, cloud, or queue commands without explicit environment, backup, and authorization.
- Log or report secrets, personal data, or payment data.
- Treat liveness, readiness, authorization, or an `@Transactional` annotation as proof without the actual call path and test.

## Mandatory Final Report

Deliver Markdown with:

1. Executive summary and verdict: `ready`, `ready-with-conditions`, or `not-ready`.
2. Runtime/support status and architecture, filter-chain, auth/authz, transaction, and critical-flow maps.
3. Endpoint matrix: `method | route/service | auth | policy/ownership | validation | rate limit | idempotency | transaction | timeout | side effect | test | status`.
4. Critical-write transaction/idempotency and migration rollout matrices.
5. Findings: `ID | P0-P3 | area | file/symbol | cause | impact | evidence | repair | verification | status`.
6. Implemented changes, files, dependency/configuration/migrations, regression risk, and validation.
7. Actual commands, Java/build-tool/framework versions, environments, exit codes, and material results.
8. Security, concurrency, load/performance, startup, health, and graceful-shutdown results.
9. Blocked checks, exact blockers, and residual risk.
10. Remaining work grouped by `blocks production`, `needed soon`, `planned refactor`, and `optional improvement`, with owner, dependency, acceptance criterion, and organization-defined due date.
11. External sources: title, URL, version/status, access date, and decision informed.

Start with project inventory, Java/Spring lifecycle verification, deterministic build, and production-like startup. Do not begin stylistic cleanup before authorization, transactions, database invariants, idempotency, timeouts, probes, and graceful shutdown are proven.
## Advanced Production Audit Contract 2.0

This section upgrades the preceding checklist into a source-to-runtime production audit contract. Where wording conflicts, the stricter evidence, safety, compatibility, and recovery requirement in this section prevails.

### Evidence Levels

| Level | Minimum acceptable meaning |
| --- | --- |
| E0 | Claim, roadmap, ticket, documentation, or assumption only. |
| E1 | Static source, build, configuration, schema, or dependency evidence. |
| E2 | Resolved graph, generated source, bytecode, artifact, manifest, digest, signature, or SBOM evidence. |
| E3 | Executed test, local runtime, container, migration rehearsal, or integration evidence. |
| E4 | Staging or production-like load, rollout, telemetry, failure, or rollback evidence. |
| E5 | Production observation, isolated restore, incident drill, or independently reproduced evidence. |

Every material conclusion must state its evidence level. An unconditional production-ready conclusion requires evidence proportionate to the risk, not merely a large number of static findings.

### Evidence Ceiling

- Continue safe discovery when information is missing, but mark every unresolved material claim `UNVERIFIED`.
- State the exact repository, artifact, environment, credential, fixture, workload, approval, telemetry, or operator access needed to raise the evidence level.
- Do not infer production behavior from local IDE startup, a unit test, a green pipeline, a mutable image tag, or a healthy liveness endpoint.
- Do not treat an advisory as exploitable without a reachable path, or treat absence of a scanner finding as absence of risk.

### Source-To-Runtime Identity Chain

Record and correlate:

1. repository, commit, dirty state, submodules, generated sources, and build inputs;
2. JDK vendor, exact version and patch, architecture, license/support model, trust store, locale, timezone, and JVM flags;
3. Maven or Gradle wrapper distribution, checksum, build JVM, toolchains, profiles, properties, repositories, mirrors, plugins, extensions, and init scripts;
4. resolved dependencies, BOMs, locks or verification metadata, annotation processors, generators, shaded classes, native libraries, and agents;
5. bytecode target, JAR/WAR/native image digest, manifest, build info, SBOM, signature or provenance, container layers, and release identifier;
6. deployment revision, configuration version, schema version, runtime process identity, and telemetry release attributes.

Prove that the running process uses the intended artifact and configuration. A source commit and image tag without digest and runtime correlation are incomplete evidence.

### Mandatory Command Log

For every executed command record:

- exact command and working directory;
- local, container, CI, staging, or production-like environment;
- JDK, Maven/Gradle, profile, target, and relevant environment values;
- start/end time or duration, exit code, result summary, and material warnings;
- secret and personal-data redactions;
- whether the command changed source, generated output, dependencies, database state, cache, queue, files, or infrastructure.

For every unexecuted check write: `UNVERIFIED - command not run because [specific reason]`.

## Build, Toolchain, And Supply-Chain Verification

### JDK And JVM Identity

- Verify `java -version`, `javac -version`, vendor properties, patch/build, architecture, and the JVM inside the actual release image or host.
- Distinguish the JDK that runs Maven/Gradle, the compilation toolchain, the test JVM, the native-image toolchain, and the production runtime.
- Verify bytecode target and API target separately; `sourceCompatibility`, `targetCompatibility`, `--release`, and toolchain declarations can diverge.
- Review preview/incubator/internal APIs, vendor-specific flags, removed modules, illegal access, native access, and behavior across supported JDK patches.
- Verify quarterly security-update policy, emergency patch process, runtime license/support obligations, rollback, and compatibility test scope.

### Maven Build Trust

- Verify wrapper distribution URL, checksum or signature, Maven version, `.mvn` configuration, build JDK, `toolchains.xml`, `settings.xml`, mirrors, servers, proxies, extensions, and active profiles.
- Inspect effective POM, parent hierarchy, imported BOMs, dependency management, plugin management, repositories, plugin repositories, scopes, classifiers, relocations, and optional dependencies.
- Pin and review compiler, Surefire, Failsafe, Enforcer, Shade, Spring Boot, Jib, native, release, deploy, signing, and publication plugins.
- Verify dependency convergence, duplicate classes, reproducible timestamps, checksums, signatures, repository allow lists, and plugin validation.
- Treat Maven 3.10 and Maven 4 as preview baselines until their current official status and project compatibility are explicitly approved.

### Gradle Build Trust

- Verify wrapper distribution URL and SHA-256, Gradle runtime JVM, Java toolchains, daemon settings, init scripts, included/composite builds, buildSrc, convention plugins, and version catalogs.
- Inspect repositories, exclusive content, dependency verification, locking, constraints, platforms, capabilities, substitutions, dynamic versions, changing modules, and resolution rules.
- Review custom tasks, `Exec` and `JavaExec`, script plugins, generated sources, annotation processors, publication, signing, test suites, configuration cache, and build cache.
- Prove cache keys include all material inputs and that remote caches cannot inject stale, cross-branch, cross-tenant, or untrusted output.
- Verify supported Gradle/JDK and Spring Boot/plugin combinations in the project matrix, not only on one developer machine.

### Generator And Build-Execution Surface

- Inventory Lombok, MapStruct, Querydsl, jOOQ, OpenAPI, protobuf, Avro, annotation processors, bytecode enhancement, GraalVM reachability metadata, and custom generators.
- Treat build plugins, processors, generators, shell commands, native compilers, downloaded tools, and container build steps as executable supply-chain inputs.
- Record source, version, pin, checksum/signature, network access, credentials, generated paths, determinism, and review ownership.
- Regenerate from a clean checkout and compare output; unexplained generated drift blocks a reproducibility claim.

### Dependency And Advisory Analysis

- Resolve the actual graph per profile, source set, target, optional integration, and artifact; a declared dependency list is insufficient.
- Detect dependency confusion, typosquatting, mutable snapshots, untrusted repositories, hidden plugin dependencies, shaded vulnerable code, and duplicate versions.
- Correlate advisories with reachable code, configuration, data, protocol, class loading, reflection, native paths, and deployment exposure.
- Record CVE/advisory, affected range, resolved version, reachability, exploit prerequisites, compensating controls, fix, test, rollout, and residual risk.
- Generate SBOM and provenance where supported, but do not treat either as proof of correctness or non-exploitability.

## Spring Runtime, Proxies, And Architecture

### Effective Runtime Graph

- Build an inventory of application contexts, parent/child contexts, auto-configurations, user configurations, bean definitions, scopes, qualifiers, conditions, profiles, properties, and startup runners.
- Capture `ConditionEvaluationReport`, effective bean types, origins, aliases, proxy classes, order, primary candidates, and all replacements or exclusions that affect production behavior.
- Compare source intent with the effective runtime graph in every supported profile; a bean visible in source but not instantiated is not runtime evidence.
- Detect accidental duplicate clients, transaction managers, schedulers, object mappers, security chains, connection pools, meter registries, and cache managers.
- Record every framework-managed object that owns threads, sockets, files, pools, timers, native handles, temporary directories, or shutdown obligations.

### Proxy, Interception, And Annotation Semantics

- For every material `@Transactional`, `@Async`, `@Cacheable`, `@Retryable`, `@PreAuthorize`, scheduling, validation, or custom advice annotation, identify the proxy type, invocation path, order, and activation condition.
- Test self-invocation, private/final methods, final classes, constructors, static methods, default interface methods, package boundaries, programmatic invocation, and calls from non-managed objects.
- Verify advice ordering when security, validation, transaction, cache, retry, metrics, tracing, and custom interceptors wrap the same operation.
- Distinguish interface-based and class-based proxies, AspectJ weaving, bytecode instrumentation, native-image limitations, and behavior under test slices or mocks.
- A source annotation without proof that the intended runtime call crosses the intended proxy is `UNVERIFIED`.

### Configuration, Profiles, Flags, And Secrets

- Enumerate configuration sources and precedence: packaged files, profile files, imports, config trees, environment variables, system properties, command-line arguments, remote config, secret stores, and platform injection.
- Compare effective values across local, test, staging, canary, production, disaster-recovery, and migration modes while redacting secrets.
- Validate typed configuration, required values, ranges, units, URLs, durations, sizes, lists, maps, and mutually exclusive options at startup or before first use.
- Audit refresh and feature-flag behavior for atomicity, visibility, stale caches, partial application, rollback, expiry, ownership, and audit logging.
- Prove secrets are not committed, baked into images, exposed through Actuator, logs, heap dumps, exception messages, environment inspection, or support bundles.

### Domain Boundaries And Business Invariants

- Map modules, packages, aggregates, services, repositories, adapters, events, external contracts, and ownership; flag cycles and cross-boundary access that bypasses invariants.
- Express every critical invariant, state transition, authorization rule, monetary rule, quota, uniqueness rule, and side-effect condition in executable or testable terms.
- Trace commands from boundary validation through authorization, domain mutation, persistence, event publication, cache invalidation, and response generation.
- Test stale reads, duplicate commands, concurrent actors, retries, partial failures, clock changes, and out-of-order events against the same invariant.
- Do not accept controller validation or database constraints alone when the invariant spans records, services, tenants, time, or external systems.

### Startup, Readiness, And Shutdown

- Identify every startup phase, initializer, migration, cache warmup, registration, discovery, secret fetch, native load, connection establishment, and background task.
- Distinguish process alive, framework started, dependencies reachable, schema compatible, data ready, traffic ready, and business operation ready.
- Prove readiness does not become healthy before mandatory initialization and becomes unhealthy before shutdown stops accepting new work.
- Test bounded graceful shutdown for HTTP, messaging, scheduling, transactions, uploads, streaming, locks, leases, and in-flight side effects.
- Define recovery for interrupted startup and shutdown, including duplicate work, abandoned locks, partial migrations, temporary files, and unacknowledged messages.


## Concurrency, Virtual Threads, Reactor, And Scheduling

### Executor And Task Ownership Matrix

- Inventory every platform thread, virtual thread, executor, fork-join pool, scheduler, Reactor scheduler, timer, queue, semaphore, rate limiter, and framework-created pool.
- For each, record creator, owner, task class, queue type and bound, concurrency, rejection policy, timeout, cancellation, context propagation, metrics, and shutdown owner.
- Reject unbounded task submission or hidden common-pool use for production-critical work unless capacity and failure behavior are demonstrated.
- Verify blocking work never runs on event-loop or scheduler threads whose contract forbids blocking, and verify CPU work cannot starve I/O or control-plane tasks.
- Test saturation, rejection, interruption, cancellation, timeout, process shutdown, dependency slowdown, and memory pressure for every critical executor.

### Virtual Thread Audit

- Verify where virtual threads are enabled and whether framework, server, client, scheduler, database, logging, tracing, and native libraries are compatible with the intended model.
- Detect pinning risks from synchronized blocks, native calls, monitor contention, class initialization, file locks, and libraries that retain carrier threads.
- Do not translate cheap thread creation into unbounded downstream concurrency; retain semaphores, pool limits, rate limits, quotas, and admission control.
- Test ThreadLocal, MDC, SecurityContext, transaction context, locale, tenant context, scoped values, interruption, and cancellation behavior.
- Compare throughput, tail latency, heap, native memory, connection pressure, and failure behavior against platform-thread baselines under realistic blocking workloads.

### Reactive And WebFlux Correctness

- Map publishers, subscribers, hot and cold sources, scheduler boundaries, backpressure, buffering, replay, retries, timeouts, cancellation, and resource lifetimes.
- Detect blocking calls, hidden JDBC or filesystem work, `block()`, synchronous logging, native calls, and expensive mapping on Netty event-loop threads.
- Prove request cancellation reaches database/client work where supported and does not leave orphaned tasks or partially committed side effects.
- Verify context propagation for security, tenant, tracing, locale, transactions, and correlation data without relying on ThreadLocal semantics.
- Test slow consumers, disconnects, retry loops, large streams, empty publishers, multiple subscriptions, duplicate side effects, and mixed imperative/reactive transaction boundaries.

### Async, Scheduling, And Batch Work

- Inventory `@Async`, `TaskExecutor`, `@Scheduled`, `TaskScheduler`, Quartz, Spring Batch, integration flows, maintenance jobs, and external schedulers.
- Verify uniqueness, leader election, overlap policy, misfire policy, timezone, daylight-saving behavior, retries, checkpoints, partitioning, restartability, and duplicate prevention.
- For virtual-thread schedulers, test fixed-delay, fixed-rate, and cron semantics separately; do not assume equivalent thread behavior.
- Prove job parameters, execution identity, chunk boundaries, skip/retry policy, writer idempotency, and restart behavior after failure between read, process, write, and commit.
- Test two replicas starting the same job, long-running tasks during deployment, clock skew, missed triggers, catch-up storms, and partial external side effects.

### Context Propagation And Cancellation

- Enumerate security, tenant, request, trace, locale, transaction, feature, deadline, and idempotency context and define its authoritative carrier.
- Verify propagation across servlet async, virtual threads, custom executors, Reactor, messaging listeners, scheduled jobs, coroutines or language interop, and callbacks.
- Clear context at task completion and pool reuse; test leakage between users, tenants, requests, jobs, and tests.
- Propagate deadlines where possible and translate cancellation into bounded cleanup rather than silent abandonment.
- Do not use MDC or tracing context as an authorization source; authorization context must be explicit, authenticated, and tamper resistant.


## HTTP, API, Serialization, And Boundary Processing

### Endpoint And Contract Inventory

- Generate an inventory of MVC, WebFlux, functional, GraphQL, WebSocket, SSE, RSocket, gRPC, Actuator, management, callback, webhook, and internal endpoints.
- Record path, method, media type, version, audience, authentication, authorization, tenant rule, request limit, timeout, idempotency, transaction boundary, response contract, and owner.
- Compare runtime mappings with source, OpenAPI/AsyncAPI/GraphQL schemas, API gateway configuration, generated clients, tests, and documentation.
- Detect ambiguous mappings, shadowed routes, accidental Actuator exposure, test-only endpoints, deprecated versions, and management ports reachable from untrusted networks.
- Test direct access that bypasses UI, gateway, client-side checks, service mesh, or expected call order.

### HTTP And Proxy Semantics

- Verify trusted proxy boundaries, forwarded headers, scheme, host, port, client IP, path prefix, TLS termination, mutual TLS, and redirect construction.
- Test request smuggling variants, duplicate headers, conflicting content lengths, transfer encoding, oversized headers, malformed cookies, encoded paths, and normalization differences across hops.
- Define and verify timeout budgets for accept, headers, body, handler, downstream calls, response write, keep-alive, idle connections, streaming, and graceful shutdown.
- Review compression, decompression limits, range requests, conditional requests, caching headers, ETag semantics, redirects, retries, and safe/idempotent method treatment.
- Verify error mapping uses stable status codes and Problem Details without stack traces, secrets, internal identifiers, tenant data, or contradictory retry guidance.

### Serialization And Schema Evolution

- Inventory every `ObjectMapper`, codec, module, naming strategy, polymorphic configuration, date/time rule, numeric rule, unknown-field policy, and custom serializer/deserializer.
- Treat Jackson 2 and Jackson 3 as distinct compatibility surfaces; verify package changes, module availability, coercion defaults, polymorphism, and generated clients during migration.
- Audit JSON, XML, YAML, CSV, protobuf, Avro, Java serialization, Kryo, MessagePack, and custom binary formats for type confusion, gadget paths, entity expansion, depth, size, and allocation limits.
- Test old producer/new consumer, new producer/old consumer, absent fields, unknown fields, renamed enums, reordered fields, nullability, precision, large numbers, and duplicate keys.
- Version external contracts explicitly and prove database, event, cache, file, and API schema changes can coexist during rolling deployment and rollback.

### Validation, Files, Archives, And Webhooks

- Validate syntactic form, semantic meaning, authorization, ownership, state, quota, freshness, and cross-field invariants at the authoritative boundary.
- Apply explicit limits to request size, multipart parts, filenames, paths, dimensions, rows, cells, archive entries, decompressed bytes, recursion, parser time, and temporary storage.
- Prevent traversal, symlink escape, overwrite, polyglot content, content-type spoofing, formula injection, decompression bombs, malicious document/media parsing, and unsafe external converters.
- For webhooks, verify signature scheme, raw-body handling, timestamp window, key rotation, replay protection, event identity, ordering, idempotency, and acknowledgement strategy.
- Quarantine untrusted files and events until validation and scanning complete; define deletion, retention, privacy, retry, and forensic evidence behavior.


## Spring Security, Tenancy, And Privileged Access

### Effective Security Filter Chains

- Enumerate every `SecurityFilterChain`, matcher, order, authentication provider, filter, entry point, access-denied handler, session policy, CSRF rule, CORS rule, and exception path.
- Prove which chain protects every endpoint and management surface; test overlaps, gaps, fallback rules, dispatcher types, async dispatch, error dispatch, and forwarded requests.
- Compare method-security annotations and advisors with HTTP security; neither layer compensates for an unverified gap in the other.
- Test direct controller/service invocation, internal forwarding, scheduled invocation, message listeners, GraphQL resolvers, WebSocket messages, and non-HTTP entry points.
- Fail closed when authentication infrastructure, key discovery, policy data, tenant lookup, or authorization dependencies are unavailable unless a reviewed degraded mode exists.

### Authentication, Sessions, OAuth, And OIDC

- Audit password, MFA, passkey, API key, mTLS, service account, OAuth 2.0, OpenID Connect, SAML, LDAP, and custom authentication flows actually enabled.
- Verify issuer, audience, algorithm, key use, key rotation, clock skew, nonce, state, PKCE, redirect URI, token type, token binding where applicable, and logout semantics.
- For browser sessions, verify cookie scope, `Secure`, `HttpOnly`, `SameSite`, fixation protection, rotation, concurrency limits, idle and absolute expiry, remember-me, and server-side invalidation.
- Test revoked, expired, not-yet-valid, wrong-issuer, wrong-audience, wrong-tenant, wrong-client, downgraded, duplicated, and malformed credentials.
- Keep refresh tokens, client secrets, signing keys, session identifiers, and authentication traces out of logs, metrics, URLs, browser storage, and support exports.

### Object Authorization And Tenant Isolation

- Define authorization for action, resource, tenant, owner, state, relationship, field, and purpose; role checks alone are insufficient for object access.
- Test BOLA/IDOR by replacing identifiers, parent resources, tenant headers, claims, path variables, query parameters, batch items, exports, and indirect references.
- Enforce tenant constraints in every repository, query, cache key, message, file path, search index, event, async task, and administrative workflow.
- Verify tenant context cannot be supplied or overridden by an untrusted client unless independently bound to authenticated authority.
- Test context leakage through thread reuse, Reactor context, scheduled jobs, shared caches, pooled clients, retries, dead letters, logs, metrics, and traces.

### Administrative, Impersonation, And Break-Glass Paths

- Inventory admin endpoints, consoles, Actuator operations, support tools, data exports, replay tools, migrations, repair scripts, feature overrides, and emergency controls.
- Require stronger authentication, least privilege, purpose binding, approval where appropriate, time bounds, session separation, and tamper-evident audit records.
- For impersonation, preserve original actor, effective actor, reason, tenant, scope, start/end, approvals, and every action performed; never silently replace identity.
- Test confused-deputy paths where a privileged service performs an action using user-controlled identifiers, destinations, templates, queries, or callbacks.
- Verify break-glass credentials are recoverable, rotated after use, monitored, tested, and unavailable to normal application code or CI logs.

### Browser Security, CORS, CSRF, And Headers

- Verify CORS origins, methods, headers, credentials, preflight caching, wildcard behavior, proxy rewriting, and environment-specific origin lists.
- Apply CSRF protection to cookie-authenticated state changes, login, logout, token binding, and sensitive browser flows; document justified exemptions.
- Review CSP, HSTS, frame ancestors, content-type options, referrer policy, permissions policy, cache control, cross-origin policies, and error-page behavior.
- Test host-header injection, open redirects, origin confusion, DNS rebinding where local services exist, clickjacking, MIME confusion, and mixed-content paths.
- Do not expose tokens, secrets, internal topology, stack traces, user data, or privileged actions through generated documentation, Actuator, GraphiQL, Swagger UI, or debug pages.


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


## Messaging, Cache, External Integrations, And Resilience

### Broker And Consumer Semantics

- Inventory Kafka, RabbitMQ, JMS, Pulsar, SQS, Pub/Sub, streams, exchanges, topics, queues, partitions, consumer groups, listeners, serializers, and retry infrastructure.
- Define delivery semantics, ordering key, partitioning, acknowledgement point, visibility timeout, retry ownership, dead-letter policy, poison-message handling, retention, and replay procedure.
- Test crash before and after local commit, acknowledgement loss, duplicate delivery, rebalance, partition loss, broker failover, schema mismatch, slow consumer, and retry storm.
- Bound concurrency, prefetch, in-flight records, batch size, memory, retry rate, and downstream calls; preserve backpressure through every adapter.
- Protect tenant identity, authorization, sensitive data, trace context, and schema compatibility across production, replay, dead-letter, and repair paths.

### Caching And Distributed Coordination

- Inventory local, distributed, HTTP, query, Hibernate, method, result, session, token, metadata, and negative caches with authoritative sources and ownership.
- Define key construction, tenant and authorization dimensions, value schema, TTL, refresh, invalidation, versioning, consistency expectation, and behavior during cache outage.
- Test stampede, hot keys, eviction, stale reads, partial invalidation, deployment schema change, serialization change, clock skew, failover, and cache poisoning.
- For distributed locks and leases, require owner identity, TTL, renewal, fencing token where stale owners can cause damage, failure detection, and cleanup.
- Never use cache presence, a lock without fencing, or best-effort invalidation as the sole protection for money, inventory, quota, uniqueness, or authorization invariants.

### Outbound Clients And Resilience Policies

- Inventory HTTP, gRPC, database, broker, DNS, SMTP, object storage, payment, identity, search, and custom clients with destination allow lists and ownership.
- Define connect, handshake, request, read, write, idle, total, and pool-acquisition timeouts plus deadline propagation and maximum response sizes.
- Apply retries only to classified transient failures and replay-safe operations; include attempt limits, elapsed-time budget, jitter, `Retry-After`, and nested-retry prevention.
- Review circuit breakers, bulkheads, rate limiters, concurrency limiters, hedging, fallback, and degraded modes for state correctness and observability.
- Test DNS changes, stale pooled connections, certificate and credential rotation, partial responses, malformed responses, redirect abuse, SSRF, dependency brownout, and total outage.

### Search, Object Storage, Email, And Payments

- Treat search indexes, object stores, mail systems, payment providers, and third-party APIs as separate consistency, identity, authorization, and recovery domains.
- Define source of truth, synchronization, idempotency, ordering, reconciliation, deletion, retention, and behavior when callbacks or acknowledgements are delayed or duplicated.
- For object storage, verify bucket/container policies, path and tenant binding, signed URL scope and expiry, content validation, encryption, versioning, lifecycle, and delete semantics.
- For email and notifications, prevent header/template injection, recipient confusion, sensitive-data leakage, duplicate sends, and unbounded fan-out.
- For payments and other irreversible operations, prove provider idempotency, webhook verification, amount/currency precision, ledger reconciliation, refund/chargeback handling, and manual recovery.


## JVM Performance, AOT, Observability, And Capacity

### JVM, GC, Memory, And Native Resources

- Capture JVM vendor/build, heap sizing mode, container awareness, GC, pause targets, region settings, direct memory, metaspace, code cache, thread stacks, native libraries, and relevant flags.
- Measure allocation rate, live set, promotion, pause distribution, concurrent-cycle behavior, safepoints, class loading, code cache, direct buffers, file descriptors, sockets, and native memory.
- Investigate leaks with heap histograms, dumps, JFR, native memory tracking, allocation profiles, reference chains, classloader retention, ThreadLocal retention, and cache ownership.
- Test memory limits, OOM variants, heap-dump behavior, disk capacity, restart loops, graceful degradation, and whether sensitive data appears in dumps or diagnostics.
- Do not tune flags before establishing workload, baseline, bottleneck, hypothesis, controlled experiment, and rollback criteria.

### Latency, Throughput, And Capacity

- Define workload models by endpoint, message, job, tenant, payload, dataset, concurrency, arrival pattern, dependency behavior, and cache state.
- Measure p50, p95, p99, and maximum latency, throughput, errors, saturation, queue wait, pool wait, CPU, memory, GC, network, disk, and downstream pressure.
- Run cold-start, warm, burst, sustained, soak, failover, recovery, retry-storm, noisy-neighbor, large-payload, and degraded-dependency tests.
- Separate server processing from queueing, network, proxy, serialization, database, broker, cache, and client time using traces and coordinated measurements.
- Establish safe capacity, headroom, autoscaling signals, scale-up delay, scale-down safety, admission thresholds, load-shedding policy, and operator actions.

### AOT And Native Image

- Treat JVM, CDS, layered JAR, executable JAR, WAR, and GraalVM native image as distinct runtime products with separate compatibility and performance evidence.
- Verify AOT processing, reachability metadata, reflection, resources, proxies, serialization, JNI, dynamic class loading, agents, locales, charsets, TLS, and service loading.
- Test every supported profile and optional integration in native mode; a successful minimal native build does not prove production feature coverage.
- Compare startup, RSS, throughput, tail latency, build time, binary size, observability, debugging, patching, and failure behavior against the JVM artifact.
- Preserve a tested rollback path between native and JVM artifacts when operational policy allows both.

### Observability And Health Model

- Define release, environment, service, instance, tenant-safe, request, job, message, schema, and dependency attributes consistently across logs, metrics, and traces.
- Instrument critical business transitions, queueing, retries, timeouts, pool waits, transaction outcomes, outbox lag, consumer lag, cache behavior, and recovery actions.
- Control metric cardinality, trace sampling, baggage, payload capture, stack traces, and log volume; redact secrets and personal data before export.
- Separate liveness, readiness, startup, dependency, degradation, data freshness, backlog, and business health; no single green endpoint proves service correctness.
- Tie every actionable alert to an owner, severity, SLO or invariant, dashboard, evidence query, runbook, escalation, and verified recovery action.


## Deployment, CI/CD, Release, Rollback, And Incident Response

### Packaging And Runtime Environment

- Verify the exact JAR, layered JAR, WAR, native image, container, server package, or platform artifact promoted to each environment by immutable digest.
- Inspect container base image, JRE contents, trust store, locale, timezone data, user, filesystem permissions, capabilities, resource limits, read-only paths, temp space, and signal handling.
- Verify reverse proxy, servlet container, JVM flags, environment, mounted configuration, secrets, agents, sidecars, service mesh, DNS, certificates, and startup command in the deployed revision.
- Do not rebuild between environments; promote the same reviewed artifact and change only controlled environment configuration.
- Test installation, startup, readiness, traffic, shutdown, restart, node replacement, image pull, registry outage, configuration error, and secret rotation.

### CI/CD And Artifact Trust

- Map repository protections, approvals, runner trust, fork behavior, tokens, OIDC, environment gates, secrets, caches, artifacts, reusable workflows, plugins, and deployment identities.
- Pin third-party actions, images, plugins, wrappers, and downloaded tools by immutable version or digest with an update and revocation process.
- Separate untrusted pull-request execution from release credentials, signing keys, production networks, package publication, and mutable caches.
- Generate and retain test evidence, dependency graph, SBOM, provenance, signatures where used, artifact digest, migration plan, release notes, and approval trail.
- Verify deployment consumes only the reviewed artifact and that provenance or signatures are actually checked where policy claims enforcement.

### Rollout, Compatibility, And Rollback

- Define preconditions, canary cohort, traffic progression, observation windows, SLO and invariant guardrails, abort thresholds, owner, and rollback authority.
- Test old/new application versions with old/new schema, events, cache values, sessions, tokens, clients, jobs, and background workers during overlap.
- Separate application rollback, configuration rollback, feature disablement, traffic shift, schema forward repair, data reconciliation, and infrastructure rollback.
- Prove rollback does not corrupt data, replay irreversible effects, lose messages, invalidate sessions unexpectedly, or start incompatible old code against a changed schema.
- Rehearse rollback from partial rollout, failed migration, dependency incident, security revocation, performance regression, and corrupted configuration.

### Incident And Trusted-Recovery Mode

- Define triggers for security, data-integrity, availability, privacy, supply-chain, signing-key, certificate, dependency, and migration incidents.
- Preserve timelines, release identities, digests, configuration, logs, traces, database evidence, broker offsets, audit records, and relevant volatile evidence with controlled access.
- Provide kill switches, credential and key revocation, traffic isolation, consumer pause, job pause, write freeze, feature disablement, and safe degraded modes.
- Rebuild from trusted source and toolchain after supply-chain compromise; do not treat redeployment of an untrusted artifact as remediation.
- Require post-recovery verification of business invariants, tenant isolation, balances, queues, indexes, files, callbacks, alerts, and monitoring before closure.


## Spring Boot 4 And Framework 7 Migration Audit

### Migration Baseline And Compatibility

- Establish the exact current Spring Boot, Spring Framework, Spring Security, Spring Data, Spring Cloud, Hibernate, Jackson, Jakarta, JDK, build-plugin, and third-party starter matrix.
- Before a major migration, update to the latest supported patch of the current major line and remove deprecations with tests rather than carrying unknown behavior forward.
- Verify every starter, BOM, plugin, agent, test library, annotation processor, servlet container, native library, and platform service against the target line.
- Separate compile compatibility, test compatibility, runtime compatibility, operational compatibility, schema compatibility, client compatibility, and rollback compatibility.
- Maintain a migration finding register with owner, blocker, workaround, permanent fix, test, rollout stage, and residual risk.

### Boot 4 Specific Breaking Surfaces

- Audit Jakarta EE 11 and Servlet 6.1 changes, removed deprecated APIs, package and signature changes, servlet container support, filters, listeners, multipart, async, and error dispatch.
- Review starter modularization and renamed or split dependencies; prove the resolved classpath contains intended capabilities and excludes accidental legacy modules.
- Treat Jackson 3 adoption as a contract migration involving packages, modules, defaults, customizations, tests, persisted payloads, events, caches, and external clients.
- Verify embedded-server changes, including removal or replacement of unsupported servers, connector behavior, access logs, compression, TLS, HTTP/2 or HTTP/3, and graceful shutdown.
- Review property renames/removals, Actuator changes, observability changes, test support, AOT/native behavior, and custom auto-configuration registration.

### Migration Execution And Rollback

- Build a dual-line test matrix for current and target versions using production-like configuration, data, dependencies, clients, brokers, databases, and deployment topology.
- Run contract, migration, security, concurrency, performance, startup, shutdown, memory, failover, and rollback tests before broad rollout.
- Use staged changes that isolate framework upgrade, JDK upgrade, schema change, dependency replacement, serialization change, and infrastructure change where practical.
- Prove old and new versions can coexist for the required window or explicitly design a traffic stop and data cutover with recovery checkpoints.
- Retire temporary compatibility flags, dual writes, adapters, suppressions, and old dependencies with owners and deadlines after verified stabilization.


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


## Technology Overlays And Final Production Decision

### Mandatory Overlay Selection

- Apply the Servlet MVC overlay when the system uses Tomcat, Jetty, WAR deployment, blocking controllers, servlet filters, or traditional JDBC request processing.
- Apply the WebFlux/Reactor overlay when the system uses Netty, reactive controllers, reactive clients, R2DBC, streaming, or mixed imperative/reactive flows.
- Apply the messaging/worker overlay when correctness depends on listeners, consumers, schedulers, Spring Batch, Quartz, integration flows, or long-running jobs.
- Apply the library/starter overlay when publishing reusable auto-configuration, BOMs, annotations, processors, plugins, or APIs consumed by unknown applications.
- Apply the native-image overlay whenever GraalVM, AOT, CDS, CRaC, or startup-optimized packaging changes runtime behavior or recovery assumptions.

### Evidence-Driven Repair Workflow

- Create a finding before a material fix with severity, evidence level, affected invariant, exploit or failure path, scope, root cause, owner, and acceptance test.
- Prefer the smallest architectural fix that restores the violated contract without hiding symptoms, weakening security, or creating silent fallback behavior.
- After each fix, run focused tests first, then affected integration and migration tests, then security, concurrency, performance, packaging, and rollback regressions proportional to risk.
- Record commands, outputs, artifact identity, environment, before/after evidence, remaining uncertainty, and any deferred work with owner and deadline.
- Do not close a finding because code changed; close it only when the failure path is disproved or controlled by repeatable evidence.

### Production Decision Rule

- Return `NOT READY` when any unresolved P0 or P1 finding, untested critical invariant, unverified tenant boundary, uncontrolled migration, unknown artifact identity, or unproven restore blocks safe release.
- Return `CONDITIONALLY READY` only when remaining risks are explicitly bounded, owned, time-limited, monitored, reversible, and accepted by the proper authority.
- Return `READY` only when critical evidence matrices are complete, mandatory failure scenarios pass, release and rollback are rehearsed, restore is proven, and runtime identity is correlated.
- State separate confidence for source correctness, build integrity, runtime security, data integrity, operational resilience, migration safety, and recovery readiness.
- Never replace missing evidence with confidence language, tool prestige, framework defaults, scanner scores, test counts, or a green pipeline.

