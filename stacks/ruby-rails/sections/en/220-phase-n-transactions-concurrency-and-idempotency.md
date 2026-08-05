## Phase N - Transactions, Concurrency And Idempotency

- Define transaction boundaries around business invariants, not controller shape or method length.
- Verify isolation level, lock order, lock timeout, deadlock retry, optimistic locking and `SELECT FOR UPDATE` semantics.
- Test lost update, write skew, duplicate submission, stale form, parallel workers and retry after unknown commit result.
- Use database constraints and atomic statements as the final enforcement layer for critical uniqueness and state transitions.
- Design idempotency keys with actor or tenant scope, request fingerprint, atomic reservation, result storage, expiry and mismatch rejection.
- Keep external side effects out of unprotected transaction gaps; use outbox, reconciliation or compensating action where needed.

