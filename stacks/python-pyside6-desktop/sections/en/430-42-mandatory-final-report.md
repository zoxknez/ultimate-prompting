## 42. Mandatory Final Report

1. Executive summary and verdict: `READY`, `READY_WITH_CONDITIONS`, `NOT_READY`, or `INCIDENT`, with evidence ceiling.
2. Application and release context: purpose, critical journeys, platforms, architectures, Python/Qt stack, distribution, identities, data, integrations, and constraints.
3. Source-to-installed-runtime identity chain with exact commits, environments, dependency graph, generated code, artifact hashes, signatures, installed paths, and unresolved breaks.
4. Architecture and trust maps: process, thread, event loop, QObject, UI/model, QML/WebEngine, IPC/helper, data, device, privilege, installer, and update.
5. Version/support table: project, resolved, packaged/runtime, current supported line, status, compatibility, action, and primary source.
6. Findings table: `ID | P0-P3 | confidence | evidence | platform | file/symbol | cause | impact | fix | test | rollback | status | owner`.
7. Implemented changes: exact files, dependencies, generated output, configuration, permissions, migrations, package/installer/update changes, and regression risk.
8. Actual commands: command, directory, environment/tool versions, platform, exit code, output summary, artifacts, and conclusion.
9. Test matrix: unit, integration, GUI, package, install, update, adversarial, performance, accessibility, rollback, restore, and blocked checks.
10. Package and distribution verification: contents, native libraries, hashes, signatures, notarization, stores, channels, update metadata, cohort, install, and uninstall.
11. Data and recovery results: migrations, concurrent/duplicate/interrupted operations, corruption, backup, restore, RPO, RTO, rollback, forward repair, and reconciliation.
12. Security and privacy summary: authorization, account isolation, secrets, files, plugins, WebEngine, IPC, devices, local services, telemetry, supply chain, and residual risk.
13. Operational readiness: budgets, telemetry, alerts, runbooks, staged rollout, abort, emergency release, key compromise, incident containment, and owners.
14. Remaining work grouped as `blocks production`, `needed soon`, `planned refactor`, and `optional`, with owner, dependency, acceptance criterion, and target date.
15. External sources consulted: title, URL, version/status, access date, and decision informed.

