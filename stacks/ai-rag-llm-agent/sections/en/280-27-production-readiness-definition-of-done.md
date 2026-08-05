## 27. Production Readiness Definition Of Done

Mark each applicable item `CONFIRMED`, `UNVERIFIED`, or `NOT_APPLICABLE` with evidence.

A system cannot be `ready` unless:

1. Workspace, credentials, data, and production systems were protected during the audit.
2. The real architecture, models, prompts, retrieval, tools, MCP, memory, and deployment units are inventoried.
3. Identity and tenant context are preserved end to end.
4. Retrieval, tools, memory, and high-impact actions enforce deterministic resource-level authorization.
5. No applicable P0 remains open.
6. P1 findings are fixed or formally contained with owner, deadline, monitoring, and recovery path.
7. Critical positive, negative, adversarial, failure, retry, and recovery tests pass with evidence.
8. Evaluation datasets and thresholds are representative, versioned, reproducible, and approved.
9. Model, prompt, retrieval, tool, policy, and provider changes have regression and rollback controls.
10. Cost, latency, capacity, availability, and budget limits are measured and acceptable.
11. Sensitive data is protected across prompts, providers, retrieval, memory, logs, traces, evals, and exports.
12. Observability, audit logs, alerts, kill switches, incident runbooks, backup, restore, and rollback are tested.
13. Applicable legal, regulatory, consent, transparency, human-oversight, and accessibility gaps are resolved or explicitly blocking.
14. Residual risk is explicit and accepted by an authorized owner.
15. No material area is declared safe solely because it was not tested.

If any applicable blocking item is incomplete, state:

> Not fully production-ready.

Then list exact blocking conditions.

