## 23. Operating-System Integration, Devices, And Privileged Helpers

### 23.1 Audit Scope

1. Inventory file associations, URL schemes, deep links, autostart, tray, notifications, global shortcuts, clipboard, drag/drop, recent files, shell integration, and single-instance behavior.
2. Review camera, microphone, screen capture, location, Bluetooth, USB, serial, HID, smart card, printing, scanners, media keys, and other device permissions.
3. Map services, daemons, scheduled tasks, drivers, kernel extensions, privileged helpers, elevation prompts, and installer custom actions.
4. Validate all OS-delivered inputs: command line, environment, file-open events, URLs, notification actions, clipboard, drag/drop, device data, and registry/plist values.
5. Assess same-user process impersonation, symlink/junction attacks, TOCTOU, insecure temporary files, inherited permissions, and writable service/helper paths.
6. Define disconnect, reconnect, permission denial, device removal, sleep/resume, fast user switching, remote desktop, and OS update behavior.

### 23.2 Required Verification

1. Fuzz deep links, file associations, notification actions, clipboard, drag/drop, command-line arguments, and device payloads with malformed and oversized input.
2. Test least-privilege operation as standard user and verify explicit, narrow elevation only where required.
3. Verify helper identity, signature, version handshake, request authorization, ACLs, installation path, update order, rollback, and compromised-helper response.
4. Exercise permission denied, revoked permission, unavailable device, device replacement, sleep/resume, session lock, user switch, and shutdown.
5. Confirm uninstall removes or intentionally retains services, tasks, drivers, associations, permissions, and data according to documented policy.

