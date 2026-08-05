## 30. Production Readiness Checklist
- [ ] Authorization, scope, support claims, and evidence ceiling are recorded.
- [ ] Source-to-runtime identity is complete for every production artifact and OTA update.
- [ ] Toolchains, dependency graphs, generated projects, and native projects are reproducible and reviewed.
- [ ] New Architecture, Codegen, native modules, Fabric, JSI, ABI, and memory boundaries are verified.
- [ ] Critical journeys, invariants, authorization, tenant isolation, idempotency, and reconciliation pass.
- [ ] Storage, offline, migration, backup, restore, account switch, and deletion behavior pass.
- [ ] Network, realtime, background, push, permissions, device, file, media, and WebView contracts pass.
- [ ] Android release build, artifact inspection, signing, installation, upgrade, device, performance, accessibility, and recovery pass.
- [ ] Apple archive, signing, privacy, installation, upgrade, device, performance, accessibility, and recovery pass.
- [ ] EAS build profiles, credentials, environment, update runtime, code signing, channels, and rollout are verified.
- [ ] Crash, ANR, hang, source-map, native-symbol, SLI, alert, dashboard, and runbook readiness pass.
- [ ] CI/CD trust, SBOM, provenance, immutable artifact promotion, store submission, and approval gates pass.
- [ ] Staged rollout, quantitative abort criteria, OTA rollback, native rollback, forward fix, and kill switches are exercised.
- [ ] Isolated restore, RPO, RTO, data reconciliation, incident containment, credential revocation, and trusted rebuild are exercised.
- [ ] All P0 and P1 findings are closed or the decision is NOT_READY or INCIDENT.
- [ ] Every accepted P2 or P3 risk has owner, deadline, compensating control, monitoring, and next verification date.

