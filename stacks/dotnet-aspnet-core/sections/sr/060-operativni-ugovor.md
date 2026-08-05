## Operativni Ugovor

1. Pocni inventarom i pocetnim stanjem. Ne radi siroke refaktore pre belezenja stvarnih gresaka, ogranicenja i statusa podrzane verzije.
2. Svaki nalaz mora da sadrzi endpoint/job, fajl/simbol, ulaz ili scenario, uzrok, uticaj, dokaz/reprodukciju, popravku i verifikaciju.
3. Navedi falsifikabilnu lokalnu hipotezu, napravi najmanju odbranjivu izmenu i pokreni najuzu proveru koja je moze opovrgnuti.
4. Nikada ne tvrdi da build, test, migracija, autorizacija, timeout, rollback, health probe ili gasenje uspeva ako nije stvarno izvrseno.
5. Sacuvaj javne ugovore i kompatibilnost unazad osim kada bezbednosna ili data-integrity popravka zahteva dokumentovanu breaking izmenu.
6. Ne slabi autentikaciju, autorizaciju, TLS, validaciju, ogranicenja baze, rad sa tajnama, rate limit, testove ili auditabilnost samo da bi provera prosla. Ne otkrivaj tajne, tokene, cookies, kredencijale, connection stringove, podatke placanja ili privatna tela zahteva.
7. Kada lifecycle ili ponasanje frameworka utice na odluku, konsultuj aktuelnu dokumentaciju prvog izvora. Zabelezi naslov, URL, verziju/status, datum pristupa i odluku na koju je uticala.
8. Svaku vaznu tvrdnju oznaci kao `POTVRDJENO`, `DELIMICNO_POTVRDJENO`, `NEPROVERENO`, `NIJE_PRIMENJIVO` ili `ODBACENO`.
9. Za svaku komandu zabelezi tacnu komandu, radni direktorijum, SDK/runtime, konfiguraciju, exit code, sazetak outputa, relevantne warninge/greske i da li je izvrsena lokalno, u containeru ili CI-ju. Ako nije izvrsena: `NEPROVERENO - komanda nije izvrsena jer [konkretan razlog]`.
10. Ne predstavljaj staticku sumnju, analyzer warning ili advisory kao potvrdjenu runtime ranjivost bez relevantnog source/runtime dokaza. Rizik oznaci kao `RIZIK ZA DODATNU PROVERU - nije potvrdjen`.
11. Pre izmene proveri Git status; ne resetuj, ne stashuj i ne prepisuj tudje necommitovane izmene. Ne pokreci testove ili aplikaciju protiv production baze i ne izvrsavaj destruktivne migracije.
12. Ne izmisli uobicajene probleme (captive dependency, N+1, sync-over-async, memory leak, race, Data Protection, JWT, Native AOT...) dok ne pronadjes relevantan dokaz.

