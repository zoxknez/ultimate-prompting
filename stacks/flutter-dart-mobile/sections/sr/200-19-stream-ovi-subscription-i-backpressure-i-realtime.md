## 19. Stream-ovi, subscription-i, backpressure i realtime

Pregledaj stream-ove kao dugotrajne ugovore resursa i redosleda.

- Popiši single-subscription i broadcast stream-ove, controller-e, subject-e, database watcher-e, socket-e, SSE, platform event channel-e i push-derived stream-ove.
- Proveri vlasništvo subscription-a, pause/resume, cancellation, close, error handling, done semantiku, replay, buffering i lifecycle vezivanje.
- Audituj redosled događaja, duplikate, praznine, reconnect, resume cursor, snapshot plus delta, clock skew, zastareo cache i obradu version conflict-a.
- Definiši backpressure, bounded queue, politiku odbacivanja/spajanja, ponašanje sporog potrošača i memorijske limite za stream-ove velikog obima.
- Spreči duple listener-e posle rebuild-a, navigacije, reconnect-a, hot reload-a, promene naloga i background/foreground tranzicija.
- Proveri da su osetljivi događaji filtrirani po trenutnom identitetu, tenant-u, vlasništvu resursa i stanju opoziva pre mutacije ili prikaza stanja.
- Testiraj disconnect storm, duple frame-ove, malformirane poruke, restart servera, istek resume tokena i duge offline periode.
- Meri event lag, dubinu queue-a, odbačene/spojene događaje, reconnect stopu, rast memorije i pritisak na server.

