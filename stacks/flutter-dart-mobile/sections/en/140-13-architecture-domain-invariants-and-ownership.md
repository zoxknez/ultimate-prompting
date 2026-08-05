## 13. Architecture, Domain Invariants, And Ownership

Judge architecture by preserved behavior, not by folder names or state-management branding.

- Map presentation, application, domain, data, platform, infrastructure, and integration responsibilities and actual dependency direction.
- Write explicit invariants for identity, authorization, money, inventory, quotas, ordering, status transitions, offline actions, synchronization, deletion, and recovery.
- Trace each critical journey from user input through state, repository, local cache, platform service, backend, persistence, telemetry, and displayed result.
- Verify ownership of mutable state, lifecycle, cancellation, retries, subscriptions, streams, controllers, caches, database handles, and platform resources.
- Detect business logic duplicated across widgets, view models, providers, blocs, repositories, backend clients, native code, and push handlers.
- Verify dependency inversion where it improves testability and platform isolation; reject ceremonial abstraction that hides behavior or error semantics.
- Identify god objects, circular dependencies, service-locator coupling, feature leakage, shared mutable models, implicit singletons, and cross-feature side effects.
- Verify platform-specific code is isolated behind explicit contracts with fallback, unsupported-state handling, tests, and observability.
- Do not refactor architecture broadly unless a confirmed risk, measurable outcome, compatibility plan, migration sequence, and rollback justify it.

