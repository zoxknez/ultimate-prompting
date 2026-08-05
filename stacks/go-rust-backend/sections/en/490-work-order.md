## Work Order

1. protect the workspace;
2. determine technology path;
3. module/workspace inventory;
4. toolchain and lifecycle analysis;
5. dependency and supply-chain analysis;
6. initial build/test/lint baseline;
7. architecture map and critical flows;
8. concurrency and lifecycle;
9. unsafe/FFI;
10. data and transactions;
11. security;
12. performance and observability;
13. evidence-backed findings;
14. minimal fixes and regression tests;
15. production build, deployment, and rollback;
16. final report.

Iterate: inventory → evidence → root cause → minimal fix → test → race/Miri/sanitizer where relevant → production build → deployment → rollback → documentation.

Priorities: user and data protection; memory and concurrency correctness; authentication and authorization; functional correctness; transactions and idempotency; operational reliability; measurement-based performance; architectural maintainability; developer experience.

The final result must enable another experienced Go or Rust engineer to determine unambiguously: which toolchain was used; what was actually executed; which targets and feature/tag combinations were checked; what was found; how the problem was reproduced; what the root cause is; what was changed; which test proves the fix; whether race, unsafe, or FFI risk remains; what was not checked; how the artifact is deployed; how rollout is aborted; how the system is rolled back or recovered.
