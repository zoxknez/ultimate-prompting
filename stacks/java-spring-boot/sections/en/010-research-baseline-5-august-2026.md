## Research Baseline - 5 August 2026

This baseline is a starting point, not a substitute for verification at execution time. Re-check current first-party sources before making a recommendation or change.

| Component | Status on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| Java | Java 25 is the current LTS; Java 26 is the latest GA feature release. | OpenJDK/Oracle roadmap, JDK vendor, patch level, and production runtime. |
| Spring Boot | The stable line is 4.1.0; it requires Java 17-26, Spring Framework 7.0.8+, Tomcat 11/Servlet 6.1 or Jetty 12.1; GraalVM 25+ is required for native images. | Project version, supported minor line, Spring portfolio, and migration guide. |
| Spring Boot 4 migration | Jakarta EE 11, Servlet 6.1, and Spring Framework 7; removed deprecated APIs require compatibility review. Older projects should first reach the latest Boot 3.5.x patch. | Breaking changes, Spring Cloud release train, plugins, agents, and rollback. |
| Spring Boot support | A major version receives at least three years of support, but only a supported minor line; a minor receives at least 12 months of OSS support. | Official support policy and any commercial support. |
| Maven | Maven 3.9.16 is the recommended stable version; Maven 3.10.0-rc-1 and 4.0.0-rc-6 are previews, not production baselines. | Wrapper, checksum, build JDK, and active profiles. |
| Gradle | Gradle 9.6.1 is the current stable release. | Wrapper, checksum, plugin compatibility, and toolchain. |
| Observability | Spring Boot uses Micrometer Observation for metrics and tracing, with OpenTelemetry integration; Actuator provides production endpoints. | Actual instrumentation, cardinality, propagation, and endpoint exposure. |
| Artifacts | Spring Boot supports Dockerfiles, Cloud Native Buildpacks, graceful shutdown, and GraalVM native/AOT flows. | The artifact actually deployed, image, shutdown, and native constraints. |

