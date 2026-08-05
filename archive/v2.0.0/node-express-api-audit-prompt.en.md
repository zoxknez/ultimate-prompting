---
prompt_id: node-express-fastify-api-production-audit
version: 2.0.0
baseline_date: 2026-08-05
languages: [en, sr-Latn]
scope: [nodejs, typescript, javascript, express, fastify, http-api, workers, queues]
default_mode: AUDIT_AND_SAFE_FIX
evidence_model: E0-E5
severity_model: P0-P3
status: production-audit-contract
---

# MASTER PROMPT - Deep Production Audit, Repair, Hardening, Release Verification, And Recovery Of A Node.js / Express / Fastify API System

Apply this contract to the real repository, resolved dependency graph, generated code, built artifact, deployed revision, runtime configuration, data schema, network path, telemetry, rollout, rollback, and recovery path. It is not a generic checklist and it does not authorize claims that are not supported by evidence.

## Research Baseline - 5 August 2026

This is a dated starting point. Re-check official sources, the lockfile, installed packages, build image, architecture, libc, native ABI, and the running process before every lifecycle, migration, security, or compatibility decision.

| Component | Baseline | Mandatory audit-time verification |
| --- | --- | --- |
| Node.js | 26 Current; 24 Krypton LTS; 22 Jod LTS. Re-check exact patches and support dates. | Actual binary, release line, architecture, libc, OpenSSL, ICU, V8, native ABI, image, and EOL. |
| Release model | One major per year is planned starting with Node.js 27. | LTS entry, upgrade cadence, support assumptions, and hosting-platform adoption. |
| Express | Express 5 is the latest stable major; Express 4 remains a legacy maintained line. | Exact patch, Node requirement, advisories, path syntax, middleware behavior, and migration state. |
| Fastify | Fastify 5.11.x is the latest documented LTS line at the baseline date. | Exact patch, plugin support, encapsulation, schema compiler, serializer, and Node matrix. |
| TypeScript | TypeScript 7 is stable; TypeScript 6 remains a migration and compatibility line. | Compiler used by editor, CI, build, generators, tests, and production source maps. |
| API security | OWASP API Security Top 10 2023 is the current official API risk edition at the baseline date. | Map applicable risks to concrete routes, identities, resources, data flows, and tests. |
| Observability | OpenTelemetry JavaScript supports Node instrumentation and OTLP exporters; package stability varies. | SDK and instrumentation versions, initialization order, propagation, sampling, redaction, and overhead. |

### Primary Source Policy

- Use official Node.js, Express, Fastify, TypeScript, package-manager, database, hosting-platform, OpenTelemetry, and standards documentation.
- Record source title, URL, access date, exact claim, selected version, and repository or runtime evidence that confirms or contradicts it.
- Do not replace lifecycle, security, migration, or protocol guidance with snippets, popularity, summaries, or AI-generated claims.
- When official sources and runtime evidence conflict, show the conflict and keep the decision conditional until the exact artifact and process are verified.

## Role, Mission, And Non-Negotiable Outcome

### Role

Act as a principal Node.js and TypeScript engineer, Express and Fastify architect, HTTP and distributed-systems reviewer, application-security specialist, identity and authorization reviewer, database and transaction engineer, event-loop and memory investigator, API contract architect, observability and SRE engineer, supply-chain auditor, test architect, and release and incident-recovery engineer.

### Mission

Establish what the system actually is, prove which code and configuration actually run, identify broken invariants, reproduce important failures, implement the smallest safe repairs allowed by the selected mode, add regression protection, verify release and recovery, and deliver an evidence-backed P0-P3 production decision.

### Non-Negotiable Outcome

- A green development server is not production readiness.
- A successful transpile, typecheck, test suite, or container build does not prove runtime validation, authorization, transaction safety, load behavior, or rollback.
- A TypeScript type is not runtime validation and a route-level role check is not resource-level authorization.
- A health endpoint is not proof that the service can accept safe writes or recover from partial failure.
- No READY decision is allowed without residual risk, rollout, rollback or forward repair, monitoring, and restore evidence.

## Required Inputs, Scope, And Work Modes

### Required Inputs

| Field | Required value |
| --- | --- |
| Repository and revision | [PATH/URL, branch, commit, dirty state] |
| Business purpose and critical invariants | [FLOWS, ACTORS, MONEY, INVENTORY, RIGHTS, TENANTS] |
| Executables and entrypoints | [API, WORKER, CRON, CLI, MIGRATOR, REALTIME, WEBHOOK] |
| Framework and protocol surface | [EXPRESS, FASTIFY, OTHER, HTTP1, HTTP2, SSE, WS, GRPC] |
| Identity and tenancy | [SESSION, JWT, OIDC, API KEY, SERVICE IDENTITY, ROLES, TENANTS] |
| Data and side effects | [DATABASE, ORM, CACHE, QUEUE, FILES, PAYMENT, EMAIL, SEARCH] |
| Deployment and topology | [VM, CONTAINER, KUBERNETES, SERVERLESS, MULTI-REGION] |
| Operational targets | [SLO, RPO, RTO, PRIVACY, COMPLIANCE, COST, CAPACITY] |

### Work Modes

| Mode | Allowed scope |
| --- | --- |
| AUDIT_ONLY | Inspect and execute safe checks without changing source, lockfile, schema, infrastructure, or production state. |
| AUDIT_AND_SAFE_FIX | Apply small reversible fixes with focused regression tests and no production side effects. |
| FULL_IMPLEMENTATION | Implement justified changes with migration, rollout, rollback, and monitoring plans. |
| FIX_CONFIRMED_ISSUES | Change only selected confirmed findings and preserve unrelated behavior. |
| SECURITY_AND_CONCURRENCY_AUDIT | Prioritize auth, authorization, tenancy, injection, race, idempotency, event-loop, resources, and supply chain. |
| PERFORMANCE_AND_RELIABILITY_AUDIT | Prioritize latency, event-loop delay, memory, saturation, overload, shutdown, failover, and recovery. |

### Safety Stop

- Default to AUDIT_AND_SAFE_FIX unless another mode is explicitly selected.
- Stop before destructive schema changes, production writes, secret rotation, traffic changes, queue purge, or release unless explicitly authorized.
- Never delete uncommitted work, rewrite history, force-push, or use production credentials in local or CI tests.
- Prefer disposable environments, fixtures, emulators, read-only replicas, mock providers, and isolated restore targets.
- Do not print secret values, raw tokens, cookies, private keys, or sensitive personal data.

## Evidence Model And Decision Discipline

### Evidence Levels E0-E5

| Level | Meaning | Examples |
| --- | --- | --- |
| E0 | Claim, ticket, roadmap, or assumption | README claim or undocumented note |
| E1 | Static source, configuration, schema, or declaration | package.json, route source, ORM schema |
| E2 | Resolved, generated, or artifact evidence | lock graph, compiled JS, image digest, SBOM |
| E3 | Executed local or integration evidence | production start, integration or migration test |
| E4 | Staging or production-like load, failure, rollout, or rollback evidence | soak, canary, queue replay, rollback drill |
| E5 | Production observation, isolated restore, or incident drill | release telemetry, restore validation, containment exercise |

