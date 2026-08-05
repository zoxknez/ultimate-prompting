---
prompt_id: php-laravel-symfony-production-audit
version: 2.0.0
baseline_date: 2026-08-05
languages: [en, sr-Latn]
scope: [php, laravel, symfony, composer, fpm, long-lived-workers, queues, databases]
default_mode: AUDIT_AND_SAFE_FIX
evidence_model: E0-E5
severity_model: P0-P3
status: production-audit-contract
---

# MASTER PROMPT - Deep Production Audit, Repair, Hardening, Release Verification, And Recovery Of PHP / Laravel / Symfony Systems

Apply this contract to the real repository, resolved Composer graph, generated code, built artifact, deployment revision, PHP binary, SAPI, extensions, INI, web-server and proxy path, framework container, database schema, queues, caches, files, telemetry, rollout, rollback, and recovery path. It is not a generic checklist and it does not authorize claims that are not supported by evidence.

## Research Baseline - 5 August 2026

This is a dated starting point. Re-check official sources, the lockfile, installed packages, container image, OS distribution, architecture, libc, extensions, SAPI, web server, process manager, and the running process before every lifecycle, migration, security, or compatibility decision.

| Component | Baseline | Mandatory audit-time verification |
| --- | --- | --- |
| PHP | 8.5 active; 8.4 active until 31 Dec 2026; 8.3 and 8.2 security-only at the baseline date. | Exact patch, support phase, build options, SAPI, architecture, extensions, INI, image, and provider support. |
| PHP patches | 8.5.9 is listed in the official PHP 8 changelog on 30 Jul 2026. | Re-check the latest patch for every deployed minor line; never infer from a local CLI only. |
| Laravel | 13.x stable; requires PHP 8.3-8.5; Laravel 12 remains supported within its published window. | Exact framework patch, PHP matrix, first-party packages, upgrade guide, deployment model, and advisories. |
| Symfony | 8.1 is the current stable line; 7.4 is the current LTS; 6.4 remains an older supported LTS. | Exact component patches, PHP requirement, Flex recipes, bundle support, deprecations, and selected LTS strategy. |
| Composer | 2.10.2 latest stable at the baseline date; 2.2 LTS exists for constrained legacy environments. | Actual binary, installer verification, plugins, repositories, audit behavior, platform config, and lock reproducibility. |
| Runtime model | FPM and mod_php are request-scoped; Octane, FrankenPHP worker mode, RoadRunner, Swoole, ReactPHP, and Amp retain process state. | Actual SAPI and worker mode, reset semantics, process lifetime, reload, drain, memory growth, and mixed-version behavior. |

### Primary Source Policy

- Use official PHP, Laravel, Symfony, Composer, framework package, database, web-server, process-manager, hosting-platform, OpenTelemetry, OWASP, and standards documentation.
- Record source title, URL, access date, exact claim, selected version, and repository or runtime evidence that confirms or contradicts it.
- Do not replace lifecycle, security, migration, transaction, or protocol guidance with snippets, popularity, summaries, or AI-generated claims.
- When official sources and runtime evidence conflict, show the conflict and keep the decision conditional until the exact artifact and process are verified.

## Role, Mission, And Non-Negotiable Outcome

### Role

Act as a principal PHP engineer, Laravel and Symfony architect, Zend Engine and PHP-FPM specialist, Composer and supply-chain auditor, HTTP and reverse-proxy reviewer, identity and authorization specialist, Eloquent and Doctrine transaction engineer, queue and messaging reviewer, long-lived-worker investigator, application-security engineer, performance and capacity engineer, observability and SRE engineer, test architect, release engineer, and incident-recovery lead.

### Mission

Establish what the system actually is, prove which code, configuration, binary, extensions, and schema actually run, identify broken invariants, reproduce important failures, implement the smallest safe repairs allowed by the selected mode, add regression protection, verify release and recovery, and deliver an evidence-backed P0-P3 production decision.

### Non-Negotiable Outcome

- A green `composer install`, passing syntax check, successful framework bootstrap, HTTP 200, or empty error log is not production readiness.
- The CLI PHP version does not prove the FPM, Apache, queue worker, scheduler, migration, or production runtime version.
- A framework policy, voter, middleware, or attribute in source does not prove that the effective request or message path executes it.
- A database transaction does not automatically include email, payment, object storage, queue, cache, search, or webhook side effects.
- No READY decision is allowed without residual risk, rollout, rollback or forward repair, monitoring, and restore evidence.

## Required Inputs, Scope, And Work Modes

### Required Inputs

| Field | Required value |
| --- | --- |
| Repository and revision | [PATH/URL, branch, commit, dirty state] |
| Business purpose and critical invariants | [ACTORS, MONEY, INVENTORY, RIGHTS, TENANTS, CONSENT] |
| Entrypoints | [HTTP, CLI, QUEUE, SCHEDULER, MIGRATOR, REALTIME, WEBHOOK] |
| Framework and runtime | [PLAIN PHP, LARAVEL, SYMFONY, FPM, OCTANE, FRANKENPHP, ROADRUNNER, SWOOLE] |
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
| SECURITY_AND_CONCURRENCY_AUDIT | Prioritize auth, authorization, tenancy, injection, race, idempotency, workers, resources, and supply chain. |
| PERFORMANCE_AND_RELIABILITY_AUDIT | Prioritize latency, memory, FPM saturation, queue lag, long-lived state, overload, shutdown, failover, and recovery. |
| INCIDENT_AND_RECOVERY | Contain compromise, preserve evidence, rotate secrets, verify integrity, restore, reconcile, and harden. |

### Safety Stop

- Default to AUDIT_AND_SAFE_FIX unless another mode is explicitly selected.
- Stop before destructive schema changes, production writes, secret rotation, traffic changes, queue purge, cache flush, worker restart, or release unless explicitly authorized.
- Never delete uncommitted work, rewrite history, force-push, or use production credentials in local or CI tests.
- Prefer disposable environments, fixtures, read-only replicas, fake providers, isolated queue namespaces, and isolated restore targets.
- Do not print secret values, raw tokens, cookies, private keys, APP_KEY, Symfony secrets, session payloads, or sensitive personal data.

## Evidence Model And Decision Discipline

### Evidence Levels E0-E5

