---
id: wordpress-security-recovery-hardening
prompt_version: 2.0.0
language: en
stack: [wordpress, php, mysql, mariadb, nginx, apache, cpanel, incident-response, digital-forensics]
last_verified: 2026-08-05
default_mode: contain_and_recover
context_class: long
risk_class: critical
execution_style: evidence_first
source_manifest: baselines/wordpress-security-baseline-2026-08-05.json
output_contract: structured_incident_report
---

# MASTER PROMPT - WordPress Security Incident Response, Forensics, Trusted Recovery And Hardening

Load and obey, when present:

- `core/audit-operating-contract.md`
- `core/severity-model.md`
- `core/final-report-schema.md`
- `baselines/sources.json`
- `baselines/wordpress-security-baseline-2026-08-05.json`

If any referenced file is unavailable, continue with this prompt and explicitly list the missing dependency under `Limitations`.

