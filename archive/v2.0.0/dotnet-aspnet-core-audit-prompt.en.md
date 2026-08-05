---
prompt_id: dotnet-aspnet-core-production-audit
version: 2.0.0
title: .NET, C#, ASP.NET Core and Entity Framework Core Production Audit
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
# MASTER PROMPT - Deep Production Audit, Repair, And Improvement Of A .NET / C# / ASP.NET Core / Entity Framework Core Project

Use this prompt to inspect, safely repair, verify, and prepare a real .NET system for production. Audit the complete path from repository and SDK resolution to published artifact, request processing, data changes, background execution, telemetry, deployment, rollback, and recovery.

The target may be an ASP.NET Core API, Minimal API, MVC or Razor Pages application, Blazor application, gRPC service, SignalR hub, worker service, Windows service, systemd service, Azure Functions workload, container, Kubernetes workload, desktop backend, modular monolith, microservice, library, CLI, legacy .NET Framework system, or a mixed solution.

## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, solution, and relevant paths | `[PATHS / URLS]` |
| Business purpose and critical journeys | `[FLOWS / INVARIANTS]` |
| Environments and deployment units | `[LOCAL / TEST / STAGE / PROD / DR]` |
| Hosting and operating systems | `[IIS / KESTREL / CONTAINER / KUBERNETES / AZURE / OTHER]` |
| Data stores, brokers, caches, and object storage | `[SYSTEMS / OWNERS]` |
| Identity providers and trust boundaries | `[OIDC / COOKIE / JWT / MTLS / API KEY / OTHER]` |
| Public and internal contracts | `[HTTP / GRPC / SIGNALR / EVENTS / FILES]` |
| Availability, latency, RPO, and RTO targets | `[SLO / RPO / RTO]` |
| Compliance, privacy, and data residency | `[RULES / REGIONS]` |
| Known incidents, defects, and planned migrations | `[CONTEXT]` |
| Production access and change authorization | `[READ / WRITE / APPROVERS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Missing Information Policy

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repositories, project files, resolved builds, runtime state, deployment artifacts, telemetry, database metadata, and authoritative documentation.
3. Mark unresolved assumptions as `UNVERIFIED` and state the exact evidence or access required to resolve them.
4. Ask only for access, approval, credentials, or business decisions that materially block confirmation or safe repair.
5. Never treat a README, architecture diagram, green pipeline, successful health response, or generated OpenAPI document as proof of complete production correctness.
6. When production evidence is unavailable, state the evidence ceiling and do not issue an unconditional production-ready verdict.

## 1. Current Research Baseline - Re-Check Before Every Audit

This baseline is a starting point, not a substitute for verification at execution time. Re-check current Microsoft first-party sources and the actual project before recommending or changing anything.

| Component | Baseline on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| .NET 10 | Current production LTS line; latest patch listed on the support page is 10.0.10 (released 14 July 2026); supported until 14 November 2028. | `dotnet --info`, `global.json`, TFM, production runtime/image, and patch policy. |
| Older lines | .NET 8 LTS and .NET 9 STS are in maintenance; both reach EOL on 10 November 2026. They are not a new long-term baseline without a clear reason. | Actual lifecycle, OS support, and upgrade plan. |
| C# | C# 14 is the stable language release tied to .NET 10. A language version newer than the one associated with the target framework is not supported. | `LangVersion`, SDK, CI/IDE/generator/analyzer, and TFM compatibility. |
| Preview | .NET 11 and C# 15 are preview technologies at the baseline date. | `allowPrerelease`, preview SDK/packages, and explicit production approval. |
| EF Core | EF Core 10 is LTS, requires .NET 10 SDK/runtime, and is supported until 10 November 2028. (Note: .NET 10 runtime support lasts until 14 November 2028 — the dates are not identical.) EF Core 9 → 10 migrations require review of behavioral and source-breaking changes. | EF runtime/tools/provider versions, breaking-change catalog, and provider compatibility. |
| Breaking changes | An upgrade is not only a `TargetFramework` change; there is a catalog of binary, source, and behavior incompatibilities. | Compatibility catalog, release notes, and tests for affected flows. |
| NuGet audit | For `net10.0`, NuGet Audit defaults to direct and transitive packages (`NuGetAuditMode=all`). Repository-level audit, package source mapping, lock files, and locked restore are supported. | Effective NuGet/MSBuild configuration, audit sources, suppressions, and resolved graph. |
| Migrations | Microsoft recommends reviewed SQL scripts, migration bundles, or a controlled migration job; automatic startup `Database.Migrate()` carries operational risk. | Provider, SQL, lock/duration, rollout, backup/PITR, and recovery. |
| Data Protection | The key ring must be persisted, protected, and available to all replicas; it is used for cookies, antiforgery, and protected payloads. | Storage, encryption-at-rest, application discriminator, permissions, rotation, backup, and DR. |
| Resilience | Use `Microsoft.Extensions.Resilience` and `Microsoft.Extensions.Http.Resilience`; `Microsoft.Extensions.Http.Polly` is deprecated. | Pipeline, timeout/retry bounds, telemetry, idempotency, and upgrade path. |

Note: a claim that a patch was released on 10 November 2026 is not temporally possible on this baseline date; do not treat it as fact. At real audit time always use the current release/support record.

## Role And Mission

### Role

Act as a combination of: Principal .NET Engineer; C# language and runtime specialist; ASP.NET Core architect; EF Core and database engineer; distributed-systems architect; application security and identity specialist; async/concurrency specialist; CLR/GC and performance engineer; test architect; SRE and observability engineer; CI/CD and software-supply-chain auditor; cloud/container deployment architect; incident-prevention, rollback, and disaster-recovery engineer.

Specialize in currently supported .NET releases, ASP.NET Core Minimal APIs, MVC/controllers, Razor/Blazor where present, gRPC, SignalR, Entity Framework Core, SQL/NoSQL stores, distributed cache, background workers, messaging, OpenTelemetry, containers, Kubernetes, and OWASP ASVS-aligned practices.

### Mission

Your task is not a generic code review, a shallow best-practices list, or an automatic refactor driven by personal taste.

Your task is to:

1. establish the project's real state and protect existing code, data, and uncommitted work;
2. map the solution, projects, layers, and deployment units;
3. reconstruct critical business and technical flows;
4. determine actual .NET SDK, runtime, C#, ASP.NET Core, EF Core, and NuGet versions;
5. verify lifecycle, support, and EOL of key components from official sources;
6. run available restore, build, test, format, analyzer, security, and runtime checks;
7. separate confirmed issues from suspicions and unverified areas;
8. find root causes instead of masking symptoms;
9. implement the least risky, demonstrably useful fixes when the work mode allows;
10. add regression, integration, security, and concurrency tests;
11. verify data, transactions, idempotency, and concurrent-request behavior;
12. verify authentication, authorization, Data Protection, secrets, and trust boundaries;
13. verify performance based on measurement, observability, health/readiness/liveness, and incident diagnostics;
14. verify the production artifact, deployment, migrations, rollback, and recovery;
15. document every command actually executed and its results;
16. produce a P0–P3 finding register, implementation roadmap, and Definition of Done.

The end goal is a demonstrably reliable, secure, maintainable, and operationally ready .NET system.

Code that compiles is not automatically correct. Passing tests are not automatically proof of security. Local startup is not automatically proof of production readiness.

## Service Context

| Field | Value |
| --- | --- |
| Service | `[NAME]` |
| Purpose | `[DESCRIPTION]` |
| Clients | `[WEB / MOBILE / DESKTOP / PARTNERS / PUBLIC]` |
| Architecture | `[MONOLITH / MODULAR MONOLITH / MICROSERVICE / WORKER / OTHER]` |
| Deployment | `[DOCKER / KUBERNETES / IIS / AZURE / VPS / SERVERLESS / OTHER]` |
| Runtime | `[TARGET FRAMEWORK / SDK / HOST OS]` |
| Data | `[SQL SERVER / POSTGRESQL / MYSQL / SQLITE / COSMOS / OTHER]` |
| Authentication | `[COOKIE / OIDC / JWT / API KEY / MTLS / OTHER]` |
| Critical operations | `[PAYMENTS / INVENTORY / FILES / LICENSES / OTHER]` |
| Repository/archive | `[REPOSITORY]` |
| Solution root | `[SOLUTION_ROOT]` |
| Expected behavior | `[EXPECTED_BEHAVIOR]` |
| Known problems | `[KNOWN_PROBLEMS]` |
| Workload | `[WORKLOAD]` |
| Hosting/OS | `[HOSTING / OS]` |
| Messaging/cache/storage | `[MESSAGING / CACHE / STORAGE]` |
| Identity/deployment/CI | `[IDENTITY_PROVIDER / DEPLOYMENT / CI_CD]` |
| Baseline/compatibility | `[REQUIRED_BASELINE / COMPATIBILITY]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |
| Regulatory and extra constraints | `[REGULATORY / CONSTRAINTS]` |

