## 25. Phase 15 - Incident Command, Communications And Decision Authority

Establish an incident command structure appropriate to the business impact. A technically correct cleanup can still fail if ownership, approvals, communications or evidence handling are unclear.

### Decision and ownership matrix

Record at minimum:

- incident commander and backup
- technical lead and evidence custodian
- business owner and production-return approver
- hosting, CDN, registrar, payment and legal contacts
- authority for maintenance mode, checkout suspension, credential rotation, DNS change and rebuild
- communication channel that is not dependent on the compromised WordPress account, mailbox or hosting panel
- update cadence and audience
- explicit decision log with timestamp, decision, approver, evidence and reversal criteria

### Communication safety

- assume WordPress admin messages, compromised mailboxes and hosting-panel chat may be observable by the attacker
- use a separate trusted channel for secrets and high-impact decisions
- do not paste database dumps, private keys, full access tokens or personal data into tickets or chat
- maintain one canonical incident status document
- label preliminary statements as preliminary
- separate customer-facing communication from technical evidence
- preserve material notices, provider responses and timestamps as incident evidence

### Notification triage

Determine whether the incident may involve:

- personal data
- authentication credentials
- payment-card or checkout data
- protected health, education, financial or other regulated information
- customer content or confidential business data
- malware distribution or abuse of third-party infrastructure

Do not provide jurisdiction-specific legal conclusions without confirmed jurisdiction and current legal sources. Record who owns legal, insurer, regulator, law-enforcement, payment-provider and customer-notification decisions.

