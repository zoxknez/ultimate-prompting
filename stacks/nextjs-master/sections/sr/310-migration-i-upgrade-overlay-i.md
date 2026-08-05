## Migration i upgrade overlay-i

### Next.js 15/16 ka 16.3

- Procitaj svaki medjukorak migration guide-a i security advisory-ja; ne preskaci major ili maintained patch linije bez dokaza.
- Inventarisi async request API-je, routing, caching, Proxy migraciju, Turbopack, images, runtime-e i uklonjeni config.
- Proveri App Router, Pages Router, mixed mode, custom server, adapter-e, instrumentation, auth, testove i observability na svakom koraku.
- Razdvoji framework upgrade od TypeScript major-a, React Compiler-a, baze, auth-a, infrastrukture i cache redizajna.
- Odrzavaj testirani rollback ili forward repair za kod, schemu, cache, asset-e, sesije i dugotrajne klijente.

### Middleware ka Proxy

- Koristi zvanicni codemod ili kontrolisani rename tek posle mapiranja matcher-a, import-a, testova, deployment pravila i dokumentacije.
- Proveri semantiku, runtime, pokrivenost, redirect-e, rewrite-e, header-e i auth pretpostavke posle migracije.
- Premesti security odluke na destination data i mutation granice kada su bile koncentrisane u Middleware-u.
- Ponovo testiraj rute, API-je, RSC request-e, static asset-e, host-ove, locale-e i encoded putanje.

### React Compiler 1.0

- Potvrdi React/compiler kompatibilnost, sintaksu, library ponasanje, lint, source map-e, debugging i cache ponasanje.
- Pocni sa izmerenim rutama ili paketima, eksplicitnim cohort-om, pre/posle metrikama, correctness testovima i brzom disable putanjom.
- Ne uklanjaj manuelnu memoizaciju dok ponasanje i performanse nisu dokazani pod compiler-om.
- Auditiraj external store-ove, identity-sensitive vrednosti, mutable objekte, effect-e i library komponente.

### TypeScript 6 ka 7

- Tretiraj TypeScript 7 kao stabilan, ali pre produkcionog usvajanja proveri njegov native compiler, language service, API-je, editor, plugin-e, generatore, bundler-e i kompatibilnost biblioteka.
- Pokreni compiler, editor, Next build, ESLint, test runner, Storybook, generatore, monorepo alate i biblioteke na compatibility branch-u.
- Zabelezi diagnostic-e, resolution, emit/bundle razlike, performanse, declaration-e i suppressed greske.
- Ne kombinuj TypeScript major sa nepovezanim framework, React, schema, cache ili deployment redizajnom.

