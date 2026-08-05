## 38. Web-Specific Audit

Flutter web is a browser application with origin, cache, deployment, accessibility, and compatibility constraints.

- Record JavaScript or Wasm mode, renderer, optimization, base href, asset URL strategy, compile-time defines, browser matrix, mobile/desktop browser support, and fallback.
- Verify CSP including nonce/hash strategy, Trusted Types where used, COOP/COEP/CORP for cross-origin isolation, CORS, permissions policy, frame policy, referrer policy, and HTTPS.
- Audit service worker, cache versioning, stale shell, asset hashing, CDN caching, HTML cache policy, update prompt, rollback, offline behavior, and partial deployment.
- Verify origin separation, cookies, browser storage, session restoration, logout, multi-tab behavior, BroadcastChannel or worker use, private mode, quota, and storage eviction.
- Audit URL handling, history, refresh, server rewrites, deep routes, canonical metadata, SEO limitations where relevant, and error fallback.
- Test accessibility with browser semantics, screen readers, keyboard-only navigation, focus, zoom, text scaling, high contrast, reduced motion, and copy/paste.
- Measure initial download, compression, caching, first paint, Flutter first frame, interaction readiness, frame performance, memory, worker cost, and low-end-device behavior.
- Inspect JavaScript interop and DOM access for schema validation, origin checks, XSS, unsafe HTML, prototype behavior, callback lifetime, and release minification differences.
- Test supported browsers, versions, devices, zoom levels, network states, cache states, old/new deployments, and extension/privacy interference.

