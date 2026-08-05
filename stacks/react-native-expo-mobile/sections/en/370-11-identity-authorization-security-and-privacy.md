## 11. Identity, Authorization, Security, And Privacy

### 11.1 Authentication And Session Lifecycle
- Audit password, OAuth 2.0, OIDC, social login, magic link, device code, MFA, passkey, biometric unlock, API key, and enterprise identity flows actually present.
- Verify state, nonce, PKCE, redirect URI, issuer, audience, algorithm, key rollover, clock skew, and deep-link handoff.
- Define access-token, refresh-token, session, device-registration, biometric-gate, and local-unlock semantics separately.
- Test refresh races, replay, revocation, logout, password reset, account disablement, device loss, reinstall, restore, and account switching.
- Do not treat biometrics or device possession as server authorization unless the protocol explicitly proves that property.
- Prevent tokens and sensitive identity data from appearing in URL, logs, analytics, crash reports, clipboard, screenshots, backups, or bundle content.

### 11.2 Authorization, BOLA, And Tenant Isolation
- Create an authorization matrix for every read, mutation, upload, download, share, export, deep link, notification action, native capability, and background operation.
- Require server-side authorization for resource ownership, role, tenant, entitlement, subscription, and state transition.
- Test direct identifier substitution, stale cached permission, offline action replay, account switch, tenant switch, restored navigation, and notification action.
- Include tenant and authorization dimensions in local keys, cache keys, query keys, files, database rows, queues, logs, and telemetry.
- Audit admin, support, impersonation, family, delegated, shared-device, enterprise-managed, and break-glass flows.
- Verify logout and account deletion invalidate or remove every tenant-scoped artifact and pending operation.

### 11.3 Secure Storage, Cryptography, And Device Trust
- Inventory Keychain, Keystore, SecureStore, encrypted database, files, AsyncStorage, MMKV, preferences, cookies, WebView stores, logs, and backups.
- Classify every stored value by sensitivity, retention, backup eligibility, accessibility while locked, biometric requirement, sharing group, and deletion rule.
- Use platform cryptographic APIs and versioned envelopes; audit nonce uniqueness, key rotation, algorithm agility, migration, corruption, and recovery.
- Do not hardcode secrets, private keys, certificate pins, update signing keys, backend credentials, or privileged API tokens in client artifacts.
- Treat root, jailbreak, hooking, instrumentation, emulator, and tamper detection as risk signals, not infallible authorization controls.
- Test device migration, OS upgrade, reinstall, backup restore, key invalidation, biometric enrollment change, and secure hardware failure.

### 11.4 Privacy And Data Governance
- Map personal, sensitive, financial, health, child, location, biometric, advertising, diagnostics, and device data from collection to deletion.
- Verify consent, purpose limitation, data minimization, retention, export, deletion, access request, and regional transfer behavior.
- Reconcile actual SDK behavior with privacy policy, store declarations, Apple privacy manifests, required-reason APIs, and Google Play Data safety.
- Audit analytics, attribution, advertising, crash, support, experimentation, session replay, push, maps, and payment SDK collection.
- Provide user-visible controls where required and prove opt-out prevents collection rather than only hiding UI.
- Test deletion and logout across local storage, native SDK stores, WebView stores, pending uploads, caches, push registration, and backend state.

