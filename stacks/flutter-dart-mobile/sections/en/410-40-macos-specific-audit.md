## 40. macOS-Specific Audit

Verify the macOS host, sandbox, entitlements, signing, notarization, package, and update behavior.

- Audit Xcode project, deployment target, architectures, Swift/Objective-C runner, pods/packages, plugins, generated registrant, frameworks, rpaths, and native libraries.
- Verify bundle identifier, version, hardened runtime, App Sandbox, entitlements, privacy purpose strings, keychain access groups, app groups, bookmarks, and file access.
- Audit Developer ID or Mac App Store signing, nested code, timestamps, notarization, stapling, Gatekeeper assessment, certificate expiry, revocation, and key custody.
- Verify multiple windows, menu bar, dock, activation policy, open-file/open-URL events, app relaunch, login items, notifications, services, and single-instance expectations.
- Test Retina/scaling, multiple displays, Spaces, full screen, Stage Manager, keyboard, trackpad, VoiceOver, reduced motion, high contrast, sleep/wake, and fast user switching.
- Audit container paths, Application Support, Caches, temporary files, iCloud behavior, backups, quarantine attributes, symlinks, and user-selected file access.
- Inspect DMG/PKG/App Store packaging, update framework/feed, signature verification, atomic install, downgrade, rollback, channel, and user-data continuity.
- Test Intel and Apple Silicon where supported, clean install, migration, old OS, new OS, restricted account, offline launch, update, rollback, and restore.

