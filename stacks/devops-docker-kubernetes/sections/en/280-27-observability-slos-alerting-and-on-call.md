## 27. Observability, SLOs, Alerting And On-Call

**Objective:** Make user impact and system failure detectable, diagnosable, and actionable.

### 27.1 Required Checks

1. Define service boundaries, user journeys, SLIs, SLOs, error budgets, reporting windows, exclusions, owners, and consequences of budget burn.
2. Verify metrics, logs, traces, events, profiles, audit logs, deployment metadata, and business signals share stable service, environment, version, tenant-safe, and correlation attributes.
3. Audit cardinality, sampling, aggregation, histogram buckets, clock synchronization, buffering, loss, backpressure, retention, encryption, access, redaction, and cost.
4. Prevent secrets, credentials, authorization headers, tokens, personal data, customer payloads, and high-risk identifiers from telemetry.
5. Design paging alerts around user impact, SLO burn, data integrity, security events, and urgent capacity risks. Separate pages, tickets, dashboards, and informational signals.
6. For every page verify threshold, duration, grouping, deduplication, inhibition, ownership, runbook, dashboard, silence policy, escalation, and resolution evidence.
7. Test telemetry-pipeline failure, missing data, delayed data, alert delivery, on-call routing, expired integration, and regional observability loss.
8. Review recent incidents and pages for time to detect, acknowledge, diagnose, mitigate, resolve, false positives, toil, and missing signals.

### 27.2 Minimum Evidence

- SLO and error-budget definitions tied to user journeys.
- Telemetry coverage, privacy, loss, retention, and cost assessment.
- Alert fire, delivery, routing, runbook, and resolution test results.

### 27.3 Exit Criteria

1. Critical user impact and security conditions produce timely actionable signals.
2. Telemetry is useful, protected, affordable, and resilient enough for incident response.
3. On-call ownership, escalation, runbooks, and alert quality are verified through real or controlled events.