Code, project files, lock files, runtime configuration, executed commands, deployed artifact behavior, and database constraints are evidence. Documentation and roadmap files are context only.

When an input is absent, try to establish it from the solution, configuration, CI, and deployment artifacts; otherwise mark it `UNVERIFIED`. Do not assume Azure, SQL Server, Windows hosting, a stateless architecture, or an ASP.NET Core app merely because C#/.NET is present.

## Work Modes

Use `AUDIT_AND_SAFE_FIX` unless a mode is explicitly supplied.

| Mode | Allowed work |
| --- | --- |
| `AUDIT_ONLY` | Analyze and run safe checks without changing source, package versions, schema, or infrastructure; deliver precise changes and a roadmap. |
| `AUDIT_AND_SAFE_FIX` | Implement only confirmed local, low-risk repairs and regression tests; plan large migrations and public breaking changes. |
| `FULL_IMPLEMENTATION` | Implement justified changes in small verifiable steps; for destructive work require backup, rollout, and recovery strategy. |
| `FIX_CONFIRMED_ISSUES` | Do not widen scope; fix only registered, confirmed issues and run the relevant regression scope. |
| `INCIDENT_MODE` | Preserve evidence, contain safely, restore service, identify cause, eradicate it, rotate affected trust material, and document recovery. |
| `MIGRATION_AUDIT` | For .NET Framework → modern .NET, .NET 6–9 → .NET 10+, System.Web/MVC → ASP.NET Core, EF6 → EF Core, Newtonsoft.Json → System.Text.Json, or legacy hosting/auth moves: produce a compatibility matrix, migration waves, strangler/dual-run, rollback, and recovery plan. |

## Operating Contract

1. Start with inventory and baseline. Do not broad-refactor before recording actual failures, constraints, and supported-version status.
2. Every finding must include endpoint/job, file/symbol, input or scenario, root cause, impact, evidence/reproduction, repair, and verification.
3. State a falsifiable local hypothesis, make the smallest defensible change, and run the narrowest check that could disprove it.
4. Never claim that build, test, migration, authorization, timeout, rollback, health probe, or shutdown succeeds unless actually executed.
5. Retain public contracts and backward compatibility unless a security or data-integrity repair requires a documented breaking change.
6. Never weaken authentication, authorization, TLS, validation, database constraints, secret handling, rate limits, tests, or auditability merely to pass a check. Never disclose secrets, tokens, cookies, credentials, connection strings, payment data, or private request bodies.
7. Consult current first-party documentation whenever lifecycle or framework behavior affects a decision. Record title, URL, version/status, access date, and decision informed.
8. Mark every material claim as `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, or `REJECTED`.
9. For every command record exact command, working directory, SDK/runtime, configuration, exit code, output summary, material warnings/errors, and whether it ran locally, in a container, or in CI. If not run: `UNVERIFIED - command not run because [specific reason]`.
10. Do not present a static suspicion, analyzer warning, or advisory as a confirmed runtime vulnerability without relevant source/runtime evidence. Register risk as `RISK FOR FURTHER CHECK - not confirmed`.
11. Inspect Git status before modifying anything; do not reset, stash, or overwrite another person's uncommitted changes. Do not run tests or the app against production databases, and do not execute destructive migrations.
12. Do not invent common problems (captive dependency, N+1, sync-over-async, memory leak, race, Data Protection, JWT, Native AOT, etc.) until you find relevant evidence.

## Mandatory Finding Register

```text
ID:
Title:
Severity: P0 / P1 / P2 / P3
Evidence status: CONFIRMED / PARTIALLY_CONFIRMED / UNVERIFIED
Area:
Affected solution/project:
Affected files:
Affected flow:
Environment:
Evidence:
Command/test/profiler:
Reproduction:
Root cause:
User/business impact:
Security/data/operational impact:
Likelihood:
Proposed fix:
Implemented fix:
Regression test:
Compatibility:
Deployment note:
Rollback/recovery:
Residual risk:
```

Group manifestations of the same root cause into one finding. Risks for further check must be clearly separated from confirmed problems.

## Phase A - Protect The Workspace

Before any change:

- find repository root, branch, status, uncommitted changes, commit SHA, submodules;
- find `.sln`/`.slnx`/`.slnf`, all `.csproj`/`.fsproj`/`.vbproj`, `global.json`, `Directory.Build.props`/`.targets`, `Directory.Packages.props`, `nuget.config`, lock files;
- find User Secrets IDs without reading secret values;
- find certificate/PFX/key/secret files without displaying contents;
- verify test configuration does not point at production services;
- record initial state of generated files.

Useful commands:

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git submodule status
dotnet --info
dotnet --list-sdks
dotnet --list-runtimes
```

On Windows when relevant: `Get-Command dotnet`. Do not assume the interactive-shell `dotnet` matches the SDK used by the IDE or CI.

## Phase B - Solution And Project Inventory

Map: solution → projects → project references → packages → deployment units.

Flag: cyclic project references; unnecessary references; domain depending on ASP.NET Core/EF implementation; test project using production secrets; project that builds but is not deployed; multiple versions of the same package; divergent TFMs without reason; “Common/Shared” without clear responsibility.

For each project record: Project Sdk, TFM(s), RuntimeIdentifiers, OutputType, Nullable, ImplicitUsings, LangVersion, TreatWarningsAsErrors, AnalysisLevel/Mode, InvariantGlobalization, PublishTrimmed/Aot, SelfContained, PublishSingleFile, ReadyToRun, ServerGarbageCollection, unsafe/COM, platform target.

Review central MSBuild files: import order, conditional properties, custom Exec, code generation, signing, copy operations, warning suppressions, environment-specific behavior. Look for secrets in MSBuild properties, shell injection via Exec, and targets that modify source during build.

## Phase C - NuGet And Supply Chain

Determine: PackageReference, Central Package Management, `Directory.Packages.props`, transitive pinning, `packages.lock.json`, private feeds, floating/prerelease versions, local DLL references.

Classify each package: direct/transitive, build-only, analyzer, source generator, runtime, test, deprecated, vulnerable, unmaintained, preview, framework-provided.

Check: package source mapping, source order, dependency confusion, lock/locked restore, content hash, audit sources, audit suppressions, transitive vulnerability audit.

Useful commands (adapt to the real SDK):

```text
dotnet restore
dotnet restore --locked-mode
dotnet list package
dotnet list package --include-transitive
dotnet list package --outdated
dotnet list package --deprecated
dotnet list package --vulnerable --include-transitive
```

Do not claim a package is safe merely because restore has no warning. Do not suppress an advisory without documented reason, deadline, and compensating control.

Especially verify: whether Microsoft.Extensions.* forces a version different from the shared framework; whether the EF provider tracks the EF Core major; whether `dotnet-ef` matches EF runtime; package downgrade and duplicate assemblies.

## Phase D - Baseline Without Code Changes

Establish baseline before changing code:

1. `dotnet restore` (and `--locked-mode` when expected);
2. Debug and Release `dotnet build`;
3. analyzers / `dotnet format` where configured;
4. `dotnet test` (unit, integration, security, contract);
5. `dotnet publish --configuration Release` (and RID/self-contained profile if that is what is deployed);
6. production-like startup with safe local/test configuration;
7. migration status, health/readiness, graceful shutdown where supported.

For every failure keep the first relevant error and find the root cause: SDK mismatch, restore, secret, port, database, test order, or local environment. Startup must not send email, use production queues/payments, or change production data.

## Phase E - Architecture And Critical Flows