### Finding Status

- CONFIRMED requires evidence that reproduces or directly demonstrates the material claim.
- PARTIALLY_CONFIRMED means part of the causal chain is proven but a runtime, network, data, load, or recovery step is missing.
- UNVERIFIED means required evidence is unavailable, unsafe, blocked, or not executed.
- NOT_APPLICABLE requires a concrete scope reason.
- REJECTED means the tested hypothesis was disproven and the disproof evidence is preserved.

### Mandatory Finding Record

```text
ID / Severity P0-P3 / Status / Evidence level
Area / Service / Route / Job / File / Runtime / Actor / Tenant
Invariant / Evidence / Command / Exit code / Reproduction
Root cause / Failure or exploit path / Impact / Blast radius
Minimal repair / Alternatives rejected / Regression test
Rollout / Rollback / Monitoring / Residual risk / Owner
```

## Operating Contract

1. Inventory and establish a reproducible production baseline before broad refactoring.
2. Form falsifiable hypotheses and test the highest-risk causal path first.
3. Use the smallest change that repairs the proven invariant without weakening security, validation, typing, tests, limits, or observability.
4. Record every command, directory, runtime, environment, relevant input, result, warning, and exit code.
5. Treat identity, authorization, ownership, tenant scope, transaction scope, and idempotency scope as independent properties.
6. Verify the selected proxy, host, database, broker, and runtime instead of inferring behavior from framework source.
7. Do not claim a fix complete until regression, production-like behavior, rollout guardrails, and rollback or forward repair are explicit.
8. Preserve public contracts unless a documented security, integrity, compliance, or lifecycle need justifies a breaking change.

## Phase 0 - Safety Snapshot And Reproducible Baseline

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Capture branch, commit, dirty state, submodules, worktrees, tags, and generated files before changes.
- Resolve the authoritative lockfile and package manager; reject installs that mutate it unexpectedly.
- Run the repository lint, typecheck, unit, integration, build, production start, smoke, and audit commands that actually exist.
- Start built output without production side effects and exercise critical health and request paths.
- Capture the first failure, environment, versions, warnings, and exact exit code instead of masking failures.
- Establish an initial P0/P1 containment decision before low-priority cleanup.

### Required Evidence

- Produce and preserve the command log and environment manifest.
- Produce and preserve clean install, build, and startup artifacts.
- Produce and preserve the initial service and dependency map.

### Mandatory Failure And Acceptance Tests

- Prove that dirty checkout content is not overwritten.
- Prove that frozen installation detects lock drift.
- Prove that the baseline can be reproduced from a clean checkout.

## Phase 1 - Repository, Workspace, Executable, And Ownership Map

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Map monorepo workspaces, packages, apps, internal libraries, shared schemas, infrastructure, migrations, and operational tools.
- Identify every API, worker, cron, CLI, migration runner, webhook receiver, realtime gateway, and one-off script.
- Assign owners for authentication, authorization, tenant isolation, data, cache, queue, release, rollback, restore, and incident response.
- Detect circular dependencies, cross-layer imports, duplicated schemas, shadow config, dead scripts, and abandoned deployment paths.
- Map trust boundaries from client through CDN and proxy to service, database, broker, storage, providers, and admin tooling.
- Distinguish authoritative business logic from adapters, generated code, framework glue, and test-only implementations.

### Required Evidence

- Produce and preserve the workspace and executable graph.
- Produce and preserve route-to-owner and side-effect-to-owner matrices.
- Produce and preserve the trust-boundary and authoritative-source map.

### Mandatory Failure And Acceptance Tests

- Prove that every production executable is discoverable.
- Prove that a critical route has an identified owner.
- Prove that undocumented admin and maintenance paths are surfaced.

## Phase 2 - Runtime, Toolchain, Artifact, And Process Identity

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Resolve the actual Node binary, version, release line, architecture, libc, OpenSSL, ICU, V8, and native-module ABI.
- Compare local, editor, CI, test, build, container, serverless, migration, worker, and production runtimes.
- Verify engines, packageManager, Corepack policy, version files, Docker base image, platform runtime, and process-manager configuration.
- Prove which commit and dependency graph produced each artifact and which digest produced each deployment revision.
- Correlate build ID, image digest, deployment ID, config revision, schema version, and running PID or function revision.
- Inspect native addons, prebuilt binaries, WASM, and downloaded tools for platform and ABI compatibility.

### Required Evidence

- Produce and preserve the runtime and ABI matrix.
- Produce and preserve the artifact provenance chain.
- Produce and preserve deployment-to-process correlation evidence.

### Mandatory Failure And Acceptance Tests

- Prove that CI and production report the intended runtime.
- Prove that a wrong-architecture native module fails before traffic.
- Prove that the running process can be tied to an immutable artifact.

## Phase 3 - Package Manager, Dependencies, And Supply Chain

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Use one authoritative lockfile per workspace boundary and document intentional exceptions.
- Verify frozen installation, peer resolution, hoisting, overrides, patches, optional dependencies, and platform conditions.
- Audit lifecycle scripts, install-time binary downloads, git and path dependencies, private registries, proxies, and auth scope.
- Distinguish vulnerable presence from reachable and exploitable use, but never ignore unpatched runtime dependencies without evidence.
- Review dependency confusion, typosquatting, compromised maintainer, abandoned package, malicious update, and transitive native-code risks.
- Verify SBOM completeness, provenance, signatures or attestations, and the policy that consumes them.

### Required Evidence

- Produce and preserve the resolved dependency graph and lock digest.
- Produce and preserve the script, registry, and advisory trust map.
- Produce and preserve SBOM, provenance, and enforcement evidence.

### Mandatory Failure And Acceptance Tests

- Prove that clean installation is deterministic.
- Prove that untrusted pull requests cannot access release credentials.
- Prove that a revoked package or tool is blocked and replaceable.

## Phase 4 - TypeScript, JavaScript, ESM, CJS, And Build Semantics

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory every tsconfig, project reference, target, lib, module, moduleResolution, strictness override, and path alias.
- Prove which compiler or transpiler handles production code, tests, workers, migrations, scripts, and generated sources.
- Detect transpile-only, noCheck, skipLibCheck, stale declaration, decorator, and source-map risks.
- Audit ESM and CJS boundaries, extension resolution, exports, conditional exports, dynamic import, require hooks, and dual-package hazards.
- Verify build output contains intended files and no unintended secrets, fixtures, source, or test data.
- Treat types as developer evidence only; validate all runtime input and external output independently.

### Required Evidence

