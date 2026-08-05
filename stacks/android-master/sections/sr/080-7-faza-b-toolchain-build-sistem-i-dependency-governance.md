## 7. Faza B - Toolchain, Build Sistem I Dependency Governance

### 7.1 Toolchain Compatibility Matrica

1. Utvrdi stvarne verzije Android Studio, AGP, Gradle Wrapper-a, JDK-a, Kotlin-a, KSP-a, Compose compiler plugin-a, SDK-a, Build Tools-a, NDK-a, CMake-a i glavnih plugin-a.
2. Proveri zvanicnu kompatibilnost tacnih koriscenih verzija.
3. Detektuj version drift izmedju lokalnog razvoja, CI-ja, release masine, Docker image-a, remote cache-a i developer dokumentacije.
4. Proveri da su Java toolchain-i, Gradle daemon JDK, `JAVA_HOME`, Kotlin JVM target, desugaring i bytecode target-i uskladjeni.
5. Proveri da su wrapper distribution URL, checksum i executable skripte kontrolisani i pregledni.
6. Detektuj dynamic plugin ili dependency verzije, promenljive snapshot-e, mutable repository-je, unpinned Git dependency-je i rizik redosleda repository-ja.
7. Proveri deprecated AGP API-je, legacy Variant API-je, custom transform-e, eager configuration, configuration-cache blokatore i AGP 10 migration rizik.
8. Proveri KAPT i KSP upotrebu, deterministicko generisanje koda, incremental processing i kompatibilnost.
9. Ne unapredjuj toolchain dok trenutni baseline nije sacuvan i upgrade nema konkretnu svrhu.

### 7.2 Build Logika, Moduli I Varijante

1. Proveri da je konfiguracija centralizovana samo tamo gde poboljsava ispravnost i ne skriva vlasnistvo modula.
2. Proveri convention plugin-e zbog skrivenog ponasanja varijanti, duplih flag-ova, task mutacije i configuration-time I/O-a.
3. Proveri da svaki product flavor i build type dobija namenjeni application ID, resurse, endpoint-e, kljuceve, feature flag-ove, manifeste i signing.
4. Proveri flavor dimension-e i paritet varijanti dynamic feature modula.
5. Proveri da debug-only dependency-ji i alati ne mogu uci u release varijante.
6. Proveri da test, benchmark, staging, internal i release varijante nisu slucajno izjednacene ili pomesane.
7. Pregledaj manifest merge report-e i resource merge konflikte za svaku materijalnu varijantu.
8. Proveri duplicate classes, dependency constraints, platform ili BOM poravnanje, capabilities, excludes i dependency substitutions.
9. Proveri da build cache, configuration cache, parallelism, worker-i i remote cache ne ugrozavaju ispravnost ili bezbednost tajni.
10. Izmeri sync i build uska grla pre optimizacije.

### 7.3 Dependency I SDK Governance

1. Napravi dependency inventar iz resolved graph-ova, a ne samo iz deklarisanih dependency-ja.
2. Identifikuj direktne, tranzitivne, bundled, native, code-generated, build-time, test i runtime dependency-je.
3. Zabelezi verzije, poreklo, licence, update channel, maintenance status, poznate advisories i data-processing ponasanje.
4. Proveri AndroidX, Compose BOM, Firebase BOM, Kotlin BOM, Media3, Room, Navigation, Hilt, WorkManager, OkHttp i druge porodice zbog pomesanih nekompatibilnih verzija.
5. Proveri dependency verification, checksum-e, repository ogranicenja, lockfile-ove gde imaju smisla i supply-chain kontrole.
6. Identifikuj SDK-ove koji dodaju dozvole, exported komponente, provider-e, receiver-e, startup initializer-e, network traffic, native kod, tracker-e ili WebView-e.
7. Proveri da je SDK inicijalizacija neophodna, odlozena gde treba, consent-aware i iskljucena u nepodrzanim okruzenjima.
8. Dependency ukloni tek nakon dokaza da se ne koristi i razumevanja reflection, manifest, code generation, resource i native referenci.

