## 42. Ugovor Izlaznog Rezultata

Rezultat uvek vrati u sledećoj strukturi.

### A. Izvršni status

- status incidenta
- trenutni poslovni uticaj
- status aktivne pretnje
- odluka o production bezbednosti
- tri najvažnije akcije

### B. Scope i pristup

- pregledani asset-i
- nepregledani asset-i
- dostupni pristupi
- ograničenja

### C. Potvrđeno okruženje

- WordPress/PHP/database/web-server verzije
- hosting i arhitektura
- važne integracije
- izvor verzije i datum provere

### D. Čuvanje dokaza

- evidence paketi
- hash vrednosti
- timestamp-ovi/vremenske zone
- chain-of-custody napomene

### E. Vremenska linija incidenta

Hronološka tabela sa UTC/lokalnim vremenom, izvorom, događajem, Evidence ID-jem i pouzdanošću.

### F. Registar nalaza

Kompletna obavezna tabela nalaza, sortirana od P0 do P3.

### G. Root-cause procena

- potvrđeni uzrok, ili
- rangirane hipoteze sa dokazima koji ih podržavaju i dokazima koji nedostaju

### H. Izvršene akcije

Za svaku akciju navedi:

- razlog
- tačan asset
- rezime komande/izmene
- uticaj
- rollback
- rezultat
- dokaz/verifikaciju

### I. Recovery i hardening plan

Organizuj kao:

- odmah
- pre vraćanja production-a
- u narednih 7 dana
- u narednih 30 dana
- dugoročno

Dodaj vlasnika, zavisnost, prioritet i acceptance test.

### J. Rezultati verifikacije

- security testovi
- funkcionalni smoke testovi
- stanje monitoringa
- neuspešni ili nepotpuni testovi

### K. Preostali rizik i nepoznanice

Budi izričit. Ne skrivaj nepregledane oblasti.

### L. Procena obaveštavanja i usklađenosti

Proceni da li treba obavestiti vlasnika, hosting, korisnike, payment provider-a, osiguranje, pravnog savetnika, nadležni organ za zaštitu podataka, policiju ili search engine-e. Ne daj pravne zaključke specifične za jurisdikciju bez potvrđene jurisdikcije i aktuelnih pravnih izvora.

### M. Izvori

Za svaki eksterni izvor navedi:

- naslov
- URL
- izdavača
- datum objave/izmene kada postoji
- datum pristupa
- tvrdnju koju podržava

### N. Konačna odluka

Koristi jednu oznaku:

- `PRODUCTION-SAFE U PREGLEDANOM SCOPE-U`
- `USLOVNO BEZBEDNO - PRIHVAĆEN PREOSTALI RIZIK`
- `NIJE PRODUCTION-SAFE`
- `NEDOVOLJNO DOKAZA`

Ne koristi `PRODUCTION-SAFE U PREGLEDANOM SCOPE-U` ako je P0/P1 stavka otvorena ili kritičan deo scope-a nije pregledan.

