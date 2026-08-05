## 54. Mandatory Adversarial And Failure Scenarios

1. Change a resource identifier, route parameter, tenant, account, notification payload, or deep-link target and verify server and local isolation.
2. Tap a mutation repeatedly under slow network and verify one logical side effect, truthful UI state, idempotency, and telemetry.
3. Switch route, account, tenant, locale, or filter while requests and streams are active and verify stale work cannot mutate new state.
4. Kill the process during startup, database migration, write, upload, payment, synchronization, and update; verify recovery and invariant preservation.
5. Deliver duplicate, delayed, reordered, malformed, expired, wrong-account, and revoked-session push or realtime events.
6. Deny, restrict, limit, revoke, or change every material permission while the feature and application are active.
7. Run offline for a long period, change clock/timezone, queue conflicting operations from multiple devices, then reconnect and reconcile.
8. Return 401, 403, 409, 412, 429, 5xx, malformed, truncated, huge, slow, redirected, and timed-out network responses during critical journeys.
9. Feed malicious URLs, files, archives, media, JavaScript messages, platform-channel payloads, FFI inputs, paths, and filenames.
10. Exercise minimum, typical, latest, low-memory, low-storage, battery-restricted, accessibility, multi-window, and architecture variants.
11. Install every supported old version, create realistic data, upgrade through skipped versions, interrupt the upgrade, restore an old backup, and attempt downgrade.
12. Serve old web shell with new assets and new shell with old assets; test stale service workers, mixed CDN caches, and rollback.
13. Use old client/new server and new client/old server combinations with schema, feature flag, notification, and background-job overlap.
14. Simulate missing plugin, native library, symbol, hardware, entitlement, system service, keychain/keyring, browser capability, and distribution service.
15. Expire or revoke signing, push, TLS, identity, store, update, and telemetry credentials; verify alerts, containment, rotation, and continuity.
16. Trigger crash loops, memory growth, retry storms, reconnect storms, notification storms, large queues, large lists, and backend overload.
17. Restore from backup or trusted artifacts in an isolated environment and prove identity, data consistency, authorization, observability, and measured RPO/RTO.
18. Rebuild after a simulated compromised dependency or build runner and prove clean provenance, new signatures where required, artifact comparison, and revocation.

