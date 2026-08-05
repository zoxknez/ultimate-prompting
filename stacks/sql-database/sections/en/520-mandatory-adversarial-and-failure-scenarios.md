## Mandatory Adversarial And Failure Scenarios

1. Two concurrent requests attempt to create the same logically unique resource.
2. Two transactions update the same balance, inventory or state transition.
3. The client times out immediately before or after commit and retries.
4. A process crashes after database commit but before message, file, cache or HTTP acknowledgement.
5. A deadlock or serialization failure occurs under representative concurrency.
6. A long transaction blocks vacuum, purge, DDL or retention work.
7. The connection pool is exhausted while the database is slow but still accepting connections.
8. A proxy, DNS target or primary changes while requests are in flight.
9. A migration runs with old and new application versions concurrently.
10. A backfill is interrupted, restarted and accidentally triggered twice.
11. Disk, WAL, binlog, undo, temporary or backup storage approaches exhaustion.
12. A replica is promoted with lag and the old primary later returns.
13. A stale replica serves an authorization-sensitive or read-after-write request.
14. Backup restore encounters a missing or corrupt log segment.
15. PITR target is interpreted in the wrong timezone or crosses daylight-saving change.
16. A credential, certificate or encryption key rotates while pools and replicas are active.
17. A tenant identifier is omitted from cache, job, export or administrative query.
18. Malformed JSON, text encoding, collation or numeric input reaches a critical query.
19. SQLite is opened by two application instances or placed on unreliable shared storage.
20. An isolated restore must become the new production source while queues and external systems contain later effects.

