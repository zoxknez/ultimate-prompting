## 18. Phase N - Evaluation System And Quality Engineering

### 18.1 Evaluation Layers

Evaluate separately:

1. deterministic unit behavior
2. prompt and structured-output behavior
3. retrieval quality
4. response quality and groundedness
5. tool selection and argument correctness
6. complete agent trajectory and final state
7. safety and policy adherence
8. human usefulness and task completion
9. latency, availability, and cost
10. production outcomes and incident signals

### 18.2 Dataset And Experimental Design

1. Build versioned golden, adversarial, edge-case, multilingual, and negative datasets from representative use cases.
2. Include critical business slices and low-frequency high-impact cases.
3. Separate development, tuning, regression, and final holdout sets.
4. Track provenance, licensing, PII status, contamination risk, ownership, and change history.
5. Use repeated trials for nondeterministic behavior and report variance or confidence intervals where meaningful.
6. Pin or record model, prompt, tool, retrieval, judge, seed, temperature, and configuration.
7. Calibrate LLM judges against human labels and test judge bias, position bias, verbosity bias, and self-preference.
8. Use deterministic checks and human review wherever they are more reliable than an LLM judge.
9. Preserve failing examples and add them to regression suites after triage.

### 18.3 Acceptance Gates

Define explicit thresholds before evaluating. At minimum include:

- critical task success rate
- critical safety-policy pass rate
- authorization and tenant-isolation pass rate
- unsupported-claim or hallucination rate
- citation correctness where required
- tool-selection and argument-validity rate
- irreversible-action approval compliance
- p50, p95, and p99 latency or applicable SLOs
- timeout, retry, and failure rate
- token and monetary cost per successful task
- regression tolerance versus the approved baseline

Do not choose thresholds after seeing results merely to obtain a pass.

### 18.4 Online Evaluation And Release Strategy

1. Use shadow, replay, canary, or limited rollout where appropriate.
2. Prevent evaluation traffic from causing real side effects.
3. Track user correction, abandonment, escalation, retry, complaint, incident, and successful-completion signals.
4. Detect drift by model, prompt, source corpus, tenant, language, tool, and use-case slice.
5. Define automatic rollback and kill-switch conditions.
6. Require review when changing model aliases, prompts, retrieval, tools, policies, or MCP capabilities.

