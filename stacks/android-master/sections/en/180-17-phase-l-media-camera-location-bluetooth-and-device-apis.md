## 17. Phase L - Media, Camera, Location, Bluetooth And Device APIs

### 17.1 Media3, Audio And Playback

1. Map player ownership, lifecycle, media source creation, DRM, tracks, subtitles, caching, downloads, session, notification, and background playback.
2. Verify a single authoritative playback state and avoid multiple competing players or controllers.
3. Verify prepare, play, pause, seek, retry, stop, release, and source replacement under rapid input.
4. Verify audio focus, noisy intent, output route changes, calls, headphones, Bluetooth, picture-in-picture, screen off, and app background.
5. Verify MediaSession commands, metadata, lock screen, notification, external controllers, Android Auto, and TV integration.
6. Verify headers, cookies, DRM tokens, redirects, TLS, and private URLs are propagated safely and not logged.
7. Test buffering, live edge, catch-up, discontinuity, track change, subtitle encoding, malformed manifests, CDN failure, and retry policy.
8. Verify wake locks, Wi-Fi locks, screen-on flags, and foreground services are held only while justified.
9. Verify player and surface release prevents decoder, context, and memory leaks.
10. Test low-memory, rapid channel switching, multi-window, multiview, and background recovery where applicable.

### 17.2 Camera, Microphone, Location, Bluetooth, NFC And Sensors

1. Verify lifecycle binding, permission timing, cancellation, resource release, and hardware-unavailable states.
2. Test interrupted capture, rotation, backgrounding, screen lock, incoming calls, and process death.
3. Verify camera and microphone indicators align with actual use and user expectations.
4. Verify location accuracy, frequency, foreground or background mode, batching, geofence transitions, and battery use.
5. Verify Bluetooth scan and connection permissions by API level, device compatibility, reconnect, duplicate devices, and spoofed input.
6. Verify NFC, USB, sensor, and accessory input validation and disconnect recovery.
7. Prevent raw media, location, identifiers, and sensor data from leaking to logs, analytics, caches, or backups.
8. Verify data is minimized and retained only as long as needed.

