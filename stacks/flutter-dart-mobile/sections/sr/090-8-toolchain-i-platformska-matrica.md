## 8. Toolchain i platformska matrica

Razreši stvarne verzije umesto čitanja samo nameravanih verzija.

- Sačuvaj `flutter --version --machine`, `dart --version`, `flutter doctor -v`, kanal, engine reviziju i provenance SDK instalacije.
- Uporedi lokalne, CI, release i developerske SDK-ove; otkrij plutajuće kanale, promenljive container-e, nepinovane setup action-e i skriveno FVM/asdf/mise ponašanje.
- Razreši Android Gradle Plugin, Gradle, Kotlin, Java, Android SDK/NDK, CMake, min/target/compile SDK, ABI, packaging i signing alate.
- Razreši Xcode, Swift, CocoaPods ili Swift Package Manager, deployment target-e, arhitekture, razlike simulator/device, provisioning i notarization alate.
- Razreši browser verzije, JavaScript ili Wasm compiler režim, renderer, web server/CDN, service worker, header-e, kompresiju i source-map pipeline.
- Razreši Visual Studio workload-e, Windows SDK, MSVC, CMake, NuGet, MSIX/installer tooling, sertifikat i ciljne arhitekture.
- Razreši macOS deployment target, Xcode command-line alate, entitlement-e, hardened runtime, signing identitet, notarizaciju i format paketa.
- Razreši Linux distribucioni baseline, compiler, CMake/Ninja, GTK, sistemske biblioteke, format paketa, sandbox/store runtime i ciljne arhitekture.
- Proveri da je svaka deklarisana platforma build-ovana, instalirana, pokrenuta, testirana, nadgledana, podržana i oporavljiva ili smanji tvrdnju o podršci.

