## 6. Authorization, Scope And Evidence Preservation

**Objective:** Create a safe audit boundary before touching any system.

### 6.1 Required Checks

1. Identify legal owner, technical owner, on-call owner, approver, and communication channel for every production scope.
2. Record accounts, subscriptions, projects, regions, clusters, namespaces, repositories, registries, and environments that are in and out of scope.
3. Verify the identity and permission level used for every tool, API, kubeconfig context, cloud session, and CI token.
4. Capture repository status, deployed revisions, controller sync state, live resource versions, and relevant change windows before mutation.
5. Define evidence handling, redaction, retention, encryption, access, and deletion rules.
6. Establish stop conditions for unexpected blast radius, degraded health, stale backups, missing rollback, or uncertain authorization.

### 6.2 Minimum Evidence

- Signed or recorded scope and approval boundary.
- Redacted inventory of identities, contexts, accounts, and owners.
- Pre-change evidence manifest with hashes or immutable references where practical.

### 6.3 Exit Criteria

1. Every action has a known identity, scope, owner, and authorization level.
2. Sensitive evidence is protected and no production mutation has occurred without approval.
3. Audit limitations and inaccessible systems are explicitly registered.

