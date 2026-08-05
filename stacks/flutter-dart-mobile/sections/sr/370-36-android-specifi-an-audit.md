## 36. Android-specifičan audit

Proveri Flutter sloj zajedno sa stvarnim Android host-om i finalnim AAB/APK artefaktom.

- Audituj Gradle settings, AGP/Kotlin/JDK/SDK/NDK kompatibilnost, repozitorijume, variant-e, flavor-e, manifest-e, resource merging, desugaring, ABI split-ove i dependency graf.
- Pregledaj application/activity klase, FlutterActivity/Fragment/Engine integraciju, launch mode, task ponašanje, proces, exported komponente, intent filter-e, provider-e, receiver-e i service-e.
- Proveri dozvole, scoped storage, media/photo picker, package visibility, PendingIntent mutability, FileProvider, network security config, backup pravila i data extraction pravila.
- Audituj lifecycle, configuration change, predictive back, edge-to-edge, system bar-ove, picture-in-picture, multi-window, foldable uređaje, velike ekrane, Android TV i ChromeOS gde su deklarisani.
- Proveri background ograničenja, WorkManager, foreground service type-ove, notification permission/channel-e, exact alarm-e, boot ponašanje, battery optimization i force-stop semantiku.
- Pregledaj app signing, upload/app-signing ključeve, kontinuitet sertifikata, Play Integrity ili ekvivalentnu upotrebu, Play Console track-ove, target API, Data safety i staged rollout.
- Build-uj i pregledaj release AAB/APK, manifest, resurse, native biblioteke, simbole, R8 izlaz, mapping, ABI, 16 KB page kompatibilnost gde je primenljivo i install ponašanje.
- Testiraj stvarne uređaje kroz podržane API, vendor, arhitekturu, memoriju, ekran, background restriction, upgrade, restore i low-storage uslove.

