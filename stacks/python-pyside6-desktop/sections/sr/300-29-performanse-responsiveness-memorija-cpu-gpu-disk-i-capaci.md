## 29. Performanse, responsiveness, memorija, CPU, GPU, disk i capacity

### 29.1 Obim audita

1. Definiši budžete za cold/warm startup, prvo interaktivno stanje, latenciju kritičnog toka, GUI-thread zastoj, frame time, memoriju, CPU, GPU, disk, mrežu, veličinu paketa i update-a.
2. Izmeri import vreme, inicijalizaciju modula, učitavanje resursa, fontova i ikona, QML kompilaciju, startup baze, mrežnu inicijalizaciju i render prvog prozora.
3. Profiliraj GUI thread, render thread, Python thread-ove, native thread-ove, event-loop lag, lock wait, queue wait, allocation, zadržavanje objekata, native heap, texture i handle-ove.
4. Proceni velike skupove podataka, slike, media, dokumente, cache-eve, istorije, undo stack-ove, background transfere, uređaje, više prozora i duge sesije.
5. Pregledaj batching, coalescing, pagination, lazy loading, caching, prefetch, kompresiju, worker limite i degraded režime uz constraint-e ispravnosti.
6. Definiši podržane klase uređaja, minimalni hardver, headroom, konkurentnost, maksimalnu veličinu projekta/podataka, disk zahteve i pragove kvara.

### 29.2 Obavezna verifikacija

1. Pokreni cold, warm, burst, sustained, soak, low-memory, disk-pressure, offline, dependency-slowdown i multi-window opterećenja na reprezentativnom hardveru.
2. Zabeleži ponovljiva before/after merenja sa tačnim artefaktom, skupom podataka, okruženjem, sampling-om i statističkim sažetkom.
3. Koristi Python i native profiler-e, Qt alate, OS trace-ove, heap snapshot-e, inspekciju handle-ova i graphics dijagnostiku prema potrebi.
4. Testiraj cancellation i cleanup nakon velikih operacija tako da memorija, privremeni fajlovi, thread-ovi, queue-evi i handle-ovi vrate prihvatljiv baseline.
5. Odbaci optimizacije koje slabe validaciju, autorizaciju, durability, accessibility, dijagnostiku ili recovery bez eksplicitnog odobrenog tradeoff-a.

