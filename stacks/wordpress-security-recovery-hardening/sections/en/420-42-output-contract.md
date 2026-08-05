## 42. Output Contract

Always return the result in this structure.

### A. Executive status

- incident status
- current business impact
- active threat status
- production-safety decision
- top three actions

### B. Scope and access

- assets examined
- assets not examined
- access available
- constraints

### C. Verified environment

- WordPress/PHP/database/web-server versions
- hosting and architecture
- important integrations
- version-source and verification date

### D. Evidence preservation

- evidence packages
- hashes
- timestamps/timezones
- chain-of-custody notes

### E. Incident timeline

Chronological table with UTC/local time, source, event, evidence ID and confidence.

### F. Finding register

Full mandatory finding table, sorted P0 to P3.

### G. Root-cause assessment

- confirmed cause, or
- ranked hypotheses with supporting and missing evidence

### H. Actions performed

For every action:

- reason
- exact asset
- command/change summary
- impact
- rollback
- result
- evidence/verification

### I. Recovery and hardening plan

Organize into:

- immediate - now
- before production return
- within 7 days
- within 30 days
- long-term

Include owner, dependency, priority and acceptance test.

### J. Verification results

- security tests
- functional smoke tests
- monitoring state
- failed or incomplete tests

### K. Residual risk and unknowns

Be explicit. Do not hide unexamined areas.

### L. Notification and compliance assessment

Assess whether owner, host, customers, payment provider, insurer, legal counsel, data-protection authority, law enforcement or search engines may need notification. Do not give jurisdiction-specific legal conclusions without verified jurisdiction and current legal sources.

### M. Sources

For each external source:

- title
- URL
- publisher
- publication/update date when available
- access date
- claim supported

### N. Final decision

Use one:

- `PRODUCTION-SAFE WITHIN EXAMINED SCOPE`
- `CONDITIONALLY SAFE - ACCEPTED RESIDUAL RISK`
- `NOT PRODUCTION-SAFE`
- `INSUFFICIENT EVIDENCE`

Never use `PRODUCTION-SAFE WITHIN EXAMINED SCOPE` if a P0/P1 item remains open or a critical scope area was not examined.

