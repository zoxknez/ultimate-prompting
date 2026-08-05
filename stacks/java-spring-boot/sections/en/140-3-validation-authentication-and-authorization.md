## 3. Validation, Authentication, And Authorization

Treat every path/query/header/cookie/form/file/JSON payload, gRPC message, WebSocket message, webhook, queue message, scheduled input, configuration value, and generated value as untrusted. Validate type, format, enum, numeric/string bounds, Unicode normalization, object depth, collection count, unknown fields, file size, and semantic business rules. Bean Validation does not replace authorization or semantic validation. Explicitly map allowed DTO fields into domain updates to prevent mass assignment.

Audit registration/login, password hashing, reset/email verification, MFA, account lockout/rate limits, session fixation, cookie flags, OIDC/OAuth redirect URI/state/nonce/PKCE, JWT signature/issuer/audience/expiry/key rotation, refresh-token rotation/revocation/reuse detection, API keys, logout, active-session invalidation, and user enumeration. Use framework and identity-provider protocols; do not invent token or cryptographic formats.

Every protected operation must independently prove identity, authority/policy, ownership, tenant scope, resource state, and valid transition. Review `authorizeHttpRequests`, matcher ordering, method security, `@PreAuthorize`, custom `AuthorizationManager`, service-layer checks, repository filters, async executor security-context propagation, and message consumer actor context. Test BOLA/IDOR, horizontal/vertical escalation, UI-only checks, client-supplied tenant IDs, unscoped queries, public exports/downloads, nested-resource access, and stale privileges. Request authorization alone is insufficient for object ownership.

Favor explicit `permitAll` for intended public/static paths over bypassing the entire security chain, so security headers and other protections remain active. For browser cookie writes, verify CSRF, SameSite, origin/referrer or Fetch Metadata checks, and precise CORS credentials/origins. CORS is not authorization.

