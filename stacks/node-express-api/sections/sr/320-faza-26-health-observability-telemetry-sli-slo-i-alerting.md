## Faza 26 - Health, Observability, Telemetry, SLI, SLO I Alerting

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Odvoji startup, liveness, readiness, degraded, dependency i deep diagnostic signale.
- Readiness mora da odrazava sposobnost prihvatanja bezbednog traffic-a, ne samo da je event loop ziv.
- Instrumentuj request rate, greske, latency, saturation, event-loop delay, memoriju, handle-ove, pool-ove, queue-ove, retry-je, timeout-e i zavisnosti.
- Inicijalizuj OpenTelemetry pre instrumentovanih modula gde je potrebno i proveri propagation konteksta kroz klijente, queue-ove i worker-e.
- Definisi sampling, cardinality limite, baggage politiku, redaction, retention, exporter failure i telemetry backpressure.
- Definisi user-centered SLI i SLO, error budget, burn-rate alert-e, owner-a, runbook, escalation i confirmation oporavka.

### Obavezni Dokazi

- Proizvedi i sacuvaj health-state i readiness tabelu odluka.
- Proizvedi i sacuvaj telemetry-coverage i redaction matricu.
- Proizvedi i sacuvaj SLI, SLO, alert, owner i runbook registar.

### Obavezni Failure I Acceptance Testovi

- Dokazi da readiness se povlaci pre nebezbednog dependency stanja.
- Dokazi da telemetry exporter failure ne moze da crash-uje ili saturira servis.
- Dokazi da alert-i se aktiviraju i razresavaju na testiranim failure i recovery putanjama.

