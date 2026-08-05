## Mandatory Adversarial And Failure Scenarios

- S1 - Cross-tenant object and nested-resource access through direct, batch, export, cache, file, and queue paths.
- S2 - Parallel critical writes causing lost update, double spend, negative inventory, duplicate entitlement, or invalid state transition.
- S3 - Idempotency key reuse with same payload, different payload, actor, tenant, expiry, timeout, and crash.
- S4 - Client disconnect or AbortSignal during database, provider, file, stream, worker, and queue work.
- S5 - Malformed, nested, oversized, compressed, multipart, duplicate-key, prototype-key, and regex-adversarial input.
- S6 - Slowloris, flood, retry storm, cache stampede, reconnect storm, fan-out amplification, and downstream brownout.
- S7 - Event-loop blocking and worker-pool saturation from CPU, crypto, compression, parser, filesystem, and native work.
- S8 - Database pool exhaustion, deadlock, failover, replica lag, partial migration, and old-new overlap.
- S9 - Broker redelivery, consumer crash around commit, poison message, rebalance, DLQ replay, and operator re-run.
- S10 - Webhook replay, reordered delivery, key rotation, timestamp boundary, raw-body mutation, and provider timeout.
- S11 - SSRF through redirect, DNS rebinding, mixed notation, IPv4-mapped IPv6, private range, and metadata endpoint.
- S12 - Path traversal, zip slip, decompression bomb, parser bomb, signed-URL misuse, aborted upload, and orphan cleanup.
- S13 - Session fixation, stale rights, refresh-token reuse, wrong issuer or audience, key rotation, logout, and revocation.
- S14 - Async context, singleton, cache, logger, worker, and scheduler leakage between actors or tenants.
- S15 - SIGTERM with long request, open stream, realtime connection, in-flight job, migration, and shutdown deadline.
- S16 - Memory pressure, handle leak, timer leak, stream error, native leak, OOM, diagnostics, and crash-loop prevention.
- S17 - Untrusted pull request, poisoned cache, lifecycle script, dependency confusion, compromised package, and artifact substitution.
- S18 - Canary regression, bad config, bad schema, old-new client mismatch, rollback, forward repair, and reconciliation.
- S19 - Isolated restore of database, keys, object storage, queue state, search index, and tenant boundaries.
- S20 - Incident containment for credential compromise, tenant leakage, corruption, supply-chain compromise, and provider outage.

