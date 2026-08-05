## Repair And Change Workflow

1. Reproduce and classify the issue with the least invasive evidence.
2. Identify the violated invariant or operational contract and the smallest safe control layer.
3. Design the minimal fix plus migration, capacity, lock, replication and security impact.
4. Add a regression test and a reconciliation or integrity query.
5. Rehearse on production-like data and the actual engine version.
6. Define rollout cohort, guardrails, abort thresholds and owner.
7. Prove rollback or forward repair, including data written by the new release.
8. Deploy the same reviewed artifact or migration without ad hoc production editing.
9. Observe correctness, locks, lag, capacity and user-visible SLOs.
10. Close the finding only after evidence and documentation are stored.