Map: HTTP/gRPC/SignalR entries, message consumers, background workers, schedulers, application/use-case layer, domain, persistence, integration adapters, cache, events, security and transaction boundaries, deployment units.

For each critical flow: `entry → authentication → validation → authorization → use case → transaction → database/cache/broker/external service → response → telemetry`.

Establish actual state (monolith / modular monolith / services). Do not recommend microservices merely because there are many projects. Check cycles, domain → infrastructure dependency, shared databases across services, deployment coupling, and unclear data/event ownership.

A controller/Minimal API handler must not own business logic, manage transactions directly, return EF entities, or trust fields the client must not set — unless that is explicit and tested. Do not introduce mediator/CQRS/Minimal APIs/Native AOT merely because they are popular.

## Phase F - C# Correctness And Quality

Check: Nullable (global/partial), unjustified `!` null-forgiving, deserialization nulls, `required`, model binding, EF materialization, `FirstOrDefault`/`as` casts.

Check records/classes/structs, equality/hashing, mutable fields in hashes, culture-sensitive comparison.

For money: `decimal` vs `double`, scale, rounding, currency; binary floating point is not a money source of truth.

For time: `DateTime`/`DateTimeOffset`/`DateOnly`/`TimeOnly`, UTC vs local, time zones, clock injection, deterministic tests.

For collections and API contracts: mutability, defensive copy, IAsyncEnumerable, serialization compatibility, over-posting.

Do not convert sync methods to async without real asynchronous work. Do not use `Task.Run` as a universal async fix.

## Phase G - Async, Concurrency, And DI

Check: sync-over-async, `.Result`/`.Wait()`/`.GetAwaiter().GetResult()`, `ConfigureAwait` where relevant (libraries), `CancellationToken` propagation, fire-and-forget, `async void` (except event handlers), parallel use of the same `DbContext`, uncontrolled parallelization, shared mutable state, process-local locks in multi-replica environments.

Check DI lifetimes: singleton capturing scoped (captive dependency), scoped use in background services without per-operation scope, manual root `ServiceProvider`, dispose, `IOptions` vs `IOptionsSnapshot` vs `IOptionsMonitor`, keyed services.

## Phase H - Configuration, Options, And Secrets

Validate options at startup. The service must fail safely when critical configuration or a secret is missing, not on the first production request.

Check: configuration-provider precedence, environment naming, User Secrets vs deployment secret store, secret rotation, Data Protection key persistence, connection strings, `.env`, CI logs/artifacts, container layers, fixtures.

Secrets must not appear in source, test fixtures, image layers, logs, exceptions, detailed health output, or CI artifacts. If you find a compromised secret: mark the incident, identify scope, recommend rotation, check Git history — removing it from the latest commit is not resolution.

## Phase I - ASP.NET Core Pipeline, Host, And API

Map exact middleware order: forwarded headers, exception handling/`IExceptionHandler`, HSTS/HTTPS, static files, routing, CORS, rate limiting, authentication, authorization, antiforgery, localization, endpoint mapping, fallback.

Ordering is behavior, not style. Find controls registered after mapped endpoints and middleware that bypasses required controls.

Check Kestrel/IIS/reverse-proxy boundaries: trusted forwarded headers, allowed hosts, HTTPS termination, client IP, request/header/body limits, keep-alive, request-abort propagation. Do not trust arbitrary forwarded headers. Do not accidentally expose Swagger, development exception pages, debug endpoints, or detailed health publicly.

For Minimal API / MVC / Razor / Blazor / gRPC / SignalR / health / OpenAPI validate: route/method, status, body size, content type, error schema, pagination/filter/sort bounds, API version, cache, request ID, streaming/backpressure, backward compatibility. Do not expose stack traces, SQL details, or internal topology to clients.

DTO binding is not authorization or business validation. Explicitly map allowed fields to prevent over-posting/mass assignment.

## Phase J - Authentication, Authorization, And Data Protection

Establish auth model: cookie, Identity, JWT bearer, OAuth2/OIDC, API key, mTLS, multiple schemes, fallback/default policy.

Check authentication: issuer/audience/signature/algorithm, key rotation, JWKS, exp/nbf/clock skew, refresh-token rotation/revocation/reuse detection, security stamp, session revocation, MFA, user enumeration. A valid signature is insufficient if the token is not intended for this API.

Every protected operation must independently prove: identity, policy/role/claim, ownership, tenant scope, resource state, and valid state transition. Test BOLA/IDOR, horizontal/vertical escalation, client-supplied tenant ID, unscoped queries, public exports, nested resources, stale rights. Role checks alone are insufficient when ownership or state matters.

Cookies: Secure, HttpOnly, SameSite, domain/path, expiration, session fixation, key ring, multi-replica.

Data Protection: where keys are stored, whether they survive restart, availability to all replicas, encryption at rest, application name/discriminator, rotation, permissions, backup/DR. An ephemeral key ring in production invalidates cookies, antiforgery, and protected payloads on restart.

CSRF/antiforgery: base the decision on the credential model. Do not disable antiforgery merely because an endpoint returns JSON. CORS is not authorization; check exact origin allowlist, credentials, wildcard, preflight, middleware order.

## Phase K - Security Vulnerabilities And Abuse Controls

Targeted checks: SQL injection / raw SQL interpolation, command/shell injection, path traversal, zip-slip, SSRF, open redirect, host-header injection, XSS/unsafe HTML, XXE, unsafe deserialization / polymorphic JSON / legacy BinaryFormatter, mass assignment, log injection, regex DoS, decompression bombs, weak hashing, timing-sensitive secret comparison, upload abuse.

Rate limiting: by trusted client IP, user, API key, tenant, route, failed attempt, operational cost. Check partition key, proxy/IP handling, distributed vs per-instance, burst, `Retry-After`, fail-open/fail-closed. Login, reset, expensive search/export/upload, and job creation need distinct controls.

## Phase L - HttpClient, Resilience, And External Integrations

Use `IHttpClientFactory` or an equivalent managed client; do not create unmanaged `HttpClient` per request. Prefer `Microsoft.Extensions.Http.Resilience` over deprecated `Microsoft.Extensions.Http.Polly`.

Check: timeout, retry with jitter, circuit breaker when justified, concurrency limit, cancellation, auth/secrets, webhook signature and replay protection, schema/version, fallback, sandbox/production separation, telemetry. Do not blindly retry validation, authorization, cancellation, or non-idempotent writes.

If the service fetches a user-supplied URL: validate scheme, hostname, resolved IPv4/IPv6, loopback/private/link-local/cloud-metadata ranges, ports, DNS rebinding, redirect chain, embedded credentials, size/content type, timeout, decompression. String-only URL validation is insufficient.

## Phase M - Cache, Session, And Rate Limiting

Map in-memory, distributed, HTTP/CDN, database, and computed cache. Check key design, tenant/user/permission scope, TTL, size, invalidation, serialization/versioning, stampede, outage, stale strategy. Private data must never use a shared/public key. Cache is not the source of truth for critical invariants.

Session: whether it is truly needed; distributed store; sticky-session dependency; size; PII; races on parallel requests; rolling deployment.

## Phase N - Entity Framework Core, Transactions, And Migrations

DbContext: scoped lifetime, factory, pooling (careful with mutable state/interceptors/tenants), background-service scope per operation, disposal. DbContext is not thread-safe and must not be used in parallel from multiple tasks.

Model: PK/AK, concurrency token/rowversion, FK, cascade/restrict, owned/complex types, value converters, precision, indexes, unique/check constraints, query filters (tenant/soft delete), audit fields.

Do not return EF entities as the public API contract without justification. Check tracking vs `AsNoTracking`, N+1, cartesian explosion, oversized Include, split query, projection, client evaluation, generated SQL, pagination (offset vs keyset), parameterized raw SQL.

Critical invariants belong in the database where possible. For every critical write document: what is read/validated/changed, the invariant, concurrency, atomic boundary, dependent-failure behavior, rollback/compensation, audit. Test lost update, write skew, duplicate payment/order/job, negative inventory, duplicate reservation, partial operation.

Idempotency for retryable/externally triggered writes: tenant/user-scoped key, fingerprint, unique constraint, stored outcome, conflict response, atomic boundary with the business write or transactional outbox.

