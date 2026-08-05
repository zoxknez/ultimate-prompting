## Faza K - Security Ranjivosti I Abuse Kontrole

Ciljano proveri: SQL injection / raw SQL interpolaciju, command/shell injection, path traversal, zip-slip, SSRF, open redirect, host-header injection, XSS/unsafe HTML, XXE, unsafe deserialization / polymorphic JSON / legacy BinaryFormatter, mass assignment, log injection, regex DoS, decompression bomb, weak hashing, timing-sensitive secret poredjenje, upload abuse.

Rate limiting: po trusted client IP, user, API key, tenant, ruti, failed attempt, operativnoj ceni. Proveri partition key, proxy/IP, distributed vs per-instance, burst, `Retry-After`, fail-open/fail-closed. Login, reset, skup search/export/upload i job creation zahtevaju odvojene kontrole.

