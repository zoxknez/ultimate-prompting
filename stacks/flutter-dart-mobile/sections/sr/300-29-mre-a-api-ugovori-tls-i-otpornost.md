## 29. Mreža, API ugovori, TLS i otpornost

Audituj kompletno client-to-service ponašanje u normalnim, degradiranim, neprijateljskim i evolutivnim uslovima.

- Popiši HTTP klijente, interceptor-e, adapter-e, WebSocket/SSE klijente, GraphQL, gRPC, upload/download stack-ove, DNS ponašanje, proxy-je i platformsku mrežnu konfiguraciju.
- Proveri base URL i izbor okruženja, scheme, host allowlist-e, redirect-e, cleartext politiku, ATS/network security config, proxy ponašanje, local network pristup i validaciju sertifikata.
- Koristi eksplicitne connect, send, receive, idle i total deadline-e gde su podržani; propagiraj cancellation i deadline operacije.
- Retry-uj samo bezbedne ili idempotentne operacije sa ograničenim pokušajima, backoff-om, jitter-om, serverskim signalima, budžetom i zaštitom od overload-a.
- Proveri API šemu, content type, kompresiju, paginaciju, parcijalni odgovor, nepoznata polja, error envelope, Problem Details, lokalizaciju i backward kompatibilnost.
- Audituj interakciju token refresh-a, replay zahteva, duple body stream-ove, upload resume, integritet download-a, uklanjanje autorizacije pri redirect-u i cancellation.
- Tretiraj TLS pinning kao operativno skup opcioni control koji zahteva backup pin-ove, rotaciju, nadzor isteka, proxy politiku, emergency disable i testiran oporavak.
- Testiraj offline, captive portal, DNS failure, IPv4/IPv6, TLS failure, istekao sertifikat, spor body, prekinut body, malformiran payload, 429, 5xx, timeout, reconnect i clock skew.
- Meri distribuciju latencije, stopu grešaka, retry-je, bajtove, cache hit-ove, queue vreme, cancellation, backend amplification i user-visible oporavak.

