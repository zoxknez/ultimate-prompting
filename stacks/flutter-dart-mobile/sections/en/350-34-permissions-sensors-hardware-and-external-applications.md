## 34. Permissions, Sensors, Hardware, And External Applications

Request the minimum capability at the moment of need and survive denial or revocation.

- Inventory camera, microphone, photos, media, contacts, calendar, location, Bluetooth, nearby devices, notifications, local network, USB, serial, NFC, biometrics, health, sensors, and screen capture.
- Map runtime requests to manifest/Info.plist/entitlement/desktop declarations, purpose text, store disclosures, privacy manifests, and actual code paths.
- Handle not determined, denied, permanently denied, restricted, limited, approximate, one-time, while-in-use, background, and revoked states accurately.
- Do not repeatedly nag, bypass platform UI, open settings without context, or claim capability that the OS has not granted.
- Verify hardware absence, busy device, interruption, route change, lifecycle transition, multi-window use, permission change, and plugin error cleanup.
- Validate external application intents, URLs, file handoff, return values, spoofed callbacks, missing handlers, and sensitive-data exposure.
- Test physical devices and relevant OS versions; emulator/simulator support is not enough for camera, Bluetooth, background location, NFC, biometrics, media, and USB.
- Measure battery, thermal, radio, CPU, memory, and privacy impact of continuous sensing or scanning.

