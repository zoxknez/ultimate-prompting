## 8. Toolchain And Platform Matrix

Resolve actual versions instead of reading intended versions only.

- Capture `flutter --version --machine`, `dart --version`, `flutter doctor -v`, channel, engine revision, and SDK installation provenance.
- Compare local, CI, release, and developer SDKs; detect floating channels, mutable containers, unpinned setup actions, and hidden FVM/asdf/mise behavior.
- Resolve Android Gradle Plugin, Gradle, Kotlin, Java, Android SDK/NDK, CMake, min/target/compile SDK, ABI, packaging, and signing tools.
- Resolve Xcode, Swift, CocoaPods or Swift Package Manager, deployment targets, architectures, simulator/device differences, provisioning, and notarization tools.
- Resolve browser versions, JavaScript or Wasm compiler mode, renderer, web server/CDN, service worker, headers, compression, and source-map pipeline.
- Resolve Visual Studio workloads, Windows SDK, MSVC, CMake, NuGet, MSIX/installer tooling, certificate, and architecture targets.
- Resolve macOS deployment target, Xcode command-line tools, entitlements, hardened runtime, signing identity, notarization, and package format.
- Resolve Linux distribution baseline, compiler, CMake/Ninja, GTK, system libraries, packaging format, sandbox/store runtime, and architecture targets.
- Verify that every claimed platform is built, installed, launched, tested, monitored, supported, and recoverable, or reduce the support claim.

