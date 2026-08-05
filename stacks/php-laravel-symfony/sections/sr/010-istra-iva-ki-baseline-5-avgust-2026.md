## Istraživački baseline - 5. avgust 2026.

Ovo je datirana početna tačka. Ponovo proveri zvanične izvore, lockfile, instalirane pakete, container image, OS distribuciju, arhitekturu, libc, ekstenzije, SAPI, web server, process manager i pokrenuti proces pre svake odluke o lifecycle-u, migraciji, bezbednosti ili kompatibilnosti.

| Komponenta | Baseline | Obavezna provera tokom audita |
| --- | --- | --- |
| PHP | 8.5 aktivan; 8.4 aktivan do 31. decembra 2026; 8.3 i 8.2 su security-only na datum baseline-a. | Tačan patch, faza podrške, build opcije, SAPI, arhitektura, ekstenzije, INI, image i podrška provajdera. |
| PHP patch verzije | 8.5.9 je naveden u zvaničnom PHP 8 changelog-u 30. jula 2026. | Ponovo proveri najnoviji patch za svaku deployment minor liniju; nikada ne zaključuj samo iz lokalnog CLI-ja. |
| Laravel | 13.x stabilan; zahteva PHP 8.3-8.5; Laravel 12 ostaje podržan u objavljenom periodu. | Tačan framework patch, PHP matrica, first-party paketi, upgrade guide, deployment model i advisories. |
| Symfony | 8.1 je aktuelna stabilna linija; 7.4 je aktuelni LTS; 6.4 ostaje stariji podržani LTS. | Tačni patch-evi komponenti, PHP zahtev, Flex recipes, podrška bundle-ova, deprecation-i i izabrana LTS strategija. |
| Composer | 2.10.2 je najnoviji stabilni na datum baseline-a; 2.2 LTS postoji za ograničena legacy okruženja. | Stvarni binary, provera instalera, plugin-ovi, repozitorijumi, audit ponašanje, platform config i reproducibilnost lock-a. |
| Runtime model | FPM i mod_php su request-scoped; Octane, FrankenPHP worker mode, RoadRunner, Swoole, ReactPHP i Amp zadržavaju process state. | Stvarni SAPI i worker mode, reset semantika, životni vek procesa, reload, drain, rast memorije i mixed-version ponašanje. |

### Politika primarnih izvora

- Koristi zvaničnu PHP, Laravel, Symfony, Composer, framework package, database, web-server, process-manager, hosting-platform, OpenTelemetry, OWASP i standards dokumentaciju.
- Zabeleži naslov izvora, URL, datum pristupa, tačnu tvrdnju, izabranu verziju i dokaz iz repozitorijuma ili runtime-a koji je potvrđuje ili joj protivreči.
- Ne zamenjuj lifecycle, security, migration, transaction ili protocol smernice snippet-ima, popularnošću, sažecima ili AI-generisanim tvrdnjama.
- Kada su zvanični izvori i runtime dokaz u sukobu, prikaži sukob i zadrži odluku uslovnom dok se ne proveri tačan artefakt i proces.

