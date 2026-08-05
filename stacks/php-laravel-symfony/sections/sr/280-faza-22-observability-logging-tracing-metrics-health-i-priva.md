## Faza 22 - Observability, logging, tracing, metrics, health i privatnost

### Cilj

Dokaži da operatori mogu da otkriju, lokalizuju, objasne i oporave user-visible i integrity kvarove bez curenja osetljivih podataka.

### Zahtevi audita

- Definiši SLI i SLO za availability, latency, correctness, freshness, durability, queue lag, autentikaciju, kritične tokove i recovery.
- Koreliraj release, artifact, commit, runtime, host, pool, worker, request, trace, user, tenant, job, message i schema identitete gde je dozvoljeno.
- Audituj structured logove, exception chain-ove, context propagation, sampling, cardinality, retention, pristup, redaction i tamper resistance.
- Instrumentuj HTTP, console, queue, scheduler, bazu, cache, spoljne pozive, file processing, poslovne tranzicije, retry i reconciliation.
- Razdvoji process liveness, traffic readiness, dependency status i degraded business capability; spreči curenje tajni kroz health endpoint-e.
- Testiraj alert routing, deduplikaciju, inhibition, obrazloženje pragova, kvalitet runbook-a, on-call ownership i ponašanje tokom kvara telemetry backend-a.

### Obavezni dokazi

- Matrica SLI-ja, SLO-a, dashboard-a, alert-a, owner-a i runbook-a.
- Trace ili correlation dokaz za najmanje jedan kritični sinhroni i asinhroni tok.
- Redaction testovi i ponašanje pri kvaru telemetry backend-a.

### Kriterijumi prihvatanja

- Kritični kvar može da se poveže sa release-om, code path-om, zavisnošću, tenant-safe context-om i recovery akcijom.
- Telemetry ne izlaže kredencijale, session identifikatore, tajne, payment podatke, osetljive fajlove ili nepotrebne lične podatke.

