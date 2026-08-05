## Phase 4 - TypeScript, JavaScript, ESM, CJS, And Build Semantics

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory every tsconfig, project reference, target, lib, module, moduleResolution, strictness override, and path alias.
- Prove which compiler or transpiler handles production code, tests, workers, migrations, scripts, and generated sources.
- Detect transpile-only, noCheck, skipLibCheck, stale declaration, decorator, and source-map risks.
- Audit ESM and CJS boundaries, extension resolution, exports, conditional exports, dynamic import, require hooks, and dual-package hazards.
- Verify build output contains intended files and no unintended secrets, fixtures, source, or test data.
- Treat types as developer evidence only; validate all runtime input and external output independently.

### Required Evidence

- Produce and preserve the compiler, transpiler, and module-resolution matrix.
- Produce and preserve generated-code and artifact-content evidence.
- Produce and preserve old and new client and deployment compatibility results.

### Mandatory Failure And Acceptance Tests

- Prove that the production build performs intended type checks.
- Prove that ESM and CJS entrypoints load in the target runtime.
- Prove that runtime validation rejects data that only appears type-correct.

