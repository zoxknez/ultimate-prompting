## 7. Repozitorijum, arhitektura i vlasništvo

### 7.1 Obim audita

1. Mapiraj pakete, application entrypoint-e, UI slojeve, domain servise, data access, infrastructure adapter-e, worker-e, helper-e, plugin-e, testove, packaging i installer kod.
2. Dokumentuj granice procesa, thread-a, event loop-a, QObject-a, model/view-a, QML-a, WebEngine-a, baze, fajlova, mreže, uređaja i privilegovanih helper-a.
3. Identifikuj globalno stanje, service locator-e, singleton objekte, kružne import-e, import-time side effect-e, skriveno vlasništvo i mutable cross-feature zavisnosti.
4. Navedi kritične korisničke tokove i poslovne invarijante sa source modulima, UI entrypoint-ima, podacima, side effect-ima i recovery putanjom.
5. Razlikuj UI stanje, domain stanje, persistirano stanje, cached stanje, izvedeno stanje i stanje operativnog sistema.
6. Zabeleži vlasnike koda, formata podataka, signing-a, installer-a, update feed-a, telemetrije, privatnosti, podrške i incident response-a.

### 7.2 Obavezna verifikacija

1. Proizvedi architecture, ownership, data-flow, privilege i lifecycle dijagrame zasnovane na source i runtime dokazima.
2. Isprati najmanje jedan kritični tok od početka do kraja kroz UI, signale, servise, persistence, spoljne pozive, error handling, telemetriju i oporavak.
3. Potvrdi da smer zavisnosti i vlasništvo sprečavaju UI kod, plugin kod ili background rad da zaobiđu domain autorizaciju i invarijante.
4. Identifikuj napuštene module, duple implementacije, nedostižan kod, stale generisani izlaz i packaging-only putanje.
5. Verifikuj da svaki kritični resurs ima jednog eksplicitnog lifecycle vlasnika i svaki cross-boundary poziv ugovor.

