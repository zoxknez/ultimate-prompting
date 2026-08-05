## 7. Repository, Architecture, And Ownership

### 7.1 Audit Scope

1. Map packages, application entrypoints, UI layers, domain services, data access, infrastructure adapters, workers, helpers, plugins, tests, packaging, and installer code.
2. Document process, thread, event-loop, QObject, model/view, QML, WebEngine, database, file, network, device, and privileged-helper boundaries.
3. Identify global state, service locators, singleton objects, circular imports, import-time side effects, hidden ownership, and mutable cross-feature dependencies.
4. List critical user journeys and business invariants with their source modules, UI entrypoints, data, side effects, and recovery path.
5. Distinguish UI state, domain state, persisted state, cached state, derived state, and operating-system state.
6. Record owners for code, data formats, signing, installer, update feed, telemetry, privacy, support, and incident response.

### 7.2 Required Verification

1. Produce architecture, ownership, data-flow, privilege, and lifecycle diagrams backed by source and runtime evidence.
2. Trace at least one critical journey end to end through UI, signals, services, persistence, external calls, error handling, telemetry, and recovery.
3. Confirm that dependency direction and ownership prevent UI code, plugin code, or background work from bypassing domain authorization and invariants.
4. Identify abandoned modules, duplicate implementations, unreachable code, stale generated output, and packaging-only code paths.
5. Verify that every critical resource has one explicit lifecycle owner and every cross-boundary call has a contract.

