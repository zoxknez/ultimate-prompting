## 17. Apple Platform Production Audit

### 17.1 iOS And iPadOS Build
- Resolve Xcode, Swift, deployment target, architectures, CocoaPods, Swift packages, frameworks, build settings, linker flags, and bitcode-related legacy assumptions.
- Inspect Info.plist, entitlements, privacy manifest, required-reason APIs, associated domains, background modes, URL types, app groups, and keychain groups.
- Verify bundle identifier, version, build number, scheme, configuration, signing identity, provisioning profile, capabilities, and export options.
- Inspect archive, IPA, dSYM, BCSymbolMap where relevant, embedded frameworks, extensions, resources, privacy files, signatures, and debug artifacts.
- Verify every bundled third-party SDK for signature, privacy manifest, architecture, minimum OS, license, symbolication, and store compliance.
- Install via the actual TestFlight, App Store, enterprise, or ad hoc path and test upgrade, fresh install, restore, migration, and uninstall.

### 17.2 Apple Runtime And Devices
- Test scene lifecycle, background suspension, termination, state restoration, memory warning, protected data, device lock, and low-power mode.
- Test iPhone and iPad layouts, Stage Manager, split view, rotation, Dynamic Type, safe areas, keyboard, pointer, external display, and supported device classes.
- Verify universal links, custom schemes, authentication sessions, handoff, push actions, widgets, extensions, and app clips where present.
- Audit Keychain accessibility, biometric policy, data protection, app groups, background URL sessions, and file coordination.
- Test permission changes, limited photo access, approximate location, Bluetooth, local network, tracking authorization, and managed-device restrictions.
- Capture watchdog termination, jetsam, native crash, hang, memory, energy, launch, animation, networking, and symbolication evidence from release builds.

