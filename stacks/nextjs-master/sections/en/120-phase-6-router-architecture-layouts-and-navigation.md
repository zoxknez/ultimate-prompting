## Phase 6 - Router Architecture, Layouts, And Navigation

Map the real routing model and prove route identity, layout lifetime, navigation semantics, and authorization.

### Audit Requirements

- Inventory App Router, Pages Router, mixed boundaries, groups, parallel/intercepting routes, dynamic/catch-all segments, and locales.
- Map layouts, templates, loading, error, not-found, forbidden, unauthorized, default, and global-error boundaries.
- Verify precedence, collisions, normalization, trailing slash, basePath, locale, case, encoding, and direct entry.
- Review Link, prefetch, refresh, back/forward, scroll, focus, optimistic navigation, and unsaved forms.
- Ensure direct URLs, reloads, alternate locales, and modal/intercepted routes enforce identical ownership.
- When routers coexist, test cookies, errors, serialization, navigation, and shared component assumptions.

### Required Evidence

- Complete route table with runtime, rendering, auth, tenant, cache, owner, and SLO.
- Layout and error-boundary lifetime diagram.
- Direct-entry versus client-navigation comparison.
- Mixed-router compatibility matrix where applicable.

### Mandatory Failure And Acceptance Tests

- Visit critical routes by direct URL, client navigation, reload, back/forward, and unauthorized deep link.
- Exercise encoded, malformed, duplicate-slash, locale, and case variants.
- Trigger every loading, missing, auth, local error, and global error state.
- Prove intercepted routes cannot bypass auth or expose stale parent-layout data.

