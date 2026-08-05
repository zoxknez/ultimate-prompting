## Istrazivacki baseline - 5. avgust 2026.

Ovaj baseline je pocetna tacka, a ne dozvola za slepu nadogradnju. Neposredno pre preporuke ili izmene ponovo proveri zvanicnu dokumentaciju engine-a, politiku podrske dobavljaca, ogranicenja managed servisa i stvarno pokrenuti sistem.

| Komponenta | Potvrdjeno stanje 5. avgusta 2026. | Obavezna audit provera |
| --- | --- | --- |
| PostgreSQL stable | 18.4 je aktuelni stabilni patch; podrzani major-i su 18, 17, 16, 15 i 14. | Proveri `server_version`, digest paketa ili image-a, ekstenzije, kompatibilnost managed servisa i patch politiku. |
| PostgreSQL lifecycle | PostgreSQL 14 dobija poslednje izdanje 12. novembra 2026; PostgreSQL 19 je beta i nije podrazumevani produkcioni baseline. | Napravi dokazima potkrepljen plan nadogradnje pre EOL-a; nikada podrazumevano ne preporucuj beta izdanje. |
| MySQL LTS | 8.4.10 je trenutno potvrdjeni patch u 8.4 LTS liniji. | Proveri tacan patch, edition, ugovor podrske, OS podrsku, connector i rezultat upgrade checker-a. |
| MySQL Innovation | 9.7.2 je trenutno potvrdjeni Innovation patch, a ne LTS izdanje; proveri ga ponovo u zvanicnim release notes. | Ne oznacavaj 9.7 kao LTS; dokazi brzi ritam nadogradnje i compatibility budzet. |
| MySQL 8.0 | MySQL 8.0 je dostigao community EOL u aprilu 2026. | Planiraj migraciju na podrzanu liniju; cloud extended support je posebna komercijalna kontrola. |
| MariaDB | 12.3 je aktuelna LTS linija i mora se tretirati kao poseban engine u odnosu na MySQL. | Proveri tacan patch i izvor podrske; ne prenosi MySQL semantiku ili putanje nadogradnje. |
| SQLite | 3.53.4 je aktuelno izdanje. | Proveri stvarno ucitanu biblioteku, `sqlite_source_id()`, compile opcije, binding i ponasanje fajl sistema. |
| Oporavak | PostgreSQL PITR zahteva base backup i neprekidan WAL; MySQL PITR zahteva backup i binary logove; SQLite zahteva koordinisanu podrzanu backup metodu. | Backup nije validan dok izolovani restore i aplikativna verifikacija ne prodju. |

Patch nivoi i cloud ponude se menjaju. Tokom izvrsavanja tretiraj baseline manifest kao dokaz koji mora ponovo da se proveri, a ne kao trajnu istinu.

