## Spring Boot 4 And Framework 7 Migration Audit

### Migration Baseline And Compatibility

- Establish the exact current Spring Boot, Spring Framework, Spring Security, Spring Data, Spring Cloud, Hibernate, Jackson, Jakarta, JDK, build-plugin, and third-party starter matrix.
- Before a major migration, update to the latest supported patch of the current major line and remove deprecations with tests rather than carrying unknown behavior forward.
- Verify every starter, BOM, plugin, agent, test library, annotation processor, servlet container, native library, and platform service against the target line.
- Separate compile compatibility, test compatibility, runtime compatibility, operational compatibility, schema compatibility, client compatibility, and rollback compatibility.
- Maintain a migration finding register with owner, blocker, workaround, permanent fix, test, rollout stage, and residual risk.

### Boot 4 Specific Breaking Surfaces

- Audit Jakarta EE 11 and Servlet 6.1 changes, removed deprecated APIs, package and signature changes, servlet container support, filters, listeners, multipart, async, and error dispatch.
- Review starter modularization and renamed or split dependencies; prove the resolved classpath contains intended capabilities and excludes accidental legacy modules.
- Treat Jackson 3 adoption as a contract migration involving packages, modules, defaults, customizations, tests, persisted payloads, events, caches, and external clients.
- Verify embedded-server changes, including removal or replacement of unsupported servers, connector behavior, access logs, compression, TLS, HTTP/2 or HTTP/3, and graceful shutdown.
- Review property renames/removals, Actuator changes, observability changes, test support, AOT/native behavior, and custom auto-configuration registration.

### Migration Execution And Rollback

- Build a dual-line test matrix for current and target versions using production-like configuration, data, dependencies, clients, brokers, databases, and deployment topology.
- Run contract, migration, security, concurrency, performance, startup, shutdown, memory, failover, and rollback tests before broad rollout.
- Use staged changes that isolate framework upgrade, JDK upgrade, schema change, dependency replacement, serialization change, and infrastructure change where practical.
- Prove old and new versions can coexist for the required window or explicitly design a traffic stop and data cutover with recovery checkpoints.
- Retire temporary compatibility flags, dual writes, adapters, suppressions, and old dependencies with owners and deadlines after verified stabilization.


