## 16. Android production audit

### 16.1 Android build i manifest
- Razresi compile SDK, target SDK, minimum SDK, AGP, Gradle, JDK, Kotlin, NDK, CMake, ABI filter, packaging pravila i repository izvore.
- Pregledaj merged manifest po exported komponentama, intent filter-ima, dozvolama, provider-ima, servisima, receiver-ima, queries, network security, backup-u i debuggability-ju.
- Proveri application ID, namespace, versionCode, versionName, signing config, product flavor, build type, manifest placeholder i resource overlay.
- Pregledaj ProGuard ili R8 pravila, resource shrinking, mapping, native simbole, startup profile, baseline profile i release-only reflection ili JNI ponasanje.
- Pregledaj AAB i generisani APK split po ABI-ju, density-ju, jeziku, poravnanju native biblioteke, 16 KB page kompatibilnosti, asset-ima, tajnama i debug ostacima.
- Instaliraj iz stvarnog distributivnog puta i proveri upgrade, odbijanje downgrade-a, fresh install, zadrzavanje podataka, backup restore i uninstall.

### 16.2 Android runtime i uredjaji
- Testiraj edge-to-edge, system bar, inset, predictive back, gesture navigaciju, tastaturu, multi-window, picture-in-picture, foldable, tablet, TV i veliki ekran gde se tvrdi podrska.
- Testiraj rekreiranje activity-ja, configuration change, gasenje procesa, task removal, force-stop, reboot, malo memorije, doze, app standby i background ogranicenja.
- Auditiraj foreground service, exact alarm, notification dozvolu, background lokaciju, media projection, battery optimization i restricted settings.
- Proveri app link, asset link, custom scheme, intent, PendingIntent mutability, share target, file provider i rezultat external activity-ja.
- Testiraj OEM-specific killer, permission manager, WebView verziju, keystore ponasanje, biometriju, Bluetooth stack i filesystem razliku.
- Sacuvaj ANR, native crash, Java ili Kotlin crash, tombstone, memoriju, bateriju, frame, mrezu i startup dokaz iz release build-a.

