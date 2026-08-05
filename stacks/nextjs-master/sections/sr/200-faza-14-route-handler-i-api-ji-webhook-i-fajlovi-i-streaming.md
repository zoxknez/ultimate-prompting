## Faza 14 - Route Handler-i, API-ji, webhook-i, fajlovi i streaming

Auditiraj svaki spolja dostupan protokol kao eksplicitan ugovor sa bounded resursima i bezbednim failure-om.

### Zahtevi audita

- Inventarisi metode, content type-ove, scheme, authn, authz, CORS, CSRF, rate, body limite, timeout-e, cache i response ugovore.
- Spreci BOLA, mass assignment, injection, traversal, open redirect, SSRF, smuggling, unbounded paginaciju i stack leakage.
- Za webhook-e proveri raw-body potpis, algoritam, rotaciju, timestamp, replay, ordering, acknowledgement, retry i idempotency.
- Za upload proveri streaming limite, magic bytes, archive ekspanziju, malware workflow, temp storage, ownership i signed URL expiry.
- Za download i export ponovo autorizuj, vezi owner/tenant, sanitizuj nazive i spreci active-content injection.
- Za SSE/streaming definisi cancellation, heartbeat, reconnect, buffering, slow consumer, backpressure, timeout i cleanup.

### Obavezni dokazi

- Endpoint i protocol matrica sa trust, resource i failure limitima.
- Posmatrani status, header-i, body, cache i error ugovor.
- Webhook signature i replay dokaz.
- Upload/download parser, storage, authorization i cleanup dokaz.

### Obavezni failure i acceptance testovi

- Bezbedno fuzz-uj malformed putanje, header-e, content type-ove, encoding-e, body-je, multipart, arhive i range-eve.
- Replay-uj webhook-e oko retry-ja, acknowledgement loss-a, crash-a i key rotation-a.
- Upload-uj oversized, polyglot, archive-bomb, traversal, duplicate-name i interrupted fajlove.
- Prekini spore streaming klijente i dokazi bounded memoriju i cleanup.

