## 39. Production Readiness Checklist

1. Source-to-installed-runtime identity is continuous and reproducible for every supported release target.
2. Exact Python, PySide6, Qt, native libraries, packaging tools, and operating-system support are current and verified.
3. Architecture, ownership, process, thread, QObject, model, QML, WebEngine, IPC, data, privilege, and update maps are complete.
4. No unresolved P0 or P1 finding remains without explicit authorized acceptance and containment.
5. GUI thread, event loops, workers, tasks, subprocesses, helpers, cancellation, shutdown, and stale-result protection are verified.
6. QObject ownership, destruction, signals, slots, reentrancy, model/view notifications, and UI state are correct under stress.
7. Authentication, authorization, tenant/account isolation, secret storage, privacy, and privileged actions are verified with negative tests.
8. Local data, migrations, concurrency, offline queues, corruption handling, backup, retention, deletion, and restore are verified.
9. Files, archives, parsers, plugins, scripts, WebEngine content, deep links, IPC, devices, and OS inputs are constrained and tested.
10. Packaging includes only intended files and native components; package, installer, signature, notarization, and installed state are verified.
11. Fresh install, upgrade matrix, interrupted update, rollback/forward repair, uninstall, and clean-machine restore are tested.
12. Performance, responsiveness, memory, CPU, GPU, disk, network, capacity, and low-resource behavior meet measured budgets.
13. Accessibility, localization, high DPI, multiple monitors, screen readers, keyboard operation, RTL, IME, and reduced motion are tested.
14. Observability identifies exact release bytes and diagnoses critical GUI, worker, update, migration, data, and native failures without leaking sensitive data.
15. CI/CD protects trusted release boundaries, verifies dependencies, produces SBOM/provenance, and promotes immutable artifacts.
16. Rollout, abort, emergency release, signing-key compromise, update-feed compromise, incident containment, and trusted rebuild are documented and exercised.
17. Every material fix has focused regression, packaged verification, owner, risk, and rollback.
18. All applicable evidence matrices and adversarial scenarios are complete or explicitly blocked with owner and acceptance plan.
19. Final diff is narrow, reviewable, documented, and free of unrelated changes or weakened tests.
20. Final report contains exact evidence, commands, artifacts, hashes, results, blockers, residual risk, owners, and authoritative sources.

