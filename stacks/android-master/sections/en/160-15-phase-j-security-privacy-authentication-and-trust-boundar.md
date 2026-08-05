## 15. Phase J - Security, Privacy, Authentication And Trust Boundaries

### 15.1 Components, Intents, Deep Links And IPC

1. Review every exported activity, service, receiver, provider, intent filter, permission, and package-visibility query.
2. Require `android:exported` and custom permissions to reflect actual callers.
3. Validate all incoming intents, extras, clips, URIs, bundles, pending intents, and Binder input.
4. Use immutable or appropriately scoped PendingIntents and prevent intent redirection.
5. Verify broadcast receivers, foreground services, jobs, and providers enforce caller and data permissions.
6. Verify content-provider selection, projection, sort order, file descriptors, and URI grants cannot expose arbitrary data.
7. Test malicious external app scenarios for each public entry point.
8. Verify app links, custom schemes, OAuth callbacks, and share targets cannot be hijacked or confused.

### 15.2 Authentication, Session And Authorization

1. Map authentication, token storage, refresh, logout, account switching, biometric gates, and server-side authorization.
2. Treat device-side checks as UX or defense in depth, not as the only authorization boundary.
3. Verify every sensitive API call is authorized server-side for the resource and account.
4. Verify token expiry, clock skew, revocation, refresh rotation, replay, and concurrent refresh handling.
5. Verify logout clears all account-bound data, caches, notifications, downloads, cookies, WebViews, and background work.
6. Verify multi-account state cannot leak across databases, repositories, workers, notifications, widgets, or media sessions.
7. Verify biometric use is bound to correct cryptographic or product semantics and has a secure fallback policy.
8. Test rooted, debug, hooked, tampered, offline, and restored-device scenarios according to the actual threat model.
9. Do not claim root or integrity detection makes client-side secrets or authorization safe.

### 15.3 Secrets, Keystore And Cryptography

1. Identify hardcoded secrets, embedded credentials, private keys, signing material, and reversible obfuscation.
2. Assume anything shipped in the app can be extracted.
3. Use Android Keystore for appropriate device-bound keys and verify authentication, invalidation, backup, rotation, and hardware support semantics.
4. Verify encrypted storage does not use static keys, fixed IVs, insecure modes, or unauthenticated encryption.
5. Verify cryptographic algorithms, parameters, random generation, encoding, and key derivation against current platform guidance.
6. Avoid custom cryptography.
7. Verify secret deletion, logout, device migration, reinstall, and lock-screen changes.
8. Verify network or backend design does not require an unrecoverable secret inside the APK.

### 15.4 WebView, Files, Parsers And Untrusted Content

1. Inventory every WebView and its JavaScript, file access, content access, mixed content, debugging, Safe Browsing, cookies, and navigation policy.
2. Restrict loaded origins and external navigation.
3. Never expose a broad JavaScript interface to untrusted content.
4. Validate file, content, data, blob, and custom-scheme URLs.
5. Verify downloads and uploads enforce size, type, origin, storage, permission, and cleanup rules.
6. Treat HTML, Markdown, SVG, XML, JSON, archives, subtitles, playlists, media metadata, images, PDFs, and third-party parser input as untrusted.
7. Bound parser recursion, entity expansion, decompression, allocation, and execution time.
8. Verify external viewers and shares use safe URIs and minimum grants.

### 15.5 Permissions, Privacy And Data Safety

1. Inventory manifest, runtime, special, role, notification, exact alarm, overlay, accessibility, VPN, media projection, package install, all-files, and restricted permissions.
2. Verify every permission is necessary, contextual, minimized, and explained before the system permission prompt where appropriate.
3. Handle denial, repeated denial, one-time permission, approximate location, selected photos, auto-reset, revocation, and settings return.
4. Verify background location, Bluetooth, nearby devices, camera, microphone, contacts, call logs, SMS, health, and advertising identifiers against current policy.
5. Map collected, processed, shared, retained, deleted, exported, and backed-up data.
6. Compare code and SDK behavior with privacy policy, consent, Data safety declarations, and regional requirements.
7. Verify analytics, attribution, crash, ads, and experimentation SDKs honor consent and account deletion.
8. Prevent sensitive data in logs, screenshots, clipboard, notifications, widgets, recents, backups, analytics, and support exports.
9. Test account deletion and data export end to end where applicable.
10. Identify child-directed, health, financial, employment, education, biometric, or other regulated use requiring specialist review.

