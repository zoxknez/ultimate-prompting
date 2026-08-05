## 18. Storage, Stateful Workloads And Data Safety

**Objective:** Protect persistence, consistency, durability, and recovery during normal and failed operations.

### 18.1 Required Checks

1. Inventory storage classes, CSI drivers, volume types, access modes, topology, encryption, snapshots, reclaim policies, expansion, quotas, performance tiers, and ownership.
2. Verify StatefulSet identity, ordering, persistent-volume claims, rescheduling, zone affinity, failover, fencing, split-brain prevention, and data-locality assumptions.
3. Audit databases, queues, caches, object stores, search systems, and operators for replication, quorum, consistency, durability, compaction, retention, corruption handling, and supported versions.
4. Separate application availability from data correctness. Verify duplicate delivery, ordering, idempotency, transactions, schema compatibility, and partial failure.
5. Verify migration expand-and-contract strategy, backward and forward compatibility, lock impact, rollback limits, backups, and owner approval.
6. Test volume attachment failure, full disk, IOPS or throughput throttling, lost node, lost zone, replica lag, corruption detection, and recovery in isolation.
7. Verify deletion protection, finalizers, reclaim behavior, snapshot ownership, orphan cleanup, and data-disposal requirements.

### 18.2 Minimum Evidence

- Stateful-system topology, consistency, and ownership map.
- Migration, failover, corruption, capacity, and recovery test results.
- Deletion, retention, snapshot, and data-disposal evidence.

### 18.3 Exit Criteria

1. Critical data systems have proven consistency, capacity, failover, backup, and recovery behavior.
2. Schema and data changes have compatible rollout and explicit rollback or compensating plans.
3. No destructive reclaim, deletion, or orphan path is uncontrolled.

