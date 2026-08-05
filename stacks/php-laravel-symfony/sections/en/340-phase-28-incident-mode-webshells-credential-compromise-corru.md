## Phase 28 - Incident Mode, Webshells, Credential Compromise, Corruption, and Trusted Rebuild

### Objective

Provide a separate evidence-preserving workflow for active compromise, integrity loss, destructive failure, and unsafe uncertainty.

### Audit Requirements

- Enter INCIDENT mode for active exploitation, webshell or unknown executable code, credential theft, signing compromise, data corruption, destructive migration, or uncertain production integrity.
- Preserve logs, process state, filesystem metadata, artifacts, database evidence, queue state, cloud audit records, deployment history, and a timestamped action log.
- Contain through traffic restriction, write freeze, worker pause, credential revocation, session invalidation, key rotation, isolation, and known-good failover as appropriate.
- Do not clean an untrusted host in place and call it recovered; identify persistence, initial access, lateral movement, affected identities, data impact, and scope.
- Rebuild from reviewed source, trusted dependencies, clean toolchains, fresh infrastructure, rotated secrets, verified migrations, and signed immutable artifacts.
- Validate data, object storage, backups, queues, search indexes, caches, sessions, external providers, and audit trails before restoring normal service.

### Required Evidence

- Incident timeline, evidence inventory, chain of custody, containment decisions, scope, and identity-revocation record.
- Known-good source, dependency, toolchain, artifact, infrastructure, and restore provenance.
- Post-rebuild integrity, authorization, recovery, reconciliation, and monitoring evidence.

### Acceptance Criteria

- Service is not declared recovered while code, credentials, data, hosts, or artifact provenance remain untrusted.
- Recovery removes persistence and root cause, restores known-good state, and adds tested recurrence controls.

