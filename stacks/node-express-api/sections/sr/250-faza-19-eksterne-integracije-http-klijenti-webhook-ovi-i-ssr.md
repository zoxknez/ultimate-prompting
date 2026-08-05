## Faza 19 - Eksterne Integracije, HTTP Klijenti, Webhook-ovi I SSRF

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Inventarisi svaki eksterni hostname, protokol, kredencijal, timeout, retry, circuit breaker, rate limit i klasifikaciju podataka.
- Postavi connect, DNS, TLS, pool acquisition, request, read, write, total i idle deadline-e odgovarajuce svakom klijentu.
- Propagiraj AbortSignal i deadline-e kroz request, database, queue, file i provider pozive gde je podrzano.
- Koristi ogranicene retry-je sa backoff-om, jitter-om, retry budget-om, svescu o idempotency-ju i sprecavanjem nested retry-ja.
- Za user-controlled URL-ove primeni scheme, resolved IP, private i metadata range-ove, redirect-e, DNS rebinding, size i timeout kontrole.
- Za webhook-ove proveri raw-body potpis, timestamp, replay window, key rotation, ordering, acknowledgement i idempotency.

### Obavezni Dokazi

- Proizvedi i sacuvaj integration, timeout i retry matricu.
- Proizvedi i sacuvaj SSRF resolution i redirect dokaz.
- Proizvedi i sacuvaj webhook signature, replay i reconciliation rezultate.

### Obavezni Failure I Acceptance Testovi

- Dokazi da private i metadata adrese ostaju nedostupne.
- Dokazi da non-idempotent write se ne retry-uje slepo.
- Dokazi da webhook replay vraca sacuvani outcome bez duplih efekata.

