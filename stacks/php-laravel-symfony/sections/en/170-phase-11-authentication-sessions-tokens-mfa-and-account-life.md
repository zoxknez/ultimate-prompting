## Phase 11 - Authentication, Sessions, Tokens, MFA, and Account Lifecycle

### Objective

Prove identity, session, credential, token, recovery, and account lifecycle controls across every application surface.

### Audit Requirements

- Inventory every guard, firewall, authenticator, provider, session store, API token, OAuth or OIDC client, passwordless flow, MFA method, and machine identity.
- Verify password hashing policy, rehash behavior, rate limits, credential stuffing defenses, breached-password handling, and secure recovery flows.
- Audit session fixation, regeneration, idle and absolute expiry, concurrent sessions, device revocation, cookie attributes, storage, and logout invalidation.
- Validate JWT, OAuth, and OIDC issuer, audience, algorithm, nonce, state, PKCE, key rotation, clock skew, refresh rotation, and replay handling.
- Audit MFA enrollment, challenge, recovery codes, trusted device, downgrade, factor replacement, step-up authentication, and support override.
- Review registration, email or phone verification, invitation, suspension, deletion, anonymization, export, reactivation, and ownership transfer.

### Required Evidence

- Authentication and account-state matrix for browser, API, console, worker, webhook, and machine clients.
- Negative tests for fixation, replay, revoked sessions, rotated keys, stale recovery links, and MFA downgrade.
- Credential and signing-key rotation evidence without forced unsafe downtime.

### Acceptance Criteria

- Revoked, expired, replayed, downgraded, or cross-account credentials cannot authenticate or preserve privilege.
- Recovery and support workflows are at least as strongly protected and audited as normal sign-in.

