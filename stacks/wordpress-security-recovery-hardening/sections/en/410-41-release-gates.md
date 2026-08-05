## 41. Release Gates

Production is not considered recovered until all applicable gates pass:

### Gate 1 - Evidence

- key evidence preserved and hashed
- chain-of-custody recorded
- timeline limitations documented

### Gate 2 - Scope

- WordPress, host, database, identity, edge and sibling-site scope assessed
- unknown/unexamined areas explicitly listed

### Gate 3 - Eradication

- known malicious artifacts removed or isolated outside production
- persistence paths checked and remediated
- initial-access vector fixed or residual risk formally accepted

### Gate 4 - Identity

- affected credentials rotated
- sessions/tokens invalidated
- unknown accounts and keys removed

### Gate 5 - Recovery

- trusted code and content restored
- functional smoke tests passed
- rollback path confirmed

### Gate 6 - Hardening

- critical/high hardening items complete
- backups and restore test validated
- monitoring enabled

### Gate 7 - Reporting

- evidence-backed report complete
- notification and legal obligations assessed
- owner accepts residual risk

If any required gate fails, state exactly:

`The site is not fully recovered or production-safe. Outstanding gates: [LIST].`