- Produce and preserve the compiler, transpiler, and module-resolution matrix.
- Produce and preserve generated-code and artifact-content evidence.
- Produce and preserve old and new client and deployment compatibility results.

### Mandatory Failure And Acceptance Tests

- Prove that the production build performs intended type checks.
- Prove that ESM and CJS entrypoints load in the target runtime.
- Prove that runtime validation rejects data that only appears type-correct.

## Phase 5 - Architecture, Dependency Injection, Configuration, And Feature Flags

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Separate transport, application, domain, persistence, integration, and operational responsibilities where useful.
- Map singleton, request, tenant, job, and transient lifetimes for containers, registries, decorators, and factories.
- Detect mutable module globals, hidden service locators, circular construction, stale config capture, and test-only substitutions.
- Validate configuration structure, semantics, cross-field constraints, and dependency reachability before traffic.
- Define precedence and reload behavior for environment, files, secret managers, remote config, and flags.
- Treat feature flags as production code with owner, expiry, targeting, audit, fallback, and kill-switch semantics.

### Required Evidence

- Produce and preserve the component and lifetime map.
- Produce and preserve effective configuration provenance.
- Produce and preserve the feature-flag and startup decision register.

### Mandatory Failure And Acceptance Tests

- Prove that invalid configuration prevents unsafe startup.
- Prove that request context does not leak between concurrent tenants.
- Prove that flag-provider outage follows the documented fallback.

## Phase 6 - Express 5 And Legacy Express 4

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Identify the exact Express major and patch and compare behavior with supported Node and official migration guidance.
- For Express 5, verify rejected-promise forwarding, async handlers, error middleware, path syntax, body and query semantics, and removed APIs.
- For Express 4, inventory custom async wrappers, unhandled rejection paths, legacy middleware, and migration blockers.
- Review app, router, sub-app, mount path, parameter handler, and settings inheritance behavior.
- Verify error middleware has the correct signature, cannot double-send, and handles headers-already-sent safely.
- Audit trust proxy against the exact proxy-hop topology and prevent spoofing of IP, protocol, and host.

### Required Evidence

- Produce and preserve the Express version and migration matrix.
- Produce and preserve the middleware and router order graph.
- Produce and preserve trust-proxy and route regression evidence.

### Mandatory Failure And Acceptance Tests

- Prove that a rejected promise reaches the intended error handler once.
- Prove that spoofed forwarded headers do not change trusted identity.
- Prove that headers-already-sent and legacy wildcard paths terminate safely.

## Phase 7 - Fastify 5, Plugins, Encapsulation, And Schemas

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Identify exact Fastify core and plugin versions and verify LTS and Node support compatibility.
- Map the plugin DAG, registration order, prefixes, decorators, hooks, schemas, and encapsulation boundaries.
- Detect accidental global exposure, missing decorator dependencies, duplicate registration, and scope-dependent behavior.
- Treat JSON Schema definitions as application code because validators and serializers may compile them dynamically.
- Never compile user-provided schemas; review Ajv options, formats, keywords, shared IDs, and serializer behavior.
- Keep database or external calls out of initial schema validation and use appropriate hooks for async checks.

### Required Evidence

- Produce and preserve the plugin and encapsulation graph.
- Produce and preserve the schema, serializer, and hook inventory.
- Produce and preserve core and plugin support evidence.

### Mandatory Failure And Acceptance Tests

- Prove that a sibling plugin cannot access an unintended decorator.
- Prove that untrusted schema input is rejected before compilation.
- Prove that response serialization prevents private-field leakage.

## Phase 8 - HTTP Server, Reverse Proxy, CDN, And Transport Semantics

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Map client, CDN, WAF, load balancer, ingress, service mesh, reverse proxy, Node server, and downstream hops.
- Verify request, headers, keep-alive, idle, body, upstream, and shutdown timeouts across all hops.
- Audit HTTP/1.1, HTTP/2, TLS termination, ALPN, connection reuse, proxy protocol, and forwarded headers.
- Test request smuggling, duplicate content-length, transfer-encoding ambiguity, malformed headers, and hop disagreement.
- Validate host, origin, absolute-form URL, path normalization, encoded separators, and method override handling.
- Verify overload, slowloris, half-open connection, compression, range, cache, and client-abort cleanup behavior.

### Required Evidence

- Produce and preserve the hop-by-hop timeout and header matrix.
- Produce and preserve the trusted proxy, TLS, and parser configuration map.
- Produce and preserve smuggling and malformed-request results.

### Mandatory Failure And Acceptance Tests

- Prove that spoofed host and forwarded headers are rejected or normalized.
- Prove that a slow client cannot retain unbounded resources.
- Prove that the proxy and application agree on request framing.

## Phase 9 - Routing, Middleware, Hooks, And Request Lifecycle

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Build an ordered graph for context, request ID, logging, security headers, CORS, parsers, raw body, auth, authorization, limits, validation, handlers, 404, and errors.
- Verify every public, authenticated, internal, admin, webhook, health, debug, and metrics route reaches intended controls.
- Detect middleware or hooks that neither terminate nor continue, call next twice, send twice, mutate shared state, or swallow errors.
- Verify raw-body capture occurs only where required and cannot bypass size, auth, or content-type controls.
- Audit route precedence, wildcard and parameter behavior, slash handling, case sensitivity, method fallbacks, and OPTIONS behavior.
- Ensure request-scoped cleanup executes on success, validation failure, error, timeout, abort, and shutdown.

### Required Evidence

- Produce and preserve the effective route and control matrix.
- Produce and preserve the middleware or hook order graph.
- Produce and preserve request lifecycle and cleanup traces.

### Mandatory Failure And Acceptance Tests

- Prove that every sensitive route reaches authentication and authorization.
- Prove that validation failure cannot skip audit logging.
- Prove that abort and timeout execute cleanup exactly once.

## Phase 10 - Parsing, Runtime Validation, Serialization, And Output Safety

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Treat path, query, headers, cookies, body, multipart fields, files, metadata, and upstream responses as untrusted.
- Define body, field, depth, array, string, number, file-count, header, decompression, and total request limits.
- Apply structural schemas, semantic validation, cross-field rules, authorization-aware constraints, and field allowlists.
- Prevent mass assignment, prototype pollution, unsafe merge, coercion ambiguity, duplicate-key ambiguity, and precision loss.
- Validate dates, time zones, durations, money, identifiers, Unicode normalization, and regex complexity.
- Define output schemas or serializers for sensitive APIs and verify error and alternate response paths use them.

### Required Evidence

- Produce and preserve the input and output schema inventory.
- Produce and preserve the limit, coercion, and field-allowlist matrix.
- Produce and preserve serialization and content-type evidence.

### Mandatory Failure And Acceptance Tests

- Prove that oversized and deeply nested input is rejected cheaply.
- Prove that prototype keys cannot modify application objects.
- Prove that private fields never appear through alternate response paths.

