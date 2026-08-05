## 12. Signali, slot-ovi, događaji, reentrancy i UI stanje

### 12.1 Obim audita

1. Inventariši kritične signal-slot konekcije, connection tipove, lambda-e/closure-e, queued argumente, event filter-e, custom event-e i direktne method pozive preko granica.
2. Identifikuj duple konekcije, connection leak-ove, stale receiver-e, captured mutable stanje, zadržane objekte, tihi signature mismatch i dvosmislenost overloaded signala.
3. Pregledaj direct, queued, blocking queued i auto connection ponašanje sa stvarnim sender i receiver thread affinity-jem.
4. Proceni nested event loop-ove iz modalnih dialoga, `processEvents`, sinhronih čekanja, drag/drop-a, menija, native dialoga i reentrant callback-ova.
5. Mapiraj tranzicije UI stanja, enabled/disabled kontrole, fokus, selekciju, progress, cancellation, optimistic izmene, greške, retry i rollback.
6. Obezbedi da user-triggered akcije ne mogu pokrenuti dupli ne-idempotent rad kroz double-click, shortcut, meni, tray, deep link ili restore-ovano stanje.

### 12.2 Obavezna verifikacija

1. Loguj i testiraj uspostavljanje konekcije, thread isporuke, redosled, duplu isporuku, destrukciju receiver-a, disconnect i shutdown.
2. Forsiraj brzo ponovljen input, modal reentrancy, odloženi završetak, out-of-order završetak, cancellation, zatvaranje prozora i promenu naloga.
3. Verifikuj da se UI izmene dešavaju samo na GUI thread-u i da se stale rezultati odbacuju pomoću operation identiteta, generation-a ili provere aktuelnog konteksta.
4. Zameni `processEvents` ili sinhrona GUI čekanja eksplicitnim asinhronim state machine-ama osim ako ostaje usko opravdana i testirana upotreba.
5. Dokaži da action gating, idempotency i domain constraint-i rade nezavisno od disabled stanja dugmeta.

