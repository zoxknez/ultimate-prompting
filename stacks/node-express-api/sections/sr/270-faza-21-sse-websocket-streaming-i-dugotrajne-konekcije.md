## Faza 21 - SSE, WebSocket, Streaming I Dugotrajne Konekcije

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Inventarisi endpoint-e, upgrade putanje, autentikaciju, autorizaciju, channel-e, room-ove, topic-e, subscription-e i fan-out topologiju.
- Autentikuj uspostavljanje i ponovo autorizuj message, channel, object, tenant i state-sensitive operacije.
- Definisi frame, message, buffer, queue, subscription, connection, heartbeat, idle i lifetime limite.
- Implementiraj backpressure, obradu slow consumer-a, bounded fan-out, disconnect politiku i replay semantiku.
- Proveri cleanup listener-a, timer-a, subscription-a, socket-a, konteksta i resursa na svakoj termination putanji.
- Testiraj resume cursor, duplicate delivery, ordering, reconnect, rights revocation, rolling deployment i old-new compatibility.

### Obavezni Dokazi

- Proizvedi i sacuvaj connection i message-authorization matricu.
- Proizvedi i sacuvaj buffer, backpressure i cleanup model.
- Proizvedi i sacuvaj reconnect, draining i version-skew dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da slow consumer ne moze da iscrpi process memoriju.
- Dokazi da opozvani user gubi channel pristup u definisanom roku.
- Dokazi da rolling deployment cuva dokumentovano realtime ponasanje.

