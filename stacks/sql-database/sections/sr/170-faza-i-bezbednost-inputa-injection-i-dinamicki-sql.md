## Faza I - Bezbednost inputa, injection i dinamicki SQL

Dokazi da podaci i identifikatori ne mogu nebezbedno da predju u izvrsivi SQL.

- Koristi parametre za vrednosti i stroge allowlist-e uz pravilno quoting pravilo za identifikatore i sort izraze.
- Pregledaj ORM raw SQL, query fragmente, stored procedure, migration generatore i administrativne skripte.
- Pregledaj multi-statement podesavanja, client-side emulation, prepared-statement rezime i encoding granice.
- Ogranici JSON path, full-text sintaksu, regular expressions, spatial input i user-defined izraze.
- Spreci second-order injection kroz sacuvane podatke koji se kasnije koriste u DDL, export, shell ili template kontekstu.
- Testiraj malformed encoding-e, komentare, separatore, duple parametre i driver-specific edge slucajeve.

