## 14. Faza I - Mreza, API-ji I Real-Time Komunikacija

1. Inventarisi sve base URL-ove, client-e, interceptor-e, authenticator-e, DNS ponasanje, proxy-je, WebSocket-e, streaming i download putanje po varijanti.
2. Proveri da connect, read, write, call, ping i overall timeout odgovaraju semantici operacije.
3. Proveri retry samo za bezbedne ili idempotentne operacije ili koristi idempotency key i server podrsku.
4. Proveri da cancellation zatvara pozive, stream-ove, parser-e, fajlove i progress job-ove.
5. Proveri da je authentication refresh pravilno serijalizovan i da ne stvara refresh storm ili token race.
6. Spreci release logovanje kredencijala, header-a, body-ja, media URL-ova, query parametara i PII-ja.
7. Proveri TLS default-e, trust manager-e, hostname verification, network security configuration, cleartext izuzetke i certificate pinning strategiju gde je opravdana.
8. Nikada ne prihvataj sve sertifikate niti iskljucuj hostname verification.
9. Validiraj response code, content type, content length, redirect, compression, charset, semu i error body.
10. Ogranici download, upload, decompression, dimenzije slika, parser depth i memory upotrebu.
11. Proveri resumable transfer, range request, temporary file, atomic rename, integrity check i cleanup.
12. Proveri pagination, caching, ETag, stale podatke, rate limit, backpressure i offline fallback.
13. Testiraj slow, flaky, captive, metered, roaming, IPv6-only, DNS-failure, proxy i no-network scenario gde je materijalno.
14. Proveri real-time reconnect, message ordering, duplicate delivery, missed event, heartbeat i background ogranicenja.
15. Proveri da su server greske mapirane u akcione, lokalizovane i privacy-safe user state-ove.