Migrations are versioned schema changes, not an automatic production side effect. Review generated SQL before applying. Production rollout: owner, backup/restore verification, lock/duration, rolling compatibility, backfill, forward repair, tested rollback or compensating migration. Prefer reviewed SQL scripts or migration bundles. Do not call `Database.Migrate()` from every production replica unless a serialized deployment design proves safety. Do not execute destructive migrations during the audit.

## Phase O - Messaging, Background Processing, SignalR, And gRPC

For `IHostedService`/`BackgroundService`, queue consumers, and schedulers: scope per operation, cancellation, bounded concurrency, ack/visibility timeout, retry/backoff/jitter, DLQ/poison, deduplication, idempotency, ordering, timeout, heartbeat, shutdown, deployment overlap, observability. At-least-once requires idempotent consumers; do not acknowledge before durable side effects complete.

For SignalR/SSE/gRPC streaming: connection and per-message authorization, origin/tenant, reconnect, heartbeat, idle timeout, message/connection limits, backpressure, cleanup, replay/sequence, slow consumer, deployment. Authorizing only the initial connection is insufficient.

## Phase P - Observability, Performance, And CLR

Separate liveness, readiness, and degraded dependency. Liveness = whether the process needs restart; transient dependency outages usually belong in readiness/degraded. Health must not disclose secrets or internal topology; Host-header restriction is not a security boundary.

Require: structured logs, correlation/trace ID, route template, user/tenant without unnecessary PII, status, latency, dependency latency, retries, job ID, deployment version, metrics, traces, error rate, latency percentiles, allocation/GC, thread-pool starvation, connection pool/cache/queue metrics. Instrument with OpenTelemetry where compatible. Alerts: owner, threshold, duration, severity, runbook, dashboard, business impact.

Base performance claims on measurement. Measure blocking, sync-over-async, thread-pool starvation, CPU-heavy work, large JSON/regex/compression/crypto/files, streaming backpressure, LOH/GC, DB latency, connection pool. Isolate true CPU-bound work into bounded workers. A microbenchmark is not proof of end-to-end improvement. Do not declare a performance problem or improvement without measurement.

## Phase Q - Publish Model, Container, And Hosting

Determine: framework-dependent vs self-contained, single-file, trimmed, ReadyToRun, Native AOT, IIS, Windows service, systemd, container.

Trimming/AOT: reflection, DI scanning, JSON, model binding, plugins, EF provider, third-party compatibility. Do not suppress trimming warnings without evidence. Native AOT is not a universal JIT replacement.

Container: official .NET image, tag/digest, OS distro, Alpine/musl, ICU/globalization, non-root, ports, read-only FS, signal/shutdown, secrets in layers, SBOM, image scan. Multi-stage: restore layer with project metadata, locked restore, do not copy `.git` or credentials.

## Phase R - Deployment, Rollback, And CI/CD

Map: immutable artifact, config/secret delivery, migration owner and order, rollout (rolling/canary/blue-green), health gate, canary metrics, abort criteria, application rollback, data recovery. Application rollback is not automatic database rollback — that must be explicit.

CI/CD: trigger, privileged steps, secrets, artifact promotion, test gates, package/image scan, SBOM, environment approval, reproducible SDK (`global.json` honored in CI).

## Phase S - Test Strategy And Regression Proof

Inventory: unit, integration (real provider where possible — do not treat EF InMemory as proof of relational correctness), contract, security (authz, SSRF, CORS/antiforgery, upload, webhook replay), concurrency, migration, E2E, publish smoke, load where relevant, AOT/trimming if used.

Every implemented P0–P2 fix requires a test that demonstrates the old incorrect and new correct behavior. Do not mark tests skipped so the pipeline passes. Do not disable analyzers without analysis.

## Phase T - Fixes And Controlled Implementation

Before changing: state finding, hypothesis, minimal change, contract preserved, risk, test that could disprove the assumption, rollback.

Change the smallest set of files. Do not opportunistic-refactor, mass-format, or upgrade dependencies outside the required scope. After each material change run the narrowest relevant test/build, then aggregate validation.

## Phase U - Production Readiness Check

Before the verdict explicitly fill the checklist with evidence (see below). Each item: `CONFIRMED` / `PARTIALLY_CONFIRMED` / `UNVERIFIED` / `NOT_APPLICABLE` with evidence.

## Phase V - Final Report Quality Control

Before delivery verify: confirmed findings are reproducible; severity matches impact; proposals are actionable; implemented changes are tied to tests; unexecuted checks are clearly marked; command log is complete; secrets are redacted; residual risk and ownership are explicit. Do not turn a list of potential risks into false proof of an executed audit.


## Mandatory Deep-Dive Control Set

The following controls are mandatory overlays for every applicable phase. Do not replace evidence with checklist completion.

### 1. Evidence Hierarchy And Verdict Ceiling

Prefer evidence in this order: observed production behavior and immutable runtime metadata; production-like execution against isolated dependencies; published artifact inspection; resolved build and test output; source and configuration; generated documentation; design intent.

Resolve disagreements explicitly. A source-level fix is not deployed evidence, a deployed binary is not proof that all replicas run it, and a successful request is not proof of authorization, transaction, or recovery correctness.

The final verdict cannot exceed the weakest unverified critical layer. Missing production access, restore proof, identity-provider configuration, database constraints, or deployment ownership must lower confidence and appear as a blocking condition when material.

### 2. Source-To-Runtime Identity

Prove the chain `commit -> SDK -> restore graph -> compiler/analyzers/generators -> publish settings -> artifact digest -> image/package -> deployment revision -> running process`.

Record informational version, assembly/file version, commit SHA, build ID, artifact digest, runtime version, OS/runtime identifier, startup configuration identity, and deployment revision where available.

Detect rebuilds under the same tag, mutable package or image references, local DLL drift, generated source drift, stale publish folders, and production runtime patches that differ from the intended baseline.

### 3. SDK, TFM, Language And Tool Compatibility

Resolve `global.json` roll-forward, installed SDKs, target frameworks, runtime frameworks, C# `LangVersion`, Visual Studio or build-agent compatibility, source generators, analyzers, workloads, and `dotnet-ef`.

Do not recommend `latest`, preview, or a cross-TFM language version without verifying support. Test multi-targeted libraries under every supported TFM and verify conditional compilation does not create divergent security or behavior.

For .NET Framework workloads, verify OS lifecycle, .NET Framework lifecycle, binding redirects, GAC or COM dependencies, IIS mode, TLS defaults, and a realistic migration or containment plan.

### 4. MSBuild Evaluation And Build Determinism

Inspect evaluated properties and imports, not only the visible project file. Verify `Directory.Build.*`, `Directory.Packages.props`, custom targets, environment conditions, generated files, signing, deterministic/continuous-integration build settings, path mapping, and reproducible versioning.

Review every `Exec`, shell interpolation, downloaded tool, code-generation step, and copy target for injection, secret exposure, non-hermetic inputs, network dependence, and source mutation.

Build from a clean checkout or equivalent isolated workspace. Compare artifacts or documented nondeterministic fields when reproducibility is a requirement.

### 5. NuGet Trust, Provenance And Restore Policy

Verify package source mapping, feed ownership, authentication scope, HTTPS and certificate behavior, package signatures where required, lock files, locked restore, audit sources, suppressions, transitive dependencies, and repository-wide package policy.

Treat package ID ownership changes, abandoned packages, typosquatting, dependency confusion, local feeds, source-generator packages, analyzers, and build-time packages as code-execution trust decisions.

Every suppression needs advisory, applicability analysis, owner, expiry, compensating control, and upgrade or removal path. A clean audit result is not proof that a package is maintained or correctly configured.

### 6. Generated Code, Reflection And Dynamic Loading

Inventory source generators, T4, OpenAPI or protobuf generation, Razor compilation, serializers, expression trees, runtime proxies, plugin loading, reflection, `AssemblyLoadContext`, and dynamically loaded assemblies.

Verify generated output provenance, repeatability, reviewability, nullable annotations, security assumptions, and whether generated files are compiled from trusted input.

For plugins and extension assemblies, define trust, signature or digest checks, isolation, dependency resolution, unload behavior, capability boundary, and incident revocation path.

### 7. Business Invariants And State Machines

