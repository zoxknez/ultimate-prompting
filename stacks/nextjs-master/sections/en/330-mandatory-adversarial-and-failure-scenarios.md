## Mandatory Adversarial And Failure Scenarios

Execute every applicable scenario safely. A blocked scenario remains UNVERIFIED with exact blocker, risk, and evidence plan.

- **S1** - Cross-user and cross-tenant reads through URL, cache, RSC, file, export, search, and jobs.
- **S2** - Privilege escalation through routes, actions, APIs, hidden fields, bound args, and stale sessions.
- **S3** - Duplicate/concurrent mutations from tabs, devices, retries, redirects, timeouts, and restarts.
- **S4** - Crash before commit, during ambiguity, after commit before response, and before acknowledgement.
- **S5** - Old/new browser, server, schema, cache, session, action, queue, and service worker overlap.
- **S6** - Cold-cache and cold-runtime burst with degraded database, provider, or region.
- **S7** - Nested retries and reconnect loops amplifying requests, queues, payments, email, or cost.
- **S8** - Dependency timeout, malformed/oversized response, redirect, DNS, certificate, and partial success.
- **S9** - Client disconnect during streaming, upload, action, database work, and external effect.
- **S10** - Memory, CPU, event-loop, connection, descriptor, bandwidth, queue, and quota exhaustion.
- **S11** - Key, token, cookie, secret, certificate, action encryption, and provider credential rotation.
- **S12** - Malicious HTML, Markdown, SVG, URL, redirect, file, archive, webhook, parser, RSC, and SSRF.
- **S13** - Proxy matcher bypass through paths, hosts, locales, route types, RSC requests, and rewrites.
- **S14** - Offline account switch, logout, multiple tabs, worker update, stale HTML, and queued conflicts.
- **S15** - Migration interruption, mixed-version reads/writes, validation, rollback attempt, and repair.
- **S16** - Observability outage, redaction failure, cardinality spike, source-map exposure, and evidence preservation.
- **S17** - Untrusted PR, compromised dependency, poisoned cache, mutable artifact, and release credential compromise.
- **S18** - Traffic rollback after irreversible data, cache, email, payment, queue, file, or worker effects.
- **S19** - Isolated restore with keys, schema, object storage, queues, search, cache warmup, and tenant verification.
- **S20** - Framework/RSC emergency advisory requiring containment, patch, canary, rollback, and trusted rebuild.

