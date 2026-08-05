## Phase 7 - Proxy, Rewrites, Redirects, And Headers

Treat Proxy or legacy Middleware as routing infrastructure, never as the sole security boundary.

### Audit Requirements

- Inventory proxy.ts, middleware.ts, matchers, negative matchers, locale logic, auth redirects, experiments, and bot handling.
- Verify version semantics, runtime constraints, API support, execution order, and platform routing interaction.
- Detect matcher gaps for encoded paths, alternate hosts, handlers, image routes, RSC requests, and slash variants.
- Validate host, forwarded host, protocol, origin, locale, tenant, and redirect target against trusted config.
- Prevent open redirect, loop, cache poisoning, header spoofing, auth confusion, and tenant crossover.
- Recheck authorization in the destination route, data layer, and mutation.

### Required Evidence

- Matcher truth table covering protected and excluded path classes.
- Observed routing order and effective response headers.
- Trusted proxy and host configuration evidence.
- Middleware-to-Proxy migration status where relevant.

### Mandatory Failure And Acceptance Tests

- Attempt protected paths through encoded, rewritten, alternate-host, prefetch, RSC, and direct API variants.
- Test untrusted Host, X-Forwarded-Host, Origin, and protocol combinations.
- Prove redirect targets cannot escape the allowlist or loop.
- Bypass Proxy in integration and prove the destination denies unauthorized access.