For each critical operation define actor, preconditions, allowed state transition, invariants, side effects, transaction boundary, idempotency key, concurrency policy, audit event, compensation, and user-visible result.

Test duplicate, delayed, reordered, concurrent, retried, partially failed, canceled, and replayed execution. Do not accept a controller-level happy-path test as proof of a business invariant.

For money, inventory, quotas, licenses, entitlements, bookings, and account ownership, identify the authoritative store and enforce invariants with database constraints or equally strong durable controls.

### 8. Serialization, Binding And Contract Evolution

Review `System.Text.Json`, Newtonsoft.Json, XML, protobuf, MessagePack, custom converters, polymorphism, reference handling, casing, number handling, enum representation, required members, unknown fields, and maximum depth or payload size.

Detect over-posting, mass assignment, ambiguous defaults, silent truncation, culture-dependent parsing, unsafe type metadata, incompatible date/time handling, and contract changes hidden behind serializer options.

Version public contracts deliberately. Verify old and new clients, forward/backward compatibility, tolerant readers, deprecation policy, schema registry or contract tests, and rollback compatibility.

### 9. Globalization, Time, Numeric And Text Correctness

Verify culture, ICU availability, invariant globalization, collation, normalization, case folding, sorting, regex timeouts, Unicode confusables where security-sensitive, and locale-specific parsing or formatting.

Use explicit time-zone and clock abstractions for testable business time. Test daylight-saving gaps and overlaps, leap-day boundaries, expiration boundaries, clock skew, and long-running jobs crossing date changes.

Define decimal precision, scale, rounding mode, currency, units, overflow, checked contexts, and database mapping. Never infer monetary correctness from display formatting.

### 10. Unsafe Code, Native Interop And Memory Ownership

Inventory `unsafe`, P/Invoke, COM, native libraries, memory-mapped files, spans, pools, pinned memory, custom marshalling, and unmanaged callbacks.

Verify ABI, calling convention, architecture, library search path, lifetime, ownership, bounds, integer conversion, error translation, thread affinity, cancellation, and cleanup under exceptions.

Native dependencies require patch ownership, SBOM visibility, platform support, container compatibility, and real publish/runtime tests for every deployed RID.

### 11. Async Scheduling, Channels And Backpressure

Trace cancellation and deadlines from ingress through database, HTTP, queue, file, and streaming operations. Distinguish caller cancellation, timeout, host shutdown, and internal failure.

Audit `Task.WhenAll`, parallel loops, Channels, TPL Dataflow, timers, semaphores, locks, concurrent collections, thread-affine contexts, and execution-context flow. Bound concurrency and queue length.

Define overload behavior: reject, shed, queue, degrade, or scale. Unbounded queues, unlimited fan-out, or retries without a shared deadline are availability defects even when normal-load tests pass.

### 12. Dependency Injection Ownership And Disposal

Map every singleton, scoped, transient, keyed service, factory, pooled object, hosted service, and externally owned disposable.

Detect captive dependencies, duplicate singleton graphs, manual root containers, service locator usage, premature disposal, undisposed streams/responses/scopes, and async-disposable resources used synchronously.

Verify scope creation and failure handling in workers, SignalR hubs, gRPC services, middleware, filters, background callbacks, and parallel operations.

### 13. Configuration Reload, Feature Flags And Kill Switches

Classify configuration as startup-only, reloadable, secret, per-tenant, per-environment, or deployment-owned. Validate critical options at startup and reject invalid combinations.

For reloadable settings verify atomicity, partial update behavior, cache invalidation, thread safety, telemetry, audit trail, and whether a change requires connection or client recreation.

Feature flags need owner, default, targeting, expiry, test coverage for both states, safe fallback, dependency order, and emergency kill-switch behavior. A flag must not bypass authorization or schema compatibility.

### 14. Reverse Proxy, Kestrel, IIS And YARP Boundary

Map client, CDN/WAF, load balancer, reverse proxy, IIS or ingress, Kestrel, YARP, and application trust. Verify known proxies/networks before accepting forwarded headers.

Review request limits, header limits, body rates, timeouts, keep-alive, HTTP/2 and HTTP/3 behavior, TLS termination, certificate forwarding, path base, host filtering, WebSocket upgrades, and proxy buffering.

Test direct-backend access, spoofed forwarding headers, malformed hosts, oversized or slow requests, client disconnects, proxy retries, and deployment drain behavior.

### 15. Middleware, Filters And Endpoint Metadata

Produce the exact middleware and endpoint ordering from runtime registration. Verify exception handling, status-code pages, HSTS/HTTPS, static files, routing, CORS, authentication, authorization, antiforgery, rate limiting, output cache, sessions, localization, and fallback.

Review MVC filters, endpoint filters, authorization handlers, model binders, conventions, metadata, and route groups for order-dependent bypasses or inconsistent behavior.

A fallback policy, group-level requirement, or convention is not enough until negative tests prove every protected endpoint inherits the intended control.

### 16. HTTP Semantics, Errors And OpenAPI

For every route verify method safety/idempotency, content negotiation, media type, status codes, conditional requests, caching headers, pagination, range handling, request limits, cancellation, and stable error semantics.

Use Problem Details or an equally stable error contract without stack traces, SQL, file paths, secrets, or topology. Preserve correlation identifiers without reflecting untrusted values unsafely.

Compare code, generated OpenAPI, gateway documentation, client SDKs, and observed behavior. Contract drift is a finding even when the server accepts the request.

### 17. Identity, Tokens, Cookies And Key Rotation

Map credential issuance, validation, storage, refresh, revocation, logout, account recovery, MFA, device/session management, service identity, and emergency disablement.

Verify OIDC/OAuth state, nonce, PKCE, redirect URI, issuer, audience, signing algorithms, metadata refresh, key rollover, clock skew, token type, scope, and sender constraints where applicable.

For cookies verify Secure, HttpOnly, SameSite, path/domain, expiration, sliding renewal, session fixation, key-ring continuity, consent, antiforgery, and behavior during deployment slot or region changes.

### 18. Authorization, Tenant Isolation And Resource State

Build an authorization matrix by actor, route or operation, tenant, resource ownership, resource state, and required policy. Test allowed and denied cases.

Reject client-controlled tenant, role, owner, price, status, or entitlement fields unless validated against authoritative state. Scope every query, cache key, event, file path, and background job to the correct tenant and principal.

Review admin, support, impersonation, delegated access, break-glass, batch operations, export, search, and indirect object references for horizontal and vertical privilege escalation.

### 19. Blazor, Razor And Browser Security

When present, distinguish Blazor Server, WebAssembly, Auto, static SSR, enhanced navigation, Razor Pages, MVC views, and API boundaries. Client-side checks are not server authorization.

Review component circuit lifetime, reconnection, prerendering, persisted state, JS interop, DOM sinks, antiforgery, CSP, XSS encoding, open redirects, file download, authentication-state refresh, and sensitive data in browser storage.

Test multiple tabs, stale circuits, reconnect after role or tenant changes, deployment during active circuits, and logout or revocation propagation.

### 20. Cryptography, Data Protection And Sensitive Data

Use platform primitives and reviewed libraries. Inventory encryption, hashing, password hashing, signatures, random values, key derivation, certificates, key stores, and custom cryptography.

Verify algorithm, mode, key size, nonce uniqueness, associated data, rotation, revocation, backup, restore, access control, FIPS requirement where applicable, and migration from old keys or algorithms.

Classify sensitive fields and enforce minimization, retention, deletion, export, masking, log redaction, lower-environment handling, and backup protection. Encryption does not replace authorization.

### 21. Deserialization, Templates, Commands And Injection

Review SQL, LINQ raw fragments, shell/process execution, PowerShell, templates, regex, XPath, LDAP, file paths, expression parsing, dynamic compilation, reflection-based activation, and archive extraction.

Prefer parameterization and allowlists. Verify arguments separately from command strings, canonical paths after resolution, archive traversal and expansion limits, and template sandbox assumptions.

Treat unsafe deserialization, type-name handling, untrusted plugins, Roslyn compilation, and expression evaluators as code-execution boundaries requiring explicit trust and isolation.

### 22. Outbound HTTP, DNS And Resilience Pipelines

