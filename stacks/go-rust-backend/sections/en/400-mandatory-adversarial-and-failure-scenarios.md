## Mandatory Adversarial And Failure Scenarios

Execute applicable scenarios with defined preconditions, observable signals, pass/fail thresholds, cleanup, and evidence level. Do not report merely that the system survived.

1. Two concurrent mutations target the same invariant, aggregate, key, account, quota, or inventory item.
2. A request or message is retried before, during, and after commit, response loss, acknowledgment loss, or process crash.
3. The client disconnects or deadline expires while database, filesystem, queue, subprocess, or foreign-library work is in flight.
4. A slow or malicious peer sends partial frames, oversized lengths, compressed bombs, endless streams, invalid encodings, or protocol state violations.
5. Database pool, connection limit, file descriptor, memory, CPU, thread, goroutine, task, queue, or ephemeral-port capacity approaches exhaustion.
6. A downstream dependency becomes slow, intermittently fails, returns overload, closes connections, changes DNS, rotates certificates, or recovers gradually.
7. Retry multiplication occurs across client, proxy, service, database, queue, and worker layers.
8. The process receives graceful shutdown while accepting work, holding locks, owning leases, serving streams, committing transactions, or publishing events.
9. The process panics, aborts, is killed, or loses the host during partial initialization, migration, write, upload, event publication, or checkpoint.
10. Old and new binaries coexist against old, intermediate, and new schemas, messages, caches, and protocol peers.
11. A build tag, feature, target, cgo/native path, allocator, TLS backend, database backend, or optional integration differs from the commonly tested default.
12. A stale lock holder, lease owner, leader, cache entry, token, configuration snapshot, or DNS answer continues after ownership or authority changed.
13. A queue delivers duplicates, reorders messages, delays messages beyond assumptions, rebalances ownership, or replays a poison message from DLQ.
14. Tenant, account, role, namespace, or object identifiers are changed while preserving valid syntax and authentication.
15. Secrets, signing keys, certificates, tokens, dependency credentials, or encryption keys rotate, expire, are revoked, or become temporarily unavailable.
16. Backup or snapshot restores into an isolated environment while binaries, migrations, keys, external dependencies, and retained events differ from backup time.
17. Telemetry, health, readiness, and alerts are evaluated during degradation to prove they distinguish dependency failure, overload, deadlock, leak, corruption, and recovery.
18. Rollback is attempted after a code-only change, configuration change, dependency change, schema change, protocol change, and partially completed rollout.

