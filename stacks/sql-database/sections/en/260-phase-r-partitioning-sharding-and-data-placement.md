## Phase R - Partitioning, Sharding, And Data Placement

Use partitioning or sharding only for demonstrated scale, lifecycle or isolation needs.

- Verify partition key matches pruning, retention, uniqueness and common access patterns.
- Test missing, future, default and empty partitions plus boundary timestamps and timezones.
- Review global versus local uniqueness, foreign keys, sequence allocation and cross-partition updates.
- Verify partition creation, detach, archive and deletion automation under failure and replay.
- For sharding, define routing authority, resharding, cross-shard transaction and reconciliation behavior.
- Test hot-shard, unavailable-shard and stale-routing scenarios.

