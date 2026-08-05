## 36. Faza 26 - Izbor Pouzdanog Backup-a, Čist Rebuild I Migracija Podataka

Backup je dokaz i kandidat za oporavak, a ne automatski pouzdan izvor.

### Procena poverenja backup-a

Za svaki kandidat backup zabeleži:

- vreme kreiranja i timezone
- source sistem i backup alat
- storage nalog i istoriju pristupa
- stanje immutability/versioning-a
- kompletnost fajlova/database-a
- encryption i dostupnost ključa
- integrity hash ili provider verifikaciju
- odnos prema prvom poznatom i najranijem mogućem kompromitovanju
- WordPress, plugin, theme, PHP i database verzije
- rezultat malware i persistence skeniranja u izolaciji
- rezultat funkcionalnog restore-a
- interval gubitka podataka i reconciliation plan

### Preporučeni redosled čistog rebuild-a

1. provision-uj nov pouzdan nalog, host, container ili VM kada scope to zahteva
2. zakrpi OS, web server, PHP, database client i management alate
3. instaliraj WordPress samo iz zvaničnog izvora
4. instaliraj samo potrebne pluginove/teme iz proverenih izvora
5. ponovo napravi konfiguraciju bez kopiranja nepoznatog izvršivog koda
6. migriraj database/sadržaj kroz pregledan i reverzibilan proces
7. proveri i sanitizuj upload-e; ne kopiraj izvršive fajlove slepo
8. generiši nove salts, kredencijale, ključeve i application tajne
9. obnovi integracije novim kredencijalima
10. izvrši security, functional, performance i recovery testove
11. prebaci saobraćaj uz dokumentovan rollback plan
12. sačuvaj staro okruženje offline prema evidence politici

### Pravila odluke o restore-u

- ako initial access ili persistence prethode backup-u, ne tretiraj taj backup kao čist
- ako provenance ili kompletnost backup-a nisu poznati, označi ga `UNVERIFIED`
- ako treba sačuvati samo sadržaj, prednost daj kontrolisanoj migraciji sadržaja umesto restore-a celog okruženja
- ako je moguć gubitak podataka, definiši reconciliation pre cutover-a
- ako bi rollback vratio ranjiv kod, kompromitovane kredencijale ili zlonamerne podatke, koristi forward repair

