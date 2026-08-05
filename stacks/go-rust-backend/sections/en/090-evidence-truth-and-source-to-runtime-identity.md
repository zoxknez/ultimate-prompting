## Evidence, Truth, And Source-To-Runtime Identity

### Evidence Levels

| Level | Meaning | Examples |
| --- | --- | --- |
| `E0` | Claim only; no inspectable evidence. | README, ticket, verbal expectation. |
| `E1` | Static repository or configuration evidence. | Source, manifest, module file, lock file. |
| `E2` | Resolved build or generated-output evidence. | Dependency graph, generated code, linker map, build metadata. |
| `E3` | Executed test, analyzer, benchmark, or controlled reproduction. | Exit code, logs, race report, Miri finding, packet trace. |
| `E4` | Release-like artifact and target-environment evidence. | Binary hash, signature, container digest, target smoke, load or failover run. |
| `E5` | Observed production behavior or proven recovery. | Telemetry tied to revision, canary result, restore drill, incident evidence. |

- Use the strongest available evidence but never promote a conclusion above the evidence actually obtained.
- Record command, working directory, environment, toolchain, target, tags or features, fixtures, exit code, duration, and material output for every executed check.
- Separate `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, and `REJECTED`; do not use vague green, looks fine, probably, or safe wording.

### Source-To-Runtime Identity Chain

- Record repository URL, commit, branch or tag, dirty state, submodules, vendored code, generated code, patches, and untracked inputs.
- Resolve the exact Go and Rust toolchains selected locally, in CI, in builders, in containers, and in release automation; record automatic toolchain download or override behavior.
- Capture module/workspace graphs, checksums, lock files, replacement or patch directives, build scripts, code generators, proc macros, C toolchains, system libraries, and linker inputs.
- Record build tags, environment variables, `GOOS`, `GOARCH`, `CGO_ENABLED`, target triples, Cargo features, profiles, `RUSTFLAGS`, linker flags, LTO, panic strategy, and reproducibility controls.
- Hash and identify binaries, libraries, debug symbols, source maps, SBOMs, signatures, provenance, container images, package manifests, and deployment revisions.
- Verify runtime version, build commit, feature or tag set, configuration source, loaded shared libraries, kernel and libc assumptions, architecture, endpoint peers, and schema compatibility.
- Reconcile source, artifact, registry, deployment, process, telemetry, database migration, and recovery identities before a release verdict.
- Detect mutable tags, rebuilds under the same version, stale generated code, wrong symbols, wrong image, wrong config, partial rollout, mixed schema, and old/new binary coexistence.

### Finding Quality Contract

| Required field | Requirement |
| --- | --- |
| Identity | Stable finding ID, language, subsystem, owner, and affected artifact or deployment. |
| Evidence | File and symbol, command, target, tags/features, data or traffic preconditions, artifact ID, and E0-E5 level. |
| Cause | Root cause and violated invariant, not only symptom or scanner text. |
| Impact | Correctness, security, availability, data, latency, cost, compatibility, and recovery consequences. |
| Repair | Smallest safe repair, alternatives, rejected shortcuts, owner, migration, and rollout constraints. |
| Verification | Regression, negative, race or memory check, target matrix, load/failure scenario, rollout gate, and rollback trigger. |

