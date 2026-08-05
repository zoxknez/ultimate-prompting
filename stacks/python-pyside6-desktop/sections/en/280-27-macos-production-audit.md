## 27. macOS Production Audit

### 27.1 Audit Scope

1. Review supported macOS versions, Intel/Apple Silicon, universal binaries, deployment target, SDK/Xcode, hardened runtime, sandbox, and Rosetta assumptions.
2. Inspect app bundle structure, Mach-O architectures, load commands, rpaths, frameworks, dylibs, Qt plugins, resources, Info.plist, entitlements, and helper apps.
3. Assess Developer ID or App Store signing, nested-code signing order, secure timestamp, notarization, stapling, Gatekeeper, quarantine, and designated requirements.
4. Review Keychain access groups, application groups, bookmarks, file access, privacy usage descriptions, TCC permissions, launch agents, and privileged helpers.
5. Test Retina/high DPI, multiple displays, spaces, full screen, sleep/wake, screen lock, locale/input methods, accessibility, and system appearance.
6. Define DMG/PKG/store installation, app translocation, update framework, key/certificate renewal, rollback, and uninstall/data-retention behavior.

### 27.2 Required Verification

1. Verify every nested binary and resource seal after final packaging and confirm notarization acceptance and stapled ticket where applicable.
2. Test clean download with quarantine, first launch, translocation-sensitive paths, standard-user operation, permission denial/revocation, and another macOS user.
3. Exercise Intel, Apple Silicon, and universal paths where supported; detect accidental Rosetta-only helpers or architecture-mismatched plugins.
4. Test TCC prompts, revoked permissions, Keychain locked/unavailable, sleep/wake, display changes, VoiceOver, locale, and IME.
5. Validate update and rollback when the app is running, helpers are active, data schema changes, certificates rotate, or notarization/update services fail.

