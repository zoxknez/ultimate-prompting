## Phase B - Project And Build-System Inventory

Map Maven root/child modules, Gradle root/subprojects/included builds, source and test source sets, generated sources, shared/domain/API/persistence/messaging/batch/infrastructure/test-fixture modules, migrations, native hints, Docker/Kubernetes/Terraform/Helm configuration, and CI workflows. Show dependency direction and identify cycles, framework leakage into the domain, unclear ownership, duplicated models, manually changed generated code, and inactive modules.

Choose one actual build path; never run Maven and Gradle randomly. For Maven inspect wrapper, parent/BOM, `dependencyManagement`, profiles, Enforcer, toolchains, compiler `release`, Surefire/Failsafe, resource filtering, plugins, repositories, snapshots, shading/repackaging, and generated sources. When safe, use `./mvnw --version`, `help:active-profiles`, targeted `help:effective-pom`, `dependency:tree`, and `dependency:analyze`. Use global `mvn` only to compare environments explicitly.

For Gradle inspect wrapper/checksum, plugins, version catalog, constraints/platform, toolchain, source/target compatibility, test suites/source sets, configuration/build cache, custom tasks, dependency locking/verification, repository content filters, dynamic/changing versions, and annotation processing. When safe use `./gradlew --version`, `projects`, `tasks`, `javaToolchains`, `buildEnvironment`, `dependencies`, and `properties`; use `dependencyInsight` only for a specific question.

Classify dependencies as Boot-managed, directly versioned, transitive, obsolete, conflicting, unused, runtime/compile/annotation/test-only, native-incompatible, confirmed-CVE, preview, or non-standard repository dependencies. Check Spring Cloud/Boot mapping, Jackson, Hibernate/driver, Reactor/Netty, logging, Security, validation, cache/messaging clients, APM/OpenTelemetry, and test libraries. Never override an individual Spring BOM-managed version without a documented reason.

