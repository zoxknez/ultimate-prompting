## 10. Faza E - Lifecycle, State, Coroutines, Flow I Navigacija

### 10.1 Coroutines I Flow

1. Pronadji `GlobalScope`, unmanaged scope-ove, orphan job-ove, custom scope-ove bez owner-a i pogresno supervisor ponasanje.
2. Proveri da su dispatcher-i injectable tamo gde testiranje ili policy to zahtevaju.
3. Detektuj disk, database, network, JSON, crypto, bitmap ili blocking rad na main thread-u.
4. Proveri da se cancellation propagira kroz repository-je, use case-ove, network pozive, database rad, player-e i UI state production.
5. Proveri exception handling, `CoroutineExceptionHandler`, `supervisorScope`, `async`, structured concurrency i izgubljene failure-e.
6. Proveri da `stateIn`, `shareIn`, replay, started policy i scope ne izazivaju leak, stale podatke, skriven background rad ili duple upstream subscription-e.
7. Proveri lifecycle-aware collection odgovarajucim API-jima kao sto su `repeatOnLifecycle` ili `collectAsStateWithLifecycle`.
8. Proveri `flowOn`, `withContext`, channel capacity, buffer, conflation, backpressure i vlasnistvo hot Flow-a.
9. Testiraj rapid input, stale search, cancellation, retry, concurrent refresh, double tap, rotation, backgrounding i process recreation.
10. Koristi `flatMapLatest`, mutex, actor, transaction, idempotency ili serialization samo gde ih stvarni concurrency model zahteva.
11. Proveri da testovi koriste deterministicke scheduler-e i ne zavise od stvarnih delay-eva.

### 10.2 ViewModel, Saved State I Process Death

1. Preferiraj screen ili destination-level ViewModel kada su njegove lifecycle prednosti primenjive.
2. Proveri da ViewModel ne zadrzava Activity, Fragment, View, NavController, mutable Context ili UI-only objekte.
3. Razdvoji durable domain podatke, screen UI state, prolazne UI event-e i navigation effect-e.
4. Proveri da state moze biti rekonstruisan nakon process death-a bez tihog oslanjanja na in-memory singleton-e.
5. `SavedStateHandle` koristi samo za mali restorable state i identifikatore, a ne kao zamenu za durable storage.
6. Proveri da one-time event-i nisu izgubljeni, duplirani ili replay-ovani nakon recreation-a.
7. Testiraj configuration change, locale, theme, font scale, multi-window, background kill i restore.
8. Proveri loading, empty, content, stale, partial, retry, permission-denied, offline i terminal error state-ove.
9. Spreci double submission i nekonzistentan UI tokom dugih write operacija.

### 10.3 Navigacija, Deep Link-ovi I Back Ponašanje

1. Mapiraj svaku destinaciju, graph, nested graph, start destination, dynamic feature i external entry point.
2. Proveri da su route argumenti typed, validirani, size-bounded i da ne prenose osetljive objekte.
3. Proveri da deep link-ovi validiraju scheme, host, path, query, identitet, tenant i autorizaciju pre prikaza ili izmene podataka.
4. Proveri da untrusted intent-i ne mogu preskociti autentikaciju, parental gate, onboarding, payment, consent ili obavezni state.
5. Testiraj cold-start, warm-start, existing-task, notification, app-link, share, restore i multiple-deep-link scenario.
6. Proveri back, predictive back, up navigation, task ponasanje, dialoge, sheet-ove, nested navigation i state restoration.
7. Spreci duple destinacije i duple side effect-e iz ponovljenih navigation event-a.
8. Proveri app link-ove i Digital Asset Links sa stvarno deploy-ovanih hostova gde je primenjivo.
9. Proveri da osetljive route ne cure kroz URL, logove, recents, screenshot-ove ili analytics.