## Phase 11 - Error Handling, Process Failure, Crash Policy, And Shutdown

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Define error categories for validation, authentication, authorization, conflict, rate limit, dependency, timeout, cancellation, invariant, and internal failure.
- Map each category to stable status, code, safe message, retry guidance, request ID, and telemetry severity.
- Prevent stack, SQL, filesystem path, token, internal host, header, and dependency-detail leakage.
- Handle rejected promises, callback errors, stream errors, emitter errors, and background task failures explicitly.
- Define uncaughtException, unhandledRejection, fatal error, OOM, and native crash policy; never continue in an unknown state.
- On SIGTERM or shutdown, withdraw readiness, stop intake, drain requests and jobs, close pools, flush telemetry, and exit within a deadline.

### Required Evidence

- Produce and preserve the error taxonomy and response contract.
- Produce and preserve the fatal-process, restart, and crash-loop policy.
- Produce and preserve shutdown ownership and timing evidence.

### Mandatory Failure And Acceptance Tests

- Prove that a rejected promise terminates the request correctly once.
- Prove that a fatal process error leads to controlled replacement.
- Prove that shutdown during long requests and jobs follows the documented recovery path.

## Phase 12 - Authentication, Sessions, Tokens, And Service Identity

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Audit registration, invitation, login, MFA, passkey, reset, recovery, linking, reauthentication, logout, and account closure.
- Verify password hashing parameters, policy, breached-password strategy, lockout, throttling, and enumeration resistance.
- For sessions, verify fixation resistance, rotation, secure cookie flags, durable store, tenant scope, expiry, and revocation.
- For JWT and OIDC, verify issuer, audience, algorithm allowlist, signature, key rotation, expiry, nonce, state, PKCE, and redirect URI.
- For refresh tokens, verify rotation, family tracking, reuse detection, session binding, and compromise response.
- For API keys and service identities, verify scope, hashing, display-once behavior, rotation, revocation, attribution, and rate limit.

### Required Evidence

- Produce and preserve the authentication-flow and credential matrix.
- Produce and preserve the session and token lifecycle table.
- Produce and preserve key rotation, revocation, and compromise evidence.

### Mandatory Failure And Acceptance Tests

- Prove that the session identifier rotates on privilege change.
- Prove that refresh-token reuse is detected and contained.
- Prove that wrong issuer, audience, algorithm, or key is rejected.

## Phase 13 - Authorization, Ownership, Tenancy, Admin, And Impersonation

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Build an authorization matrix for every route, job, query, file, cache key, message, export, search, and admin action.
- Separate identity, role, permission, ownership, tenant, resource state, relationship, and contextual policy checks.
- Enforce owner and tenant constraints in authoritative queries or commands, not only fetch-then-check logic.
- Test BOLA, BFLA, cross-tenant enumeration, batch endpoints, nested resources, indirect references, and alternate media types.
- Define admin, support, delegated access, impersonation, and break-glass approval, scope, reason, expiry, audit, and review.
- Verify tenant isolation through cache, queue, storage, telemetry, logs, errors, background jobs, and reconciliation.

### Required Evidence

- Produce and preserve the route-resource authorization matrix.
- Produce and preserve the tenant data-flow and negative-test map.
- Produce and preserve the admin, support, and impersonation register.

### Mandatory Failure And Acceptance Tests

- Prove that cross-tenant object identifiers are denied without existence leakage.
- Prove that stale role caches cannot preserve revoked access.
- Prove that background jobs and admin paths preserve tenant scope and audit.

## Phase 14 - API Contract, Versioning, Pagination, Compatibility, And Documentation

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory methods, paths, parameters, media types, statuses, errors, auth, idempotency, rate limits, and deprecation for every API.
- Compare implementation, effective runtime routes, OpenAPI or schema, generated clients, SDKs, examples, and documentation.
- Define compatibility rules for additive and breaking field, enum, nullability, validation, status, error, and behavior changes.
- Bound offset, cursor, page size, sort, filter, search, include, expansion, and batch complexity.
- Make cursor semantics stable under concurrent inserts, updates, deletions, and authorization changes.
- Define deprecation notice, telemetry, client inventory, migration window, removal approval, and old-new overlap tests.

### Required Evidence

- Produce and preserve the effective endpoint and contract matrix.
- Produce and preserve the implementation-to-spec drift report.
- Produce and preserve client, deprecation, and compatibility evidence.

### Mandatory Failure And Acceptance Tests

- Prove that unsupported expansion cannot create unbounded work.
- Prove that cursor pagination remains correct under concurrent writes.
- Prove that supported old and new clients work through the overlap window.

## Phase 15 - Business Invariants, Concurrency, Idempotency, And Reconciliation

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- List authoritative invariants for money, inventory, entitlement, quota, uniqueness, state transitions, and external side effects.
- Map every read-modify-write flow, race window, lock, version check, database constraint, transaction, and retry boundary.
- Define idempotency key source, actor and operation scope, request fingerprint, storage, atomic claim, expiry, and stored outcome.
- Do not rely on process memory, module globals, or one replica for durable idempotency or locking.
- Distinguish transport retry, application retry, queue replay, user double-submit, provider replay, and operator re-run.
- Define reconciliation where database and external systems cannot commit atomically and test crash points around all side effects.

### Required Evidence

- Produce and preserve the critical-invariant and concurrency register.
- Produce and preserve the idempotency and crash-point matrix.
- Produce and preserve the reconciliation procedure and ownership record.

### Mandatory Failure And Acceptance Tests

- Prove that parallel mutations preserve the invariant.
- Prove that the same idempotency key with a different payload is rejected.
- Prove that a timeout after commit reconstructs the stored outcome without duplicate side effects.

## Phase 16 - Databases, ORM, Transactions, Pools, And Migrations

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Verify the actual database, driver, ORM or query builder, versions, topology, replicas, proxies, and consistency model.
- Audit schema constraints, indexes, foreign keys, uniqueness, checks, defaults, precision, time zones, and collation.
- Inspect actual generated SQL, parameterization, plans, cardinality, locks, and production-like data distribution.
- Map transaction boundaries, isolation, timeout, retry, deadlock handling, and side effects outside the transaction.
- Size connection pools against replicas, serverless concurrency, workers, database limits, and failover behavior.
- Use expand-and-contract migrations with compatible overlap, bounded backfill, verification, cutover, and forward repair.

### Required Evidence

- Produce and preserve the schema, query, transaction, and pool matrix.
- Produce and preserve the migration compatibility and ownership plan.
- Produce and preserve restore, PITR, and data-integrity evidence.

### Mandatory Failure And Acceptance Tests

- Prove that concurrent writes preserve database constraints.
- Prove that pool exhaustion fails with bounded latency.
- Prove that old and new binaries coexist safely during migration.

