## 32. Observability, dijagnostika, crash reporting i supportability

### 32.1 Obim audita

1. Inventariši strukturisane logove, audit event-e, metrike, trace-ove, crash reporting, native dump-ove, Python exception hook-ove, Qt poruke, performance trace-ove i support bundle-ove.
2. Zabeleži release, artifact hash, kanal, platformu, arhitekturu, Python, Qt, PySide6, packaging režim, data schema-u, konfiguraciju, pseudonim naloga/tenant-a i feature flag-ove gde privatnost dozvoljava.
3. Pregledaj log nivoe, cardinality, sampling, retention, redaction, lokalno skladištenje, consent za upload, offline buffering, exporter kvar i support pristup.
4. Obezbedi da GUI-thread zastoji, worker kvarovi, deadlock-i, rast queue-a, memory pressure, update kvar, migration kvar, device disconnect i data corruption budu dijagnostikovani.
5. Definiši health i readiness za lokalne helper-e, servise, baze, update kanale, mrežne zavisnosti i kritične background worker-e.
6. Mapiraj user-facing incident ID-jeve na privacy-safe tehničke dokaze bez izlaganja tajni ili internih implementacionih detalja.

### 32.2 Obavezna verifikacija

1. Forsiraj reprezentativne kvarove i verifikuj da instalirana aplikacija emituje dovoljne, korelisane i redigovane dokaze i actionable korisnička uputstva.
2. Potvrdi da crash i support artefakti mogu identifikovati tačne isporučene bajtove i učitane native komponente, ne samo marketing verziju.
3. Testiraj offline buffering, pun disk, exporter outage, permission denial, crash-loop rate limiting i user opt-out ponašanje.
4. Verifikuj da je generisanje support bundle-a bounded, cancellable, consented, redigovano, reviewable i bezbedno od symlink/path napada.
5. Definiši dashboard-e, alert-e, runbook-e, vlasnike, eskalaciju i release-correlation procedure za materijalne produkcione signale.

