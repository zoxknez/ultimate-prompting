## Phase 13 - Server Actions, Forms, And Mutation Semantics

Treat every Server Action and form mutation as a privileged remote command with explicit identity, authorization, validation, transaction, idempotency, and recovery.

### Audit Requirements

- Inventory every use server function, exported action, bound action, form action, imperative call, and indirect reference.
- Authenticate and authorize inside the action using current server state; never trust hidden fields, bound IDs, client state, Proxy, or UI visibility.
- Validate structure, semantics, ownership, state transition, size, file content, rate, and business invariants.
- Define idempotency key, scope, duplicate response, expiry, and behavior across retry, navigation, timeout, disconnect, and crash.
- Use database constraints and transactions; coordinate external effects with outbox, reconciliation, or compensation.
- Review allowedOrigins, host/origin, body limits, encryption key behavior, rotation, and multi-instance compatibility.

### Required Evidence

- Action matrix with actor, tenant, schema, authz, transaction, idempotency, rate, cache effect, and owner.
- Constraint and transaction evidence for critical invariants.
- Origin, host, body-size, key, and multi-instance config evidence.
- Audit and reconciliation evidence for external effects.

### Mandatory Failure And Acceptance Tests

- Replay the same action before, during, and after commit, timeout, redirect, and restart.
- Change hidden IDs, tenant, role, price, status, and ownership fields.
- Submit concurrently from multiple tabs, devices, and actors against one invariant.
- Rotate or mismatch action encryption material and verify compatibility and recovery.

