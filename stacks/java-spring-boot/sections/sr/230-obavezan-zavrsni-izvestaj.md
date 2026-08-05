## Obavezan Zavrsni Izvestaj

Isporuci Markdown sa:

1. Izvrsnim sazotkom i presudom: `ready`, `ready-with-conditions` ili `not-ready`.
2. Runtime/support statusom i mapama arhitekture, filter chaina, auth/authz, transakcija i kriticnih tokova.
3. Endpoint matricom: `method | route/service | auth | policy/ownership | validation | rate limit | idempotency | transaction | timeout | side effect | test | status`.
4. Matricama kriticnih upisa transaction/idempotency i migration rollouta.
5. Nalazima: `ID | P0-P3 | area | file/symbol | cause | impact | evidence | repair | verification | status`.
6. Implementiranim izmenama, fajlovima, dependency/configuration/migration promenama, regresionim rizikom i validacijom.
7. Stvarnim komandama, Java/build-tool/framework verzijama, okruzenjima, exit kodovima i bitnim rezultatima.
8. Rezultatima bezbednosti, konkurentnosti, load/performance, startupa, healtha i graceful shutdowna.
9. Blokiranim proverama, tacnim blokatorima i preostalom riziku.
10. Preostalom radu grupisanom u `blocks production`, `needed soon`, `planned refactor` i `optional improvement`, sa vlasnikom, zavisnoscu, kriterijumom prihvatanja i rokom koji definise organizacija.
11. Spoljnim izvorima: naslov, URL, verzija/status, datum pristupa i odluka na koju su uticali.

Pocni projekt inventarom, Java/Spring lifecycle proverom, deterministickim buildom i produkciji slicnim startupom. Ne pocinji stilsko ciscenje dok autorizacija, transakcije, database invarijante, idempotentnost, timeouti, probe i graceful shutdown nisu dokazani.
