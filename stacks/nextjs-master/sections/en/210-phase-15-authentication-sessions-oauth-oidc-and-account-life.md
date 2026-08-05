## Phase 15 - Authentication, Sessions, OAuth/OIDC, And Account Lifecycle

Prove the complete identity lifecycle across browser, server, providers, sessions, devices, roles, revocation, and recovery.

### Audit Requirements

- Inventory login, registration, invitation, linking, reset, magic link, MFA, passkey, reauth, logout, and recovery.
- Verify issuer, audience, nonce, state, PKCE, redirect URI, token algorithm, clock skew, key rollover, and provider mix-up resistance.
- Review session storage, cookie flags, domain/path, rotation, fixation, expiry, concurrency, revocation, and rights propagation.
- Separate authentication from authorization and guard at the point of data use.
- Prevent enumeration, stuffing, reset replay, email-change takeover, unsafe linking, and stale privileged sessions.
- Ensure logout, disable, role/tenant removal, password change, and key rotation invalidate intended sessions and caches.

### Required Evidence

- Identity flow and session-state diagrams.
- Provider configuration and token-validation evidence.
- Cookie and session observations from real responses and storage.
- Revocation and rights-change propagation measurements.

### Mandatory Failure And Acceptance Tests

- Attempt login CSRF, state/nonce replay, redirect substitution, audience mismatch, and provider mix-up.
- Use a session after logout, password change, role removal, tenant removal, disable, and key rollover.
- Link identities with conflicting ownership and prevent takeover.
- Exercise parallel refresh or session rotation from multiple tabs and devices.

