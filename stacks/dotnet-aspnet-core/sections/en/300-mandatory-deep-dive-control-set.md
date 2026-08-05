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

