## Mandatory Adversarial and Failure Scenarios

Execute or faithfully simulate all applicable scenarios. For every skipped scenario, record the reason, risk, owner, and compensating evidence.

1. A second authenticated tenant requests, mutates, exports, or downloads another tenant's resource through direct and indirect identifiers.
2. Two clients submit the same critical mutation concurrently with and without the same idempotency key.
3. The process crashes before database commit, during commit uncertainty, and after commit but before the response or message acknowledgement.
4. A queue message is duplicated, reordered, delayed, replayed after DLQ, and consumed by old and new worker versions.
5. A scheduled task runs twice, misses a run, loses its lock, exceeds lock TTL, and overlaps across replicas.
6. The database becomes slow, rejects connections, returns deadlocks, loses a primary, or exposes replica lag during a critical flow.
7. Redis or session storage becomes unavailable, evicts keys, returns stale data, or fails over during authentication and authorization.
8. An external provider times out, rate-limits, returns malformed success, duplicates a webhook, rotates keys, and confirms a side effect late.
9. A user logs out or is suspended while sessions, API tokens, queued jobs, signed URLs, and long-running exports still exist.
10. Two sequential requests from different users and tenants execute on the same long-lived worker and exercise locale, auth, tracing, and singleton state.
11. A large, deeply nested, compressed, malformed, or parser-hostile payload targets JSON, XML, YAML, archive, image, PDF, CSV, and regex paths.
12. A URL importer or webhook target uses redirects, DNS rebinding, alternate IP syntax, internal hostnames, and cloud metadata addresses.
13. A deployment occurs with old FPM children, stale OPcache, old queue workers, warmed new caches, mixed schema, and in-flight requests.
14. A secret, session key, webhook key, OAuth key, or signing key rotates while old and new processes coexist.
15. The application receives SIGTERM during an HTTP mutation, queue side effect, scheduled job, migration, file conversion, and export.
16. A migration is paused, retried, partially applied, rolled back at application level, and followed by a forward repair.
17. A cache key, session payload, queued message, or serialized object produced by an old release is consumed by a new release and vice versa.
18. A restore is performed in isolation from backup and point-in-time logs, then validated for authorization, integrity, queue state, files, and search.
19. A vulnerable dependency, malicious Composer plugin, poisoned CI cache, substituted artifact, or compromised deployment credential is detected.
20. An active webshell or unknown executable file is discovered on a production host while code, credentials, and data integrity are uncertain.

