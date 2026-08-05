## Faza 0 - Safety snapshot i reproduktivan baseline

### Obavezne komande

```bash
git status --short --branch
git rev-parse HEAD
git submodule status --recursive || true
node --version
corepack --version || true
# use the package manager selected by the lockfile
# npm ci | pnpm install --frozen-lockfile | yarn install --immutable
# run repository lint, typecheck, unit, integration, production build, production start, and smoke scripts
```

### Baseline pravila

- Pokreni iz cistog checkout-a ili zabelezi svaku lokalnu izmenu koja utice na rezultat.
- Koristi frozen ili immutable instalaciju i prekini na lockfile drift-u.
- Ne koristi dev-mode uspeh kao zamenu za production build i production start.
- Sacuvaj route manifest-e, build izlaz, upozorenja, static/dynamic odluke, bundle analizu i runtime logove.
- Ponovi autoritativni build u release platform image-u, arhitekturi, klasi okruzenja i package-manager mode-u.
- Pokreni izgradjeni artefakt bez produkcionih side effect-a i smoke-testiraj kriticne tokove.

### Baseline izlazi

- Log komandi sa exit code-ovima i relevantnim upozorenjima.
- Tabela verzija i lifecycle-a za framework, runtime, package manager, ORM, auth i platformu.
- Pocetni inventar ruta, runtime-a, cache-a, identiteta, podataka i deployment-a.
- Pocetna P0/P1 containment odluka pre rada nizeg prioriteta.

