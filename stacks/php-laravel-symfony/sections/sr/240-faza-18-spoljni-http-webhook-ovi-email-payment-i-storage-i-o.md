## Faza 18 - Spoljni HTTP, webhook-ovi, email, payment-i, storage i otpornost provider-a

### Cilj

Audituj outbound trust, timeout, retry, identity, reconciliation i degraded ponašanje za svaku spoljnu zavisnost.

### Zahtevi audita

- Inventariši svaki HTTP klijent, SDK, payment provider, mail servis, object store, identity provider, search servis, analytics sink i custom integraciju.
- Proveri connect, TLS, pool, request, response, total i queue timeout budget-e plus cancellation i propagaciju deadline-a.
- Audituj retry eligibility, backoff, jitter, maksimalne pokušaje, retry budget, nested retry, circuit breaking, bulkhead-e, rate limite i load shedding.
- Validiraj TLS trust, hostname, rotaciju sertifikata, mTLS identitet, DNS, redirect policy, korišćenje proxy-ja, credential scope i SSRF otpornost.
- Za inbound webhook-ove proveri raw-body potpise, canonicalization, timestamp, replay window, key rotation, event identitet, ordering i idempotency.
- Za payment-e i druge nepovratne efekte dokaži state-machine tranzicije, duplicate postupanje, asinhronu potvrdu, refund-e, dispute-e i reconciliation.

### Obavezni dokazi

- Matrica ugovora zavisnosti sa owner-om, timeout-om, retry-jem, kredencijalom, podacima, SLO-om i degraded režimom.
- Dokaz slow, unavailable, malformed, replayed, rotated-key, rate-limited i partial-success testova.
- Dokaz provider reconciliation-a i manuelnog recovery-ja za nepovratne efekte.

### Kriterijumi prihvatanja

- Spor ili neispravan provider ne može da iscrpi servis ili napravi nekontrolisane duplicate side effect-e.
- Svako spolja potvrđeno poslovno stanje može da se reconciliuje sa authoritative provider zapisom.

