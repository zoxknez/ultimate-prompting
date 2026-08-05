---
id: wordpress-security-recovery-hardening
prompt_version: 2.0.0
language: sr
stack: [wordpress, php, mysql, mariadb, nginx, apache, cpanel, incident-response, digital-forensics]
last_verified: 2026-08-05
default_mode: contain_and_recover
context_class: long
risk_class: critical
execution_style: evidence_first
source_manifest: baselines/wordpress-security-baseline-2026-08-05.json
output_contract: structured_incident_report
---

# MASTER PROMPT - WordPress Bezbednosni Incident, Forenzika, Pouzdan Oporavak I Hardening

Učitaj i poštuj, kada postoje:

- `core/audit-operating-contract.md`
- `core/severity-model.md`
- `core/final-report-schema.md`
- `baselines/sources.json`
- `baselines/wordpress-security-baseline-2026-08-05.json`

Ako neki referencirani fajl nije dostupan, nastavi koristeći ovaj prompt i izričito navedi nedostajuću zavisnost u odeljku `Ograničenja`.

