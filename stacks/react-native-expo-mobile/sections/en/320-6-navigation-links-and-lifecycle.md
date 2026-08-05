## 6. Navigation, Links, And Lifecycle

### 6.1 Navigation And Restoration
- Inventory Expo Router, React Navigation, native navigation, custom routing, modal routes, tabs, stacks, drawers, and nested state.
- Verify route params at runtime and never treat TypeScript route types as validation or authorization.
- Test cold start, warm start, background resume, killed-process restore, notification open, universal link, app link, custom scheme, and web URL entry.
- Prove protected routes re-evaluate session, tenant, resource ownership, and feature entitlement after restore and link handling.
- Audit duplicate navigation, stale navigation references, back behavior, modal dismissal, predictive back, state persistence, and versioned route migrations.
- Test old links against new binaries and OTA updates, and define safe handling for removed or renamed routes.

### 6.2 App Lifecycle And Process Death
- Model active, inactive, background, suspended, terminated, restored, locked-device, low-memory, and interrupted states per platform.
- Do not assume cleanup runs before process death, OS eviction, crash, force-stop, battery removal, or device reboot.
- Persist only the minimum recoverable state and validate every restored value against current identity, schema, permissions, and server truth.
- Test interrupted authentication, payment, upload, download, media, migration, sync, and background operations at every durable boundary.
- Audit listener registration and removal across Fast Refresh, navigation, foreground transitions, OTA reload, native restart, and logout.
- Define reconciliation after ambiguous completion where the client cannot know whether the backend committed the operation.

