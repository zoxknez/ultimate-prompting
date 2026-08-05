## 8. Phase C - Build, Release, Signing And Packaging

### 8.1 Baseline Build Matrix

Run only applicable tasks and record exact results:

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

1. Prefer targeted module and variant tasks before an expensive full build.
2. Do not use `clean` as a default diagnostic step if it would destroy useful incremental evidence.
3. Separate source, configuration, dependency, resource, manifest, code generation, dexing, shrinking, packaging, signing, install, runtime, and test failures.
4. Preserve reports, stack traces, scan references, test XML, HTML, APKs, AABs, mappings, native symbols, and baseline profiles.
5. Confirm release tasks, not only debug tasks.

### 8.2 Release Variant And R8

1. Verify release uses the intended endpoints, feature flags, logging level, analytics project, network security, certificates, database name, and update channel.
2. Verify minification, optimization, resource shrinking, and obfuscation are enabled or intentionally justified.
3. Review app keep rules, consumer rules, generated rules, reflection, serialization, JNI, navigation, dependency injection, and WebView JavaScript interfaces.
4. Use R8 diagnostics and configuration analysis where supported.
5. Investigate missing classes and keep-rule growth instead of adding broad `-keep class ** { *; }` rules.
6. Verify release-only code paths, desugaring, service loaders, dynamic features, split installs, and native loading.
7. Verify mapping files and native debug symbols are archived and uploaded to the crash platform.
8. Verify reproducibility or at least traceable provenance from source revision to signed artifact.
9. Compare debug and release behavior on critical journeys.

### 8.3 Signing, Versioning And Update Safety

1. Verify debug, upload, app-signing, enterprise, and OEM keys are separated and access-controlled.
2. Verify no debug keystore or hardcoded signing password is used for production.
3. Verify key aliases, certificate validity, rotation plan, backup, ownership, and least privilege.
4. Verify version codes are monotonic for all tracks, ABIs, splits, and channels.
5. Verify application ID and signing continuity support updates of installed production versions.
6. Test upgrade from at least the oldest supported production schema and a representative recent version.
7. Test downgrade behavior only where the distribution model permits it.
8. Verify rollback does not corrupt data or strand users on incompatible schemas.
9. Verify Play App Signing, internal app sharing, enterprise signing, or sideload procedures from actual configuration, not assumption.

### 8.4 APK, AAB, Splits And Native Libraries

1. Inspect final APK and AAB contents with APK Analyzer, bundletool, or equivalent.
2. Verify manifest, resources, assets, native libraries, DEX count, permissions, features, package visibility, and split configuration.
3. Verify ABI filters do not exclude supported devices or package unnecessary ABIs.
4. Verify every packaged `.so` has known provenance and matches supported ABIs.
5. Verify 16 KB ELF segment alignment and package alignment for every native library, including transitive SDKs.
6. Test on a real or emulator 16 KB environment where applicable and record page-size evidence.
7. Verify JNI assumptions, hardcoded page sizes, memory mapping, native crashes, symbol files, and sanitizer strategy.
8. Verify asset packs, dynamic features, install-time, fast-follow, and on-demand delivery behavior under failure and low storage.
9. Verify compressed and uncompressed native library settings are intentional.

