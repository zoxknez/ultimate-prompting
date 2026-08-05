## 20. Performance, memorija, baterija i kapacitet

### 20.1 Ugovor merenja
- Definisi budzet za cold start, warm start, time to interactive, navigaciju, input response, list scroll, animaciju, memoriju, bundle, binary, mrezu, bateriju i storage.
- Meri release build na reprezentativnim fizickim uredjajima niske, srednje i visoke klase sa realnim podacima i mreznim uslovima.
- Odvoji JavaScript thread, UI thread, native module, render, GPU, I/O, mrezu, bazu, image decode i backend latenciju.
- Sacuvaj p50, p95, p99, maksimum, varijansu, regression prag, velicinu uzorka, warmup i sum okruzenja.
- Uporedi stanje pre i posle svake performance promene i odbaci poboljsanje koje zrtvuje ispravnost, accessibility, memoriju, bateriju ili crash safety.
- Ne zatvaraj performance nalaz samo na osnovu simulatora, debug-a, remote debugger-a ili microbenchmark-a.

### 20.2 Startup, liste, animacije i slike
- Profilisi inicijalizaciju modula, startup native SDK-a, sinhroni storage, ucitavanje fonta, asset-a, authentication bootstrap, spremnost navigacije i prvi koristan sadrzaj.
- Auditiraj FlatList, SectionList, VirtualizedList, FlashList, custom recycler, item key, procenjenu velicinu, window, clipping, pagination i nested scrolling.
- Auditiraj Reanimated, Gesture Handler, LayoutAnimation, native animacije, shared value, worklet, UI-thread rad, cancellation i stale callback.
- Ogranici dimenzije slike, cache, prefetch, decode, transformaciju, animated image, thumbnail, placeholder i zadrzavanje pune rezolucije.
- Testiraj brzu navigaciju, duge liste, ponovljene medije, promenu orijentacije, fold/unfold, malo memorije, background-resume i OTA reload.
- Koristi platformske profiler-e i React Native DevTools zajedno i sacuvaj trace povezan sa identitetom izdanja.

### 20.3 Memorija, baterija, temperatura i mrezni trosak
- Meri JavaScript heap, native heap, graphics memoriju, image memoriju, database cache, socket buffer i zadrzane object grafove.
- Otkrij leak iz listener-a, timer-a, closure-a, navigacije, native modula, Fabric view-a, medija, senzora, WebView-a, SDK-a, task-a i cache-a.
- Auditiraj wakeup, polling, reconnect loop, background lokaciju, push obradu, animaciju, medije, sync i network batching po uticaju na bateriju.
- Testiraj low-memory warning, memory pressure, thermal throttling, low-power mode, data saver, metered mrezu i ograniceno background izvrsavanje.
- Postavi capacity i abuse limite za pagination, search, upload, download, offline queue, notification, medije, mape i realtime dogadjaje.
- Povezi tehnicku potrosnju resursa sa korisnickim tokom, klasom uredjaja, SLO-om, infrastrukturnim troskom i store-quality metrikom.

