## 16. Android Production Audit

### 16.1 Android Build And Manifest
- Resolve compile SDK, target SDK, minimum SDK, AGP, Gradle, JDK, Kotlin, NDK, CMake, ABI filters, packaging rules, and repository sources.
- Inspect merged manifests for exported components, intent filters, permissions, providers, services, receivers, queries, network security, backup, and debuggability.
- Verify application ID, namespace, versionCode, versionName, signing config, product flavors, build types, manifest placeholders, and resource overlays.
- Inspect ProGuard or R8 rules, resource shrinking, mapping, native symbols, startup profiles, baseline profiles, and release-only reflection or JNI behavior.
- Inspect AAB and generated APK splits for ABI, density, language, native library alignment, 16 KB page compatibility, assets, secrets, and debug remnants.
- Install from the actual distribution path and verify upgrade, downgrade rejection, fresh install, data retention, backup restore, and uninstall.

### 16.2 Android Runtime And Devices
- Test edge-to-edge, system bars, insets, predictive back, gesture navigation, keyboard, multi-window, picture-in-picture, foldables, tablets, TV, and large screens where claimed.
- Test activity recreation, configuration changes, process death, task removal, force-stop, reboot, low memory, doze, app standby, and background restrictions.
- Audit foreground services, exact alarms, notification permission, background location, media projection, battery optimization, and restricted settings.
- Verify app links, asset links, custom schemes, intents, PendingIntent mutability, share targets, file providers, and external activity results.
- Test OEM-specific killers, permission managers, WebView versions, keystore behavior, biometrics, Bluetooth stacks, and filesystem differences.
- Capture ANR, native crash, Java or Kotlin crash, tombstone, memory, battery, frame, network, and startup evidence from release builds.

