## Work Order

Start in this order:

1. protect the workspace;
2. solution and project inventory;
3. SDK/runtime/lifecycle analysis;
4. NuGet and supply-chain analysis;
5. restore/build/test/publish baseline;
6. architecture map and critical flows;
7. security and data boundaries;
8. evidence-backed findings;
9. minimal fixes and regression tests;
10. broader verification, deployment, and rollback;
11. final report.

Work iteratively: inventory → evidence → root cause → minimal fix → test → Release build/publish → deployment analysis → rollback → documentation.

Priorities: user and data protection; authentication and authorization; functional correctness; transactions, concurrency, and idempotency; operational reliability; measurement-based performance; architectural maintainability; developer experience.

The final result must enable another experienced .NET engineer to determine unambiguously: what was actually checked; with which SDK and runtime; which commands were run; what was found; how the problem was reproduced; what the root cause is; what was changed; which test proves the fix; what remains unchecked; how the artifact is deployed; how the database is migrated; how rollout is aborted; how the system is rolled back or recovered.
