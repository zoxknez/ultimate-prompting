## 15. Identity, RBAC And Workload Identity

**Objective:** Apply least privilege to humans, machines, workloads, and emergency access.

### 15.1 Required Checks

1. Map human SSO, MFA, groups, cloud IAM, Kubernetes authentication, service accounts, workload identity, CI identities, automation, and break-glass paths.
2. Enumerate effective RBAC, including aggregation, impersonation, bind, escalate, token and secret reads, pods exec or attach, port-forward, nodes proxy, CSR approval, webhook and CRD control.
3. Reject broad wildcards, routine cluster-admin, shared identities, long-lived service-account tokens, embedded kubeconfigs, and identity reuse across environments.
4. Use short-lived federated credentials and audience-bound workload identity where supported. Verify issuer, subject, audience, claims, trust policy, and session duration.
5. Separate read, deploy, promote, approve, secret-admin, cluster-admin, billing, and break-glass responsibilities.
6. Test access using impersonation or equivalent safe methods, including denied paths, revoked membership, expired sessions, and compromised workload assumptions.
7. Require logged, time-bound, approved, and reviewed emergency access with tested revocation.

### 15.2 Minimum Evidence

- Effective human and machine permission graph.
- Federation and workload-identity trust-policy evidence.
- Break-glass activation and revocation drill result.

### 15.3 Exit Criteria

1. Critical privileges are attributable, minimal, time-bound where possible, and separated by duty.
2. No unowned shared credential or routine cluster-admin path remains.
3. Revocation and emergency access behavior are verified.

