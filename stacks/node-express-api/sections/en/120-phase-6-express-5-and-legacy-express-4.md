## Phase 6 - Express 5 And Legacy Express 4

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Identify the exact Express major and patch and compare behavior with supported Node and official migration guidance.
- For Express 5, verify rejected-promise forwarding, async handlers, error middleware, path syntax, body and query semantics, and removed APIs.
- For Express 4, inventory custom async wrappers, unhandled rejection paths, legacy middleware, and migration blockers.
- Review app, router, sub-app, mount path, parameter handler, and settings inheritance behavior.
- Verify error middleware has the correct signature, cannot double-send, and handles headers-already-sent safely.
- Audit trust proxy against the exact proxy-hop topology and prevent spoofing of IP, protocol, and host.

### Required Evidence

- Produce and preserve the Express version and migration matrix.
- Produce and preserve the middleware and router order graph.
- Produce and preserve trust-proxy and route regression evidence.

### Mandatory Failure And Acceptance Tests

- Prove that a rejected promise reaches the intended error handler once.
- Prove that spoofed forwarded headers do not change trusted identity.
- Prove that headers-already-sent and legacy wildcard paths terminate safely.

