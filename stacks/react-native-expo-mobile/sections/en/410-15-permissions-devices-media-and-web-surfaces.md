## 15. Permissions, Devices, Media, And Web Surfaces

### 15.1 Permissions And Hardware
- Inventory camera, microphone, photos, media library, location, Bluetooth, nearby devices, contacts, calendar, notifications, motion, health, NFC, USB, and local network.
- Verify manifest, Info.plist, entitlements, privacy strings, config plugins, runtime prompts, limited access, approximate access, and denial handling.
- Request permission only at a user-understandable point and explain required, optional, degraded, and permanently denied behavior.
- Re-check authorization after settings changes, OS upgrade, restore, managed-device policy, app update, and account switch.
- Audit hardware resource ownership, concurrent use, interruption, route changes, thermal pressure, disconnection, and cleanup.
- Test physical devices across supported OS versions, vendors, architectures, screen forms, peripherals, and constrained conditions.

### 15.2 Media And Graphics
- Audit audio focus, interruptions, route changes, Bluetooth, lock-screen controls, background playback, recording, camera sessions, and concurrent media use.
- Verify codec, DRM, subtitle, track, streaming, download, cache, resume, and offline-license behavior where applicable.
- Bound image dimensions, decode memory, texture memory, frame buffers, prefetch, cache, and transformed asset growth.
- Test backgrounding, call interruption, unplugged device, route change, process death, low memory, thermal throttling, and native error propagation.
- Verify permissions, secure output, screenshots, screen recording, protected content, metadata privacy, and temporary-file cleanup.
- Measure release-mode startup, first frame, dropped frames, decode time, memory, battery, network, and storage cost.

### 15.3 WebView, Browser, And Local Web Content
- Inventory all WebViews, authentication browser sessions, in-app browsers, local HTML, custom schemes, injected JavaScript, and message bridges.
- Define trusted origins, navigation allowlist, popup policy, download policy, mixed-content policy, certificate handling, cookies, and storage isolation.
- Treat every bridge message as untrusted and authorize origin, frame, session, tenant, command, resource, and payload.
- Prevent arbitrary external URL, file URL, intent URL, JavaScript URL, universal-link loop, and custom-scheme abuse.
- Test stale pages after logout, account switch, OTA update, native update, certificate rotation, and offline cache restoration.
- Prove that privileged native functions cannot be reached from untrusted, navigated, compromised, or nested content.

