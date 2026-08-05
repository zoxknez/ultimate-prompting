## Phase H - Architecture, Domain Boundaries And Invariants

- Map requests, websocket events, jobs, mailers, commands and one-off tasks through authentication, validation, authorization, domain logic, transaction, side effects and observability.
- Write critical business invariants explicitly and identify the database, application and reconciliation controls enforcing each one.
- Detect business logic hidden in callbacks, views, serializers, observers, concerns, controller filters and model validations.
- Flag circular dependencies, god objects, shared mutable state, implicit tenant scoping and side effects during object construction.
- Prefer explicit use-case or domain boundaries where they improve transaction, authorization and test clarity; do not add layers only for style.

