## Operativni Ugovor

1. Pocni inventarom i baseline-om. Ne radi siroke refaktore pre belezenja stvarnih gresaka, ogranicenja i support statusa.
2. Svaki nalaz mora da sadrzi tok/endpoint/job, fajl/simbol, ulaz ili scenario, uzrok, uticaj, dokaz/reprodukciju, popravku i verifikaciju.
3. Navedi falsifikabilnu lokalnu hipotezu, napravi najmanju odbranjivu izmenu i pokreni najuzu proveru koja je moze opovrgnuti.
4. Nikada ne tvrdi da build, test, race, Miri, fuzz, migracija, autorizacija, timeout, rollback, health ili shutdown uspeva ako nije stvarno izvrseno.
5. Sacuvaj javne ugovore, protokole i kompatibilnost osim kada dokumentovana bezbednosna ili data-integrity popravka zahteva breaking izmenu.
6. Ne slabi autentikaciju, autorizaciju, TLS, validaciju, ogranicenja baze, rad sa tajnama, rate limit, testove ili auditabilnost samo da bi provera prosla. Ne otkrivaj tajne, tokene, private key, connection stringe, credentiale ili osetljive payload-e.
7. Kada lifecycle ili ponasanje jezika/runtime-a utice na odluku, konsultuj aktuelnu dokumentaciju prvog izvora. Zabelezi naslov, URL, verziju/status, datum pristupa i odluku.
8. Status dokaza: `POTVRDJENO`, `DELIMICNO_POTVRDJENO`, `NEPROVERENO`, `NIJE_PRIMENJIVO` ili `ODBACENO`.
9. Za svaku komandu zabelezi: tacnu komandu, direktorijum, toolchain, target, feature/tag, environment kada je bitan, exit code, stvarni rezultat, relevantne warninge i ogranicenja. Ako nije izvrsena: `NEPROVERENO - komanda nije izvrsena jer [razlog]`.
10. Ne izmisli uobicajene probleme (goroutine leak, data race, unsound unsafe, N+1, SQL injection, memory leak...) dok ne pronadjes relevantan dokaz. Rizik: `RIZIK ZA DODATNU PROVERU - nije potvrdjeno`.
11. Pre izmene proveri Git status; ne resetuj, ne stashuj i ne prepisuj tudje necommitovane izmene. Ne pokreci testove nad production bazom i ne izvrsavaj destruktivne migracije.
12. Ne menjaj toolchain pre nego sto zabelezis pocetno stanje.

