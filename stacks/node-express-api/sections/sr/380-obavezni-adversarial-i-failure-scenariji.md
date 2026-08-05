## Obavezni Adversarial I Failure Scenariji

- S1 - Cross-tenant pristup objektu i nested resursu kroz direct, batch, export, cache, file i queue putanje.
- S2 - Paralelni kriticni write-ovi koji izazivaju lost update, double spend, negative inventory, duplicate entitlement ili nevalidan state transition.
- S3 - Ponovna upotreba idempotency key-a sa istim payload-om, razlicitim payload-om, akterom, tenant-om, expiry-jem, timeout-om i crash-om.
- S4 - Client disconnect ili AbortSignal tokom database, provider, file, stream, worker i queue rada.
- S5 - Malformed, nested, oversized, compressed, multipart, duplicate-key, prototype-key i regex-adversarial input.
- S6 - Slowloris, flood, retry storm, cache stampede, reconnect storm, fan-out amplifikacija i downstream brownout.
- S7 - Blokiranje event loop-a i saturacija worker pool-a zbog CPU, crypto, compression, parser, filesystem i native rada.
- S8 - Database pool exhaustion, deadlock, failover, replica lag, parcijalna migracija i old-new overlap.
- S9 - Broker redelivery, consumer crash oko commit-a, poison message, rebalance, DLQ replay i operator re-run.
- S10 - Webhook replay, promenjen redosled delivery-ja, key rotation, timestamp boundary, raw-body mutacija i provider timeout.
- S11 - SSRF kroz redirect, DNS rebinding, mixed notation, IPv4-mapped IPv6, private range i metadata endpoint.
- S12 - Path traversal, zip slip, decompression bomb, parser bomb, zloupotreba signed URL-a, prekinut upload i orphan cleanup.
- S13 - Session fixation, stale prava, refresh-token reuse, pogresan issuer ili audience, key rotation, logout i revocation.
- S14 - Curenje async context-a, singleton-a, cache-a, logger-a, worker-a i scheduler-a izmedju aktera ili tenant-a.
- S15 - SIGTERM sa dugim request-om, otvorenim stream-om, realtime konekcijom, in-flight job-om, migracijom i shutdown deadline-om.
- S16 - Memory pressure, handle leak, timer leak, stream error, native leak, OOM, dijagnostika i sprecavanje crash loop-a.
- S17 - Untrusted pull request, poisoned cache, lifecycle skripta, dependency confusion, kompromitovan paket i artifact substitution.
- S18 - Canary regresija, losa konfiguracija, losa schema, old-new client mismatch, rollback, forward repair i reconciliation.
- S19 - Izolovani restore database-a, kljuceva, object storage-a, queue stanja, search index-a i tenant granica.
- S20 - Incident containment za kompromitovanje kredencijala, tenant leakage, korupciju, supply-chain kompromitovanje i provider outage.

