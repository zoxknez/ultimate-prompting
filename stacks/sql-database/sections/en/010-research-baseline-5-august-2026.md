## Research Baseline - 5 August 2026

This baseline is a starting point, not permission to upgrade blindly. Re-check official engine documentation, vendor support policy, managed-service restrictions and the real running system immediately before recommendations or changes.

| Component | Verified status on 5 August 2026 | Mandatory audit check |
| --- | --- | --- |
| PostgreSQL stable | 18.4 is the current stable patch; supported majors are 18, 17, 16, 15 and 14. | Verify `server_version`, package or image digest, extensions, managed-service compatibility and patch policy. |
| PostgreSQL lifecycle | PostgreSQL 14 reaches final release on 12 November 2026; PostgreSQL 19 is beta and not a default production baseline. | Create an evidence-backed upgrade plan before EOL; never recommend beta by default. |
| MySQL LTS | 8.4.10 is the current verified patch in the 8.4 LTS line. | Verify exact patch, edition, support contract, OS support, connector and upgrade checker output. |
| MySQL Innovation | 9.7.2 is the current verified Innovation patch, not an LTS release. | Do not label 9.7 as LTS; prove the faster upgrade cadence and compatibility budget. |
| MySQL 8.0 | MySQL 8.0 reached community EOL in April 2026. | Plan migration to a supported line; cloud extended support is a separate commercial control. |
| MariaDB | 12.3 is the current LTS line and must be treated as a distinct engine from MySQL. | Verify exact patch and support source; do not transfer MySQL semantics or upgrade paths. |
| SQLite | 3.53.4 is the current release. | Verify the actually loaded library, `sqlite_source_id()`, compile options, binding and filesystem behavior. |
| Recovery | PostgreSQL PITR requires base backup plus continuous WAL; MySQL PITR requires backup plus binary logs; SQLite needs a coordinated supported backup method. | A backup is not valid until an isolated restore and application-level verification succeed. |

Patch levels and cloud offerings move. At execution time, treat the baseline manifest as evidence to re-check, not as a permanent truth.

