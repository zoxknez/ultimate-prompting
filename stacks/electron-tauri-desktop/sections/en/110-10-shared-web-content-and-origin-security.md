## 10. Shared Web, Content, And Origin Security

### 10.1 Content Origins And Navigation

1. Inventory every local, custom-protocol, file, data, blob, extension, development-server, remote HTTPS, WebSocket, and user-provided origin.
2. Classify each origin as trusted local application content, trusted remote application content, third-party content, user-generated content, authentication content, update content, or untrusted arbitrary content.
3. Define an allowlist for top-level navigation, redirects, new windows, downloads, external protocol handling, OAuth callbacks, and embedded frames.
4. Canonicalize and validate URLs with a real parser. Reject username confusion, encoded separators, mixed case, punycode/homograph traps, alternate schemes, local addresses, and redirect chains where relevant.
5. Do not grant local privileges to remote content merely because it is served by the application's domain. Account takeover, DNS/CDN compromise, XSS, or supply-chain compromise can make that content hostile.
6. Separate trusted and untrusted content into distinct webviews/windows, sessions, storage partitions, permissions, and bridge surfaces.
7. Block unexpected navigation and window creation at the privileged layer, not only in frontend click handlers.
8. Test redirects, target blank, window.open, iframe, drag-and-drop, pasted HTML, markdown, SVG, PDF, media, and downloaded content.

### 10.2 CSP, Injection, And Browser Surface

1. Define a restrictive Content Security Policy for each content class. Avoid broad `unsafe-eval`, `unsafe-inline`, wildcard origins, unrestricted `connect-src`, and permissive frame/object rules.
2. Trace all HTML, markdown, template, SVG, CSS, URL, script, and command construction from source to sink. Validate sanitization configuration and bypasses.
3. Audit DOM XSS, prototype pollution, unsafe deserialization, dynamic import, eval-like behavior, worker creation, WebAssembly loading, and plugin-defined script execution.
4. Verify Trusted Types or equivalent controls where practical, but do not treat policy presence as proof that unsafe sinks are unreachable.
5. Audit browser storage, IndexedDB, Cache Storage, service workers, cookies, localStorage, sessionStorage, and shared partitions for sensitive data and cross-account leakage.
6. Disable or justify experimental browser features, insecure content, certificate bypasses, disabled web security, permissive CORS workarounds, and debugging ports.
7. Verify clipboard, drag/drop, paste, print, screen capture, notifications, media capture, geolocation, USB, serial, HID, Bluetooth, and filesystem permissions.
8. Test with malicious content that attempts to reach every exposed bridge, navigate, open external applications, exfiltrate data, persist state, and trigger expensive work.

### 10.3 Authentication Content And Session Boundaries

1. Prefer system-browser authorization with PKCE when appropriate. If embedded authentication is required, document provider support, cookie/storage isolation, phishing risk, and bridge restrictions.
2. Validate custom protocol or app-link callbacks against state, nonce, PKCE verifier, expected issuer, redirect URI, account, and one-time use.
3. Prevent one account's cookies, cache, local storage, database rows, files, tokens, pending operations, or window state from leaking after logout or account switch.
4. Store refresh tokens and long-lived credentials in operating-system protected storage or a clearly justified alternative; do not expose them to the renderer.
5. Define token refresh single-flight, expiry, clock-skew, offline, revocation, password change, device removal, and server-side session invalidation behavior.
6. Verify local authorization for privileged offline operations; an old cached UI state is not authorization.
7. Protect login, license, payment, and account-recovery windows from navigation, arbitrary preload/command access, screenshots where required, and external content injection.
8. Test multiple windows, multiple profiles, fast account switching, concurrent refresh, expired sessions, revoked accounts, and sleep/wake transitions.

