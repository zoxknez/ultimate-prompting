## Technology Overlays And Final Production Decision

### Mandatory Overlay Selection

- Apply the Servlet MVC overlay when the system uses Tomcat, Jetty, WAR deployment, blocking controllers, servlet filters, or traditional JDBC request processing.
- Apply the WebFlux/Reactor overlay when the system uses Netty, reactive controllers, reactive clients, R2DBC, streaming, or mixed imperative/reactive flows.
- Apply the messaging/worker overlay when correctness depends on listeners, consumers, schedulers, Spring Batch, Quartz, integration flows, or long-running jobs.
- Apply the library/starter overlay when publishing reusable auto-configuration, BOMs, annotations, processors, plugins, or APIs consumed by unknown applications.
- Apply the native-image overlay whenever GraalVM, AOT, CDS, CRaC, or startup-optimized packaging changes runtime behavior or recovery assumptions.

### Evidence-Driven Repair Workflow

- Create a finding before a material fix with severity, evidence level, affected invariant, exploit or failure path, scope, root cause, owner, and acceptance test.
- Prefer the smallest architectural fix that restores the violated contract without hiding symptoms, weakening security, or creating silent fallback behavior.
- After each fix, run focused tests first, then affected integration and migration tests, then security, concurrency, performance, packaging, and rollback regressions proportional to risk.
- Record commands, outputs, artifact identity, environment, before/after evidence, remaining uncertainty, and any deferred work with owner and deadline.
- Do not close a finding because code changed; close it only when the failure path is disproved or controlled by repeatable evidence.

### Production Decision Rule

- Return `NOT READY` when any unresolved P0 or P1 finding, untested critical invariant, unverified tenant boundary, uncontrolled migration, unknown artifact identity, or unproven restore blocks safe release.
- Return `CONDITIONALLY READY` only when remaining risks are explicitly bounded, owned, time-limited, monitored, reversible, and accepted by the proper authority.
- Return `READY` only when critical evidence matrices are complete, mandatory failure scenarios pass, release and rollback are rehearsed, restore is proven, and runtime identity is correlated.
- State separate confidence for source correctness, build integrity, runtime security, data integrity, operational resilience, migration safety, and recovery readiness.
- Never replace missing evidence with confidence language, tool prestige, framework defaults, scanner scores, test counts, or a green pipeline.

