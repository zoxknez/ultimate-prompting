## Phase 4 - TypeScript, Module Semantics, And Generated Contracts

Prove that editors, CI, tests, generators, and Next build check the same supported TypeScript contract.

### Audit Requirements

- Inventory every tsconfig, project reference, path alias, moduleResolution, target, lib, JSX mode, strictness override, and emitted boundary.
- Detect noCheck, skipLibCheck, allowJs, transpile-only paths, unchecked declarations, and build tools that bypass tsc.
- Verify ESM/CJS boundaries, conditional exports, server/client entrypoints, dynamic imports, and test resolution.
- Review unsafe any, assertions, non-null operators, unchecked indexes, and schema/type drift at trust boundaries.
- Generate API, database, GraphQL, protobuf, and validation types deterministically.
- Treat a TypeScript major as a compiler, editor, linter, bundler, generator, library, and source migration.

### Required Evidence

- Executed typecheck and effective compiler config for every package.
- List of build/test paths that transpile without full checking.
- Generated contract provenance and drift check.
- Compatibility matrix for current and planned TypeScript lines.

### Mandatory Failure And Acceptance Tests

- Seed invalid generated output and prove CI detects it.
- Resolve the same package through editor, build, tests, and production bundle.
- Build a controlled upgrade branch on all supported tooling.
- Test malformed runtime input that satisfies an incorrectly broad static type.

