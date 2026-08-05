## 40. Phase 30 - WordPress Incident Acceptance Criteria

The strongest available decision is limited to the examined scope and evidence quality.

### READY criteria

All applicable conditions must be true:

- authorization, scope and decision owners are documented
- evidence is preserved with hashes and chain-of-custody
- active abuse is contained
- WordPress bootstrap, executable code, database, identities, schedulers, host and edge persistence are examined
- source and provenance are established for every retained executable component
- initial access is fixed, or the unresolved path is explicitly accepted with compensating controls
- credentials, sessions, application passwords and relevant external keys are rotated or revoked
- trusted rebuild or verified restore is complete
- critical business flows and security assertions pass
- caches, OPcache, CDN and workers serve the intended release
- backup restore, rollback/forward-repair and monitoring are demonstrated
- no open P0 or P1 finding remains

### Conditional or blocked outcomes

Use:

- `CONDITIONALLY SAFE - ACCEPTED RESIDUAL RISK` only when the owner explicitly accepts documented non-P0/P1 residual risk
- `NOT PRODUCTION-SAFE` when active compromise, persistence, unknown privileged access, untrusted code, failed recovery or an open P0/P1 remains
- `INSUFFICIENT EVIDENCE` when critical scope or evidence is unavailable

Never convert missing evidence into a passing result.

