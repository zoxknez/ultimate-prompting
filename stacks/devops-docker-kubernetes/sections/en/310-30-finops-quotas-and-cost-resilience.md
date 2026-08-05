## 30. FinOps, Quotas And Cost Resilience

**Objective:** Control cost without weakening reliability, security, or recovery.

### 30.1 Required Checks

1. Attribute spend to account, environment, service, owner, tenant, workload, region, resource type, and business outcome where feasible.
2. Audit budgets, forecasts, anomaly detection, commitments, reservations, savings plans, spot or preemptible use, egress, support, licenses, storage growth, logs, metrics, and backup cost.
3. Identify idle, oversized, orphaned, duplicated, over-retained, cross-region, over-replicated, and low-utilization resources with business and recovery context.
4. Verify quotas, service limits, budget actions, billing permissions, cost-export integrity, and alert delivery before exhaustion or runaway spend.
5. Model normal, peak, failover, incident, restore, scale-out, data growth, and observability cost.
6. Do not remove redundancy, retention, logging, encryption, support, headroom, or rollback capacity without explicit risk acceptance.
7. Define unit economics and cost guardrails that do not create availability or data-loss cliffs.

### 30.2 Minimum Evidence

- Cost allocation, trend, anomaly, and ownership report.
- Savings backlog with reliability and recovery impact.
- Quota, budget, and failover-cost test evidence.

### 30.3 Exit Criteria

1. Critical spend is attributable and material anomalies alert responsible owners.
2. Savings recommendations preserve accepted SLO, RPO, RTO, security, and rollback.
3. Quota and cost exhaustion cannot create an unobserved sudden outage.

