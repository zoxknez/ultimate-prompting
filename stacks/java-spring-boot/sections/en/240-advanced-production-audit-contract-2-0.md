## Advanced Production Audit Contract 2.0

This section upgrades the preceding checklist into a source-to-runtime production audit contract. Where wording conflicts, the stricter evidence, safety, compatibility, and recovery requirement in this section prevails.

### Evidence Levels

| Level | Minimum acceptable meaning |
| --- | --- |
| E0 | Claim, roadmap, ticket, documentation, or assumption only. |
| E1 | Static source, build, configuration, schema, or dependency evidence. |
| E2 | Resolved graph, generated source, bytecode, artifact, manifest, digest, signature, or SBOM evidence. |
| E3 | Executed test, local runtime, container, migration rehearsal, or integration evidence. |
| E4 | Staging or production-like load, rollout, telemetry, failure, or rollback evidence. |
| E5 | Production observation, isolated restore, incident drill, or independently reproduced evidence. |

Every material conclusion must state its evidence level. An unconditional production-ready conclusion requires evidence proportionate to the risk, not merely a large number of static findings.

### Evidence Ceiling

- Continue safe discovery when information is missing, but mark every unresolved material claim `UNVERIFIED`.
- State the exact repository, artifact, environment, credential, fixture, workload, approval, telemetry, or operator access needed to raise the evidence level.
- Do not infer production behavior from local IDE startup, a unit test, a green pipeline, a mutable image tag, or a healthy liveness endpoint.
- Do not treat an advisory as exploitable without a reachable path, or treat absence of a scanner finding as absence of risk.

### Source-To-Runtime Identity Chain

Record and correlate:

1. repository, commit, dirty state, submodules, generated sources, and build inputs;
2. JDK vendor, exact version and patch, architecture, license/support model, trust store, locale, timezone, and JVM flags;
3. Maven or Gradle wrapper distribution, checksum, build JVM, toolchains, profiles, properties, repositories, mirrors, plugins, extensions, and init scripts;
4. resolved dependencies, BOMs, locks or verification metadata, annotation processors, generators, shaded classes, native libraries, and agents;
5. bytecode target, JAR/WAR/native image digest, manifest, build info, SBOM, signature or provenance, container layers, and release identifier;
6. deployment revision, configuration version, schema version, runtime process identity, and telemetry release attributes.

Prove that the running process uses the intended artifact and configuration. A source commit and image tag without digest and runtime correlation are incomplete evidence.

### Mandatory Command Log

For every executed command record:

- exact command and working directory;
- local, container, CI, staging, or production-like environment;
- JDK, Maven/Gradle, profile, target, and relevant environment values;
- start/end time or duration, exit code, result summary, and material warnings;
- secret and personal-data redactions;
- whether the command changed source, generated output, dependencies, database state, cache, queue, files, or infrastructure.

For every unexecuted check write: `UNVERIFIED - command not run because [specific reason]`.

