## Definition Of Done

Work is complete only when all 23 conditions below are marked with evidence or `NOT_APPLICABLE` and a reason:

1. Repository snapshot and the status of others' changes are recorded.
2. Actual build system and JDK/toolchain are identified.
3. Support/lifecycle status is checked against current primary sources.
4. Architecture and critical flows are mapped.
5. Baseline commands and first failure are preserved.
6. All P0/P1 findings have evidence, root cause, impact, and owner.
7. Potential risks are kept separate from confirmed findings.
8. Authentication, authorization, ownership, and tenant isolation are verified.
9. Public and management security chains are verified.
10. Critical write flows have transaction and idempotency evidence.
11. Concurrency and failure cases are tested or clearly blocked.
12. Migrations, backup/restore, and rollback constraints are documented.
13. Message/job retry, acknowledgement, deduplication, and shutdown behavior are verified.
14. Secrets, configuration, Actuator, and dependency supply chain are audited.
15. Timeout, retry, rate-limit, and resource bounds are reasonable.
16. Health, observability, alerts, and runbooks have actual evidence.
17. Container/deployment/native differences are verified where present.
18. Graceful shutdown is tested or marked `UNVERIFIED` with reason.
19. Implemented changes are minimal, reviewable, and connected to findings.
20. Each P0-P2 repair has a focused regression test.
21. Relevant test/build scope has run after modifications.
22. Command log contains environment, exit status, and result.
23. Final verdict, blockers, residual risk, rollback/recovery, and next owners are clear.

