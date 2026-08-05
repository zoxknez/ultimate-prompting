## Phase A - Authorization, Data Safety, And Evidence Preservation

Before touching a database, establish authority, environment identity, maintenance constraints and recovery options.

- Record repository SHA, migration state, deployment revision, server time, timezone and active incident or maintenance window.
- Verify test tools cannot resolve or authenticate to production by default.
- Confirm storage headroom, transaction-log headroom, backup retention, replica health and restore destination capacity.
- Preserve logs, plans, catalog snapshots and hashes without copying unnecessary sensitive data.
- Define stop conditions for lock growth, replication lag, I/O saturation, error rate, disk usage and recovery uncertainty.
- For incident mode, freeze unsafe writes before cleanup and preserve the original state.

