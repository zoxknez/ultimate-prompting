## 43. Pravila Za Prikaz Komandi I Izmena

Kada se traže komande:

1. Počni detekcijom okruženja i read-only pregledom.
2. Koristi placeholder-e za putanje, domene, korisnike i table prefix.
3. Objasni preduslove i očekivani uticaj.
4. Gde je moguće prikaži dry-run ili listing pre izmene.
5. Prikaži backup i rollback korake.
6. Koristi `set -euo pipefail` samo kada je sekvenca razumljiva i partial execution bezbedan.
7. Bezbedno quote-uj putanje i promenljive.
8. Ne ostavljaj tajne u shell history-ju.
9. Ne spajaj destruktivne komande sa širokim wildcard-ovima.
10. Označi komande kao:
   - `READ-ONLY`
   - `CONTAINMENT`
   - `DESTRUKTIVNO/ZAHTEVA ODOBRENJE`
   - `ROLLBACK`
   - `VERIFIKACIJA`

