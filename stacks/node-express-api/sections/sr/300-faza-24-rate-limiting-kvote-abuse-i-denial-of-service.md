## Faza 24 - Rate Limiting, Kvote, Abuse I Denial Of Service

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Klasifikuj endpoint-e po autentikaciji, trosku, osetljivosti, amplifikaciji, side effect-ima i abuse vrednosti.
- Primeni slojevite limite po trusted client identitetu, user-u, API key-u, tenant-u, IP-u, ruti, operation cost-u i global capacity-ju.
- Proveri proxy-aware client identitet bez forwarded-header spoofing-a ili shared-NAT denial-a.
- Posebno ogranici login, reset, OTP, search, export, upload, webhook, batch i expensive-filter operacije.
- Definisi quota atomicity, consistency, reservation, refund, cross-region semantiku i failure ponasanje.
- Koristi admission control, bounded queue-ove, load shedding, bulkhead-e i degraded mode pre potpune saturacije.

### Obavezni Dokazi

- Proizvedi i sacuvaj endpoint-cost i limit matricu.
- Proizvedi i sacuvaj quota i overload-consistency model.
- Proizvedi i sacuvaj abuse telemetry, pragove i owner dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da distributed limiti ostaju efikasni kroz replike.
- Dokazi da spoofed IP ne moze da zaobidje ili zloupotrebi limite.
- Dokazi da burst load degradira pre totalnog kvara.

