## Phase T - Backup, Restore, PITR, And Data Verification

Backups are only potential recovery material until restore and verification succeed.

- Inventory full, incremental, logical, physical, snapshot and log-archive backups plus retention and immutability.
- Verify encryption, key custody, checksums, catalog metadata, cross-account or offsite copies and deletion protection.
- Perform isolated restore using documented credentials, network, DNS and application verification steps.
- Verify PITR to timestamps immediately before and after a known transaction and confirm timezone interpretation.
- Validate schema, row-count ranges, critical invariants, checksums where meaningful and application smoke tests.
- Measure actual RPO and RTO and include queue, object storage, search and configuration recovery dependencies.