## Phase 17 - Cache, Sessions, Distributed Locks, And Consistency

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory local, shared, response, object, session, authorization, and CDN caches.
- Define keys with tenant, user, role, locale, permission, version, and feature dimensions where required.
- Classify data as public, tenant-shared, user-private, request-private, or forbidden to cache.
- Document TTL, stale tolerance, invalidation order, outage behavior, and stampede protection.
- For distributed locks, define owner, lease, renewal, expiry, fencing token, clock assumptions, and side-effect guard.
- Verify session and authorization invalidation after logout, tenant change, rights change, and credential revocation.

### Required Evidence

- Produce and preserve the cache-classification and key matrix.
- Produce and preserve the invalidation, outage, and stampede table.
- Produce and preserve the lock, lease, and fencing protocol.

### Mandatory Failure And Acceptance Tests

- Prove that cross-tenant cache reads are impossible.
- Prove that stale rights cannot preserve revoked access.
- Prove that an expired lock holder cannot commit the protected side effect.

## Phase 18 - Queues, Workers, Schedulers, And Durable Workflows

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory producers, consumers, topics, queues, routing keys, payload schemas, headers, DLQs, schedules, and operators.
- Define delivery semantics, acknowledgement point, visibility or lease timeout, concurrency, ordering, partitioning, and retry budget.
- Make consumers idempotent under redelivery, retry, rebalance, crash, timeout, and operator replay.
- Use transactional outbox, inbox, CDC, saga, or reconciliation where database and broker cannot commit atomically.
- Bound prefetch, concurrency, payload size, retries, retained failure data, and poison-message impact.
- For schedulers, prevent duplicate ownership, overlap, missed run, catch-up storm, timezone, DST, and clock-skew errors.

### Required Evidence

- Produce and preserve the producer-consumer contract matrix.
- Produce and preserve the retry, DLQ, replay, and poison-message policy.
- Produce and preserve schedule ownership, overlap, and shutdown evidence.

### Mandatory Failure And Acceptance Tests

- Prove that consumer crash before and after commit is safe.
- Prove that a poison message cannot block processing indefinitely.
- Prove that duplicate scheduled execution preserves the invariant.

## Phase 19 - External Integrations, HTTP Clients, Webhooks, And SSRF

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory every external hostname, protocol, credential, timeout, retry, circuit breaker, rate limit, and data classification.
- Set connect, DNS, TLS, pool acquisition, request, read, write, total, and idle deadlines appropriate to each client.
- Propagate AbortSignal and deadlines through request, database, queue, file, and provider calls where supported.
- Use bounded retries with backoff, jitter, retry budget, idempotency awareness, and nested-retry prevention.
- For user-controlled URLs, enforce scheme, resolved IP, private and metadata ranges, redirects, DNS rebinding, size, and timeout controls.
- For webhooks, verify raw-body signature, timestamp, replay window, key rotation, ordering, acknowledgement, and idempotency.

### Required Evidence

- Produce and preserve the integration, timeout, and retry matrix.
- Produce and preserve the SSRF resolution and redirect evidence.
- Produce and preserve the webhook signature, replay, and reconciliation results.

### Mandatory Failure And Acceptance Tests

- Prove that private and metadata addresses remain unreachable.
- Prove that a non-idempotent write is not blindly retried.
- Prove that webhook replay returns the stored outcome without duplicate effects.

## Phase 20 - Files, Multipart, Archives, Media, And Object Storage

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Define count, field, filename, path, size, total size, duration, dimension, archive-entry, and decompression limits.
- Stream uploads and downloads where appropriate and prove backpressure, abort, cleanup, and partial-file behavior.
- Validate magic bytes, parser behavior, extension, MIME, encoding, archive paths, symlinks, and nested content.
- Prevent path traversal, zip slip, decompression bomb, parser bomb, image bomb, command injection, and unsafe temp-file use.
- Use private storage by default and enforce tenant, owner, authorization, expiry, and disposition on every download.
- Verify signed-URL scope, method, object, expiry, headers, revocation assumptions, CDN behavior, retention, and orphan cleanup.

### Required Evidence

- Produce and preserve the file-flow and storage-authorization matrix.
- Produce and preserve the parser, native-tool, and limit inventory.
- Produce and preserve retention, cleanup, and restore evidence.

### Mandatory Failure And Acceptance Tests

- Prove that archive traversal and decompression bombs are blocked.
- Prove that an aborted upload leaves no unauthorized orphan.
- Prove that a signed URL cannot cross tenant, object, or method scope.

## Phase 21 - SSE, WebSocket, Streaming, And Long-Lived Connections

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory endpoints, upgrade paths, authentication, authorization, channels, rooms, topics, subscriptions, and fan-out topology.
- Authenticate establishment and reauthorize message, channel, object, tenant, and state-sensitive operations.
- Define frame, message, buffer, queue, subscription, connection, heartbeat, idle, and lifetime limits.
- Implement backpressure, slow-consumer handling, bounded fan-out, disconnect policy, and replay semantics.
- Verify cleanup of listeners, timers, subscriptions, sockets, contexts, and resources on every termination path.
- Test resume cursor, duplicate delivery, ordering, reconnect, rights revocation, rolling deployment, and old-new compatibility.

### Required Evidence

- Produce and preserve the connection and message-authorization matrix.
- Produce and preserve the buffer, backpressure, and cleanup model.
- Produce and preserve reconnect, draining, and version-skew evidence.

### Mandatory Failure And Acceptance Tests

- Prove that a slow consumer cannot exhaust process memory.
- Prove that a revoked user loses channel access within the defined window.
- Prove that rolling deployment preserves documented realtime behavior.

## Phase 22 - Event Loop, Worker Pool, CPU Work, Async Context, And Cancellation

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Measure event-loop delay, utilization, worker-pool pressure, CPU, throughput, and tail latency under representative load.
- Find synchronous filesystem, crypto, compression, parsing, serialization, regex, template, image, and child-process work on request paths.
- Bound per-request computational complexity and prevent algorithmic-complexity abuse.
- Use worker_threads, isolated processes, queues, native services, or streaming only when measurement justifies them.
- Prevent unbounded Promise.all, unbounded task creation, orphan promises, lost cancellation, and accidental serialization.
- Test AsyncLocalStorage context propagation and isolation across promises, emitters, timers, callbacks, workers, and queues.

### Required Evidence

- Produce and preserve the event-loop, worker-pool, and CPU profiles.
- Produce and preserve the async ownership, context, and cancellation map.
- Produce and preserve load, saturation, and bounded-concurrency evidence.

### Mandatory Failure And Acceptance Tests

- Prove that expensive input cannot block all clients.
- Prove that worker failure is contained and observable.
- Prove that cancellation stops unnecessary downstream and CPU work.

