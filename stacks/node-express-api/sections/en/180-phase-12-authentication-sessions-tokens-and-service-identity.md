## Phase 12 - Authentication, Sessions, Tokens, And Service Identity

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Audit registration, invitation, login, MFA, passkey, reset, recovery, linking, reauthentication, logout, and account closure.
- Verify password hashing parameters, policy, breached-password strategy, lockout, throttling, and enumeration resistance.
- For sessions, verify fixation resistance, rotation, secure cookie flags, durable store, tenant scope, expiry, and revocation.
- For JWT and OIDC, verify issuer, audience, algorithm allowlist, signature, key rotation, expiry, nonce, state, PKCE, and redirect URI.
- For refresh tokens, verify rotation, family tracking, reuse detection, session binding, and compromise response.
- For API keys and service identities, verify scope, hashing, display-once behavior, rotation, revocation, attribution, and rate limit.

### Required Evidence

- Produce and preserve the authentication-flow and credential matrix.
- Produce and preserve the session and token lifecycle table.
- Produce and preserve key rotation, revocation, and compromise evidence.

### Mandatory Failure And Acceptance Tests

- Prove that the session identifier rotates on privilege change.
- Prove that refresh-token reuse is detected and contained.
- Prove that wrong issuer, audience, algorithm, or key is rejected.

