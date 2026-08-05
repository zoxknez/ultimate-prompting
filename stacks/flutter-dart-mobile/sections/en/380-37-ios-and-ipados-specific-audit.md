## 37. iOS And iPadOS-Specific Audit

Verify Flutter, Runner/native hosts, extensions, entitlements, signing, and App Store behavior together.

- Audit Xcode project/workspace, build settings, configurations, schemes, deployment targets, Swift/Objective-C code, pods/packages, scripts, architectures, and generated settings.
- Inspect AppDelegate, SceneDelegate/UIScene configuration, FlutterEngine integration, multiple scenes/windows, restoration, deep links, universal links, and add-to-app lifecycle.
- Verify Info.plist purpose strings, entitlements, capabilities, privacy manifests, required-reason APIs, ATS, associated domains, keychain groups, app groups, and extensions.
- Audit background modes, BGTaskScheduler, silent push, notification extensions, audio/location/Bluetooth behavior, process suspension, termination, and user force-quit semantics.
- Verify data protection class, keychain accessibility, backup/restore, iCloud behavior, files, pasteboard, screenshots, screen recording, and protected-data availability.
- Inspect signing certificates, provisioning profiles, team/bundle IDs, App Store Connect roles, TestFlight groups, export options, archive, dSYM, symbol upload, and certificate expiry.
- Test iPhone and iPad device classes, orientations, multitasking, external keyboard, pointer, Stage Manager, memory pressure, accessibility, upgrade, restore, and old/new OS versions.
- Review App Store privacy, tracking, subscription/payment, account deletion, review, export compliance, encryption declarations, and phased release requirements.

