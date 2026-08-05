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

