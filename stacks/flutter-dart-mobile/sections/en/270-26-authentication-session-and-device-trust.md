## 26. Authentication, Session, And Device Trust

Authentication must survive hostile input, lifecycle interruption, token rotation, multi-device use, and account switching.

- Map sign-in, registration, verification, MFA, passkey, biometric unlock, recovery, refresh, logout, logout-all, device enrollment, and account deletion.
- Verify OAuth/OIDC authorization code with PKCE, redirect URI ownership, state, nonce, issuer, audience, signature, clock skew, token type, and key rotation.
- Store only necessary secrets using platform-appropriate protected storage; verify lock state, backup/restore, device migration, rooted/jailbroken behavior, and uninstall semantics.
- Audit refresh single-flight, token rotation, revocation, replay, concurrent 401 handling, stale request retry, background refresh, and session-expiry UX.
- Separate local biometric convenience from server authentication and authorization; define fallback, lockout, re-enrollment, and compromised-device response.
- Ensure logout and account switch clear memory, caches, databases, files, notifications, background work, realtime subscriptions, WebViews, and screenshots as required.
- Test duplicate callbacks, canceled browser login, wrong redirect, deep-link hijack, offline login, expired keys, changed password, revoked device, and old/new app versions.
- Do not log credentials, tokens, authorization codes, biometric results, recovery data, or sensitive identity claims.

