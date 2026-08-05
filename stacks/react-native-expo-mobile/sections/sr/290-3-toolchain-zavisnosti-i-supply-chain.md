## 3. Toolchain, zavisnosti i supply chain

### 3.1 Matrica verzija i kompatibilnosti
- Razresi tacne verzije iz lock fajlova i generisanih native projekata umesto iz README primera ili semver opsega.
- Validiraj podrzanu matricu izmedju React Native, Expo SDK, React, Hermes, Metro, Expo Router, Reanimated, Screens, Gesture Handler i native biblioteka.
- Proveri minimalne zahteve za Node, JDK, Android SDK, NDK, Xcode, iOS deployment target, CocoaPods, Ruby i operativni sistem.
- Odvoji framework kompatibilnost od kompatibilnosti third-party biblioteke, config plugin-a, native SDK-a, store pravila i uredjaja.
- Klasifikuj nepodrzane, end-of-cycle, prerelease, canary, nightly, forkovane, patch-ovane i neodrzavane zavisnosti.
- Ne preporucuj sirok upgrade bez compatibility grafa, redosleda migracije, reprezentativnih release testova, rollout plana i rollback plana.

### 3.2 Poverenje u package i native supply chain
- Auditiraj npm registry konfiguraciju, privatne scope-ove, integritet lock fajla, lifecycle skripte, Git zavisnosti, lokalne putanje, override-e, patch-eve i workspace linkove.
- Auditiraj Maven, Gradle Plugin Portal, CocoaPods, Swift Package Manager, binarne framework-e, XCFramework, NDK biblioteke i preuzete alate.
- Pregledaj install, postinstall, prepare, patch-package, codegen, config-plugin, Gradle, Ruby, shell i Xcode build skripte kao izvrsni kod.
- Zahtevaj provenance, vlasnistvo, status odrzavanja, vulnerability status, licencu i put opoziva za kriticne pakete i native SDK-ove.
- Generisi i sacuvaj SBOM koji obuhvata JavaScript, Java/Kotlin, Objective-C/Swift, C/C++, native binarne fajlove i bundlovane asset-e gde je izvodljivo.
- Definisi hitan odgovor za kompromitovan paket, config plugin, native SDK, signing identitet, update kljuc, build image ili CI runner.

