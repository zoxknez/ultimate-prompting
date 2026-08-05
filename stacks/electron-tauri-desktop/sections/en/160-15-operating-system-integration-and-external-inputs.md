## 15. Operating-System Integration And External Inputs

### 15.1 Deep Links, Protocol Handlers, File Associations, And CLI

1. Inventory custom URI schemes, app links, universal links, file associations, open-with handlers, shell verbs, context-menu entries, command-line switches, startup arguments, and store activation payloads.
2. Treat every payload as untrusted. Parse structurally, bound size/count, canonicalize paths/URLs, require expected action types, and reject unknown fields and schemes.
3. Protect authentication callbacks with state, nonce, PKCE, expected issuer, account binding, one-time use, and expiry.
4. Prevent argument, shell, URL, path, and template injection when forwarding payloads to an existing instance or helper.
5. Define behavior before the app is ready, during update, with multiple instances, with no signed-in account, and after account switch.
6. Do not execute or auto-open content merely because the OS associated it with the application.
7. Register and unregister integrations consistently across fresh install, per-user/per-machine install, upgrade, repair, portable mode, store install, channel coexistence, and uninstall.
8. Test malformed encoding, huge payloads, duplicate activation, nested URL, local-file URL, alternate scheme, stale account, and simultaneous activations.

### 15.2 Tray, Menus, Shortcuts, Clipboard, Notifications, And Autostart

1. Map every tray/menu/global-shortcut/notification action to an authorized command and current account/window state.
2. Do not trust menu IDs, notification payloads, or global shortcut events as proof of user identity or intent.
3. Prevent duplicate registrations and stale handlers across reload, update, account switch, display changes, sleep/wake, and multiple instances.
4. Minimize sensitive clipboard exposure; clear only with careful ownership logic and never destroy unrelated user clipboard content.
5. Sanitize notification content and actions. Avoid displaying secrets on the lock screen and validate activation payloads.
6. Justify autostart, background mode, login-item helpers, scheduled tasks, services, and startup registry/plist entries. Provide visible user control and removal.
7. Verify accessibility and keyboard navigation of native menus, tray flows, dialogs, and shortcuts, including conflicts and localized labels.
8. Test denied OS permission, revoked permission, changed default app, stale notification, shortcut conflict, multiple monitors, locked session, and OS restart.

### 15.3 Devices, Media, Screen Capture, Printing, And Hardware

1. Inventory camera, microphone, display capture, audio output, USB, serial, HID, Bluetooth, smart card, printer, scanner, GPU, codec, and custom-driver use.
2. Request the minimum OS and web permission at the moment of need, explain the purpose, handle denial, and support revocation.
3. Authorize device selection and operations against the current user/account and business policy; device presence is not authorization.
4. Validate device descriptors and data lengths. Bound streams, frame sizes, sample rates, buffers, recording duration, and storage.
5. Prevent unintended background capture after window close, logout, sleep, lock, account switch, or permission revocation.
6. Audit screen-capture source selection and prevent silent capture of sensitive windows where policy requires.
7. Treat printer names, paths, page settings, media files, codecs, and device firmware responses as untrusted inputs.
8. Test device removal, permission denial, partial frames, malformed data, driver crash, hotplug storms, sleep/wake, multiple devices, and update during active use.