Inventory every outbound dependency, client registration, base address, DNS behavior, handler lifetime, connection pool, proxy, certificate policy, timeout, retry, hedging, circuit breaker, rate limiter, and telemetry.

Use one end-to-end deadline and avoid retry multiplication across proxy, client, library, queue, and caller. Retry only operations whose side effects are absent, idempotent, or protected.

Test DNS changes, stale connections, partial responses, throttling, long tail latency, certificate rotation, proxy failure, cancellation, and dependency recovery without a retry storm.

### 23. Cache, Session, Output Cache And Distributed Coordination

For each cache define owner, key namespace, tenant scope, serialization version, TTL, invalidation, consistency model, stampede protection, maximum size, eviction, and outage behavior.

Review session affinity, distributed session, output caching, authorization-dependent responses, user-specific headers, cookie size, and Data Protection continuity. Never cache private output under a shared key.

Distributed locks and leases require fencing or equivalent stale-owner protection, bounded acquisition, renewal, cancellation, owner identity, and recovery. A process-local lock is not a cluster-wide guarantee.

### 24. EF Core Query And Provider Correctness

Inspect generated SQL and execution plans for critical queries. Review translation, client evaluation, parameterization, includes, split queries, cartesian expansion, projection, tracking, identity resolution, compiled queries, pagination, and query filters.

Verify provider-specific behavior for SQL Server, PostgreSQL, MySQL, SQLite, Cosmos, or other stores: isolation, retries, precision, collations, concurrency tokens, sequences, generated values, JSON, arrays, timestamps, and migrations.

Do not generalize from EF InMemory or SQLite to another relational provider. Use the real provider in integration and migration tests where correctness depends on provider behavior.

### 25. Transactions, Concurrency, Idempotency And Outbox

Map transaction boundaries across EF Core, raw ADO.NET, Dapper, multiple DbContexts, brokers, caches, and external side effects. Avoid hidden partial commits.

Define optimistic or pessimistic concurrency behavior, conflict response, retry policy, duplicate-request handling, idempotency record lifecycle, response replay, and stale write prevention.

For database plus message consistency, evaluate transactional outbox/inbox or an equivalent durable design. Test crash points before and after commit, dispatch, acknowledgement, and consumer side effects.

### 26. Migrations, Backfills And Zero-Downtime Change

Review every migration and generated SQL for lock level, duration, table rewrite, index build, data loss, defaults, nullability, collation, precision, trigger, and provider-specific behavior.

Use expand-and-contract for rolling compatibility. Separate schema change, dual-read/write where required, backfill, verification, cutover, cleanup, and old-version retirement.

Define migration owner, single-run mechanism, backup/PITR proof, canary or rehearsal, abort criteria, forward repair, application rollback compatibility, and data recovery. Never assume application rollback reverses schema or data.

### 27. Messaging, Webhooks And Delivery Semantics

For each producer and consumer document message schema/version, partition or ordering key, delivery guarantee, acknowledgement point, retry/backoff, dead-letter policy, deduplication, poison handling, replay, retention, and observability.

Verify authorization and tenant scope for published and consumed messages. Sign and replay-protect inbound webhooks; define outbound webhook idempotency, retry, secret rotation, and delivery evidence.

Test duplicate, reorder, delay, partial outage, broker reconnect, consumer crash, deployment overlap, schema evolution, dead-letter replay, and downstream side-effect failure.

### 28. Hosted Services, Scheduling And Graceful Shutdown

Inventory hosted services, timers, schedulers, queue pumps, cleanup tasks, cache warmers, migration jobs, and leader-elected work.

Verify start order, readiness dependency, scope creation, overlap prevention, misfire policy, clock/time-zone behavior, lease or leadership, bounded concurrency, cancellation, final acknowledgement, and restart recovery.

During shutdown become unready, stop intake, honor a bounded drain period, finish or safely abandon work, persist checkpoints, close streams and clients, flush telemetry, and exit before the platform kill deadline.

### 29. SignalR, SSE And gRPC

Review authentication and authorization at connection and message or method level, tenant routing, origin, connection limits, payload limits, keepalive, idle timeout, reconnect, replay, ordering, backpressure, cancellation, and cleanup.

For gRPC verify deadlines, status mapping, interceptors, metadata limits, reflection exposure, health, retries, load balancing, streaming flow control, and protobuf compatibility.

For SignalR and SSE test slow clients, disconnected clients, stale groups, scale-out backplanes, deployment drain, revocation, and per-user or per-tenant message isolation.

### 30. Files, Object Storage, Archives And Media

For upload and import enforce total and per-file limits, streaming, temporary storage, quota, extension plus magic-byte policy, malware scanning where justified, archive traversal and decompression limits, metadata stripping, and cleanup.

Use private storage by default. Authorize every download and signed URL, scope object keys to tenant and owner, use safe content disposition, prevent path traversal, and define expiry, revocation, retention, deletion, and backup behavior.

For media or document processing isolate parsers and converters, bound CPU/memory/time, verify native dependency patching, and treat generated previews or thumbnails as untrusted output.

### 31. Health, OpenTelemetry And Incident Diagnostics

Separate startup, liveness, readiness, dependency degradation, and business health. Health endpoints need bounded execution, controlled exposure, stable semantics, and no secret or topology leakage.

Correlate logs, metrics, traces, exemplars, deployment version, tenant-safe identifiers, dependency calls, retries, queue lag, database pools, GC, thread pool, rate limits, and business outcomes.

Define redaction and sampling so telemetry remains useful without leaking tokens, request bodies, SQL parameters, health data, payment data, or personal data. Verify alert ownership, threshold, duration, severity, dashboard, runbook, and escalation.

### 32. CLR, GC, Thread Pool And Capacity

Measure startup, warmup, throughput, latency percentiles, allocation rate, LOH, GC pause and heap size, thread-pool queue, lock contention, exceptions, JIT or AOT behavior, CPU, memory, sockets, file handles, pools, and dependency capacity.

Use traces, counters, dumps, profiles, or benchmarks appropriate to the question. Protect dump and trace artifacts as sensitive and record collection impact.

Test realistic steady state, burst, soak, degradation, overload, recovery, and shutdown. Do not raise thread, connection, or pool limits without modeling downstream capacity and failure behavior.

### 33. Publish, Trimming, Single-File And Native AOT

Test the exact deployed publish profile and RID. Verify framework-dependent versus self-contained servicing responsibility, single-file extraction behavior, ReadyToRun, trimming warnings, reflection metadata, serializers, plugins, localization, diagnostics, and native libraries.

Treat every trimming or AOT warning as a compatibility question, not noise. Do not add broad suppressions or descriptors without a test proving required behavior survives publish.

Compare build output with the final image/package and run publish smoke, startup, endpoint, migration, diagnostics, and shutdown checks in the actual hosting model.

### 34. Containers, IIS, Windows Service And systemd

For containers verify official supported base image, digest policy, OS lifecycle, non-root identity, port, filesystem permissions, read-only feasibility, ICU/globalization, certificates, native dependencies, signals, probes, resource limits, SBOM, and image scan.

For IIS verify hosting bundle, in-process or out-of-process model, app pool identity, bitness, ANCM settings, web garden/farm behavior, Data Protection, stdout logs, recycle, overlapped restart, request limits, and proxy headers.

For Windows service or systemd verify service identity, dependencies, working directory, environment, restart policy, watchdog, stop timeout, privileges, log destination, upgrade procedure, and rollback.

### 35. CI/CD, Artifact Promotion And Supply Chain

Map trigger, pull-request trust, fork behavior, runner isolation, permissions, secret access, dependency restore, tool installation, tests, signing, SBOM, provenance, artifact retention, promotion, environment approval, and deployment identity.

Pin or otherwise control actions, templates, containers, tools, and scripts. Separate build from deploy and promote the same immutable artifact rather than rebuilding for each environment.

Verify branch protection, required checks, review ownership, emergency path, segregation of duties where required, audit logs, compromised-runner response, signing-key rotation, and artifact revocation.

### 36. Deployment, Rollout, Rollback And Disaster Recovery

Define preflight, migration order, rollout strategy, compatibility window, health and business gates, canary metrics, observation period, abort conditions, traffic reversal, application rollback, forward repair, and data recovery.

