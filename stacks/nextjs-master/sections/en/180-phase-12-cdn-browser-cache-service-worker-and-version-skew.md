## Phase 12 - CDN, Browser Cache, Service Worker, And Version Skew

Audit caches outside application code and prove coherent behavior across deploys, regions, tabs, browsers, and offline states.

### Audit Requirements

- Inventory CDN rules, surrogate keys, Cache-Control, Vary, cookies, auth headers, image optimization, static assets, HTML, and RSC caching.
- Prove public responses do not vary on unlisted identity inputs and private responses cannot become public.
- Map service-worker precache, runtime routes, navigation fallback, API caching, activation, and cleanup.
- Prevent old HTML referencing deleted assets, new clients calling incompatible old servers, and old tabs issuing incompatible mutations.
- Use deployment IDs, asset retention, compatibility windows, or explicit reload handling.
- Review multi-region propagation, purge delay, stale-if-error, CDN outage, and origin shielding.

### Required Evidence

- Effective headers for public, authenticated, tenant, error, redirect, and RSC responses.
- Service-worker route and cache inventory with privacy class.
- Old/new deployment compatibility and retained-asset policy.
- Regional purge and propagation measurements.

### Mandatory Failure And Acceptance Tests

- Keep an old tab open through deployment and exercise reads, writes, navigation, and reload.
- Serve stale HTML or RSC intentionally and verify version-skew protection.
- Go offline, update the service worker, reconnect, and verify private data and mutation safety.
- Delay one regional purge and prove bounded inconsistency or traffic isolation.

