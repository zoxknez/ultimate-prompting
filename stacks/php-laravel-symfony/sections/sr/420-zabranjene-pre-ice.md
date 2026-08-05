## Zabranjene prečice

- Ne izvodi produkcionu istinu iz source konfiguracije, `.env.example`, lokalnog Docker-a, zelenog pipeline-a ili framework default-a.
- Ne tretiraj `composer install`, unit testove, statičku analizu ili uspešan HTTP smoke test kao kompletan release dokaz.
- Ne pretpostavljaj da CLI i FPM koriste isti PHP, INI, ekstenzije, okruženje, working directory, korisnika ili filesystem.
- Ne pretpostavljaj da su Laravel i Symfony annotation-i, attribute-i, policy-ji, voter-i, middleware, listener-i ili service definicije efektivni bez runtime-path dokaza.
- Ne koristi UI ograničenja, hidden polja, model fillable podešavanja, route naming ili TypeScript tipove kao autorizaciju ili validaciju.
- Ne dodaj slepe retry-je oko ne-idempotentnih operacija, nested klijenata, transakcija ili provider poziva.
- Ne koristi cache, session, distributed lock, search index, queue ili object storage kao neispitan source of truth.
- Ne pokreći destruktivne migracije, backfill-eve, mass fix-eve, bulk replay ili cache flush bez odobrenja, ograničenja, observability-ja i recovery-ja.
- Ne tvrdi zero downtime dok stari FPM child procesi, stale OPcache, stari worker-i, nekompatibilne poruke ili stare schema-e ostaju neprovereni.
- Ne izlaži debug, profiler, Horizon, Telescope, Pulse, Ignition, phpinfo, health detalje ili stack trace-ove kao operativnu prečicu.
- Ne deploy-uj rebuild-ovan artifact pod istom verzijom, ne koristi mutable tagove, ne instaliraj zavisnosti u produkciji i ne menjaj vendor kod in-place.
- Ne čisti kompromitovan host in-place i ne proglašavaj ga trusted, niti radi restore iz neproverenog backup-a.
- Ne označavaj nalaz kao popravljen dok uzrok, regression test, packaged artifact, deployment putanja, telemetry i rollback ili recovery nisu verifikovani.

