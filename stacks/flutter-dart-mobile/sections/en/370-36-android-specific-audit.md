## 36. Android-Specific Audit

Verify the Flutter layer together with the actual Android host and final AAB/APK.

- Audit Gradle settings, AGP/Kotlin/JDK/SDK/NDK compatibility, repositories, variants, flavors, manifests, resource merging, desugaring, ABI splits, and dependency graph.
- Inspect application/activity classes, FlutterActivity/Fragment/Engine integration, launch mode, task behavior, process, exported components, intent filters, providers, receivers, and services.
- Verify permissions, scoped storage, media/photo picker, package visibility, PendingIntent mutability, FileProvider, network security config, backup rules, and data extraction rules.
- Audit lifecycle, configuration change, predictive back, edge-to-edge, system bars, picture-in-picture, multi-window, foldables, large screens, Android TV, and ChromeOS where claimed.
- Verify background restrictions, WorkManager, foreground service types, notification permission/channels, exact alarms, boot behavior, battery optimization, and force-stop semantics.
- Inspect app signing, upload/app-signing keys, certificate continuity, Play Integrity or equivalent use, Play Console tracks, target API, Data safety, and staged rollout.
- Build and inspect release AAB/APK, manifest, resources, native libraries, symbols, R8 output, mapping, ABI, 16 KB page compatibility where applicable, and install behavior.
- Test real devices across supported API, vendor, architecture, memory, display, background restriction, upgrade, restore, and low-storage conditions.

