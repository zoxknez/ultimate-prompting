## 29. Incident Response, Forensics And Supply-Chain Compromise

**Objective:** Prepare to contain, investigate, eradicate, recover, and learn without destroying evidence.

### 29.1 Required Checks

1. Define incident roles, severity, commander, communications, legal and privacy escalation, vendor contacts, evidence custodians, business decisions, and public-status responsibilities.
2. Prepare playbooks for compromised CI, runner, source account, package, action, base image, registry, signing identity, cluster credential, workload, node, KMS key, secret manager, DNS, or cloud account.
3. Preserve logs, audit trails, artifacts, images, provenance, signatures, workflow runs, controller history, cloud events, runtime metadata, memory or disk evidence, and chain of custody.
4. Contain with the smallest effective action: revoke identity, block digest, quarantine workload, pause promotion, isolate account or namespace, disable route, or restrict egress.
5. Avoid broad deletion, rebuilding, node termination, log clearing, key rotation, or redeployment until evidence and dependency impact are considered.
6. Trace blast radius across artifacts, environments, identities, data, customers, regions, dependencies, backups, and recovery systems.
7. Rebuild from trusted source and builders, rotate in dependency order, verify clean artifacts, restore safely, monitor recurrence, and preserve rollback.
8. Run a tabletop or technical exercise and convert lessons into owned, dated changes.

### 29.2 Minimum Evidence

- Incident authority, contact, severity, and evidence-handling plan.
- Supply-chain and credential-compromise playbooks.
- Exercise timeline, decisions, evidence, gaps, and assigned improvements.

### 29.3 Exit Criteria

1. The organization can revoke, quarantine, rebuild, redeploy, and verify critical components without relying on the compromised path.
2. Evidence preservation and communication responsibilities are clear.
3. Exercise findings have owners, deadlines, verification, and leadership visibility.

