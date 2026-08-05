## Faza 4 - TypeScript, module semantika i generisani ugovori

Dokazi da editori, CI, testovi, generatori i Next build proveravaju isti podrzani TypeScript ugovor.

### Zahtevi audita

- Inventarisi svaki tsconfig, project reference, path alias, moduleResolution, target, lib, JSX mode, strictness override i emitted boundary.
- Detektuj noCheck, skipLibCheck, allowJs, transpile-only putanje, neproverene declaration-e i build alate koji zaobilaze tsc.
- Proveri ESM/CJS granice, conditional exports, server/client entrypoint-e, dynamic import-e i test resolution.
- Pregledaj unsafe any, assertion-e, non-null operatore, unchecked index-e i schema/type drift na trust boundary-jima.
- Generisi API, database, GraphQL, protobuf i validation tipove deterministicki.
- Tretiraj TypeScript major kao compiler, editor, linter, bundler, generator, library i source migraciju.

### Obavezni dokazi

- Izvrseni typecheck i efektivni compiler config za svaki paket.
- Lista build/test putanja koje transpiluju bez pune provere.
- Provenance generisanih ugovora i drift provera.
- Matrica kompatibilnosti za aktuelne i planirane TypeScript linije.

### Obavezni failure i acceptance testovi

- Seed-uj neispravan generisani izlaz i dokazi da ga CI detektuje.
- Resolve-uj isti paket kroz editor, build, testove i production bundle.
- Izgradi kontrolisani upgrade branch na svim podrzanim alatima.
- Testiraj malformed runtime ulaz koji zadovoljava pogresno sirok staticki tip.

