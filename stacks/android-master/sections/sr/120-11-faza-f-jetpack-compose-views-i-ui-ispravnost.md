## 11. Faza F - Jetpack Compose, Views I UI Ispravnost

### 11.1 Compose State I Side Effect-i

1. Proveri da su state ownership i hoisting postavljeni sto nize uz ocuvanog jednog owner-a.
2. Detektuj mutable objekte predstavljene kao immutable state, unstable collection-e i in-place mutaciju koju Compose ne moze pravilno da opazi.
3. Pregledaj `remember`, `rememberSaveable`, custom saver-e, key-eve i ownership kroz navigaciju i configuration change.
4. Pregledaj `LaunchedEffect`, `DisposableEffect`, `SideEffect`, `produceState`, `snapshotFlow` i `rememberUpdatedState` zbog ispravnih key-eva i cleanup-a.
5. Proveri da composable funkcije ne pokrecu nekontrolisan rad niti rade I/O tokom composition-a.
6. Proveri da su event lambda-e stabilne gde to materijalno koristi i da ne hvataju stale state.
7. Proveri da lazy layout-i koriste stabilne jedinstvene key-eve i ispravne content type vrednosti gde treba.
8. Proveri derived state, snapshot read, nested scrolling, focus, input, animation i measure policy zbog ispravnosti.
9. Proveri da preview, screenshot fixture-i i fake podaci ne cure u production kod.
10. Potvrdi da je UI state deterministican pri recomposition-u i ne zavisi od slucajnog broja poziva.

### 11.2 Compose Performanse I Stability

1. Meri pre optimizacije. Koristi recomposition tooling, compiler report-e, traces, Macrobenchmark i reprezentativne release build-ove.
2. Detektuj skupe kalkulacije, alokacije, sortiranje, filtriranje, image processing, formatiranje i kreiranje objekata u hot composition putanjama.
3. Stability pregledaj samo gde dokazi pokazuju nepotrebnu recomposition ili problem sa preskakanjem.
4. Ne dodaj `@Stable` ili `@Immutable` da bi utisao report osim kada je ugovor zaista tacan.
5. Proveri strong skipping i compiler ponasanje za stvarni Kotlin i Compose toolchain.
6. Odlozi citanje brzo promenljivog state-a do najuzeg prakticnog phase-a.
7. Proveri da animacije, liste, grid-ovi, pager-i, nested scroll, slike i video ne stvaraju merljiv jank.
8. Testiraj release mode sa R8 jer debug performanse nisu reprezentativne.
9. Proveri da Baseline Profiles pokrivaju stvarne kriticne tokove i da su upakovani u release artefakt.
10. Zabelezi frame timing, jank, startup, allocation i memory dokaze pre i posle popravke.

### 11.3 Views, Fragment-i I Interoperabilnost

1. Proveri da se Fragment view binding cisti u `onDestroyView` i ne nadzivljava view lifecycle.
2. Proveri da observer-i i collector-i koriste ispravan lifecycle owner.
3. Proveri adapter-e, DiffUtil identity, stable ID-jeve, recycled state, payload-e, listener-e i selection ponasanje.
4. Proveri da custom view podrzava state saving, accessibility, measurement, RTL, font scale i configuration change.
5. Proveri ComposeView disposal strategy i View-in-Compose lifecycle ownership.
6. Proveri mixed navigation i state ownership preko Fragment, Activity, Compose i ViewModel granica.
7. Detektuj synthetic view pretpostavke, deprecated API-je, retained fragment-e i callback leak-ove.
8. Ne prepisuj stabilne Views ekrane u Compose bez merljivog product ili maintenance razloga.

