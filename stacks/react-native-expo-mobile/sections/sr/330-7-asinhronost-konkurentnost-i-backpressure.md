## 7. Asinhronost, konkurentnost i backpressure

### 7.1 Vlasnistvo JavaScript async rada
- Popisi promise, timer, event emitter, observable, socket, stream, queue, background callback i native callback sa vlasnikom i terminalnim uslovom.
- Propagiraj cancellation i deadline kroz UI nameru, query sloj, network klijent, native modul, upload/download, bazu i background rad gde je podrzano.
- Zastiti se od stale zavrsetka posle navigacije, logout-a, promene tenant-a, zamene stavke, list recycling-a ili unistenja native view-a.
- Ogranici fan-out, paralelne zahteve, task queue, event buffer, retry, reconnect loop, upload delove i prefetch.
- Definisi ponasanje za dupli tap, dupli callback, kasni callback, delimican uspeh, timeout, disconnect, suspenziju aplikacije i gasenje procesa.
- Testiraj deterministicke race uslove sa kontrolisanim satom, odlozenim odgovorom, promenjenim redosledom dogadjaja, ponovljenim notification-om i prinudnom lifecycle tranzicijom.

### 7.2 Stream, realtime i spori consumer-i
- Posebno auditiraj WebSocket, SSE, GraphQL subscription, Bluetooth, sensor, media, location i custom native event stream.
- Definisi ordering, deduplikaciju, replay, sequence gap, resume token, reconnect backoff, refresh autentikacije i resubscription.
- Ogranici zadrzane dogadjaje i memoriju kada su JS thread, UI thread, uredjaj ili consumer spori.
- Proveri da native emitter prestaje kada listener nestane i da ne zadrzava unisteni view, activity, fragment, view controller ili bridge stanje.
- Testiraj background aplikacije, promenu mreze, airplane mode, restart servera, istek tokena, OTA reload i native upgrade tokom aktivnog stream-a.
- Izlozi metrike za dubinu queue-a, broj reconnect-a, odbacene dogadjaje, duple dogadjaje, lag i vreme od poslednjeg potvrdjenog stanja.

