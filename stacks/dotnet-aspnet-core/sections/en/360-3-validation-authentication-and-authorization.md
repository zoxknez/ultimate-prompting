## 3. Validation, Authentication, And Authorization

Treat every input as untrusted. DTO binding is not authorization. Prevent over-posting with explicit mapping.

Audit Identity/login/password/MFA/lockout, cookie/session, OIDC/OAuth (redirect URI, state/nonce/PKCE), JWT (signature/issuer/audience/lifetime/clock skew/rotation), refresh tokens, API keys, logout, user enumeration.

Every protected operation must prove identity, policy, ownership, tenant, resource state, and valid transition. Find BOLA/IDOR, UI-only checks, client-supplied tenant, unscoped queries. Role alone is insufficient when ownership or state matters.

For cookie browser writes: antiforgery, SameSite, origin/Fetch Metadata, precise CORS. CORS is not authorization. The Data Protection key ring must be persisted and shared in multi-replica environments.

