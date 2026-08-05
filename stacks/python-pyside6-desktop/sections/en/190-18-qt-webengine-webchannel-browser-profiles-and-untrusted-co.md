## 18. Qt WebEngine, WebChannel, Browser Profiles, And Untrusted Content

### 18.1 Audit Scope

1. Inventory every WebEngine view, profile, page, process model, storage partition, cache, cookie store, download handler, permission request, certificate handler, and custom URL scheme.
2. Record all local and remote origins, navigation rules, popup behavior, external-open behavior, CSP, mixed content, service workers, DevTools access, and command-line switches.
3. Map WebChannel objects, exposed methods/properties/signals, origin binding, frame binding, argument validation, authorization, and lifetime.
4. Review JavaScript injection, HTML generation, local file access, `qrc` and custom-scheme privileges, clipboard, camera, microphone, geolocation, notifications, and screen capture.
5. Assess profile isolation between users, tenants, accounts, environments, and privileged/unprivileged content.
6. Treat web content as attacker-controlled unless origin, transport, content integrity, and update ownership are proven.

### 18.2 Required Verification

1. Test navigation to malicious, redirected, downgraded, local-file, custom-scheme, popup, iframe, and compromised-origin content.
2. Attempt WebChannel calls from unauthorized origins, frames, stale pages, restored sessions, and after account or environment changes.
3. Verify explicit allowlists for navigation, external opening, downloads, permissions, certificates, and custom-scheme resources.
4. Inspect packaged Chromium/Qt WebEngine versions and security support; verify sandbox/process behavior on each platform.
5. Confirm browser data, cookies, credentials, cache, downloads, and service workers are removed or isolated correctly on logout and uninstall.

