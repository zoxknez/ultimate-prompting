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

