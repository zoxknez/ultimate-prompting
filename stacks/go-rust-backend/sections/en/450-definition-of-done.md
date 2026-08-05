## Definition Of Done

Work is complete only when applicable items are marked with evidence or `NOT_APPLICABLE`:

1. Technology path confirmed; all relevant modules/workspaces/crates inventoried.
2. Toolchain, lifecycle, and support status verified from current sources.
3. Dependency graph mapped; supply chain reviewed.
4. Initial build/test baseline and production artifact actually built.
5. Target/feature/tag compatibility verified or marked UNVERIFIED.
6. Critical flows mapped.
7. Every reported problem has evidence; cause separated from symptom.
8. P0/P1 fixed or have containment and recovery; fixes have regression tests.
9. Go concurrency checked with the race detector where possible.
10. Rust unsafe has documented safety invariants; Miri/sanitizer limits are clear.
11. Goroutine/task lifecycle and shutdown verified; cancellation/timeout propagated.
12. Concurrency bounded to dependency capacity.
13. Transactions and idempotency verified; migrations have rollout/recovery plan.
14. Security trust boundaries tested; secrets neither disclosed nor baked into artifacts.
15. Performance not declared without measurement.
16. Observability enables diagnosis; debug/profiler endpoints not unsafely exposed.
17. Graceful shutdown matches the deployment platform.
18. Rollout, abort, and rollback documented.
19. Final diff free of accidental changes; command log complete.
20. Unverified areas explicit; no production-readiness claim without evidence.

If any condition is unmet: **The project is not yet fully production-ready.** List the blocking conditions precisely.

