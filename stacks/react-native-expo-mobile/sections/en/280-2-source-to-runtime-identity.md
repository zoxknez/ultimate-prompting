## 2. Source-To-Runtime Identity

### 2.1 Identity Chain
- Link repository URL, commit, dirty state, submodules, workspace graph, lockfile digest, package-manager version, Node binary, and environment.
- Record React Native, Expo SDK, React, Hermes, Metro, Expo CLI, EAS CLI, Gradle, Android Gradle Plugin, Kotlin, JDK, NDK, Xcode, Swift, CocoaPods, and Ruby identities.
- Capture generated Codegen outputs, Expo prebuild outputs, config-plugin modifications, Podfile.lock, Gradle dependency graphs, native assets, and binary frameworks.
- Link AAB, APK, IPA, archive, dSYM, mapping file, native symbols, JavaScript bundle, Hermes bytecode, source maps, update manifest, and artifact digest.
- At runtime expose or retain app version, native build number, runtimeVersion, update ID, channel, branch, deployment revision, architecture, and environment safely.
- Prove that telemetry, crash symbols, source maps, store records, and OTA metadata resolve to the same release identity.

### 2.2 Reproducibility And Drift
- Reproduce dependency installation from a clean checkout with the committed package manager and immutable lockfile mode.
- Run Expo config and prebuild inspection twice and compare outputs to detect non-deterministic config plugins or hidden local state.
- Compare generated native projects with committed projects and classify intentional ownership, drift, and regeneration consequences.
- Compare local, CI, EAS, and store builds for toolchain, environment, credentials, flags, native dependencies, bundle content, and artifact hashes.
- Treat Expo Go, development build, debug build, internal distribution build, and store release as different products until equivalence is demonstrated.
- Report any source, generated project, dependency, artifact, deployed revision, or installed-runtime mismatch as an explicit drift finding.

