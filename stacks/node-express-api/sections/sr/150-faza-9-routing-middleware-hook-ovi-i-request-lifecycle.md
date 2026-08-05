## Faza 9 - Routing, Middleware, Hook-ovi I Request Lifecycle

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Napravi uredjen graf za context, request ID, logging, security header-e, CORS, parser-e, raw body, auth, autorizaciju, limite, validaciju, handler-e, 404 i greske.
- Proveri da svaka public, authenticated, internal, admin, webhook, health, debug i metrics ruta prolazi kroz nameravane kontrole.
- Detektuj middleware ili hook-ove koji niti zavrsavaju niti nastavljaju, pozivaju next dva puta, salju dva puta, menjaju shared state ili gutaju greske.
- Proveri da se raw-body capture desava samo gde je potreban i da ne moze zaobici size, auth ili content-type kontrole.
- Audituj route precedence, wildcard i parameter ponasanje, slash obradu, case sensitivity, method fallback-e i OPTIONS ponasanje.
- Obezbedi da request-scoped cleanup radi na success, validation failure, error, timeout, abort i shutdown putanjama.

### Obavezni Dokazi

- Proizvedi i sacuvaj efektivnu matricu ruta i kontrola.
- Proizvedi i sacuvaj graf redosleda middleware-a ili hook-ova.
- Proizvedi i sacuvaj request lifecycle i cleanup trace-ove.

### Obavezni Failure I Acceptance Testovi

- Dokazi da svaka osetljiva ruta prolazi autentikaciju i autorizaciju.
- Dokazi da validation failure ne moze da preskoci audit logging.
- Dokazi da abort i timeout izvrsavaju cleanup tacno jednom.

