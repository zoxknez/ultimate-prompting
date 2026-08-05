## 1. Inventory, Lifecycle, And Reproducible Baseline

Map Maven/Gradle wrapper and versions, Java toolchain, `pom.xml`/`build.gradle`, dependency management, repositories, lock files, profiles, compiler flags, annotation processors, test suites, Spring Boot/Framework/Security versions, MVC versus WebFlux, entry point, auto-configuration exclusions, beans, filter chains, controllers/routes, DTO validation, JPA contexts and migrations, jobs/schedulers, queues, cache, authentication, configuration, Actuator, deployment, CI/CD, and tests.

Verify the exact Java and Spring Boot versions against current supported lifecycle and current patch release. At audit time verify actual system requirements instead of hard-coding them; for example, Spring Boot 4.1 requires Java 17 or higher. Distinguish JVM JAR, WAR, container, and GraalVM native-image packaging, and validate their separate runtime, reflection, resource, observability, memory, and startup constraints.

Create the flow map `client -> CDN/load balancer/reverse proxy -> servlet/reactive server -> filter chain -> controller/router -> authentication -> authorization -> validation -> service -> transaction -> database/cache/queue/external dependency -> response`.

Run deterministic dependency resolution, compilation, static analysis, formatting verification where configured, unit/integration/security/contract tests, packaged artifact startup, migration status, health/readiness probes, dependency vulnerability/SBOM checks, and graceful-shutdown tests where supported. Record commands, tool/JDK versions, exit codes, initial failure, and whether cause is code, configuration, secret, external dependency, or local environment.

