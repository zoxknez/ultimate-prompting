## 8. Faza C - Build, Release, Signing I Pakovanje

### 8.1 Baseline Build Matrica

Pokreni samo primenjive task-ove i zabelezi tacne rezultate:

```text
./gradlew clean
./gradlew assembleDebug
./gradlew testDebugUnitTest
./gradlew lintDebug
./gradlew assembleRelease
./gradlew bundleRelease
./gradlew lintRelease
./gradlew connectedDebugAndroidTest
```

1. Preferiraj ciljane module i variant task-ove pre skupog punog build-a.
2. Ne koristi `clean` kao default diagnostic korak ako bi unistio korisne incremental dokaze.
3. Razdvoji source, configuration, dependency, resource, manifest, code generation, dexing, shrinking, packaging, signing, install, runtime i test kvarove.
4. Sacuvaj report-e, stack trace-ove, scan reference, test XML, HTML, APK, AAB, mapping, native symbols i baseline profile artefakte.
5. Potvrdi release task-ove, a ne samo debug task-ove.

### 8.2 Release Varijanta I R8

1. Proveri da release koristi namenjene endpoint-e, feature flag-ove, logging level, analytics projekat, network security, sertifikate, ime baze i update channel.
2. Proveri da su minification, optimization, resource shrinking i obfuscation ukljuceni ili namerno obrazlozeni.
3. Pregledaj app keep rules, consumer rules, generisana pravila, reflection, serialization, JNI, navigation, dependency injection i WebView JavaScript interface-e.
4. Koristi R8 diagnostics i configuration analysis gde je podrzano.
5. Istrazuj missing class probleme i rast keep pravila umesto dodavanja sirokih `-keep class ** { *; }` pravila.
6. Proveri release-only putanje, desugaring, service loader-e, dynamic feature-e, split install i native loading.
7. Proveri da se mapping fajlovi i native debug symbols arhiviraju i upload-uju crash platformi.
8. Proveri reproducibility ili najmanje sledljivo poreklo od source revision-a do signed artefakta.
9. Uporedi debug i release ponasanje na kriticnim tokovima.

### 8.3 Signing, Versioning I Bezbednost Update-a

1. Proveri da su debug, upload, app-signing, enterprise i OEM kljucevi razdvojeni i access-controlled.
2. Proveri da se debug keystore ili hardkodovana signing lozinka ne koriste za produkciju.
3. Proveri key alias-e, validnost sertifikata, plan rotacije, backup, vlasnistvo i least privilege.
4. Proveri da su version code vrednosti monotone za sve track-ove, ABI-je, split-ove i channel-e.
5. Proveri da application ID i signing kontinuitet podrzavaju update instaliranih produkcionih verzija.
6. Testiraj upgrade najmanje sa najstarije podrzane produkcione seme i reprezentativne novije verzije.
7. Downgrade ponasanje testiraj samo gde model distribucije to dozvoljava.
8. Proveri da rollback ne korumpira podatke niti ostavlja korisnike na nekompatibilnim semama.
9. Proveri Play App Signing, internal app sharing, enterprise signing ili sideload procedure iz stvarne konfiguracije, a ne pretpostavke.

### 8.4 APK, AAB, Split-ovi I Native Biblioteke

1. Pregledaj sadrzaj finalnog APK-a i AAB-a pomocu APK Analyzer-a, bundletool-a ili ekvivalenta.
2. Proveri manifest, resurse, assets, native biblioteke, DEX count, dozvole, feature-e, package visibility i split konfiguraciju.
3. Proveri da ABI filter-i ne iskljucuju podrzane uredjaje niti pakuju nepotrebne ABI-je.
4. Proveri da svaka upakovana `.so` biblioteka ima poznato poreklo i odgovara podrzanim ABI-jima.
5. Proveri 16 KB ELF segment alignment i package alignment za svaku native biblioteku, ukljucujuci tranzitivne SDK-ove.
6. Testiraj na stvarnom ili emulator 16 KB okruzenju gde je primenjivo i zabelezi page-size dokaz.
7. Proveri JNI pretpostavke, hardkodovane page size vrednosti, memory mapping, native crash-eve, symbol fajlove i sanitizer strategiju.
8. Proveri asset pack, dynamic feature, install-time, fast-follow i on-demand delivery ponasanje pri gresci i low-storage stanju.
9. Proveri da su compressed i uncompressed native library podesavanja namerna.

