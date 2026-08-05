## Spring Security, Tenancy, And Privileged Access

### Effective Security Filter Chains

- Enumerate every `SecurityFilterChain`, matcher, order, authentication provider, filter, entry point, access-denied handler, session policy, CSRF rule, CORS rule, and exception path.
- Prove which chain protects every endpoint and management surface; test overlaps, gaps, fallback rules, dispatcher types, async dispatch, error dispatch, and forwarded requests.
- Compare method-security annotations and advisors with HTTP security; neither layer compensates for an unverified gap in the other.
- Test direct controller/service invocation, internal forwarding, scheduled invocation, message listeners, GraphQL resolvers, WebSocket messages, and non-HTTP entry points.
- Fail closed when authentication infrastructure, key discovery, policy data, tenant lookup, or authorization dependencies are unavailable unless a reviewed degraded mode exists.

### Authentication, Sessions, OAuth, And OIDC

- Audit password, MFA, passkey, API key, mTLS, service account, OAuth 2.0, OpenID Connect, SAML, LDAP, and custom authentication flows actually enabled.
- Verify issuer, audience, algorithm, key use, key rotation, clock skew, nonce, state, PKCE, redirect URI, token type, token binding where applicable, and logout semantics.
- For browser sessions, verify cookie scope, `Secure`, `HttpOnly`, `SameSite`, fixation protection, rotation, concurrency limits, idle and absolute expiry, remember-me, and server-side invalidation.
- Test revoked, expired, not-yet-valid, wrong-issuer, wrong-audience, wrong-tenant, wrong-client, downgraded, duplicated, and malformed credentials.
- Keep refresh tokens, client secrets, signing keys, session identifiers, and authentication traces out of logs, metrics, URLs, browser storage, and support exports.

### Object Authorization And Tenant Isolation

- Define authorization for action, resource, tenant, owner, state, relationship, field, and purpose; role checks alone are insufficient for object access.
- Test BOLA/IDOR by replacing identifiers, parent resources, tenant headers, claims, path variables, query parameters, batch items, exports, and indirect references.
- Enforce tenant constraints in every repository, query, cache key, message, file path, search index, event, async task, and administrative workflow.
- Verify tenant context cannot be supplied or overridden by an untrusted client unless independently bound to authenticated authority.
- Test context leakage through thread reuse, Reactor context, scheduled jobs, shared caches, pooled clients, retries, dead letters, logs, metrics, and traces.

### Administrative, Impersonation, And Break-Glass Paths

- Inventory admin endpoints, consoles, Actuator operations, support tools, data exports, replay tools, migrations, repair scripts, feature overrides, and emergency controls.
- Require stronger authentication, least privilege, purpose binding, approval where appropriate, time bounds, session separation, and tamper-evident audit records.
- For impersonation, preserve original actor, effective actor, reason, tenant, scope, start/end, approvals, and every action performed; never silently replace identity.
- Test confused-deputy paths where a privileged service performs an action using user-controlled identifiers, destinations, templates, queries, or callbacks.
- Verify break-glass credentials are recoverable, rotated after use, monitored, tested, and unavailable to normal application code or CI logs.

### Browser Security, CORS, CSRF, And Headers

- Verify CORS origins, methods, headers, credentials, preflight caching, wildcard behavior, proxy rewriting, and environment-specific origin lists.
- Apply CSRF protection to cookie-authenticated state changes, login, logout, token binding, and sensitive browser flows; document justified exemptions.
- Review CSP, HSTS, frame ancestors, content-type options, referrer policy, permissions policy, cache control, cross-origin policies, and error-page behavior.
- Test host-header injection, open redirects, origin confusion, DNS rebinding where local services exist, clickjacking, MIME confusion, and mixed-content paths.
- Do not expose tokens, secrets, internal topology, stack traces, user data, or privileged actions through generated documentation, Actuator, GraphiQL, Swagger UI, or debug pages.


