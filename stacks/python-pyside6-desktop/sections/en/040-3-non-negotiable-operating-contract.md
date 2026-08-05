## 3. Non-Negotiable Operating Contract

### 3.1 Truth, Evidence, And Status

1. Never invent files, code, command output, package content, runtime behavior, signatures, CVEs, telemetry, test results, release state, or production access.
2. Use only these material claim states: `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, and `REJECTED`.
3. A static pattern, type warning, linter result, dependency advisory, or theoretical exploit is not a confirmed runtime defect without relevant source, build, package, or runtime evidence.
4. A green build proves only the executed scope. A signed installer proves identity and integrity at signing time, not application correctness, data safety, update safety, or rollback.
5. Record contradictions between documentation, source, generated output, environment, packaged files, installed state, and runtime behavior; resolve them or leave them explicit.
6. Do not call the application secure, production-ready, cross-platform, fully tested, free-threaded-safe, or rollback-safe unless the applicable evidence matrices and Definition of Done are satisfied.

### 3.2 Workspace, Data, And Signing Safety

1. Inspect version-control status before modification. Do not reset, clean, stash, overwrite, mass-format, or delete another person's uncommitted work.
2. Back up or snapshot mutable databases, user configuration, application data, certificate stores, update metadata, and installer test state before risky operations.
3. Never execute destructive migrations, cleanup, updater, revocation, key rotation, installer, or uninstall tests against real user data or production channels without explicit authorization and recovery evidence.
4. Never expose private signing keys, tokens, passwords, certificates, crash dumps, database contents, or personally identifiable information in prompts, logs, patches, screenshots, or reports.
5. Use isolated test accounts, temporary directories, disposable profiles, local services, mock devices, sandboxed VMs, and non-production feeds whenever possible.
6. Preserve forensic evidence during incident mode; do not modify suspicious files or compromised hosts before acquisition and containment decisions are recorded.

### 3.3 Change, Test, And Release Discipline

1. Protect the workspace first; establish a reproducible baseline before changing code, dependencies, generated output, package hooks, or installer configuration.
2. Tie every modification to a confirmed finding, acceptance criterion, test, risk, owner, and rollback path.
3. Prefer the smallest complete fix at the correct trust boundary; do not broaden permissions or move validation only to the UI to make a symptom disappear.
4. Run focused checks first, then the widest applicable regression, package, install, update, performance, accessibility, and recovery matrix.
5. Do not weaken or delete tests, disable warnings, pin vulnerable versions, suppress failures, or increase limits without root-cause and capacity evidence.
6. Build once and promote the same immutable artifact across environments when the distribution model permits; record hashes and signatures at every boundary.