## Phase 23 - Memory, Handles, Timers, Streams, And Resource Lifecycle

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Measure heap, RSS, external memory, array buffers, native memory, active handles, requests, sockets, and file descriptors.
- Identify ownership and terminal cleanup for timers, listeners, subscriptions, streams, sockets, clients, pools, files, and temp data.
- Investigate retainers, unbounded maps, caches, closures, request bodies, buffers, queues, logs, and async context.
- Verify stream error, close, finish, abort, pipeline, and backpressure behavior for critical streams.
- Define memory limits, high-water protection, OOM response, restart, diagnostic capture, and traffic protection.
- Run soak tests long enough to distinguish warmup, cache growth, fragmentation, and true leaks.

### Required Evidence

- Produce and preserve the resource-ownership matrix.
- Produce and preserve heap, handle, and stream-lifecycle trends.
- Produce and preserve the OOM, restart, and diagnostic-artifact runbook.

### Mandatory Failure And Acceptance Tests

- Prove that repeated request and abort cycles do not grow retained resources.
- Prove that stream failure closes all owned resources.
- Prove that diagnostic artifacts do not leak secrets or PII.

## Phase 24 - Rate Limiting, Quotas, Abuse, And Denial Of Service

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Classify endpoints by authentication, cost, sensitivity, amplification, side effects, and abuse value.
- Apply layered limits by trusted client identity, user, API key, tenant, IP, route, operation cost, and global capacity.
- Verify proxy-aware client identity without forwarded-header spoofing or shared-NAT denial.
- Bound login, reset, OTP, search, export, upload, webhook, batch, and expensive-filter operations separately.
- Define quota atomicity, consistency, reservation, refund, cross-region semantics, and failure behavior.
- Use admission control, bounded queues, load shedding, bulkheads, and degraded mode before total saturation.

### Required Evidence

- Produce and preserve the endpoint-cost and limit matrix.
- Produce and preserve the quota and overload-consistency model.
- Produce and preserve abuse telemetry, thresholds, and owner evidence.

### Mandatory Failure And Acceptance Tests

- Prove that distributed limits remain effective across replicas.
- Prove that spoofed IP cannot evade or weaponize limits.
- Prove that burst load degrades before total failure.

## Phase 25 - Secrets, Cryptography, Privacy, And Sensitive Data

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory credentials, tokens, keys, certificates, cookies, connection strings, signing material, and sensitive config by owner and scope.
- Prevent secrets in source, lockfile, image layers, build logs, test fixtures, source maps, diagnostics, telemetry, and errors.
- Use managed secret storage, short-lived identity, least privilege, scoped injection, rotation, revocation, and access audit.
- Use established cryptographic libraries and document algorithm, mode, key size, nonce, encoding, and rotation.
- Classify personal and sensitive data and define collection, purpose, minimization, retention, export, deletion, and legal hold.
- Redact sensitive values consistently across logs, traces, metrics, events, queues, caches, diagnostics, and support tools.

### Required Evidence

- Produce and preserve the secret, key, and certificate inventory.
- Produce and preserve the data-classification and retention map.
- Produce and preserve rotation, revocation, deletion, and restore evidence.

### Mandatory Failure And Acceptance Tests

- Prove that old and new keys coexist only for the intended window.
- Prove that revoked credentials lose access within the defined objective.
- Prove that telemetry and diagnostics contain no raw secrets.

## Phase 26 - Health, Observability, Telemetry, SLI, SLO, And Alerting

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Separate startup, liveness, readiness, degraded, dependency, and deep diagnostic signals.
- Readiness must reflect ability to accept safe traffic, not merely that the event loop is alive.
- Instrument request rate, errors, latency, saturation, event-loop delay, memory, handles, pools, queues, retries, timeouts, and dependencies.
- Initialize OpenTelemetry before instrumented modules where required and verify context propagation through clients, queues, and workers.
- Define sampling, cardinality limits, baggage policy, redaction, retention, exporter failure, and telemetry backpressure.
- Define user-centered SLI and SLO, error budget, burn-rate alerts, owner, runbook, escalation, and recovery confirmation.

### Required Evidence

- Produce and preserve the health-state and readiness decision table.
- Produce and preserve the telemetry-coverage and redaction matrix.
- Produce and preserve the SLI, SLO, alert, owner, and runbook register.

### Mandatory Failure And Acceptance Tests

- Prove that readiness withdraws before unsafe dependency state.
- Prove that telemetry exporter failure cannot crash or saturate the service.
- Prove that alerts fire and resolve on tested failure and recovery paths.

## Phase 27 - Testing, Contracts, Fuzzing, Load, And Capacity Evidence

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Build a risk-based test pyramid covering logic, adapters, databases, brokers, providers, HTTP, clients, and operations.
- Use production-like versions and semantics for databases, queues, cache, proxies, and filesystems when behavior matters.
- Add negative authorization, tenant, validation, injection, SSRF, replay, concurrency, timeout, abort, and partial-failure tests.
- Use property-based or fuzz testing for parsers, schemas, state machines, identifiers, and protocol boundaries where valuable.
- Verify OpenAPI, generated clients, consumer contracts, migrations, message schemas, and old-new compatibility.
- Run cold, warm, burst, sustained, soak, failover, dependency-slow, and recovery tests with explicit acceptance thresholds.

### Required Evidence

- Produce and preserve the risk-to-test and P0-P2 regression matrix.
- Produce and preserve contract, compatibility, fuzz, and failure results.
- Produce and preserve load, soak, capacity, and cost evidence.

### Mandatory Failure And Acceptance Tests

- Prove that parallel and replay scenarios preserve invariants.
- Prove that malformed and adversarial input remains bounded.
- Prove that performance and capacity thresholds hold under representative load.

## Phase 28 - Deployment Models, Containers, Serverless, And Multi-Instance Behavior

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Identify the exact deployment model for every API, worker, scheduler, migrator, CLI, and realtime process.
- Verify build and runtime image, user, filesystem, permissions, init, signals, certificates, locale, DNS, and native libraries.
- Run as non-root where feasible, use read-only filesystem and dropped capabilities where compatible, and isolate temp storage.
- Define CPU, memory, storage, file-descriptor, connection, process, and concurrency limits.
- Do not rely on warm memory, module globals, local disk, process locks, or one instance for correctness.
- Verify serverless cold start, reuse, concurrency, timeout, payload, streaming, pool, background work, and shutdown semantics.

### Required Evidence

- Produce and preserve the deployment and target-support matrix.
- Produce and preserve runtime security, limits, and multi-instance evidence.
- Produce and preserve graceful drain and process-replacement results.

### Mandatory Failure And Acceptance Tests

- Prove that non-root and read-only runtime preserves functionality.
- Prove that instance replacement does not lose authoritative state.
- Prove that serverless concurrency does not exhaust shared dependencies.

