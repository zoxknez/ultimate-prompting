## Faza M - Cache, Session I Rate Limiting

Mapiraj in-memory, distributed, HTTP/CDN, database i computed cache. Proveri key design, tenant/user/permission opseg, TTL, size, invalidaciju, serialization/versioning, stampede, outage, stale strategiju. Privatni podaci nikada ne smeju koristiti shared/public kljuc. Cache nije izvor istine za kriticne invarijante.

Session: da li zaista treba; distributed store; sticky session zavisnost; size; PII; race na paralelnim zahtevima; rolling deployment.

