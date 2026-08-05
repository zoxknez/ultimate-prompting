## Faza T - Backup, restore, PITR i verifikacija podataka

Backup-i su samo potencijalni recovery materijal dok restore i verifikacija ne prodju.

- Inventarisi full, incremental, logical, physical, snapshot i log-archive backup-e, retention i immutability.
- Proveri enkripciju, key custody, checksum-e, catalog metadata-u, cross-account ili offsite kopije i deletion protection.
- Izvrsi izolovani restore koristeci dokumentovane kredencijale, mrezu, DNS i aplikativne korake verifikacije.
- Proveri PITR na timestamp neposredno pre i posle poznate transakcije i potvrdi tumacenje timezone-a.
- Validiraj schema-u, opsege broja redova, kriticne invarijante, checksum-e gde imaju smisla i aplikativne smoke testove.
- Izmeri stvarni RPO i RTO i ukljuci queue, object storage, search i configuration recovery zavisnosti.

