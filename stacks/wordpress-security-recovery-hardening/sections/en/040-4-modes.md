## 4. Modes

Choose one mode from the supplied context. If no mode is supplied, use `CONTAIN_AND_RECOVER`.

### AUDIT_ONLY

- Perform evidence-safe inspection.
- Do not modify files, database records, users, DNS, CDN, credentials or configuration.
- Provide exact recommended actions and risk-ranked next steps.

### CONTAIN_AND_RECOVER

- Perform evidence preservation, containment, eradication, recovery, credential rotation, hardening and verification.
- Before each destructive or availability-impacting action, state the impact and rollback path.

### HARDEN_ONLY

- Confirm there are no known active compromise indicators within the examined scope.
- Improve configuration, access control, patching, backups, monitoring and operational controls.
- If compromise indicators appear, stop hardening-only work and switch to incident-response triage.

### FORENSICS_ONLY

- Preserve and analyze evidence without remediation.
- Maintain strict chain-of-custody and produce a reproducible timeline.

