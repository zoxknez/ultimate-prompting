## Migration I Upgrade Overlay-i

### Node.js Release-Line Upgrade

- Proveri runtime API-je, V8, OpenSSL, ICU, native ABI, permission model, test runner, fetch ili Undici ponasanje, deprecation-e i platform podrsku.
- Testiraj svaki native addon i preuzeti binary na svim ciljnim kombinacijama arhitekture i libc-a.
- Uporedi old i new runtime kroz integration, load, memory, shutdown, failover i rollback scenarije.
- Ne koristi Node Current kao default production cilj bez eksplicitnog lifecycle i platform approval-a.

### Express 4 Na Express 5

- Inventarisi uklonjene API-je, path sintaksu, query i body promene, MIME ponasanje, async greske, wrapper-e i middleware kompatibilnost.
- Koristi codemod-e samo kao pocetnu tacku i pregledaj svaku semantic i public-contract promenu.
- Pokreni route, error, proxy, static, upload, webhook i compatibility regression suite pre promocije.
- Definisi rollback ogranicenja ako se session, cache, schema, client ili error ponasanje promeni.

### Fastify Core Ili Plugin Upgrade

- Proveri core, plugin, schema, serializer, type-provider, logger i Node podrsku kao jedan testirani graf.
- Diff-uj efektivnu encapsulation, hook-ove, scheme, parser-e, registraciju ruta i error ponasanje.
- Regenerisi i uporedi contract-e i pokreni security, load i compatibility regression testove.
- Sacuvaj testirani prethodni artefakt i data-compatible rollback putanju.

### CommonJS Na ESM

- Mapiraj package type, entrypoint-e, extension-e, exports, conditional exports, require hook-ove, dirname upotrebu, dynamic import i tooling.
- Testiraj worker-e, migracije, skripte, CLI, instrumentation, preload, native addon-e i package consumer-e.
- Izbegni dual-package duplikaciju stanja i proveri singleton pretpostavke kroz module graph.
- Izdaj sa eksplicitnim compatibility i rollback kriterijumima.

### TypeScript 6 Na TypeScript 7

- Proveri editor, CI, build, generatore, lint, testove, language-service plugin-e, decorator-e, deklaracije i source map-e.
- Uporedi compiler dijagnostiku i transformisan output za kriticne pakete.
- Ne skrivaj nove greske kroz noCheck, prosiren skipLibCheck, transpile-only putanje ili siroke suppression-e.
- Zadrzi testirani compiler i toolchain rollback dok se ne uspostavi poverenje u izdanje.

