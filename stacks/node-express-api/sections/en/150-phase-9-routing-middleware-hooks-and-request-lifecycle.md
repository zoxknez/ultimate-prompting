## Phase 9 - Routing, Middleware, Hooks, And Request Lifecycle

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Build an ordered graph for context, request ID, logging, security headers, CORS, parsers, raw body, auth, authorization, limits, validation, handlers, 404, and errors.
- Verify every public, authenticated, internal, admin, webhook, health, debug, and metrics route reaches intended controls.
- Detect middleware or hooks that neither terminate nor continue, call next twice, send twice, mutate shared state, or swallow errors.
- Verify raw-body capture occurs only where required and cannot bypass size, auth, or content-type controls.
- Audit route precedence, wildcard and parameter behavior, slash handling, case sensitivity, method fallbacks, and OPTIONS behavior.
- Ensure request-scoped cleanup executes on success, validation failure, error, timeout, abort, and shutdown.

### Required Evidence

- Produce and preserve the effective route and control matrix.
- Produce and preserve the middleware or hook order graph.
- Produce and preserve request lifecycle and cleanup traces.

### Mandatory Failure And Acceptance Tests

- Prove that every sensitive route reaches authentication and authorization.
- Prove that validation failure cannot skip audit logging.
- Prove that abort and timeout execute cleanup exactly once.