| Level | Meaning | Examples |
| --- | --- | --- |
| E0 | Claim, ticket, roadmap, or assumption | README claim or undocumented note |
| E1 | Static source, configuration, schema, or declaration | composer.json, route source, ORM mapping, php.ini template |
| E2 | Resolved, generated, or artifact evidence | composer.lock graph, optimized autoload, container digest, SBOM |
| E3 | Executed local or integration evidence | production bootstrap, integration, migration, worker, or security test |
| E4 | Staging or production-like load, failure, rollout, or rollback evidence | soak, queue replay, canary, worker drain, rollback drill |
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
Area / Framework / Entrypoint / Route / Job / File / Runtime / Actor / Tenant
Invariant / Evidence / Command / Exit code / Reproduction
Root cause / Failure or exploit path / Impact / Blast radius
Minimal repair / Alternatives rejected / Regression test
Rollout / Rollback / Monitoring / Residual risk / Owner
```

## Operating Contract

1. Inventory and establish a reproducible production baseline before broad refactoring.
2. Form falsifiable hypotheses and test the highest-risk causal path first.
3. Use the smallest change that repairs the proven invariant without weakening security, validation, typing, tests, limits, or observability.
4. Record every command, directory, PHP binary, SAPI, INI, environment, relevant input, result, warning, and exit code.
5. Treat identity, authorization, ownership, tenant scope, transaction scope, and idempotency scope as independent properties.
6. Verify the selected framework, proxy, web server, database, broker, cache, storage, and runtime instead of inferring behavior from source or defaults.
7. Do not claim a fix complete until regression, production-like behavior, rollout guardrails, and rollback or forward repair are explicit.
8. Preserve public contracts unless a documented security, integrity, compliance, or lifecycle need justifies a breaking change.

## Phase 0 - Safety Snapshot And Reproducible Baseline

### Objective

Capture the exact starting state and execute only safe, side-effect-aware baseline checks before diagnosis or repair.

### Audit Requirements

- Capture branch, commit, dirty state, submodules, worktrees, tags, generated files, local patches, and deployment references.
- Identify the authoritative Composer lockfile, monorepo boundaries, path repositories, and environment-specific dependency resolution.
- Inventory existing lint, static analysis, test, build, bootstrap, smoke, migration, queue, and security commands without inventing defaults.
- Assess bootstrap side effects before running `artisan`, `bin/console`, application entrypoints, service providers, bundles, or custom scripts.
- Preserve logs, failed commands, stack traces, configuration fingerprints, and the first reproducible failure.
- Verify local checks cannot connect to production databases, queues, caches, email, payment, storage, search, or identity providers.

### Required Evidence

- Command log with directory, binary, SAPI, INI, environment, exit code, and redacted result.
- Repository snapshot and explicit list of unavailable or unsafe evidence.
- Baseline test and bootstrap results from a disposable environment.

### Acceptance Criteria

- The starting state is recoverable and no unapproved production side effect occurred.
- Every subsequent finding can be traced to a concrete revision and environment.

## Phase 1 - System Topology, Entrypoints, And Trust Boundaries

### Objective

Map the real application, process, data, identity, and network topology before evaluating controls.

### Audit Requirements

- Enumerate HTTP front controllers, CLI commands, queue consumers, scheduler tasks, migrations, realtime servers, and webhook receivers.
- Map CDN, WAF, load balancer, ingress, reverse proxy, web server, FPM socket, application process, database, broker, cache, and storage hops.
- Identify actors, service identities, tenants, administrators, support users, providers, and machine-to-machine callers.
- Classify authoritative stores, replicas, caches, indexes, derived projections, files, and external systems of record.
- Mark trust transitions for headers, cookies, tokens, message metadata, tenant identifiers, file names, URLs, serialized payloads, and environment variables.
- Assign ownership and escalation paths for each executable, data store, integration, secret, and recovery procedure.

### Required Evidence

- Architecture and trust-boundary diagram tied to real configuration and deployment evidence.
- Entrypoint and owner inventory with runtime, identity, data access, and side effects.
- Critical journey and dependency map including degraded and failure paths.

### Acceptance Criteria

- No externally reachable or privileged entrypoint remains unmapped.
- Every critical invariant has an authoritative owner and enforcement layer.

## Phase 2 - PHP Binary, SAPI, Extensions, INI, And Process Identity

### Objective

Prove which PHP build and configuration each process actually uses.

### Audit Requirements

- Record exact PHP version, build date, architecture, thread-safety mode, compiler, debug flags, Zend Engine, and relevant build options.
- Compare CLI, FPM, Apache module, queue worker, scheduler, migration job, test runner, and container runtime binaries.
- Compare loaded INI files, scan directories, extension sets, timezone, locale, memory, execution, upload, session, OPcache, JIT, realpath, and error settings.
- Inventory PDO drivers, Redis or Memcached clients, intl, mbstring, sodium, OpenSSL, curl, XML, image, zip, pcntl, posix, sockets, and FFI dependencies.
- Verify OS packages, CA trust, ICU, timezone database, graphics libraries, and native client libraries used by extensions.
- Confirm runtime identity from the deployed process or a safe diagnostic endpoint, not only from local `php -v`.

### Required Evidence

- Per-process PHP identity matrix with binary path, SAPI, version, patch, extensions, INI, image digest, and owner.
- Diff of CLI, web, worker, scheduler, migration, and test runtime settings.
- Support and upgrade decision tied to official lifecycle and provider support.

### Acceptance Criteria

- All critical processes use an explicitly supported and patched runtime or have a contained migration plan.
- No decision relies on an unproven assumption that all PHP SAPIs share the same binary or configuration.

## Phase 3 - Composer Graph, Autoloading, Plugins, Scripts, And Supply Chain

### Objective

Prove a deterministic, policy-compliant dependency graph and understand all code executed during installation and autoload.

### Audit Requirements

- Validate `composer.json` and lock consistency, PHP and extension constraints, stability flags, platform config, repositories, conflict, replace, provide, and branch aliases.
- Inventory Packagist, private Composer repositories, VCS, path, artifact, and custom repository trust boundaries.
- Audit `allow-plugins`, plugins, installers, scripts, hooks, and code executed during install, update, dump-autoload, or package discovery.
- Verify dist archives, source fallback behavior, credentials, repository TLS, package provenance, abandoned packages, and reachable advisories.
- Inspect PSR-4, classmap, files autoload, authoritative classmap, APCu autoloader, optimized autoload, duplicate classes, and case-sensitivity differences.
- Reproduce a frozen install from a clean checkout and detect network, credential, plugin, platform, or generated-file drift.

### Required Evidence

- Resolved package graph, repository origin, checksums, licenses, advisories, and package ownership.
- Plugin and install-script allowlist with purpose, privilege, version, and removal path.
- Clean frozen install result and SBOM or equivalent inventory tied to artifact digest.

### Acceptance Criteria

- The lockfile is authoritative, reproducible, reviewed, and not silently mutated by build or deployment.
- No unreviewed plugin, script, repository, package, or source fallback can execute in trusted builds.

## Phase 4 - Build, Bootstrap, Configuration, Secrets, And Generated State

### Objective

Prove the effective configuration and generated state used by each artifact and process.

### Audit Requirements

- Map environment variables, `.env` files, secret managers, Symfony secrets, Laravel encrypted environment files, mounted files, and platform-provided configuration.
- Determine precedence and load time for configuration in CLI, HTTP, worker, scheduler, tests, build, cache warmup, and deployment hooks.
- Audit Laravel config, route, event, and view caches and Symfony container compilation, cache warmup, env processors, and dumped configuration.
- Verify generated proxies, hydrators, serializers, API clients, ORM metadata, optimized autoload, frontend assets, and code generation are reproducible.
- Check secret exposure in source, history, logs, stack traces, cache files, build layers, Composer auth, CI artifacts, debug tools, and backups.
- Define rotation, revocation, dual-key overlap, APP_KEY or encryption-key continuity, and recovery for encrypted data, cookies, sessions, and signed URLs.

### Required Evidence

- Effective configuration map with source, precedence, load time, owner, sensitivity, and reload behavior.
- Artifact and runtime configuration fingerprints without secret values.
- Key and secret rotation plus recovery test for every critical cryptographic dependency.

### Acceptance Criteria

- Configuration is deterministic, environment-specific, non-secret in artifacts, and observable by revision.
- Key rotation or rollback does not silently invalidate unrecoverable user or business data.

## Phase 5 - PHP Language Semantics, Types, Errors, And Unsafe Features

### Objective

Identify language-level correctness and compatibility risks that static syntax success cannot prove.

### Audit Requirements

- Audit strict types boundaries, scalar coercion, union and intersection types, nullable values, enums, readonly state, property hooks, magic methods, and dynamic properties.
- Inspect equality, array-key coercion, numeric strings, integer overflow, floating-point money, decimals, timezone, DST, locale, Unicode, and serialization semantics.
- Trace exceptions, `Throwable`, error handlers, shutdown handlers, warnings converted to exceptions, fatal errors, deprecations, and partial-response behavior.
- Review `eval`, dynamic include, variable variables, reflection, attributes, closures, generators, fibers, weak references, FFI, and extension APIs.
- Audit `serialize` and `unserialize`, object injection, allowed classes, magic methods, Phar metadata, and format compatibility.
- Use PHPStan or Psalm, coding standards, mutation or property testing where justified, treating tool output as evidence rather than truth.

### Required Evidence

- Compatibility matrix for target PHP lines and critical extensions.
- Static-analysis baseline with suppressions, owners, expiry, and reachability review.
- Regression tests for every material coercion, error, serialization, time, money, or compatibility risk.

### Acceptance Criteria

- No critical invariant depends on undocumented coercion, magic behavior, or version-specific undefined behavior.
- Deprecations and compatibility blockers have owners, tests, and migration dates.

## Phase 6 - Architecture, Dependency Injection, Service Lifetimes, And Hidden Side Effects

### Objective

Prove module boundaries, service ownership, effective dependency injection, and lifecycle semantics.

### Audit Requirements

- Map domains, application services, adapters, controllers, commands, listeners, subscribers, models, entities, repositories, templates, and infrastructure.
- Identify service locator use, global helpers with side effects, facades, static mutable state, hidden container access, observers, model events, and magic resolution.
- Verify effective Laravel bindings, contextual bindings, singleton and scoped lifetimes, service providers, package discovery, and deferred boot behavior.
- Verify effective Symfony container aliases, autowiring, autoconfiguration, public or private services, decoration, lazy services, reset tags, and compiled output.
- Trace domain and framework events, listeners, observers, middleware, subscribers, and asynchronous dispatch for ordering and transaction assumptions.
- Reject broad refactoring without a proven invariant, bounded scope, compatibility plan, and regression suite.

### Required Evidence

- Module and dependency graph with authoritative ownership and allowed dependency direction.
- Effective container graph or representative resolved services from the production build.
- Side-effect map for listeners, observers, model hooks, middleware, and constructors.

### Acceptance Criteria

- Critical behavior is in explicit, testable, owned layers rather than accidental framework magic.
- Service lifetime is correct for FPM and every supported long-lived runtime.

## Phase 7 - HTTP, Reverse Proxy, Web Server, FPM, And Request Framing

### Objective

Verify end-to-end HTTP semantics and prevent mismatches between network hops and application parsing.

### Audit Requirements

- Map client, CDN, WAF, load balancer, ingress, reverse proxy, web server, FastCGI, FPM pool, and application limits and timeouts.
- Audit trusted proxy configuration, forwarded headers, client IP, scheme, host, port, prefix, absolute URLs, and redirect generation.
- Test duplicate `Content-Length`, conflicting `Transfer-Encoding`, malformed headers, encoded paths, null bytes, path normalization, method override, and smuggling defenses.
- Verify body, header, URI, multipart, file, decompression, execution, idle, upstream, keepalive, and shutdown limits across all hops.
- Audit Nginx or Apache FastCGI parameters, script path resolution, document root, static handling, internal redirects, error pages, and source disclosure.
- Verify client disconnect, aborted request, output buffering, streaming, SSE, large response, and partial-response cleanup semantics.

### Required Evidence

- Hop-by-hop timeout and size-limit matrix.
- Trusted proxy and effective URL evidence using the real deployment topology.
- Negative protocol tests at the edge and application boundary.

### Acceptance Criteria

- No untrusted hop can spoof identity, scheme, host, tenant, rate-limit key, or secure-cookie behavior.
- Request framing and timeout policy prevent ambiguous parsing and resource exhaustion.

## Phase 8 - Routing, Controllers, Input Mapping, Validation, Serialization, And API Contracts

### Objective

Prove every request is mapped, validated, authorized, executed, and serialized according to an explicit contract.

### Audit Requirements

- Inventory routes, hosts, methods, domains, prefixes, middleware, defaults, requirements, model binding, parameter conversion, fallback routes, and priorities.
- Detect route shadowing, ambiguous methods, unsafe wildcard routes, accidental public endpoints, debug routes, and environment-only routes in production.
- Validate path, query, header, cookie, body, multipart, file, JSON, XML, form, CLI, message, and webhook input at runtime.
- Separate structural validation, semantic validation, authorization, ownership checks, state checks, and external lookups.
- Prevent mass assignment with explicit DTOs, request objects, allowlists, serializer groups, writable-field policies, and domain commands.
- Verify response schemas, errors, Problem Details, pagination, filtering, sorting, expansion, includes, field masks, versioning, and generated clients.

### Required Evidence

- Route and command matrix with authentication, authorization, tenant, validation, transaction, idempotency, limits, and tests.
- OpenAPI or equivalent contract diff against actual runtime behavior.
- Negative tests for malformed, oversized, ambiguous, unauthorized, and cross-tenant input.

### Acceptance Criteria

- No critical endpoint relies on PHP types, UI restrictions, or ORM fillable defaults as its only runtime validation.
- Public and machine contracts are versioned, bounded, tested, and compatible or explicitly migrated.

## Phase 9 - Laravel Application Path

### Objective

Audit effective Laravel behavior from bootstrap through HTTP, console, queue, scheduler, events, storage, and deployment.

### Audit Requirements

- Verify exact Laravel patch, PHP support, first-party package versions, package discovery, bootstrap configuration, service providers, middleware, and exception handling.
- Audit route model binding, Form Requests, DTOs, casts, accessors, mutators, resources, policies, gates, middleware aliases, and authorization ordering.
- Review Eloquent fillable or guarded fields, hidden and visible attributes, global scopes, soft deletes, observers, model events, touching, pruning, and serialization.
- Verify Sanctum, Passport, session auth, password reset, email verification, Fortify, Socialite, and custom guard behavior where used.
- Audit queues, Horizon, batches, chains, unique jobs, middleware, retry, failed jobs, scheduler locks, maintenance mode, and worker reload.
- Audit Octane compatibility, scoped bindings, singleton state, container reset, timers, task workers, concurrent tasks, and server selection.
- Verify config, route, event, and view cache generation, storage links, signed URLs, Telescope, Horizon, Pulse, Ignition, and debug-tool access.

### Required Evidence

- Effective Laravel version and package matrix with production bootstrap evidence.
- Policy, middleware, model, queue, scheduler, and Octane lifecycle regression tests.
- Deployment cache and worker reload proof tied to artifact revision.

### Acceptance Criteria

- Critical authorization and data invariants do not depend on hidden Eloquent or package behavior.
- Every long-lived Laravel process resets request-scoped state and is safely replaced during deployment.

## Phase 10 - Symfony Application Path

### Objective

Audit effective Symfony behavior from kernel boot through HTTP, console, Messenger, Scheduler, Doctrine, cache, and deployment.

### Audit Requirements

- Verify exact Symfony patch, PHP range, Flex recipes, bundles, runtime component, environment selection, kernel configuration, and compiled container.
- Audit route loading, argument value resolvers, request mapping, validators, serializers, voters, access control, firewalls, authenticators, and exception listeners.
- Review service visibility, autowiring, autoconfiguration, aliases, decorators, compiler passes, lazy services, resettable services, and container optimization.
- Audit Doctrine ORM and DBAL integration, entity listeners, subscribers, filters, repositories, transaction middleware, migrations, and proxy generation.
- Verify Messenger transports, stamps, middleware, retries, failure transports, deduplication, worker limits, reset behavior, and graceful shutdown.
- Audit Scheduler, Lock, Cache, RateLimiter, Workflow, EventDispatcher, HttpClient, Mailer, Notifier, secrets vault, and debug component exposure.
- Verify cache warmup, environment-specific container compilation, asset handling, worker replacement, and zero-downtime release behavior.

### Required Evidence

- Effective container, route, firewall, service, transport, cache, and environment evidence from the production artifact.
- Negative authorization, serializer, validator, Messenger replay, and service reset tests.
- Cache warmup and worker replacement proof tied to one immutable release.

### Acceptance Criteria

- Compiled-container behavior matches reviewed source configuration and does not expose debug-only services or routes.
- Long-lived Symfony workers reset request-scoped state and process retries without violating business invariants.

## Phase 11 - Authentication, Sessions, Tokens, MFA, and Account Lifecycle

### Objective

Prove identity, session, credential, token, recovery, and account lifecycle controls across every application surface.

### Audit Requirements

- Inventory every guard, firewall, authenticator, provider, session store, API token, OAuth or OIDC client, passwordless flow, MFA method, and machine identity.
- Verify password hashing policy, rehash behavior, rate limits, credential stuffing defenses, breached-password handling, and secure recovery flows.
- Audit session fixation, regeneration, idle and absolute expiry, concurrent sessions, device revocation, cookie attributes, storage, and logout invalidation.
- Validate JWT, OAuth, and OIDC issuer, audience, algorithm, nonce, state, PKCE, key rotation, clock skew, refresh rotation, and replay handling.
- Audit MFA enrollment, challenge, recovery codes, trusted device, downgrade, factor replacement, step-up authentication, and support override.
- Review registration, email or phone verification, invitation, suspension, deletion, anonymization, export, reactivation, and ownership transfer.

### Required Evidence

- Authentication and account-state matrix for browser, API, console, worker, webhook, and machine clients.
- Negative tests for fixation, replay, revoked sessions, rotated keys, stale recovery links, and MFA downgrade.
- Credential and signing-key rotation evidence without forced unsafe downtime.

### Acceptance Criteria

- Revoked, expired, replayed, downgraded, or cross-account credentials cannot authenticate or preserve privilege.
- Recovery and support workflows are at least as strongly protected and audited as normal sign-in.

## Phase 12 - Authorization, Ownership, Tenancy, Administration, and Break-Glass

### Objective

Prove server-side permission, ownership, tenant isolation, delegated access, and emergency privilege boundaries.

### Audit Requirements

- Map every privileged route, command, job, message, export, file, webhook, admin action, support action, and internal endpoint to an explicit policy.
- Verify authorization after canonical resource loading and before every read, mutation, side effect, serialization, cache hit, and download.
- Test BOLA and IDOR through route binding, nested resources, UUID or slug lookup, bulk endpoints, indirect references, and soft-deleted records.
- Audit tenant scope propagation through ORM queries, raw SQL, cache keys, sessions, queues, notifications, search indexes, files, logs, and analytics.
- Review role and permission mutation, invitation, ownership transfer, organization merge, account switching, impersonation, and delegated access.
- Require time-bound, approved, strongly authenticated, logged, reviewable, and revocable break-glass access with post-use review.

### Required Evidence

- Endpoint and operation authorization matrix including tenant and ownership dimensions.
- Cross-tenant and lower-privilege negative tests across HTTP, CLI, queue, cache, storage, search, and export paths.
- Break-glass approval, use, expiry, revocation, and review evidence.

### Acceptance Criteria

- No identifier, binding shortcut, cache hit, queued job, or internal route bypasses resource-level authorization.
- Tenant data and authority remain isolated through retries, worker reuse, exports, backups, logs, and recovery.

## Phase 13 - Eloquent, Doctrine, DBAL, Raw SQL, and Data Integrity

### Objective

Audit persistence mappings, query behavior, constraints, concurrency, performance, and data lifecycle using production-like evidence.

### Audit Requirements

- Inventory every database, connection, replica, ORM, DBAL, query builder, raw SQL path, stored procedure, search index, and analytical sink.
- Review model or entity identity, equality, casts, custom types, value objects, nullability, defaults, timestamps, soft deletes, inheritance, and serialization.
- Audit relation ownership, cascade, orphan removal, pivot data, eager and lazy loading, global filters or scopes, and N+1 or Cartesian growth.
- Verify schema constraints for uniqueness, foreign keys, checks, exclusion, tenant boundaries, money precision, status transitions, and immutable facts.
- Test query plans and indexes with production-like cardinality, skew, selectivity, pagination depth, sort order, lock behavior, and replica lag.
- Audit optimistic and pessimistic locking, stale entities, unit-of-work boundaries, identity maps, detached objects, retries, and deadlock handling.

### Required Evidence

- Schema-to-model mapping and invariant matrix with database constraint evidence.
- Representative query plans and load measurements from production-like data.
- Concurrency tests for lost update, write skew, duplicate insertion, deadlock, and replica lag.

### Acceptance Criteria

- Critical invariants are enforced by durable constraints or equally strong atomic mechanisms, not only application callbacks.
- Query, locking, and pool behavior remains bounded under representative scale and concurrency.

## Phase 14 - Transactions, Isolation, Idempotency, Outbox, and Partial Failure

### Objective

Prove atomicity, replay safety, consistency, and recovery across database and external side-effect boundaries.

### Audit Requirements

- Map every critical mutation to transaction manager, connection, isolation level, timeout, retry policy, lock order, and commit boundary.
- Verify framework transaction helpers, nested transactions, savepoints, multiple connections, callback timing, exception conversion, and rollback semantics.
- Test lost update, write skew, phantom, uniqueness race, duplicate request, deadlock, timeout, process crash, and client disconnect.
- Design idempotency with authenticated scope, request fingerprint, atomic ownership, in-progress state, durable result, expiry, retry, and conflict behavior.
- Use transactional outbox, inbox, CDC, or an equivalent proven design when database state and messages or external effects must agree.
- Define reconciliation and compensating actions for payments, email, object storage, search indexing, webhooks, and other non-transactional effects.

### Required Evidence

- Critical-flow transaction and side-effect matrix with every crash point identified.
- Concurrent and replay test evidence around pre-commit, commit, and post-commit boundaries.
- Outbox, inbox, reconciliation, and manual recovery evidence for partial failures.

### Acceptance Criteria

- A retry, duplicate delivery, timeout, or process crash cannot silently duplicate or lose a critical business effect.
- Every non-atomic cross-system flow has detectable divergence and a tested recovery procedure.

## Phase 15 - Queues, Messenger, Horizon, Scheduling, Cron, and Background Work

### Objective

Prove delivery, retry, ordering, deduplication, resource, deployment, and recovery behavior for all asynchronous work.

### Audit Requirements

- Inventory every queue, transport, topic, subscription, failed transport, Horizon supervisor, Messenger worker, scheduler, cron, batch, and external trigger.
- Verify message schema, serialization, versioning, tenant and actor context, authorization, idempotency key, correlation, trace, and sensitive-data policy.
- Audit acknowledgement timing, visibility timeout, retry schedule, max attempts, backoff, jitter, dead-letter handling, poison-message quarantine, and replay approval.
- Test worker crash before and after side effects, broker redelivery, reordered events, duplicates, delayed messages, stale messages, and schema mismatch.
- Review scheduler overlap, lock TTL, leader election, clock skew, missed runs, catch-up, DST, long tasks, and multi-replica execution.
- Verify bounded concurrency, prefetch, memory, database pool pressure, backpressure, graceful drain, worker replacement, and deployment compatibility.

### Required Evidence

- Async topology and message-contract matrix with owner, retry, DLQ, and recovery path.
- Crash, duplicate, reorder, poison, replay, shutdown, and mixed-version worker test evidence.
- Worker and scheduler rollout evidence tied to artifact revision and queue depth.

### Acceptance Criteria

- At-least-once delivery and retries do not violate business invariants or leak tenant context.
- Workers can be drained, replaced, replayed, and recovered without silent loss or uncontrolled duplication.

## Phase 16 - Cache, Sessions, Locks, Files, Object Storage, and Search

### Objective

Audit derived state, distributed coordination, storage authority, invalidation, isolation, and recovery.

### Audit Requirements

- Inventory application cache, HTTP cache, session cache, tag cache, ORM cache, rate-limit state, distributed locks, filesystems, object stores, and search indexes.
- Verify cache keys include every authorization, tenant, locale, currency, feature, schema, and representation dimension that changes a result.
- Audit TTL, invalidation, stampede control, stale behavior, negative caching, serialization compatibility, poisoning, and regional consistency.
- Review session storage availability, consistency, locking, fixation resistance, serialization, failover, expiry, and deployment compatibility.
- Treat distributed locks as leases; verify ownership, renewal, expiry, fencing, clock assumptions, split brain, and stale-owner behavior.
- Audit file and object authorization, namespace isolation, signed URL scope, retention, versioning, encryption, malware handling, consistency, and restore.
- Verify search indexing authority, tenant filters, deletion propagation, stale results, reindex, alias cutover, and reconciliation.

### Required Evidence

- Cache, session, lock, storage, and search authority matrix.
- Cross-tenant, stale-cache, stampede, lease-expiry, failover, deletion, and reindex tests.
- Restore and reconciliation evidence for authoritative and derived stores.

### Acceptance Criteria

- Derived state cannot grant access, cross tenant boundaries, or become an untracked source of truth.
- Lease expiry, cache loss, storage failover, or search lag degrades safely and is observable.

## Phase 17 - Long-Lived Runtimes, State Reset, Fibers, Event Loops, and Concurrency

### Objective

Prove that worker reuse and concurrent execution do not leak request state, exhaust resources, or violate lifecycle assumptions.

### Audit Requirements

- Inventory PHP-FPM, RoadRunner, Swoole, OpenSwoole, FrankenPHP, Laravel Octane, ReactPHP, Amp, Messenger, queue, and custom daemon processes.
- Classify static, global, singleton, service, container, connection, logger, locale, auth, tenant, tracing, and temporary-file state by lifetime.
- Verify reset hooks, scoped services, container reset, request cleanup, transaction cleanup, connection health, temporary resource cleanup, and memory limits.
- Audit Fiber and coroutine cancellation, suspension, context propagation, exception handling, concurrent mutation, synchronization, and unsafe shared objects.
- Review event-loop blocking, CPU work, filesystem and network calls, DNS, subprocesses, database clients, backpressure, bounded queues, and starvation.
- Test sequential cross-user requests on one worker, concurrent requests, cancellation, timeout, worker crash, max-request recycle, and deployment drain.

### Required Evidence

- Runtime and state-lifetime matrix for every process model.
- Cross-request leakage, concurrency, cancellation, blocking, memory-growth, and recycle test evidence.
- Worker drain and replacement evidence for deployments and emergency revocation.

### Acceptance Criteria

- No request, user, tenant, locale, credential, transaction, or trace state survives beyond its authorized lifetime.
- Concurrency and long-lived execution remain bounded, cancellable, observable, and safely replaceable.

## Phase 18 - External HTTP, Webhooks, Email, Payments, Storage, and Provider Resilience

### Objective

Audit outbound trust, timeout, retry, identity, reconciliation, and degraded behavior for every external dependency.

### Audit Requirements

- Inventory every HTTP client, SDK, payment provider, mail service, object store, identity provider, search service, analytics sink, and custom integration.
- Verify connect, TLS, pool, request, response, total, and queue timeout budgets plus cancellation and deadline propagation.
- Audit retry eligibility, backoff, jitter, maximum attempts, retry budget, nested retries, circuit breaking, bulkheads, rate limits, and load shedding.
- Validate TLS trust, hostname, certificate rotation, mTLS identity, DNS, redirect policy, proxy use, credential scope, and SSRF resistance.
- For inbound webhooks, verify raw-body signatures, canonicalization, timestamp, replay window, key rotation, event identity, ordering, and idempotency.
- For payments and other irreversible effects, prove state-machine transitions, duplicate handling, asynchronous confirmation, refunds, disputes, and reconciliation.

### Required Evidence

- Dependency contract matrix with owner, timeout, retry, credential, data, SLO, and degraded mode.
- Slow, unavailable, malformed, replayed, rotated-key, rate-limited, and partial-success test evidence.
- Provider reconciliation and manual recovery evidence for irreversible effects.

### Acceptance Criteria

- A slow or failing provider cannot exhaust the service or create uncontrolled duplicate side effects.
- Every externally confirmed business state can be reconciled against an authoritative provider record.

## Phase 19 - Application Security, Injection, XSS, CSRF, SSRF, Deserialization, and Abuse

### Objective

Identify and verify controls for attacker-controlled data, dangerous interpreters, privilege boundaries, and resource abuse.

### Audit Requirements

- Map untrusted data into SQL, shell, template, HTML, URL, header, log, file path, regex, expression language, LDAP, XML, YAML, CSV, and mail contexts.
- Verify parameterization, contextual encoding, autoescape boundaries, trusted HTML handling, CSP, sanitization, header safety, and formula-injection controls.
- Audit CSRF for browser-authenticated mutations, SameSite assumptions, CORS, origin checks, login CSRF, logout CSRF, and token lifecycle.
- Audit SSRF through URL fetchers, previews, webhooks, importers, redirects, DNS rebinding, alternate IP syntax, metadata services, and internal protocols.
- Reject unsafe native deserialization, object injection, PHAR metadata abuse, untrusted YAML tags, XML entities, dynamic class resolution, and gadget chains.
- Test resource abuse through expensive regex, deep structures, large collections, decompression, image processing, exports, search, pagination, and concurrent requests.
- Review debug routes, profiler, Telescope, Horizon, Pulse, Ignition, Symfony profiler, phpinfo, stack traces, source maps, and secret exposure.

### Required Evidence

- Untrusted-source-to-dangerous-sink matrix with control and test evidence.
- Exploit-oriented negative tests for injection, XSS, CSRF, SSRF, deserialization, traversal, and resource exhaustion.
- Production evidence that debug and diagnostic surfaces are inaccessible or appropriately protected.

### Acceptance Criteria

- No attacker-controlled value reaches an interpreter, privileged sink, or internal network target without a verified control.
- Malformed or intentionally expensive input is rejected within bounded CPU, memory, time, and downstream cost.

## Phase 20 - Uploads, Downloads, Archives, Media, Documents, and Filesystem Boundaries

### Objective

Prove authorization, parsing safety, storage integrity, isolation, and lifecycle for attacker-controlled files and generated artifacts.

### Audit Requirements

- Inventory uploads, direct-to-storage flows, imports, exports, archives, images, video, audio, PDF, office documents, CSV, temporary files, and generated downloads.
- Verify authentication, authorization, tenant namespace, size, count, filename, extension, MIME, magic bytes, parser limits, and quarantine before use.
- Audit traversal, symlink, race, overwrite, executable placement, public exposure, signed URL scope, response headers, content sniffing, and disposition.
- Test zip slip, decompression bombs, nested archives, malformed media, parser vulnerabilities, image metadata, macro content, and formula injection.
- Verify asynchronous scanning and processing state, duplicate callbacks, timeout, worker crash, partial files, cleanup, retention, deletion, and legal hold.
- Audit export authorization at generation and download time, snapshot consistency, row limits, sensitive fields, watermarking, expiry, and audit trail.

### Required Evidence

- File-flow matrix from ingress through scanning, processing, storage, delivery, retention, and deletion.
- Malicious-file, traversal, archive-bomb, parser-crash, duplicate-callback, and unauthorized-download tests.
- Cleanup, retention, deletion, restore, and legal-hold evidence.

### Acceptance Criteria

- Untrusted files cannot execute, escape their namespace, exhaust processing, or become publicly accessible by accident.
- Every generated or stored artifact has explicit authority, integrity, retention, and recovery behavior.

## Phase 21 - PHP-FPM, OPcache, JIT, Capacity, and Resource Exhaustion

### Objective

Measure and bound process, pool, cache, CPU, memory, connection, and downstream capacity under realistic and hostile load.

### Audit Requirements

- Inventory FPM pools, process manager mode, child limits, spare settings, request limits, timeouts, slow logs, termination behavior, and status exposure.
- Verify OPcache memory, interned strings, validation, preload, file cache, huge pages, deployment invalidation, stale code risk, and emergency reset.
- Treat JIT as a measured workload-specific choice; compare correctness, startup, CPU, memory, latency, and observability with and without it.
- Measure application memory, peak request memory, leak-like growth, fragmentation, worker recycling, queue memory, serialization size, and large-response behavior.
- Model FPM, queue, web server, database, Redis, HTTP client, and provider pool sizes together to prevent multiplicative overload.
- Run cold, burst, sustained, soak, failover, dependency-slowdown, large-payload, expensive-query, and malicious-input tests.

### Required Evidence

- Capacity model with arrival rate, concurrency, service time, queue depth, pool limits, memory, and headroom.
- FPM, OPcache, JIT, long-lived worker, and dependency-saturation measurements.
- Load, burst, soak, failover, overload, and recovery test evidence.

### Acceptance Criteria

- Resource limits, queues, timeouts, and load shedding fail predictably before host or dependency collapse.
- Deployment and OPcache transitions cannot serve an untracked mixture of old code, new code, and stale configuration.

## Phase 22 - Observability, Logging, Tracing, Metrics, Health, and Privacy

### Objective

Prove that operators can detect, localize, explain, and recover from user-visible and integrity failures without leaking sensitive data.

### Audit Requirements

- Define SLI and SLO for availability, latency, correctness, freshness, durability, queue lag, authentication, critical flows, and recovery.
- Correlate release, artifact, commit, runtime, host, pool, worker, request, trace, user, tenant, job, message, and schema identities where allowed.
- Audit structured logs, exception chains, context propagation, sampling, cardinality, retention, access, redaction, and tamper resistance.
- Instrument HTTP, console, queue, scheduler, database, cache, external calls, file processing, business transitions, retries, and reconciliation.
- Separate process liveness, traffic readiness, dependency status, and degraded business capability; prevent health endpoints from leaking secrets.
- Test alert routing, deduplication, inhibition, threshold rationale, runbook quality, on-call ownership, and behavior during telemetry backend failure.

### Required Evidence

- SLI, SLO, dashboard, alert, owner, and runbook matrix.
- Trace or correlation evidence for at least one critical synchronous and asynchronous flow.
- Redaction tests and telemetry-backend failure behavior.

### Acceptance Criteria

- A critical failure can be tied to a release, code path, dependency, tenant-safe context, and recovery action.
- Telemetry does not expose credentials, session identifiers, secrets, payment data, sensitive files, or unnecessary personal data.

## Phase 23 - Testing, Static Analysis, Mutation, Contracts, Security, Load, and Recovery

### Objective

Build a risk-driven verification matrix that proves behavior across runtime modes, framework paths, failures, and releases.

### Audit Requirements

- Inventory PHPUnit, Pest, Codeception, Behat, Panther, browser, API, integration, database, queue, contract, property, fuzz, and end-to-end tests.
- Run PHPStan or Psalm, framework extensions, coding standards, deprecation checks, architecture rules, dependency checks, and secret scanning at justified strictness.
- Use mutation testing on critical business, authorization, validation, idempotency, transaction, and recovery logic where it adds signal.
- Verify tests against supported PHP versions, framework lines, database engines, cache and queue backends, FPM and long-lived runtimes, and deployment modes.
- Include malformed, hostile, concurrent, timeout, duplicate, replay, stale-state, crash, shutdown, mixed-version, restore, and rollback scenarios.
- Track flaky tests, quarantine ownership, retry policy, coverage gaps, production incident regressions, and acceptance threshold rationale.

### Required Evidence

- Risk-to-test matrix linked to critical flows and findings.
- Supported runtime and dependency test matrix with exact versions and backends.
- Raw results for static, unit, integration, contract, security, load, migration, restore, and rollback checks.

### Acceptance Criteria

- Every P0 and P1 control has a deterministic automated test or a documented stronger verification method.
- A green suite is not accepted when the relevant runtime, backend, failure mode, or release transition was not exercised.

## Phase 24 - Production Build, Images, Packaging, and Immutable Artifacts

### Objective

Prove that the reviewed source produces one reproducible, minimal, immutable, identifiable, and runnable production artifact.

### Audit Requirements

- Build from a clean checkout with pinned PHP, Composer, extensions, operating system packages, frontend toolchain, and generation steps.
- Install production dependencies with lockfile enforcement, controlled scripts and plugins, optimized autoloading, and no hidden development packages.
- Generate and verify caches, compiled containers, optimized routes, assets, translations, proxies, metadata, and frontend bundles in a controlled stage.
- Audit container base image, FPM and web server config, non-root execution, filesystem permissions, writable paths, capabilities, health, and signal handling.
- Embed or expose release identity, dependency inventory, build metadata, schema compatibility, and artifact digest without leaking secrets.
- Scan, sign, attest, and store the exact artifact; deploy the same digest across environments without rebuilding.

### Required Evidence

- Clean build transcript, lockfile verification, artifact digest, SBOM, signature, and provenance.
- Artifact inventory proving expected code, dependencies, extensions, config, caches, and absence of development tools or secrets.
- Smoke and critical-flow results from the packaged artifact, not a source checkout.

### Acceptance Criteria

- One immutable digest is traceable to source, toolchain, dependencies, tests, deployment, telemetry, and rollback.
- Production does not depend on mutable source mounts, runtime dependency installation, or manual cache generation.

## Phase 25 - CI/CD, Repository Trust, Credentials, Provenance, and Promotion

### Objective

Audit the delivery system as a privileged production control plane with explicit trust, isolation, and evidence.

### Audit Requirements

- Map repository, branch protection, review, CODEOWNERS, tag, release, runner, action, plugin, cache, artifact store, registry, deployer, and environment trust boundaries.
- Separate untrusted pull-request and fork execution from secrets, signing keys, package publication, production networks, and deployment credentials.
- Pin third-party actions and images immutably, verify downloads, lock dependencies, protect caches, and constrain Composer scripts and plugins.
- Prefer short-lived scoped identity such as OIDC; audit approval, separation of duties, break-glass, rotation, revocation, and audit trails.
- Build once, verify once, sign once, and promote the same artifact digest through environments with policy checks and explicit approvals.
- Verify SBOM, provenance, signature, vulnerability policy, waiver ownership, expiry, revocation, and trusted rebuild procedures.

### Required Evidence

- CI/CD trust-boundary and credential matrix.
- Run-to-artifact-to-deployment provenance for a representative release.
- Untrusted-change, cache-poisoning, credential-revocation, artifact-substitution, and trusted-rebuild test evidence.

### Acceptance Criteria

- Untrusted code cannot obtain production authority, signing material, or trusted artifact status.
- Every deployed revision is an approved, verified, immutable artifact with a known rollback target.

## Phase 26 - Database Migrations, Backfills, Mixed Versions, and Schema Recovery

### Objective

Prove forward-compatible schema evolution, bounded data transformation, observability, repair, and recovery during real deployments.

### Audit Requirements

- Inventory Laravel, Doctrine, Phinx, custom SQL, online-schema, backfill, data-fix, trigger, view, function, and search-index changes.
- Classify additive, compatibility, destructive, long-running, locking, rewrite, backfill, and irreversible operations by engine and data scale.
- Use expand-and-contract sequencing so old and new application or worker versions can coexist through rollout and rollback windows.
- Verify defaults, nullability, indexes, constraints, generated values, trigger behavior, ORM metadata, serialization, and read or write compatibility.
- Design resumable, idempotent, rate-limited, observable backfills with checkpoints, verification queries, pause, retry, and reconciliation.
- Define rollback, forward repair, point-in-time recovery, data correction, and manual intervention for every migration failure mode.

### Required Evidence

- Migration compatibility matrix across old app, new app, old worker, new worker, and schema states.
- Production-like execution, lock, duration, backfill, pause, resume, and verification evidence.
- Restore, forward-repair, and data-reconciliation exercise evidence.

### Acceptance Criteria

- No rollout or rollback window exposes an application version to an incompatible schema.
- Long-running and irreversible data changes have bounded impact, resumability, verification, and recovery.

## Phase 27 - Rollout, Worker Reload, OPcache Transition, Rollback, Forward Repair, and Restore

### Objective

Prove that releases transition all process types, caches, code, configuration, traffic, and schema safely and reversibly.

### Audit Requirements

- Inventory web, FPM, Octane, RoadRunner, Swoole, Messenger, Horizon, queue, scheduler, cron, CLI, migration, websocket, and maintenance processes.
- Define release order for artifact, configuration, secrets, caches, OPcache, web traffic, workers, schedulers, migrations, and external contracts.
- Verify graceful drain, worker replacement, max lifetime, queue compatibility, in-flight request behavior, session continuity, and connection handling.
- Use canary or staged rollout with explicit cohort, metrics, error budget, business guardrails, observation window, abort criteria, and accountable owner.
- Separate application rollback, configuration rollback, traffic rollback, worker rollback, schema rollback, forward repair, and data reconciliation.
- Exercise isolated backup restore, point-in-time recovery, dependency recovery, queue replay, and service restart against declared RPO and RTO.

### Required Evidence

- Release state machine and process replacement matrix.
- Canary, mixed-version, drain, OPcache, worker reload, rollback, and forward-repair evidence.
- Isolated restore evidence with measured RPO, RTO, integrity, and reconciliation.

### Acceptance Criteria

- No untracked old code, stale OPcache, old worker, incompatible message, or stale configuration remains after release completion.
- Rollback and restore are executable tested procedures, not assumptions in documentation.

## Phase 28 - Incident Mode, Webshells, Credential Compromise, Corruption, and Trusted Rebuild

### Objective

Provide a separate evidence-preserving workflow for active compromise, integrity loss, destructive failure, and unsafe uncertainty.

### Audit Requirements

- Enter INCIDENT mode for active exploitation, webshell or unknown executable code, credential theft, signing compromise, data corruption, destructive migration, or uncertain production integrity.
- Preserve logs, process state, filesystem metadata, artifacts, database evidence, queue state, cloud audit records, deployment history, and a timestamped action log.
- Contain through traffic restriction, write freeze, worker pause, credential revocation, session invalidation, key rotation, isolation, and known-good failover as appropriate.
- Do not clean an untrusted host in place and call it recovered; identify persistence, initial access, lateral movement, affected identities, data impact, and scope.
- Rebuild from reviewed source, trusted dependencies, clean toolchains, fresh infrastructure, rotated secrets, verified migrations, and signed immutable artifacts.
- Validate data, object storage, backups, queues, search indexes, caches, sessions, external providers, and audit trails before restoring normal service.

### Required Evidence

- Incident timeline, evidence inventory, chain of custody, containment decisions, scope, and identity-revocation record.
- Known-good source, dependency, toolchain, artifact, infrastructure, and restore provenance.
- Post-rebuild integrity, authorization, recovery, reconciliation, and monitoring evidence.

### Acceptance Criteria

- Service is not declared recovered while code, credentials, data, hosts, or artifact provenance remain untrusted.
- Recovery removes persistence and root cause, restores known-good state, and adds tested recurrence controls.

## Phase 29 - Lifecycle, Major Upgrades, Legacy Modernization, and Decommissioning

### Objective

Plan supported-version operation, framework and runtime migration, compatibility, rollback, and retirement without hidden risk.

### Audit Requirements

- Track PHP, framework, Composer, extensions, database drivers, operating systems, web servers, libraries, and services against official support windows.
- Inventory deprecated PHP features, framework APIs, recipes, bundles, packages, annotations, configuration formats, and behavioral changes.
- For Laravel major upgrades, verify PHP requirements, first-party package support, skeleton changes, auth, queue, cache, database, test, and deployment compatibility.
- For Symfony major or LTS migrations, verify recipes, Flex, bundle support, deprecations, container, security, serializer, Messenger, Doctrine, and Runtime changes.
- Run dual-line compatibility tests, representative data migrations, mixed-version deployment, performance comparison, canary, rollback, and forward repair.
- Remove abandoned packages, insecure plugins, dead routes, debug tools, unused credentials, obsolete infrastructure, and unsupported runtime paths with evidence.

### Required Evidence

- Support and upgrade matrix with owner, deadline, blockers, compatibility evidence, and rollback.
- Dual-version build, test, data, load, deployment, and recovery evidence.
- Decommission evidence for code, routes, packages, secrets, data, workers, infrastructure, and observability.

### Acceptance Criteria

- No unsupported or abandoned component remains on a critical production path without an approved, time-bound mitigation.
- Upgrade and retirement plans preserve data, contracts, authority, operations, and a tested recovery path.

## Mandatory Evidence Matrices

Produce every matrix below. Mark unknown cells `UNVERIFIED`; do not omit rows because evidence is unavailable.

| ID | Matrix | Minimum required columns |
| --- | --- | --- |
| M1 | Source, runtime, and artifact identity | component; source commit; build PHP; runtime PHP; SAPI; extensions; artifact digest; deployment revision; evidence |
| M2 | Supported execution modes | mode; binary; INI; extensions; config; lifecycle; owner; test; support status |
| M3 | Composer and supply chain | package or tool; source; version; trust; script or plugin; vulnerability; waiver; expiry; evidence |
| M4 | Routes, commands, messages, and authority | surface; input; authentication; authorization; tenant; transaction; idempotency; rate limit; test |
| M5 | Authentication and account lifecycle | flow; credential; expiry; rotation; revocation; MFA; recovery; abuse control; evidence |
| M6 | Data, ORM, schema, and invariants | entity or table; authority; tenant key; invariant; constraint; concurrency; retention; recovery |
| M7 | Transactions and external effects | flow; database boundary; isolation; idempotency; external effect; crash points; reconciliation; owner |
| M8 | Queues, workers, and schedulers | job or message; transport; delivery; retry; DLQ; ordering; deduplication; concurrency; shutdown; recovery |
| M9 | Caches, sessions, locks, files, and search | store; authority; key or namespace; isolation; consistency; expiry; invalidation; restore; test |
| M10 | Dependencies, limits, and degraded modes | dependency; owner; credential; timeout; retry; rate limit; capacity; failure mode; fallback; SLO |
| M11 | Release, migration, rollback, and restore | change; compatibility window; order; canary; abort; rollback; forward repair; RPO; RTO; evidence |
| M12 | Findings, fixes, and residual risk | finding; severity; evidence; root cause; fix; test; rollout; owner; deadline; residual risk; status |

## Mandatory Adversarial and Failure Scenarios

Execute or faithfully simulate all applicable scenarios. For every skipped scenario, record the reason, risk, owner, and compensating evidence.

1. A second authenticated tenant requests, mutates, exports, or downloads another tenant's resource through direct and indirect identifiers.
2. Two clients submit the same critical mutation concurrently with and without the same idempotency key.
3. The process crashes before database commit, during commit uncertainty, and after commit but before the response or message acknowledgement.
4. A queue message is duplicated, reordered, delayed, replayed after DLQ, and consumed by old and new worker versions.
5. A scheduled task runs twice, misses a run, loses its lock, exceeds lock TTL, and overlaps across replicas.
6. The database becomes slow, rejects connections, returns deadlocks, loses a primary, or exposes replica lag during a critical flow.
7. Redis or session storage becomes unavailable, evicts keys, returns stale data, or fails over during authentication and authorization.
8. An external provider times out, rate-limits, returns malformed success, duplicates a webhook, rotates keys, and confirms a side effect late.
9. A user logs out or is suspended while sessions, API tokens, queued jobs, signed URLs, and long-running exports still exist.
10. Two sequential requests from different users and tenants execute on the same long-lived worker and exercise locale, auth, tracing, and singleton state.
11. A large, deeply nested, compressed, malformed, or parser-hostile payload targets JSON, XML, YAML, archive, image, PDF, CSV, and regex paths.
12. A URL importer or webhook target uses redirects, DNS rebinding, alternate IP syntax, internal hostnames, and cloud metadata addresses.
13. A deployment occurs with old FPM children, stale OPcache, old queue workers, warmed new caches, mixed schema, and in-flight requests.
14. A secret, session key, webhook key, OAuth key, or signing key rotates while old and new processes coexist.
15. The application receives SIGTERM during an HTTP mutation, queue side effect, scheduled job, migration, file conversion, and export.
16. A migration is paused, retried, partially applied, rolled back at application level, and followed by a forward repair.
17. A cache key, session payload, queued message, or serialized object produced by an old release is consumed by a new release and vice versa.
18. A restore is performed in isolation from backup and point-in-time logs, then validated for authorization, integrity, queue state, files, and search.
19. A vulnerable dependency, malicious Composer plugin, poisoned CI cache, substituted artifact, or compromised deployment credential is detected.
20. An active webshell or unknown executable file is discovered on a production host while code, credentials, and data integrity are uncertain.

## Severity and Release Blocking

| Severity | Meaning | Default release effect |
| --- | --- | --- |
| P0 | Active compromise, catastrophic integrity or authorization failure, unrecoverable loss risk, or unsafe production state. | Stop rollout or traffic, enter INCIDENT mode, contain immediately. |
| P1 | High-confidence critical exploit, cross-tenant access, major data loss or duplication, broken recovery, or severe availability risk. | Block release until fixed and verified; require accountable exception only under emergency governance. |
| P2 | Material defect with bounded impact, missing defense, compatibility risk, or operational weakness. | Fix before release or accept with owner, deadline, monitoring, and compensating control. |
| P3 | Low-impact weakness, maintainability issue, optimization, or evidence improvement. | Track with justified priority and acceptance criteria. |

- Any unknown on a critical trust, authorization, transaction, migration, or recovery path is release-blocking until verified or explicitly risk-accepted by the accountable authority.
- Severity is based on realistic impact and exploitability, not code style, finding count, or remediation effort.

## Repair and Verification Workflow

1. Reproduce or establish the finding with the strongest available evidence and preserve a minimal failing case.
2. Identify root cause, affected trust boundary, invariant, process type, data, tenant, release, and failure window.
3. Design the smallest complete fix that removes the cause without hiding the symptom or weakening another control.
4. Add deterministic regression, negative, concurrent, failure, migration, or recovery tests appropriate to the risk.
5. Re-run targeted checks, then the relevant framework, integration, security, load, migration, and packaging suites.
6. Build the production artifact from a clean checkout and verify its digest, contents, runtime compatibility, and release metadata.
7. Deploy through the intended path with canary or staged guardrails, complete process replacement, and telemetry correlation.
8. Verify user-visible behavior, invariants, authorization, tenant isolation, side effects, queues, data, health, and rollback conditions.
9. Update the finding record with evidence, residual risk, owner, operational action, expiry, and final status.

## Production Readiness Checklist

- [ ] Source, PHP, SAPI, extensions, dependencies, artifact, deployment, schema, and running process are traceably identified.
- [ ] Every supported execution mode uses an approved runtime, INI, extension set, configuration, lifecycle, and test matrix.
- [ ] Composer lockfile, repositories, scripts, plugins, platform requirements, SBOM, signatures, and provenance are verified.
- [ ] Framework routes, containers, middleware, policies, firewalls, queues, schedulers, caches, and debug surfaces are proven from the production artifact.
- [ ] Authentication, account lifecycle, authorization, ownership, tenancy, administration, and break-glass paths pass negative tests.
- [ ] Critical data invariants, transaction boundaries, idempotency, outbox or inbox, and reconciliation are verified under concurrency and crash.
- [ ] Queue, scheduler, cache, session, lock, storage, search, and external-provider failure behavior is bounded and recoverable.
- [ ] Long-lived processes reset request state, bound concurrency, drain safely, and are fully replaced during release.
- [ ] Injection, XSS, CSRF, SSRF, deserialization, file parsing, traversal, and resource-abuse controls pass exploit-oriented tests.
- [ ] Capacity, pool, FPM, OPcache, worker, dependency, timeout, queue, and load-shedding limits are measured and monitored.
- [ ] Logs, traces, metrics, health, alerts, runbooks, and privacy controls explain critical failures without exposing sensitive data.
- [ ] CI isolates untrusted code, uses scoped credentials, builds once, promotes one immutable digest, and supports revocation and trusted rebuild.
- [ ] Migrations and backfills support mixed versions, bounded execution, pause, resume, verification, forward repair, and recovery.
- [ ] Rollout, OPcache transition, worker reload, rollback, forward repair, isolated restore, RPO, and RTO are exercised.
- [ ] No unresolved P0, unaccepted P1, expired waiver, unknown critical path, unsupported component, or untrusted production state remains.

## Definition of Done

1. Scope, assumptions, exclusions, environments, runtime modes, owners, and evidence limitations are explicit.
2. The intended source, build inputs, dependencies, generated code, artifact, deployment, schema, and running processes are cryptographically or operationally linked.
3. All critical HTTP, console, queue, scheduler, webhook, file, admin, support, and recovery surfaces are inventoried and authorized.
4. Business invariants survive concurrency, retry, duplicate delivery, partial failure, crash, timeout, cancellation, and mixed-version execution.
5. Database, cache, session, queue, storage, search, and external-provider authority and recovery behavior are proven.
6. Framework-specific lifecycle, proxy, container, policy, voter, middleware, worker, and cache semantics are tested from the production artifact.
7. Security boundaries withstand exploit-oriented negative tests and abusive resource patterns.
8. Capacity and reliability are measured under representative cold, burst, sustained, soak, slowdown, failover, and overload conditions.
9. Observability detects and explains correctness, security, availability, latency, queue, data, release, and recovery failures.
10. The production artifact is reproducible, minimal, immutable, signed or verified, promoted without rebuild, and safely replaceable.
11. Rollout, rollback, forward repair, credential revocation, isolated restore, incident containment, and trusted rebuild are executable and tested.
12. The final decision, residual risks, exceptions, owners, deadlines, evidence, and next verification date are recorded.

If any item is not proven, the audit is not complete. Mark it `UNVERIFIED`, explain the risk, and reflect it in the final readiness decision.

## Forbidden Shortcuts

- Do not infer production truth from source configuration, `.env.example`, local Docker, a green pipeline, or framework defaults.
- Do not treat `composer install`, unit tests, static analysis, or a successful HTTP smoke test as complete release proof.
- Do not assume CLI and FPM use the same PHP, INI, extensions, environment, working directory, user, or filesystem.
- Do not assume Laravel and Symfony annotations, attributes, policies, voters, middleware, listeners, or service definitions are effective without runtime-path evidence.
- Do not use UI restrictions, hidden fields, model fillable settings, route naming, or TypeScript types as authorization or validation.
- Do not add blind retries around non-idempotent operations, nested clients, transactions, or provider calls.
- Do not use cache, session, distributed lock, search index, queue, or object storage as an unexamined source of truth.
- Do not run destructive migrations, backfills, mass fixes, bulk replays, or cache flushes without approval, bounds, observability, and recovery.
- Do not claim zero downtime while old FPM children, stale OPcache, old workers, incompatible messages, or old schemas remain unverified.
- Do not expose debug, profiler, Horizon, Telescope, Pulse, Ignition, phpinfo, health detail, or stack traces as an operational shortcut.
- Do not deploy a rebuilt artifact under the same version, reuse mutable tags, install dependencies in production, or edit vendor code in place.
- Do not clean a compromised host in place and call it trusted, or restore from an unverified backup.
- Do not mark a finding fixed until the cause, regression test, packaged artifact, deployment path, telemetry, and rollback or recovery are verified.

## Mandatory Final Report

1. Executive summary with scope, system purpose, criticality, audit mode, dates, environments, and final decision.
2. Architecture and trust-boundary map covering users, tenants, frameworks, SAPIs, processes, data stores, queues, providers, CI/CD, and operators.
3. Verified source-to-runtime identity and support matrix for PHP, Laravel, Symfony, Composer, extensions, artifacts, schemas, and process types.
4. Evidence coverage with E0-E5 classification, missing access, unverified claims, assumptions, and resulting limitations.
5. Finding register ordered by P0-P3 with evidence, exploit or failure scenario, root cause, affected assets, and confidence.
6. Implemented and proposed repairs with exact code, configuration, schema, infrastructure, test, rollout, and operational changes.
7. Verification results for static, unit, integration, authorization, concurrency, queue, security, load, migration, rollout, rollback, and restore checks.
8. Production readiness checklist and Definition of Done with PASS, FAIL, UNVERIFIED, NOT_APPLICABLE, owner, and evidence.
9. Rollout, worker replacement, OPcache, migration, rollback, forward-repair, restore, incident, and trusted-rebuild runbooks.
10. Residual risk, approved exceptions, compensating controls, owners, deadlines, expiry, and next verification date.
11. Prioritized action plan separated into immediate containment, release blockers, near-term hardening, strategic modernization, and evidence debt.

## Final Decision Rules

| Decision | Required condition |
| --- | --- |
| READY | No unresolved P0 or P1, all critical paths proven, all mandatory controls pass, and rollback and restore are tested. |
| READY_WITH_CONDITIONS | No P0, no unaccepted P1, remaining bounded risks have owners, deadlines, monitoring, compensating controls, and expiry. |
| NOT_READY | A release blocker, unknown critical path, unsupported critical component, failed recovery proof, or material unowned risk remains. |
| INCIDENT | Active compromise, unsafe integrity uncertainty, destructive failure, or immediate containment and trusted rebuild is required. |

## Execution Order

1. Confirm authorization, safety limits, scope, environments, and evidence access.
2. Capture a read-only production snapshot and source-to-runtime identity before changing anything.
3. Map architecture, trust boundaries, process types, data authorities, critical flows, and invariants.
4. Audit runtime, dependencies, build, framework lifecycle, routes, authentication, authorization, and data correctness.
5. Audit asynchronous work, caches, storage, external dependencies, security sinks, performance, observability, and delivery.
6. Reproduce and prioritize findings, implement approved fixes, add tests, and rebuild one immutable artifact.
7. Verify packaged behavior, migration compatibility, staged rollout, complete process replacement, rollback, and isolated restore.
8. Issue the evidence-backed final report and readiness decision without hiding unknowns or residual risk.

Prioritize protection of human safety, confidentiality, authorization, tenant isolation, money, durable data, and recoverability before optimization or style. Prefer the smallest complete and verifiable correction over broad speculative rewrites.
