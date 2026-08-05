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


