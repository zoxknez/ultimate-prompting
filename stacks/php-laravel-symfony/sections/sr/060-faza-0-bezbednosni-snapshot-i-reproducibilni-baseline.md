## Faza 0 - Bezbednosni snapshot i reproducibilni baseline

### Cilj

Zabeleži tačno početno stanje i izvrši samo bezbedne baseline provere svesne side effect-a pre dijagnoze ili popravke.

### Zahtevi audita

- Zabeleži branch, commit, dirty state, submodule-e, worktree-e, tagove, generisane fajlove, lokalne patch-eve i deployment reference.
- Identifikuj autoritativni Composer lockfile, monorepo granice, path repozitorijume i environment-specific dependency resolution.
- Popiši postojeće lint, static analysis, test, build, bootstrap, smoke, migration, queue i security komande bez izmišljanja default-a.
- Proceni bootstrap side effect-e pre pokretanja `artisan`, `bin/console`, application entrypoint-a, service provider-a, bundle-ova ili custom skripti.
- Sačuvaj logove, neuspele komande, stack trace-ove, konfiguracione fingerprint-e i prvi reproduktibilni kvar.
- Proveri da lokalne provere ne mogu da se povežu na produkcione baze, redove, cache, email, payment, storage, search ili identity provajdere.

### Obavezni dokazi

- Dnevnik komandi sa direktorijumom, binary-jem, SAPI-jem, INI-jem, okruženjem, exit code-om i redigovanim rezultatom.
- Snapshot repozitorijuma i eksplicitna lista nedostupnih ili nebezbednih dokaza.
- Rezultati baseline testova i bootstrap-a iz disposable okruženja.

### Kriterijumi prihvatanja

- Početno stanje je povratno i nije nastao neodobren produkcioni side effect.
- Svaki naredni nalaz može da se poveže sa konkretnom revizijom i okruženjem.