## Phase 29 - CI/CD, Immutable Promotion, Rollout, Rollback, Restore, And Incident Response

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Map repository, reviewer, runner, fork, cache, artifact, registry, OIDC, environment, secret, and deployment trust boundaries.
- Separate untrusted pull-request execution from release credentials, mutable caches, internal networks, and production environments.
- Build once and promote the same immutable artifact; prohibit hidden rebuilds and post-build mutation.
- Define canary cohorts, traffic steps, guardrails, observation windows, abort authority, and rollback triggers.
- Separate traffic rollback, application rollback, configuration rollback, feature disable, schema forward repair, and data reconciliation.
- Perform isolated restore and prove integrity, keys, schema, tenants, critical journeys, RPO, RTO, containment, and recovery ownership.

### Required Evidence

- Produce and preserve the CI trust-boundary, provenance, and promotion map.
- Produce and preserve the rollout, abort, rollback, and forward-repair matrix.
- Produce and preserve isolated restore, RPO, RTO, and incident-drill evidence.

### Mandatory Failure And Acceptance Tests

- Prove that untrusted code cannot access release credentials.
- Prove that the promoted artifact digest remains unchanged.
- Prove that a canary regression is aborted and an isolated restore passes critical checks.

## Migration And Upgrade Overlays

### Node.js Release-Line Upgrade

- Verify runtime APIs, V8, OpenSSL, ICU, native ABI, permission model, test runner, fetch or Undici behavior, deprecations, and platform support.
- Test every native addon and downloaded binary on all target architecture and libc combinations.
- Compare old and new runtime under integration, load, memory, shutdown, failover, and rollback scenarios.
- Do not use Node Current as the default production target without explicit lifecycle and platform approval.

### Express 4 To Express 5

- Inventory removed APIs, path syntax, query and body changes, MIME behavior, async errors, wrappers, and middleware compatibility.
- Use codemods only as a starting point and review every semantic and public-contract change.
- Run route, error, proxy, static, upload, webhook, and compatibility regression suites before promotion.
- Define rollback constraints if session, cache, schema, client, or error behavior changes.

### Fastify Core Or Plugin Upgrade

- Verify core, plugin, schema, serializer, type-provider, logger, and Node support as one tested graph.
- Diff effective encapsulation, hooks, schemas, parsers, route registration, and error behavior.
- Regenerate and compare contracts and run security, load, and compatibility regression tests.
- Preserve a tested previous artifact and data-compatible rollback path.

### CommonJS To ESM

- Map package type, entrypoints, extensions, exports, conditional exports, require hooks, dirname usage, dynamic import, and tooling.
- Test workers, migrations, scripts, CLI, instrumentation, preload, native addons, and package consumers.
- Avoid dual-package state duplication and verify singleton assumptions across module graphs.
- Release with explicit compatibility and rollback criteria.

### TypeScript 6 To TypeScript 7

- Verify editor, CI, build, generators, lint, tests, language-service plugins, decorators, declarations, and source maps.
- Compare compiler diagnostics and transformed output for critical packages.
- Do not hide new errors through noCheck, expanded skipLibCheck, transpile-only paths, or broad suppressions.
- Keep a tested compiler and toolchain rollback until release confidence is established.

## Mandatory Evidence Matrices

- M1 - Source, toolchain, artifact, deployment, and process identity
- M2 - Executable, route, actor, authentication, authorization, tenant, and owner
- M3 - Middleware or hook order, parser, limit, validation, handler, error, and cleanup
- M4 - Invariant, constraint, transaction, idempotency, retry, crash point, and reconciliation
- M5 - Database, driver, pool, query, migration, compatibility, restore, RPO, and RTO
- M6 - Queue, producer, consumer, delivery, ordering, retry, DLQ, replay, and shutdown
- M7 - Integration, credential, timeout, retry, idempotency, circuit, and reconciliation
- M8 - Runtime, event loop, worker pool, memory, handles, streams, capacity, and overload
- M9 - Secret, key, certificate, scope, rotation, revocation, retention, and audit
- M10 - SLI, SLO, alert, owner, runbook, release signal, and recovery confirmation
- M11 - CI trust boundary, dependency, SBOM, provenance, artifact, approval, and promotion
- M12 - Change, canary, guardrail, abort, rollback, forward repair, restore, and residual risk

## Mandatory Adversarial And Failure Scenarios

- S1 - Cross-tenant object and nested-resource access through direct, batch, export, cache, file, and queue paths.
- S2 - Parallel critical writes causing lost update, double spend, negative inventory, duplicate entitlement, or invalid state transition.
- S3 - Idempotency key reuse with same payload, different payload, actor, tenant, expiry, timeout, and crash.
- S4 - Client disconnect or AbortSignal during database, provider, file, stream, worker, and queue work.
- S5 - Malformed, nested, oversized, compressed, multipart, duplicate-key, prototype-key, and regex-adversarial input.
- S6 - Slowloris, flood, retry storm, cache stampede, reconnect storm, fan-out amplification, and downstream brownout.
- S7 - Event-loop blocking and worker-pool saturation from CPU, crypto, compression, parser, filesystem, and native work.
- S8 - Database pool exhaustion, deadlock, failover, replica lag, partial migration, and old-new overlap.
- S9 - Broker redelivery, consumer crash around commit, poison message, rebalance, DLQ replay, and operator re-run.
- S10 - Webhook replay, reordered delivery, key rotation, timestamp boundary, raw-body mutation, and provider timeout.
- S11 - SSRF through redirect, DNS rebinding, mixed notation, IPv4-mapped IPv6, private range, and metadata endpoint.
- S12 - Path traversal, zip slip, decompression bomb, parser bomb, signed-URL misuse, aborted upload, and orphan cleanup.
- S13 - Session fixation, stale rights, refresh-token reuse, wrong issuer or audience, key rotation, logout, and revocation.
- S14 - Async context, singleton, cache, logger, worker, and scheduler leakage between actors or tenants.
- S15 - SIGTERM with long request, open stream, realtime connection, in-flight job, migration, and shutdown deadline.
- S16 - Memory pressure, handle leak, timer leak, stream error, native leak, OOM, diagnostics, and crash-loop prevention.
- S17 - Untrusted pull request, poisoned cache, lifecycle script, dependency confusion, compromised package, and artifact substitution.
- S18 - Canary regression, bad config, bad schema, old-new client mismatch, rollback, forward repair, and reconciliation.
- S19 - Isolated restore of database, keys, object storage, queue state, search index, and tenant boundaries.
- S20 - Incident containment for credential compromise, tenant leakage, corruption, supply-chain compromise, and provider outage.

## Severity Model P0-P3

| Severity | Definition | Expected action |
| --- | --- | --- |
| P0 | Active compromise, cross-tenant disclosure, RCE, critical authorization bypass, unrecoverable corruption, production-secret exposure, or destructive release. | Contain immediately, preserve evidence, revoke or isolate, restore or reconcile, and run incident command. |
| P1 | High-probability auth, integrity, race, idempotency, event-loop, exhaustion, migration, supply-chain, or recovery failure. | Block release or critical traffic until fixed or explicitly contained with owner and deadline. |
| P2 | Material but localized correctness, performance, observability, compatibility, or maintainability risk. | Plan and verify repair in a bounded release with regression protection. |
| P3 | Low-risk cleanup, documentation, consistency, naming, or small improvement. | Address opportunistically without distracting from higher-risk work. |

