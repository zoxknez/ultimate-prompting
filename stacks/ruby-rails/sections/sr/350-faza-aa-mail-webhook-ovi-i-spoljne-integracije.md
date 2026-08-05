## Faza AA - Mail, Webhook-ovi I Spoljne Integracije

- Audituj Action Mailer delivery, queueing, retry-je, otkrivanje podataka u template-u, header injection i duplo slanje.
- Proveri outbound webhook potpis, timestamp, rotaciju kljuceva, canonicalization, retry, ordering, idempotency i dead-letter handling.
- Za inbound webhook validiraj potpis pre parsiranja skupog sadrzaja i odbaci replay i cross-account routing.
- Definisi connect, TLS, request, read, write, total i pool-acquisition timeout-e za svaku spoljnu zavisnost.
- Koristi bounded retry, jitter, circuit breaking, bulkhead-e i reconciliation bez umnozavanja retry slojeva.
- Audituj SSRF, redirect-e, DNS rebinding, proxy podesavanja, credential scope i response-size limite.

