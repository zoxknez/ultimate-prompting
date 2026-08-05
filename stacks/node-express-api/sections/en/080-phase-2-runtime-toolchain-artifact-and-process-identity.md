## Phase 2 - Runtime, Toolchain, Artifact, And Process Identity

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Resolve the actual Node binary, version, release line, architecture, libc, OpenSSL, ICU, V8, and native-module ABI.
- Compare local, editor, CI, test, build, container, serverless, migration, worker, and production runtimes.
- Verify engines, packageManager, Corepack policy, version files, Docker base image, platform runtime, and process-manager configuration.
- Prove which commit and dependency graph produced each artifact and which digest produced each deployment revision.
- Correlate build ID, image digest, deployment ID, config revision, schema version, and running PID or function revision.
- Inspect native addons, prebuilt binaries, WASM, and downloaded tools for platform and ABI compatibility.

### Required Evidence

- Produce and preserve the runtime and ABI matrix.
- Produce and preserve the artifact provenance chain.
- Produce and preserve deployment-to-process correlation evidence.

### Mandatory Failure And Acceptance Tests

- Prove that CI and production report the intended runtime.
- Prove that a wrong-architecture native module fails before traffic.
- Prove that the running process can be tied to an immutable artifact.