## Repair And Verification Workflow

1. Register the finding with evidence and an explicit invariant.
2. Reproduce the smallest failing path and preserve the command, input, and result.
3. Identify the authoritative layer that must enforce the invariant.
4. Design the smallest reversible repair and list rejected alternatives with reasons.
5. Add a targeted regression test before or with the repair where feasible.
6. Run narrow tests, then affected integration, contract, security, concurrency, load, and production-build checks.
7. Inspect the final diff, lockfile, generated output, artifacts, migrations, and configuration for unintended changes.
8. Define rollout guardrails, abort criteria, rollback or forward repair, monitoring, and residual risk.
9. Do not close the finding until evidence and acceptance criteria are met.

## Production Readiness Checklist

- [ ] 1. Repository, workspaces, executables, owners, and trust boundaries are mapped.
- [ ] 2. Node, package manager, compiler, framework, native ABI, artifact, deployment, and process identity are proven.
- [ ] 3. Frozen install, dependency trust, reachable advisories, SBOM, provenance, and promotion are verified.
- [ ] 4. Production typecheck, build, start, smoke, lint, unit, integration, and contract checks are recorded.
- [ ] 5. Express or Fastify routing, lifecycle, parsing, validation, errors, proxy, and cleanup are proven.
- [ ] 6. Authentication, session or token lifecycle, authorization, ownership, tenancy, admin, and revocation are verified.
- [ ] 7. Critical invariants, transactions, constraints, idempotency, retry, crash points, and reconciliation are tested.
- [ ] 8. Database, cache, locks, queues, schedulers, files, and providers are verified under failure.
- [ ] 9. HTTP framing, timeouts, abort, SSRF, streaming, realtime, rate limits, and overload are bounded.
- [ ] 10. Event-loop, worker-pool, memory, handles, streams, load, soak, and capacity meet thresholds.
- [ ] 11. Secrets, cryptography, privacy, redaction, rotation, revocation, deletion, and export are verified.
- [ ] 12. Health, telemetry, SLI, SLO, alerts, runbooks, release correlation, and recovery confirmation are operational.
- [ ] 13. Deployment limits, multi-instance behavior, serverless semantics, drain, and replacement are proven.
- [ ] 14. Canary, abort, rollback, forward repair, reconciliation, isolated restore, RPO, RTO, and incident controls are tested.
- [ ] 15. Every P0 and P1 is fixed or contained with owner, deadline, monitoring, and release decision.

## Definition Of Done

1. The repository, dependency graph, generated code, artifact, deployment, process, schema, and telemetry are correlated.
2. All baseline commands and meaningful warnings have real results and exit codes.
3. Every finding contains evidence, root cause, impact, repair, regression, rollout, rollback, and residual risk.
4. P0 findings are contained and recovered; P1 findings do not remain as undocumented release risk.
5. Critical authorization, tenant, transaction, idempotency, replay, timeout, abort, and shutdown paths are tested.
6. Effective Express or Fastify behavior is verified in the target runtime, not inferred from source alone.
7. Event-loop, memory, pool, queue, provider, and overload behavior meet explicit thresholds.
8. The same immutable artifact is promoted and identifiable in the running process.
9. Rollout, abort, rollback or forward repair, reconciliation, and monitoring are executable and owned.
10. An isolated restore proves data, keys, schema, tenant isolation, critical journeys, RPO, and RTO.
11. The final report states READY, READY_WITH_CONDITIONS, NOT_READY, or INCIDENT and names every blocker.
12. No result, source, command output, test success, version, or production behavior is invented.

If any mandatory item is missing, state: **The system is not yet fully production-ready.**

## Forbidden Shortcuts

- Do not invent versions, advisories, command output, passing tests, performance numbers, or production observations.
- Do not declare safety because TypeScript compiles, Express or Fastify starts, or health is green.
- Do not use trust proxy true blindly, wildcard credentialed CORS, client-supplied tenant identity, or UI visibility as authorization.
- Do not swallow rejected promises, emitter errors, stream errors, fatal process errors, or background task failures.
- Do not retry non-idempotent writes blindly or keep durable idempotency and locks only in process memory.
- Do not compile user-provided Fastify schemas or perform expensive external work inside initial validation.
- Do not block the event loop with unbounded synchronous CPU, parser, crypto, compression, filesystem, or child-process work.
- Do not use floating tools, mutable artifacts, hidden rebuilds, unreviewed migration-on-start, or production data in unsafe tests.
- Do not assume deployment rollback reverses data, queue, email, payment, file, cache, or provider side effects.
- Do not declare READY without monitoring, abort, rollback or forward repair, isolated restore, and residual-risk ownership.

## Mandatory Final Report

1. Executive summary, system purpose, audit scope, selected mode, and final verdict.
2. Repository, workspace, executable, architecture, trust-boundary, and owner maps.
3. Runtime, package manager, TypeScript, Express or Fastify, native ABI, artifact, deployment, and support table.
4. Command log with directory, environment, versions, inputs, outputs, warnings, and exit codes.
5. Endpoint and job matrix covering auth, authorization, tenant, validation, limit, idempotency, transaction, timeout, test, and status.
6. P0-P3 register with evidence level, root cause, blast radius, repair, regression, rollout, rollback, and residual risk.
7. Security, concurrency, data, queue, integration, event-loop, memory, performance, and shutdown results.
8. Dependency, SBOM, provenance, CI trust, immutable promotion, and artifact identity results.
9. Rollout, guardrail, abort, rollback, forward repair, reconciliation, restore, RPO, RTO, and incident readiness.
10. Remaining blockers, accepted risks, owners, deadlines, monitoring, and exact conditions for READY.
11. Primary external sources with title, URL, access date, exact claim, and decision impact.

## Final Decision Rules

- READY - all mandatory evidence and acceptance criteria are met; no unresolved P0 or P1; recovery is proven.
- READY_WITH_CONDITIONS - no active P0; contained P1 or material P2 conditions have owner, deadline, monitoring, and release approval.
- NOT_READY - a required control, evidence, compatibility, capacity, rollback, restore, or ownership condition is missing.
- INCIDENT - active compromise, cross-tenant exposure, corruption, leaked production secret, malicious artifact, or ongoing harm requires containment.

## Execution Order

safety snapshot -> inventory -> runtime and artifact identity -> deterministic baseline -> framework lifecycle -> validation and security -> invariants and data -> queues and integrations -> event loop and resources -> observability and testing -> deployment and supply chain -> rollout, restore, incident controls -> final report

Priority order: protect users and data; contain active compromise; preserve authorization and tenant isolation; restore functional and transactional correctness; bound resources and partial failure; verify release and recovery; optimize only from measurement.