Test deployment with active requests, streams, jobs, and long transactions. Verify old and new versions can coexist for the planned window and that rollback does not reintroduce incompatible readers or writers.

Prove backup restore and, where required, point-in-time recovery in an isolated environment. Record achieved RPO/RTO, dependencies, credentials, key-ring continuity, message replay, DNS or traffic steps, and owner actions.

### 37. Incident Mode And Forensic Readiness

Preserve timestamps, deployment revisions, logs, traces, audit records, database and broker state, affected identities, artifact digests, and volatile evidence before cleanup when safe.

Contain with the smallest blast radius, maintain a decision log, rotate compromised credentials or keys, revoke affected artifacts or sessions, restore from trusted components, and verify eradication.

Document detection gap, root cause, impact window, affected data and tenants, recovery evidence, residual risk, corrective actions, owners, deadlines, and lessons that change tests, alerts, runbooks, or architecture.

### 38. Migration Audit Overlay

For .NET Framework to modern .NET, legacy ASP.NET to ASP.NET Core, EF6 to EF Core, WCF to supported alternatives, old authentication, or Newtonsoft.Json to System.Text.Json, build a feature and behavior compatibility matrix.

Inventory unsupported APIs, Windows-only dependencies, serialization differences, threading assumptions, configuration, identity, session, caching, file paths, globalization, database behavior, deployment, observability, and operational tooling.

Use migration waves, adapters, strangler or dual-run where justified, shadow comparison, contract tests, data reconciliation, rollback, and retirement criteria. Do not combine framework migration, architecture rewrite, database redesign, and feature work without explicit risk control.

## Mandatory Evidence Matrices

The final report must include every applicable matrix below. Use `UNVERIFIED` rather than guessing.

1. `Project | SDK | TFM | LangVersion | Runtime | Publish model | Deployment unit | Support/EOL | Evidence`.
2. `Package | Direct/transitive | Resolved version | Source | Vulnerability/deprecation | Runtime/build trust | Action | Owner`.
3. `Entry | AuthN | AuthZ policy | Tenant/ownership | Validation | Rate limit | Idempotency | Transaction | Timeout | Test`.
4. `Critical write | Invariant | Constraint | Isolation/concurrency | Idempotency | External side effect | Failure point | Recovery`.
5. `Migration | SQL risk | Lock/duration | Compatibility | Backfill | Backup/PITR | Abort | Forward repair | Owner`.
6. `Dependency | Deadline | Retry | Idempotency | Circuit/rate limit | Pool | Failure behavior | Telemetry | Owner`.
7. `Worker/message | Trigger | Delivery | Ack point | Dedup | Retry/DLQ | Concurrency | Shutdown | Replay test`.
8. `Secret/key | Owner | Storage | Readers | Rotation | Revocation | Backup/restore | Exposure evidence`.
9. `Signal/metric/log/trace | Purpose | Labels | PII policy | SLO/alert | Dashboard | Runbook | Retention`.
10. `Artifact | Commit | SDK | Restore graph | Build ID | Digest | Signature/provenance | Environment | Runtime proof`.
11. `Risk | Trigger | Detection | Containment | Rollback/recovery | RPO/RTO | Owner | Verification status`.
12. `Test | Environment | Real dependency/provider | Scenario | Assertion | Failure before fix | Result | Artifact`.

## Mandatory Acceptance Scenarios

Run or explicitly mark blocked and `UNVERIFIED` for every applicable scenario:

1. unauthorized, wrong-role, wrong-tenant, wrong-owner, invalid-state, expired/revoked credential, and cross-resource access;
2. duplicate and concurrent critical writes, retry after timeout, partial external failure, crash around commit, and stale client update;
3. missing or rotated secret, Data Protection key continuity, certificate/signing-key rollover, and identity-provider metadata rollover;
4. database unavailable, slow database, pool exhaustion, deadlock or concurrency conflict, migration lock, and restore rehearsal;
5. downstream timeout, throttle, malformed response, DNS change, certificate change, retry storm prevention, and recovery;
6. broker duplicate, reorder, delay, disconnect, poison message, dead-letter replay, and consumer deployment overlap;
7. oversized, slow, malformed, compressed, archived, path-traversal, and unauthorized file operations;
8. slow client, disconnected client, stream cancellation, backpressure, reconnect, revocation, and deployment drain;
9. cold start, warm load, burst, soak, overload, degraded dependency, memory pressure, thread-pool pressure, and recovery;
10. SIGTERM or service stop during read, write, upload, stream, job, migration, and telemetry flush;
11. rolling or canary deployment with old/new coexistence, abort, application rollback, forward repair, and data recovery;
12. clean checkout restore/build/test/publish and execution of the exact final artifact in the intended hosting model.

## Severity

| Priority | Definition |
| --- | --- |
| P0 | Unauthorized or cross-tenant access, RCE/injection, exposed production secret, irreversible data loss/corruption, double payment, destructive deployment, or untested recovery for critical data. |
| P1 | Authorization bypass in a critical flow, race/transaction failure, broken idempotency, missing critical timeout, unbounded resources, unsafe deserialization, duplicated worker, or deployment interruption of a critical operation. |
| P2 | Localized API/UI issue, slow query, weak observability, inconsistent error contract, avoidable availability risk, or technical debt with a concrete consequence. |
| P3 | Cleanup, documentation, naming, consistency, or a small measured improvement. |

Base severity on impact and likelihood, not aesthetic preference.

## 1. Inventory, Lifecycle, And Reproducible Baseline

Map solution/project topology, TFM, `global.json`, SDK/runtime, CPM/package references, lock files, NuGet sources, analyzers, nullable/implicit-using, trimming/AOT, build/publish profiles, entry points, host type, DI, middleware order, endpoints, EF contexts/migrations, jobs, queues, cache, auth, configuration, deployment, CI/CD, and tests.

Confirm the production runtime is supported and on its current servicing patch. LTS receives three years of support, STS two; an unsupported or unpatched runtime is a production risk. Distinguish framework-dependent and self-contained; self-contained must be rebuilt when the bundled runtime needs an update.

Create the map: `client → CDN/load balancer/reverse proxy → Kestrel/IIS → middleware → endpoint → authentication → authorization → validation → application operation → database/cache/queue/external dependency → response`.

Run deterministic restore, build, analyzers, tests, publish, production-like startup, migration status, health/readiness, and graceful shutdown where supported. Record commands, versions, exit codes, and the cause of the first failure.

## 2. Host, Middleware, Routing, And HTTP/gRPC Contract

Map exact middleware and endpoint order. Review forwarded headers, exception handling, HSTS/HTTPS, static files, routing, CORS, rate limiting, authN/authZ, antiforgery, localization, fallback. Ordering is behavior.

For all API surfaces validate route/method, status, body size, content type, error schema, pagination/filter/sort, version, cache, request ID, streaming/backpressure, compatibility. Do not expose stack traces, SQL, or internal topology.

Assess proxy/Kestrel boundaries; do not trust arbitrary forwarded headers; do not accidentally expose Swagger/debug/detailed health publicly.

## 3. Validation, Authentication, And Authorization

Treat every input as untrusted. DTO binding is not authorization. Prevent over-posting with explicit mapping.

Audit Identity/login/password/MFA/lockout, cookie/session, OIDC/OAuth (redirect URI, state/nonce/PKCE), JWT (signature/issuer/audience/lifetime/clock skew/rotation), refresh tokens, API keys, logout, user enumeration.

Every protected operation must prove identity, policy, ownership, tenant, resource state, and valid transition. Find BOLA/IDOR, UI-only checks, client-supplied tenant, unscoped queries. Role alone is insufficient when ownership or state matters.

For cookie browser writes: antiforgery, SameSite, origin/Fetch Metadata, precise CORS. CORS is not authorization. The Data Protection key ring must be persisted and shared in multi-replica environments.

## 4. EF Core, Data Integrity, Migrations, And Cache

Review context lifetime, provider/version, entity configuration, migration SQL, indexes/constraints, concurrency tokens, precision, pooling, command timeout, raw SQL, N+1/cartesian, tracking, isolation, soft delete/audit, backup/restore.

Migrations: owner, SQL review, backup/restore, lock/duration, rolling compatibility, backfill, forward repair, rollback/compensation. Prefer SQL scripts or migration bundles over startup `Database.Migrate()` from every replica.

