## Repair And Verification Workflow

1. Freeze scope and record baseline, findings, and safety constraints.
2. Select one confirmed or highest-risk falsifiable hypothesis.
3. Reproduce with the smallest safe environment and data set.
4. Identify the authoritative invariant and exact failing boundary.
5. Design the smallest repair and document rejected alternatives, compatibility, migration, and rollback.
6. Implement a reviewable increment without unrelated refactoring.
7. Add a regression test that fails before and passes after.
8. Run narrow, affected, production build, artifact smoke, and applicable failure tests.
9. Verify telemetry, rollout guardrail, recovery, and residual risk.
10. Update findings, logs, matrices, release notes, runbooks, and decision.

