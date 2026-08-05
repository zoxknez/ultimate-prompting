## Phase M - Idempotency, Duplicate Delivery, And Reconciliation

Assume retries, duplicate requests and process crashes will occur.

- Define idempotency key scope, request fingerprint, ownership, expiration and conflict behavior.
- Store idempotency claim and business result atomically when possible.
- Test duplicate requests before, during and after commit, including timeout after commit.
- Test duplicate queue messages, CDC events, webhooks and scheduled jobs.
- Use database constraints as the final defense against duplicate durable effects.
- Provide reconciliation and manual repair procedures for ambiguous outcomes.

