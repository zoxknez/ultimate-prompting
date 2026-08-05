## 36. Phase 26 - Trusted Backup Selection, Clean Rebuild And Data Migration

A backup is evidence and a recovery candidate, not automatically a trusted source.

### Backup trust assessment

For every candidate backup record:

- creation timestamp and timezone
- source system and backup tool
- storage account and access history
- immutability/versioning state
- file/database completeness
- encryption and key availability
- integrity hash or provider verification
- relation to first known and earliest plausible compromise
- WordPress, plugin, theme, PHP and database versions
- malware and persistence scan result in isolation
- functional restore result
- data-loss interval and reconciliation plan

### Preferred clean rebuild sequence

1. provision a new trusted account, host, container or VM when scope warrants it
2. patch the OS, web server, PHP, database client and management tooling
3. install WordPress only from the official source
4. install only required plugins/themes from verified sources
5. recreate configuration without copying unknown executable code
6. migrate database/content through a reviewed and reversible process
7. validate and sanitize uploads; do not copy executable files blindly
8. generate new salts, credentials, keys and application secrets
9. restore integrations with newly issued credentials
10. run security, functional, performance and recovery tests
11. cut traffic over with a documented rollback plan
12. preserve the old environment offline according to evidence policy

### Restore decision rules

- if initial access or persistence predates a backup, do not treat that backup as clean
- if backup provenance or completeness is unknown, mark it `UNVERIFIED`
- if only content must be preserved, prefer controlled content migration over full environment restoration
- if data loss is possible, define reconciliation before cutover
- if rollback would restore vulnerable code, compromised credentials or malicious data, use forward repair instead

