## 4. Evidence, Findings And Severity

### 4.1 Finding Schema

For every finding record:

```text
ID
severity: P0 | P1 | P2 | P3
status: OPEN | FIXED | CONTAINED | ACCEPTED | REJECTED | UNVERIFIED
component
environment
actor and tenant
untrusted input or trigger
preconditions
reproduction or evaluation case
evidence status
evidence location
root cause
security, privacy, quality, reliability, cost, or legal impact
blast radius
recommended repair
implemented change, if any
verification and regression test
rollback or containment
residual risk
owner and deadline, if known
```

### 4.2 AI-Specific Severity Model

Use the shared severity model, plus these minimum interpretations:

- `P0`: confirmed cross-tenant or privileged data exfiltration; unauthenticated high-impact action; tool or sandbox escape with host impact; production secret disclosure; destructive production action without valid approval; material compromise of safety-critical use.
- `P1`: practical prompt-injection path with privileged consequence; retrieval ACL bypass; confused-deputy tool use; missing action-level authorization; unbounded agent spend or loop; unsafe autonomous payment, deployment, account, delete, shell, or communication action; material provider-retention or privacy-policy violation.
- `P2`: measurable quality, retrieval, evaluation, availability, latency, cost, observability, governance, or recoverability weakness without immediate critical impact.
- `P3`: maintainability, documentation, naming, low-impact UX, or non-blocking consistency issue.

Severity is based on impact and exploitability, not on how many best practices are missing.

### 4.3 Command And Evaluation Log

For every executed command or evaluation, record:

```text
command or eval ID
cwd or service
runtime and toolchain
model, provider, prompt, index, dataset, and config versions
input dataset or fixture ID
seed, temperature, sampling, and repetition count where applicable
start and end time
exit status
summary metrics
warnings and errors
artifact or trace location
execution environment: local | container | CI | staging | production-read-only
```

Do not report aggregate metrics without preserving the underlying run configuration and sample set.

