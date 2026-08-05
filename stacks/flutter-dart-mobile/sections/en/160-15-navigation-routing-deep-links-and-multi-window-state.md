## 15. Navigation, Routing, Deep Links, And Multi-Window State

Treat navigation as a security, lifecycle, and state-consistency boundary.

- Inventory Navigator APIs, Router, declarative routing packages, nested navigators, shell routes, modal routes, restoration IDs, and custom transitions.
- Verify path, query, fragment, route extras, serialized state, and platform deep-link inputs are parsed, normalized, bounded, and authorized.
- Test cold start, warm start, background resume, killed process, logged-out state, expired session, wrong tenant, missing resource, and duplicate deep link delivery.
- Prevent authorization bypass by direct route entry; UI hiding is not authorization.
- Verify browser back/forward, URL synchronization, refresh, history restoration, canonical URLs, and unsupported route behavior on web.
- Verify multiple windows, scenes, desktop instances, secondary displays, notification taps, and add-to-app engines do not share or overwrite the wrong navigation state.
- Audit redirect loops, async guards, stale guards, race conditions between session restoration and routing, and error-page information disclosure.
- Require route contract tests and platform deep-link tests for all privileged and business-critical destinations.

