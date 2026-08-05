<!-- section:CORE-OPERATING-CONTRACT -->
# Jezgro — Operativni Ugovor Audita

Učitati ovaj ugovor za **svaki** audit stack-a.

## Prvo istina

1. Nikada ne izmišljati izlaz komandi, CVE ID-jeve, sadržaj fajlova, metrike ili rezultate testova.
2. Svaka materijalna tvrdnja koristi: `POTVRDJENO` | `DELIMICNO_POTVRDJENO` | `NEVERIFIKOVANO` | `NIJE_PRIMENLJIVO` | `ODBACENO`.
3. Sumnje bez dokaza: `RIZIK ZA DODATNU PROVERU — nije potvrdjeno`.
4. Nepokrenute komande: `NEVERIFIKOVANO — nije pokrenuto zbog [konkretnog razloga]`.

## Prvo zaštita

- Sačuvati nekomitovan rad korisnika; ne raditi reset/stash/overwrite bez pristanka.
- Nikada ne štampati tajne (env, ključeve, tokene, lozinke za konekciju, materijal za potpisivanje).
- Nikada ne pokretati testove ili migracije nad produkcionim podacima po default-u.
- Prednost dati read-only dijagnostici pre bilo kakvog upisivanja.

## Režimi rada

Default: `AUDIT_AND_SAFE_FIX` ako nije navedeno.

| Režim | Dozvoljeno |
| ----- | ---------- |
| `AUDIT_ONLY` | Analiza + bezbedne provere; bez izmene koda/lock/schema/infra |
| `AUDIT_AND_SAFE_FIX` | Potvrđene popravke niskog rizika + regresioni testovi; planirati velike izmene |
| `FULL_IMPLEMENTATION` | Obrazložene izmene u malim koracima; backup pre destruktivnog rada |
| `FIX_CONFIRMED_ISSUES` | Samo registrovani potvrdjeni problemi |

Stack overlay-i mogu dodati režime (`SECURITY_AUDIT`, `MIGRATION_AUDIT`).

## Minimalna izmena

- Bez prepisivanja framework-a radi mode.
- Bez masovnih nadogradnji zavisnosti kao "popravke".
- Bez brisanja lockfile fajlova.
- Bez onemogućavanja bezbednosnih kontrola da bi build prošao.

## Politika verzija

- Prednost dati **linijama** (npr. Node 24 LTS) umesto izmišljenih zakrpa.
- Ponovo proveriti zvanične URL-ove u `baselines/sources.json` tokom audita.
- Zabeležiti: naslov izvora, URL, viđenu verziju, datum pristupa, odluku.

## Shema komandnog loga

Za svaku izvršenu komandu zabeležiti:

`komanda | cwd | toolchain | config | exit | rezime | upozorenja | local|container|CI`
