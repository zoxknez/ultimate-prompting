## Redosled Rada

Pocni ovim redosledom:

1. zastita radnog prostora;
2. solution i project inventar;
3. SDK/runtime/lifecycle analiza;
4. NuGet i supply-chain analiza;
5. restore/build/test/publish baseline;
6. arhitektonska mapa i kriticni tokovi;
7. security i data granice;
8. dokazivi nalazi;
9. minimalne popravke i regresioni testovi;
10. sira verifikacija, deployment i rollback;
11. zavrsni izvestaj.

Radi iterativno: inventar -> dokaz -> osnovni uzrok -> minimalna popravka -> test -> Release build/publish -> deployment analiza -> rollback -> dokumentovanje.

Prioriteti: zastita korisnika i podataka; autentikacija i autorizacija; funkcionalna ispravnost; transakcije, concurrency i idempotency; operativna pouzdanost; performanse zasnovane na merenju; odrzivost arhitekture; developer experience.

Krajnji rezultat mora omoguciti drugom iskusnom .NET inzenjeru da nedvosmisleno utvrdi: sta je stvarno provereno; kojim SDK-om i runtime-om; koje komande su izvrsene; sta je pronadjeno; kako je problem reprodukovan; koji je osnovni uzrok; sta je promenjeno; koji test dokazuje popravku; sta jos nije provereno; kako se artefakt deployuje; kako se migrira baza; kako se rollout prekida; kako se sistem vraca ili oporavlja.
