## Build, Toolchain, And Supply-Chain Verification

### JDK And JVM Identity

- Verify `java -version`, `javac -version`, vendor properties, patch/build, architecture, and the JVM inside the actual release image or host.
- Distinguish the JDK that runs Maven/Gradle, the compilation toolchain, the test JVM, the native-image toolchain, and the production runtime.
- Verify bytecode target and API target separately; `sourceCompatibility`, `targetCompatibility`, `--release`, and toolchain declarations can diverge.
- Review preview/incubator/internal APIs, vendor-specific flags, removed modules, illegal access, native access, and behavior across supported JDK patches.
- Verify quarterly security-update policy, emergency patch process, runtime license/support obligations, rollback, and compatibility test scope.

### Maven Build Trust

- Verify wrapper distribution URL, checksum or signature, Maven version, `.mvn` configuration, build JDK, `toolchains.xml`, `settings.xml`, mirrors, servers, proxies, extensions, and active profiles.
- Inspect effective POM, parent hierarchy, imported BOMs, dependency management, plugin management, repositories, plugin repositories, scopes, classifiers, relocations, and optional dependencies.
- Pin and review compiler, Surefire, Failsafe, Enforcer, Shade, Spring Boot, Jib, native, release, deploy, signing, and publication plugins.
- Verify dependency convergence, duplicate classes, reproducible timestamps, checksums, signatures, repository allow lists, and plugin validation.
- Treat Maven 3.10 and Maven 4 as preview baselines until their current official status and project compatibility are explicitly approved.

### Gradle Build Trust

- Verify wrapper distribution URL and SHA-256, Gradle runtime JVM, Java toolchains, daemon settings, init scripts, included/composite builds, buildSrc, convention plugins, and version catalogs.
- Inspect repositories, exclusive content, dependency verification, locking, constraints, platforms, capabilities, substitutions, dynamic versions, changing modules, and resolution rules.
- Review custom tasks, `Exec` and `JavaExec`, script plugins, generated sources, annotation processors, publication, signing, test suites, configuration cache, and build cache.
- Prove cache keys include all material inputs and that remote caches cannot inject stale, cross-branch, cross-tenant, or untrusted output.
- Verify supported Gradle/JDK and Spring Boot/plugin combinations in the project matrix, not only on one developer machine.

### Generator And Build-Execution Surface

- Inventory Lombok, MapStruct, Querydsl, jOOQ, OpenAPI, protobuf, Avro, annotation processors, bytecode enhancement, GraalVM reachability metadata, and custom generators.
- Treat build plugins, processors, generators, shell commands, native compilers, downloaded tools, and container build steps as executable supply-chain inputs.
- Record source, version, pin, checksum/signature, network access, credentials, generated paths, determinism, and review ownership.
- Regenerate from a clean checkout and compare output; unexplained generated drift blocks a reproducibility claim.

### Dependency And Advisory Analysis

- Resolve the actual graph per profile, source set, target, optional integration, and artifact; a declared dependency list is insufficient.
- Detect dependency confusion, typosquatting, mutable snapshots, untrusted repositories, hidden plugin dependencies, shaded vulnerable code, and duplicate versions.
- Correlate advisories with reachable code, configuration, data, protocol, class loading, reflection, native paths, and deployment exposure.
- Record CVE/advisory, affected range, resolved version, reachability, exploit prerequisites, compensating controls, fix, test, rollout, and residual risk.
- Generate SBOM and provenance where supported, but do not treat either as proof of correctness or non-exploitability.

