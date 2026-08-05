## Phase J - Authentication, Authorization, And Data Protection

Establish auth model: cookie, Identity, JWT bearer, OAuth2/OIDC, API key, mTLS, multiple schemes, fallback/default policy.

Check authentication: issuer/audience/signature/algorithm, key rotation, JWKS, exp/nbf/clock skew, refresh-token rotation/revocation/reuse detection, security stamp, session revocation, MFA, user enumeration. A valid signature is insufficient if the token is not intended for this API.

Every protected operation must independently prove: identity, policy/role/claim, ownership, tenant scope, resource state, and valid state transition. Test BOLA/IDOR, horizontal/vertical escalation, client-supplied tenant ID, unscoped queries, public exports, nested resources, stale rights. Role checks alone are insufficient when ownership or state matters.

Cookies: Secure, HttpOnly, SameSite, domain/path, expiration, session fixation, key ring, multi-replica.

Data Protection: where keys are stored, whether they survive restart, availability to all replicas, encryption at rest, application name/discriminator, rotation, permissions, backup/DR. An ephemeral key ring in production invalidates cookies, antiforgery, and protected payloads on restart.

CSRF/antiforgery: base the decision on the credential model. Do not disable antiforgery merely because an endpoint returns JSON. CORS is not authorization; check exact origin allowlist, credentials, wildcard, preflight, middleware order.