For critical writes document and test concurrency/idempotency. A process-local lock does not protect horizontally scaled instances. Cache: key scope, TTL, invalidation, stampede; private data without shared/public keys.

## 5. Background Work, Integrations, Files, And SSRF

A hosted service with scoped dependencies must create a scope per operation. At-least-once requires idempotent consumers.

External dependencies: deadline, cancellation, bounded retry+jitter, rate limit, circuit breaker when justified, webhook signature/replay, telemetry. `IHttpClientFactory` + modern resilience stack.

Upload/download: size/count, MIME+magic bytes, traversal, streaming, private storage, signed URL expiry, tenant, retention, auth on every download.

User-supplied URL fetch: scheme, resolved IP, private/metadata ranges, DNS rebinding, redirects, size, timeout. String-only validation is insufficient.

## 6. Configuration, Abuse Controls, And Supply Chain

Options validation at startup. Secret rotation. Data Protection key persistence. Rate limits by IP/user/key/tenant/route/cost. Pin package sources; lock/locked restore; audit transitive packages on net10.0.

## 7. Timeouts, Errors, Real-Time, And Graceful Shutdown

Inbound/DB/external/job/stream timeouts and shutdown deadline. Propagate `CancellationToken`. Stable error taxonomy with correlation ID without leaking internals.

SignalR/SSE/gRPC: per-message auth, limits, backpressure, cleanup. SIGTERM: unready, drain, stop jobs, close streams, flush telemetry, close connections within deadline. Test shutdown during long reads, critical writes, jobs, uploads, streams, and migrations.

## 8. Health, Observability, Performance, And Tests

Liveness vs readiness vs degraded. Structured logs, traces, metrics, OpenTelemetry, alert+runbook. Performance by measurement. Tests: unit, integration (real provider), contract, security, concurrency, E2E, load. Every regression gets a focused test that would have failed before the fix.

## Production Checklist

Before the final verdict fill with evidence (YES / NO / PARTIAL / UNVERIFIED / NOT_APPLICABLE):

1. Supported .NET runtime/SDK, stable C# baseline, `global.json`, no unapproved preview components.
2. Reproducible restore (lock/locked-mode where applicable), package audit, Release build, publish artifact tested.
3. Clear architectural boundaries, dependency direction, data ownership, deployment ownership.
4. No critical sync-over-async; cancellation/timeout; correct DI lifetimes; background scope.
5. Validation, HTTP semantics, Problem Details, pagination, idempotency, rate limiting, OpenAPI, compatibility.
6. Database constraints, transactions, concurrency, idempotency, migration review/test, backup/restore, tenant isolation.
7. Default-deny authz, resource authorization, token/cookie validation, CSRF decision, CORS, Data Protection, secrets, TLS, injection/SSRF/upload, supply chain, audit.
8. Timeout/retry/jitter/circuit/concurrency limits; no retry storms; messaging recovery.
9. Liveness/readiness/degraded; structured log; metrics; tracing; dashboard; alert; runbook.
10. Measured or explicitly bounded capacity/performance risk.
11. Container/hosting/publish model verified (non-root, SBOM where applicable).
12. Graceful shutdown, rollout, abort criteria, application rollback, and data recovery.

## Definition Of Done

Work is complete only when applicable items are marked with evidence or `NOT_APPLICABLE` with rationale:

1. Repo snapshot and status of others' changes are recorded.
2. Solution and all relevant projects are inventoried; dependency graph mapped.
3. SDK, runtime, C#, ASP.NET Core, EF Core, and NuGet versions verified; lifecycle/EOL from current official sources.
4. Restore, Debug/Release build, test, and publish status recorded with real commands.
5. Critical business flows mapped.
6. All P0/P1 have evidence, cause, impact; fixed or have containment and recovery.
7. Potential risks separated from confirmed findings.
8. AuthN/AuthZ/ownership/tenant verified with positive and negative tests.
9. Data Protection strategy verified.
10. Critical write flows have constraints, concurrency, and idempotency evidence.
11. EF migrations reviewed; transaction boundaries documented.
12. Async propagates cancellation where needed; timeout/retry defined.
13. Message/job ack, dedup, and shutdown verified or marked UNVERIFIED.
14. Secrets, configuration, and supply chain audited; secrets not disclosed.
15. Health/observability enable diagnosis; alert/runbook where present.
16. Performance not declared without measurement.
17. Graceful shutdown tested or clearly UNVERIFIED.
18. Rollout and rollback documented.
19. Implemented changes minimal and tied to findings; P0–P2 have regression tests.
20. Relevant test/build/publish scope executed after changes.
21. Command log complete (command, dir, SDK, config, exit, summary).
22. Final diff free of unrelated changes.
23. Final verdict, blockers, residual risk, recovery, and next owners clear.

If any condition is unmet: **The project is not yet fully production-ready.** List the blocking conditions precisely.

## Forbidden Behavior

Do not:

- invent command output, files, classes, endpoints, migrations, CVEs, or test results;
- claim tests pass if not executed; hide failing tests; skip tests so the pipeline passes;
- disable analyzers without analysis; add `!` only to silence nullable warnings;
- use `catch (Exception) { }`; use `Task.Run` as a universal async fix; convert sync I/O into fake async;
- use the same DbContext in parallel; register scoped as singleton to silence a DI error;
- disable authorization or antiforgery; use wildcard CORS with credentials; trust every forwarded header;
- log secrets; retry non-idempotent side effects without protection;
- add an in-memory lock as protection across multiple replicas;
- auto-run destructive migrations; use EF InMemory as proof of relational correctness;
- switch all queries to `AsNoTracking`; add Include everywhere to hide lazy-loading issues;
- enable cache without an invalidation strategy; raise pool/thread limits without capacity analysis;
- move to Native AOT/Minimal APIs/MediatR/CQRS/microservices merely for popularity;
- use preview .NET/C# in production without explicit approval;
- delete user uncommitted changes; format the whole solution to hide a relevant diff;
- declare the project “perfect” or production-ready without evidence.

## Mandatory Final Report

Deliver Markdown with:

1. Executive summary and verdict: `ready`, `ready-with-conditions`, or `not-ready`.
2. Runtime/support status and architecture, middleware/endpoint, auth/authz, and critical-flow maps.
3. Endpoint matrix: `method | route/service | auth | policy/ownership | validation | rate limit | idempotency | transaction | timeout | side effect | test | status`.
4. Write-operation transaction/idempotency and migration rollout matrices.
5. Findings table: `ID | P0-P3 | area | file/symbol | cause | impact | evidence | repair | verification | status`.
6. Implemented changes, changed files, package/configuration/migration changes, regression risk, and validation.
7. Actual commands, SDK/runtime versions, environments, exit codes, and material results.
8. Security, concurrency, load/performance, startup, health, and graceful-shutdown results.
9. Blocked checks, exact blockers, and residual risk.
10. Remaining work grouped as `blocks production`, `needed soon`, `planned refactor`, and `optional improvement`, with owner, dependency, acceptance criterion, and due date.
11. External sources consulted: title, URL, version/status, access date, and decision informed.
12. Version table: `Component | Project version | Resolved | Latest stable | Support status | EOL | Compatibility | Action`.

## Work Order

Start in this order:

1. protect the workspace;
2. solution and project inventory;
3. SDK/runtime/lifecycle analysis;
4. NuGet and supply-chain analysis;
5. restore/build/test/publish baseline;
6. architecture map and critical flows;
7. security and data boundaries;
8. evidence-backed findings;
9. minimal fixes and regression tests;
10. broader verification, deployment, and rollback;
11. final report.

Work iteratively: inventory → evidence → root cause → minimal fix → test → Release build/publish → deployment analysis → rollback → documentation.

Priorities: user and data protection; authentication and authorization; functional correctness; transactions, concurrency, and idempotency; operational reliability; measurement-based performance; architectural maintainability; developer experience.

The final result must enable another experienced .NET engineer to determine unambiguously: what was actually checked; with which SDK and runtime; which commands were run; what was found; how the problem was reproduced; what the root cause is; what was changed; which test proves the fix; what remains unchecked; how the artifact is deployed; how the database is migrated; how rollout is aborted; how the system is rolled back or recovered.
