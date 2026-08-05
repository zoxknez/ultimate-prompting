## Phase K - Security Vulnerabilities And Abuse Controls

Targeted checks: SQL injection / raw SQL interpolation, command/shell injection, path traversal, zip-slip, SSRF, open redirect, host-header injection, XSS/unsafe HTML, XXE, unsafe deserialization / polymorphic JSON / legacy BinaryFormatter, mass assignment, log injection, regex DoS, decompression bombs, weak hashing, timing-sensitive secret comparison, upload abuse.

Rate limiting: by trusted client IP, user, API key, tenant, route, failed attempt, operational cost. Check partition key, proxy/IP handling, distributed vs per-instance, burst, `Retry-After`, fail-open/fail-closed. Login, reset, expensive search/export/upload, and job creation need distinct controls.

