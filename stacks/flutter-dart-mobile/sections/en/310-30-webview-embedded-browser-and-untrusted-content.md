## 30. WebView, Embedded Browser, And Untrusted Content

A WebView combines remote content with application privileges and requires strict isolation.

- Inventory every WebView/browser view, origin, navigation source, JavaScript setting, bridge, cookie jar, storage, file access, media permission, download path, and popup behavior.
- Allowlist schemes, hosts, paths, redirects, and external-open destinations; reject lookalike hosts, mixed content, unsafe schemes, userinfo, malformed URLs, and open redirects.
- Expose the smallest possible message bridge with schema validation, origin/frame validation, authorization, rate limits, correlation, timeout, and lifecycle binding.
- Do not expose tokens, raw filesystem, shell, arbitrary URL launch, clipboard, contacts, camera, database, or device APIs to untrusted content.
- Verify cookie flags, SameSite behavior, SSO logout, cache clearing, account switch, storage partitioning, certificate errors, safe browsing, and download validation.
- Test XSS in remote content, malicious redirects, nested frames, bridge spoofing, replay, navigation during a privileged request, process recreation, and offline cached pages.
- Keep browser and platform WebView versions in the compatibility matrix and define unsupported-version behavior.
- Require security review for every new origin, bridge method, file permission, download type, or authentication flow.

