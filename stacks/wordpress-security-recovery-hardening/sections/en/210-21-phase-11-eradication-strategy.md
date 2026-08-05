## 21. Phase 11 - Eradication Strategy

Choose and justify one strategy:

### Strategy A - Clean rebuild, preferred for confirmed compromise

- provision a clean environment or clean document root
- install fresh WordPress core from the official source
- install known-good plugins/themes from verified sources
- migrate only verified content and required configuration
- recreate trusted administrators
- regenerate salts and secrets
- validate before traffic cutover

### Strategy B - Verified backup restore

Use only when:

- backup predates the earliest credible compromise
- backup provenance and integrity are known
- backup is scanned and compared before restoration
- the initial-access vector is fixed before exposure
- post-restore credentials are rotated

### Strategy C - In-place remediation

Use only when rebuild/restore is infeasible and document the increased residual risk. Replace compromised components from trusted packages rather than hand-editing them as the final state.

### Eradication requirements

- quarantine evidence, do not merely rename it inside a public directory
- remove unauthorized users, keys, cron jobs, triggers, workers and rules
- remove persistence across WordPress, host, database and edge
- patch or remove the initial-access vector
- clear OPcache, object cache, page cache and CDN cache after evidence collection and code replacement
- verify there are no compromised sibling sites that can reinfect the target

