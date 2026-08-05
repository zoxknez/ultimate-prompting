## 3. Toolchain, Dependencies, And Supply Chain

### 3.1 Version And Compatibility Matrix
- Resolve exact versions from lockfiles and generated native projects rather than README examples or semver ranges.
- Validate the supported matrix among React Native, Expo SDK, React, Hermes, Metro, Expo Router, Reanimated, Screens, Gesture Handler, and native libraries.
- Check minimum Node, JDK, Android SDK, NDK, Xcode, iOS deployment target, CocoaPods, Ruby, and operating-system requirements.
- Separate framework compatibility from third-party library, config-plugin, native SDK, store-policy, and device compatibility.
- Classify unsupported, end-of-cycle, prerelease, canary, nightly, forked, patched, and unmaintained dependencies.
- Do not recommend a broad upgrade without a compatibility graph, migration sequence, representative release tests, rollout plan, and rollback plan.

### 3.2 Package And Native Supply-Chain Trust
- Audit npm registry configuration, private scopes, lockfile integrity, lifecycle scripts, Git dependencies, local paths, overrides, patches, and workspace links.
- Audit Maven, Gradle Plugin Portal, CocoaPods, Swift Package Manager, binary frameworks, XCFrameworks, NDK libraries, and downloaded tools.
- Inspect install, postinstall, prepare, patch-package, codegen, config-plugin, Gradle, Ruby, shell, and Xcode build scripts as executable code.
- Require provenance, ownership, maintenance status, vulnerability status, license, and revocation path for critical packages and native SDKs.
- Generate and retain an SBOM that includes JavaScript, Java/Kotlin, Objective-C/Swift, C/C++, native binaries, and bundled assets where feasible.
- Define an emergency response for compromised package, config plugin, native SDK, signing identity, update key, build image, or CI runner.

