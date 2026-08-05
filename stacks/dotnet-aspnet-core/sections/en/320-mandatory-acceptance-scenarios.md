## Mandatory Acceptance Scenarios

Run or explicitly mark blocked and `UNVERIFIED` for every applicable scenario:

1. unauthorized, wrong-role, wrong-tenant, wrong-owner, invalid-state, expired/revoked credential, and cross-resource access;
2. duplicate and concurrent critical writes, retry after timeout, partial external failure, crash around commit, and stale client update;
3. missing or rotated secret, Data Protection key continuity, certificate/signing-key rollover, and identity-provider metadata rollover;
4. database unavailable, slow database, pool exhaustion, deadlock or concurrency conflict, migration lock, and restore rehearsal;
5. downstream timeout, throttle, malformed response, DNS change, certificate change, retry storm prevention, and recovery;
6. broker duplicate, reorder, delay, disconnect, poison message, dead-letter replay, and consumer deployment overlap;
7. oversized, slow, malformed, compressed, archived, path-traversal, and unauthorized file operations;
8. slow client, disconnected client, stream cancellation, backpressure, reconnect, revocation, and deployment drain;
9. cold start, warm load, burst, soak, overload, degraded dependency, memory pressure, thread-pool pressure, and recovery;
10. SIGTERM or service stop during read, write, upload, stream, job, migration, and telemetry flush;
11. rolling or canary deployment with old/new coexistence, abort, application rollback, forward repair, and data recovery;
12. clean checkout restore/build/test/publish and execution of the exact final artifact in the intended hosting model.

