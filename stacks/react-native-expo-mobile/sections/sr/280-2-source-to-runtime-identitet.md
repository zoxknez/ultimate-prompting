## 2. Source-to-runtime identitet

### 2.1 Lanac identiteta
- Povezi URL repozitorijuma, commit, dirty stanje, submodule, workspace graf, digest lock fajla, verziju package manager-a, Node binary i okruzenje.
- Zabelezi identitet React Native, Expo SDK, React, Hermes, Metro, Expo CLI, EAS CLI, Gradle, Android Gradle Plugin, Kotlin, JDK, NDK, Xcode, Swift, CocoaPods i Ruby alata.
- Sacuvaj generisane Codegen izlaze, Expo prebuild izlaze, config-plugin izmene, Podfile.lock, Gradle dependency grafove, native asset-e i binarne framework-e.
- Povezi AAB, APK, IPA, archive, dSYM, mapping fajl, native simbole, JavaScript bundle, Hermes bytecode, source map, update manifest i digest artefakta.
- U runtime-u bezbedno izlozi ili sacuvaj verziju aplikacije, native build broj, runtimeVersion, update ID, kanal, branch, deployment revision, arhitekturu i okruzenje.
- Dokazi da telemetrija, crash simboli, source map-ovi, store zapisi i OTA metadata ukazuju na isti identitet izdanja.

### 2.2 Reproducibilnost i drift
- Reprodukuj instalaciju zavisnosti iz cistog checkout-a sa commit-ovanim package manager-om i immutable lockfile rezimom.
- Pokreni Expo config i prebuild pregled dva puta i uporedi izlaze radi otkrivanja nedeterministickih config plugin-a ili skrivenog lokalnog stanja.
- Uporedi generisane native projekte sa commit-ovanim projektima i klasifikuj namerno vlasnistvo, drift i posledice regeneracije.
- Uporedi lokalni, CI, EAS i store build po toolchain-u, okruzenju, kredencijalima, flag-ovima, native zavisnostima, bundle sadrzaju i hash-evima artefakta.
- Tretiraj Expo Go, development build, debug build, internal distribution build i store release kao razlicite proizvode dok se ne dokaze ekvivalentnost.
- Prijavi svako neslaganje source koda, generisanog projekta, zavisnosti, artefakta, deployment revision-a ili instaliranog runtime-a kao eksplicitan drift nalaz.

