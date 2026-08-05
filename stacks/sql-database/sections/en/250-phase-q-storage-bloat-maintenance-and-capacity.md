## Phase Q - Storage, Bloat, Maintenance, And Capacity

Prove that routine maintenance keeps data structures healthy without violating SLOs.

- Measure data, index, log, temporary, undo, WAL or binlog and backup growth separately.
- Review autovacuum or purge behavior, checkpoints, flushing, compaction and fragmentation as applicable.
- Model disk headroom for peak writes, migration rewrite, index build, backup, restore and failover.
- Review temporary-file and spill limits, memory per operation and aggregate concurrency.
- Verify maintenance jobs are bounded, monitored, restartable and safe during topology changes.
- Create capacity thresholds and lead-time alerts before exhaustion.

