## Redosled Rada

1. zastita radnog prostora;
2. odredjivanje tehnoloske staze;
3. module/workspace inventar;
4. toolchain i lifecycle analiza;
5. dependency i supply-chain analiza;
6. pocetni build/test/lint baseline;
7. arhitektonska mapa i kriticni tokovi;
8. concurrency i lifecycle;
9. unsafe/FFI;
10. data i transaction;
11. security;
12. performance i observability;
13. dokazivi nalazi;
14. minimalne popravke i regresioni testovi;
15. production build, deployment i rollback;
16. zavrsni izvestaj.

Iterativno: inventar -> dokaz -> osnovni uzrok -> minimalna popravka -> test -> race/Miri/sanitizer gde relevantno -> production build -> deployment -> rollback -> dokumentovanje.

Prioriteti: zastita korisnika i podataka; memorijska i concurrency ispravnost; autentikacija i autorizacija; funkcionalna ispravnost; transakcije i idempotency; operativna pouzdanost; performanse zasnovane na merenju; odrzivost arhitekture; developer experience.

Krajnji rezultat mora omoguciti drugom iskusnom Go ili Rust inzenjeru da nedvosmisleno utvrdi: koji toolchain je koriscen; sta je stvarno izvrseno; koji targeti i feature/tag kombinacije su provereni; sta je pronadjeno; kako je problem reprodukovan; koji je osnovni uzrok; sta je promenjeno; koji test dokazuje popravku; da li postoji race, unsafe ili FFI rizik; sta nije provereno; kako se artefakt deployuje; kako se rollout prekida; kako se sistem vraca ili oporavlja.
