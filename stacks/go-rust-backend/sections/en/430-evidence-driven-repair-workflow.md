## Evidence-Driven Repair Workflow

1. Freeze scope, protect work and data, and establish the evidence ceiling.
2. Reproduce the defect or prove the violated invariant with the smallest safe scenario.
3. Identify root cause across source, generated code, toolchain, dependency, configuration, data, runtime, platform, and operations.
4. Design the smallest safe repair and explicitly reject fixes that only hide symptoms, widen privilege, remove validation, disable checks, or increase capacity without analysis.
5. Add a regression test plus concurrency, failure, security, migration, compatibility, or recovery coverage appropriate to the cause.
6. Execute focused checks, then the supported language, target, tag/feature, integration, artifact, load, deployment, and rollback matrix.
7. Review the final diff, dependency and lock changes, generated output, artifacts, telemetry, residual risk, ownership, and operational documentation.

