## 5. Arhitektura, domen, state i React semantika

### 5.1 Domen i vlasnistvo
- Mapiraj funkcije, domenska pravila, repository-je, API klijente, native servise, navigaciju, state store-ove, cache, persistence, background worker-e i vlasnike observability-ja.
- Eksplicitno navedi kriticne invarijante i utvrdi gde se sprovode na klijentu, native sloju, backend-u, bazi i store/update sistemima.
- Otkrij duplirani autoritet izmedju React state-a, query cache-a, lokalne baze, native singleton-a, navigation parametara, persistent storage-a i backend stanja.
- Definisi vlasnistvo i cleanup za subscription, listener, timer, socket, task, native handle, media session, senzor i background registraciju.
- Odvoji poslovnu politiku od UI pogodnosti i nikada se ne oslanjaj na skriven, disabled ili unmounted UI kao autorizaciju.
- Dokumentuj degraded, offline, logged-out, suspended, process-restored i delimicno migrirana stanja.

### 5.2 State management i server state
- Auditiraj Redux, Zustand, MobX, Recoil, Jotai, Context, custom store-ove i query biblioteke prema stvarnoj upotrebi, a ne ideologiji.
- Dokazi da cache kljucevi ukljucuju user, tenant, locale, permission, environment, filter i version dimenzije kada su potrebne.
- Proveri da login, logout, promena naloga, promena tenant-a, token refresh, restart aplikacije, OTA update i native update bezbedno ciste ili migriraju state.
- Auditiraj optimistic mutation po conflict detection-u, rollback-u, idempotentnosti, retry-ju, reconciliation-u i korisniku vidljivoj neizvesnosti.
- Otkrij stale closure, stale selector, slucajne global singleton-e, non-serializable state, neogranicenu istoriju i persistence prolaznih tajni.
- Testiraj paralelne ekrane, vise tabova, background refresh, duplirane zahteve i out-of-order odgovore.

### 5.3 React rendering i concurrent funkcije
- Pregledaj identitet komponente, stabilnost key-a, memoization, context fan-out, granularnost selector-a, skup render rad i nepotrebne bridge ili JSI pozive.
- Auditiraj svaki effect po ispravnosti dependency-ja, cleanup-u, idempotentnosti, stale callback obradi, abort ponasanju i osetljivosti na Strict Mode.
- Proveri Suspense, transition, optimistic state, deferred rad i error boundary pod navigacijom, retry-jem, backgrounding-om i rekreiranjem procesa.
- Ne zakljucuj performance samo iz broja rendera; koreliraj JS rad, UI-thread rad, Fabric commit, layout, native pozive, GPU frame-ove i korisnicki dozivljenu latenciju.
- Testiraj brzo mount-unmount ponavljanje, zamenu ekrana, nested navigator-e, list recycling, prekid animacije i stale asinhroni zavrsetak.
- Tretiraj React Compiler ili automatsku memoizaciju kao merenu migraciju, a ne zamenu za ispravno vlasnistvo i state dizajn.

