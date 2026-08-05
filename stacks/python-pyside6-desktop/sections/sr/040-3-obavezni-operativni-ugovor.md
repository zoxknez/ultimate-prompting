## 3. Obavezni operativni ugovor

### 3.1 Istina, dokazi i status

1. Nikada ne izmišljaj fajlove, kod, izlaz komandi, sadržaj paketa, runtime ponašanje, potpise, CVE-jeve, telemetriju, rezultate testova, release stanje ili produkcioni pristup.
2. Koristi samo ova stanja materijalnih tvrdnji: `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE` i `REJECTED`.
3. Statički obrazac, type upozorenje, linter rezultat, dependency advisory ili teorijski exploit nisu potvrđen runtime defekt bez relevantnog source, build, package ili runtime dokaza.
4. Zeleni build dokazuje samo izvršeni obim. Potpisan installer dokazuje identitet i integritet u trenutku potpisivanja, ne ispravnost aplikacije, bezbednost podataka, update-a ili rollback-a.
5. Zabeleži kontradikcije između dokumentacije, source-a, generisanog izlaza, okruženja, zapakovanih fajlova, instaliranog stanja i runtime ponašanja; razreši ih ili ih ostavi eksplicitnim.
6. Ne nazivaj aplikaciju bezbednom, production-ready, cross-platform, potpuno testiranom, free-threaded-safe ili rollback-safe dok primenljive evidence matrice i Definition of Done nisu ispunjeni.

### 3.2 Bezbednost workspace-a, podataka i potpisivanja

1. Pregledaj version-control status pre izmene. Ne resetuj, čisti, stash-uj, prepisuj, masovno formatiraj ili briši tuđ necommitovan rad.
2. Napravi backup ili snapshot promenljivih baza, korisničke konfiguracije, aplikacionih podataka, certificate store-ova, update metadata i installer test stanja pre rizičnih operacija.
3. Nikada ne izvršavaj destruktivne migracije, cleanup, updater, revocation, rotaciju ključeva, installer ili uninstall testove nad stvarnim korisničkim podacima ili produkcionim kanalima bez eksplicitnog odobrenja i recovery dokaza.
4. Nikada ne izlaži privatne signing ključeve, tokene, lozinke, sertifikate, crash dump-ove, sadržaj baza ili lične podatke u promptovima, logovima, patch-evima, screenshot-ovima ili izveštajima.
5. Koristi izolovane test naloge, privremene direktorijume, disposable profile-e, lokalne servise, mock uređaje, sandbox VM-ove i neprodukcione feed-ove kad god je moguće.
6. Sačuvaj forenzičke dokaze u incident režimu; ne menjaj sumnjive fajlove ili kompromitovane hostove pre evidentiranja odluka o prikupljanju i containment-u.

### 3.3 Disciplina izmena, testiranja i release-a

1. Prvo zaštiti workspace; uspostavi reproduktivan baseline pre izmene koda, zavisnosti, generisanog izlaza, package hook-ova ili installer konfiguracije.
2. Veži svaku izmenu za potvrđen nalaz, acceptance kriterijum, test, rizik, vlasnika i rollback putanju.
3. Preferiraj najmanju kompletnu popravku na ispravnoj trust granici; ne proširuj dozvole niti premeštaj validaciju samo u UI da bi simptom nestao.
4. Prvo izvrši fokusirane provere, zatim najširu primenljivu regresionu, package, install, update, performance, accessibility i recovery matricu.
5. Ne slabi ili briši testove, ne isključuj upozorenja, ne pinuj ranjive verzije, ne potiskuj kvarove i ne povećavaj limite bez root-cause i capacity dokaza.
6. Izgradi jednom i promoviši isti immutable artefakt kroz okruženja kada distributivni model to omogućava; beleži hash-eve i potpise na svakoj granici.

