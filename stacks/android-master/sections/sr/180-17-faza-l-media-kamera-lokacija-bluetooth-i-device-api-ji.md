## 17. Faza L - Media, Kamera, Lokacija, Bluetooth I Device API-ji

### 17.1 Media3, Audio I Playback

1. Mapiraj player ownership, lifecycle, kreiranje media source-a, DRM, track-ove, subtitle, caching, download, session, notification i background playback.
2. Proveri jedan authoritative playback state i izbegni vise konkurentnih player-a ili controller-a.
3. Proveri prepare, play, pause, seek, retry, stop, release i source replacement pri rapid input-u.
4. Proveri audio focus, noisy intent, promenu output route-a, pozive, slusalice, Bluetooth, picture-in-picture, screen off i app background.
5. Proveri MediaSession command-e, metadata, lock screen, notification, external controller-e, Android Auto i TV integraciju.
6. Proveri da se header-i, cookie-ji, DRM token-i, redirect-i, TLS i private URL-ovi prosledjuju bezbedno i ne loguju.
7. Testiraj buffering, live edge, catch-up, discontinuity, track change, subtitle encoding, malformed manifest, CDN failure i retry policy.
8. Proveri da se wake lock, Wi-Fi lock, screen-on flag i foreground service drze samo dok je opravdano.
9. Proveri da release player-a i surface-a sprecava decoder, context i memory leak.
10. Testiraj low-memory, rapid channel switching, multi-window, multiview i background recovery gde je primenjivo.

### 17.2 Kamera, Mikrofon, Lokacija, Bluetooth, NFC I Senzori

1. Proveri lifecycle binding, permission timing, cancellation, release resursa i hardware-unavailable state.
2. Testiraj interrupted capture, rotation, backgrounding, screen lock, incoming call i process death.
3. Proveri da camera i microphone indikator odgovaraju stvarnoj upotrebi i ocekivanjima korisnika.
4. Proveri location accuracy, frequency, foreground ili background mode, batching, geofence transition i battery use.
5. Proveri Bluetooth scan i connection permission po API level-u, device kompatibilnost, reconnect, duplicate device i spoofed input.
6. Proveri NFC, USB, sensor i accessory input validaciju i disconnect recovery.
7. Spreci curenje raw media, location, identifier i sensor podataka u logove, analytics, cache ili backup.
8. Proveri da su podaci minimalizovani i zadrzani samo koliko je potrebno.

