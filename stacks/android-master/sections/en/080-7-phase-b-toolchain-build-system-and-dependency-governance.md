## 7. Phase B - Toolchain, Build System And Dependency Governance

### 7.1 Toolchain Compatibility Matrix

1. Resolve actual Android Studio, AGP, Gradle Wrapper, JDK, Kotlin, KSP, Compose compiler plugin, SDK, Build Tools, NDK, CMake, and major plugin versions.
2. Verify official compatibility for the exact versions in use.
3. Detect version drift among local development, CI, release machine, Docker image, remote cache, and developer documentation.
4. Verify Java toolchains, Gradle daemon JDK, `JAVA_HOME`, Kotlin JVM target, desugaring, and bytecode targets are coherent.
5. Verify the wrapper distribution URL, checksum, and executable scripts are controlled and reviewable.
6. Detect dynamic plugin or dependency versions, changing snapshots, mutable repositories, unpinned Git dependencies, and repository-order risk.
7. Check deprecated AGP APIs, legacy Variant APIs, custom transforms, eager configuration, configuration-cache blockers, and AGP 10 migration risk.
8. Verify KAPT and KSP usage, generated-code determinism, incremental processing, and compatibility.
9. Do not upgrade the toolchain until the current baseline is captured and the upgrade has a specific purpose.

### 7.2 Build Logic, Modules And Variants

1. Verify configuration is centralized only where it improves correctness and does not obscure module ownership.
2. Check convention plugins for hidden variant behavior, duplicated flags, task mutation, and configuration-time I/O.
3. Verify every product flavor and build type receives the intended application ID, resources, endpoints, keys, feature flags, manifests, and signing.
4. Check flavor dimensions and dynamic-feature variant parity.
5. Verify debug-only dependencies and tools cannot enter release variants.
6. Verify test, benchmark, staging, internal, and release variants are not accidentally equivalent or mixed.
7. Inspect manifest merge reports and resource merge conflicts for each material variant.
8. Check duplicate classes, dependency constraints, platform or BOM alignment, capabilities, excludes, and dependency substitutions.
9. Verify build cache, configuration cache, parallelism, workers, and remote cache do not compromise correctness or secret safety.
10. Measure sync and build bottlenecks before optimizing them.

### 7.3 Dependency And SDK Governance

1. Produce a dependency inventory from resolved graphs, not only declared dependencies.
2. Identify direct, transitive, bundled, native, code-generated, build-time, test, and runtime dependencies.
3. Record versions, provenance, licenses, update channel, maintenance status, known advisories, and data-processing behavior.
4. Check AndroidX, Compose BOM, Firebase BOM, Kotlin BOM, Media3, Room, Navigation, Hilt, WorkManager, OkHttp, and other families for mixed incompatible versions.
5. Verify dependency verification, checksums, repository restrictions, lockfiles where suitable, and supply-chain controls.
6. Identify SDKs that add permissions, exported components, providers, receivers, startup initializers, network traffic, native code, trackers, or WebViews.
7. Verify SDK initialization is necessary, deferred where appropriate, consent-aware, and disabled in unsupported environments.
8. Remove dependencies only after proving they are unused and understanding reflection, manifest, code generation, resource, and native references.

