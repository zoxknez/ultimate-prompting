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

