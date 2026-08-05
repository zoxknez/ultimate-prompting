## 25. Faza 15 - Upravljanje Incidentom, Komunikacije I Ovlašćenja Za Odluke

Uspostavi strukturu upravljanja incidentom primerenu poslovnom uticaju. Tehnički ispravno čišćenje može da propadne ako vlasništvo, odobrenja, komunikacije ili rukovanje dokazima nisu jasni.

### Matrica odluka i vlasništva

Zabeleži najmanje:

- komandanta incidenta i zamenu
- tehničkog vođu i čuvara dokaza
- poslovnog vlasnika i odobravaoca povratka u produkciju
- kontakte hostinga, CDN-a, registra, payment provajdera i pravnog tima
- ovlašćenje za maintenance režim, obustavu checkout-a, rotaciju kredencijala, DNS izmenu i rebuild
- komunikacioni kanal koji ne zavisi od kompromitovanog WordPress naloga, mailbox-a ili hosting panela
- ritam izveštavanja i publiku
- eksplicitan dnevnik odluka sa vremenom, odlukom, odobravaocem, dokazom i kriterijumima za poništavanje

### Bezbednost komunikacije

- pretpostavi da WordPress admin poruke, kompromitovani mailbox-i i hosting-panel chat mogu biti vidljivi napadaču
- koristi zaseban pouzdan kanal za tajne i odluke visokog uticaja
- ne nalepi database dump, privatni ključ, pun access token ili lične podatke u tiket ili chat
- održavaj jedan kanonski dokument statusa incidenta
- preliminarne izjave označi kao preliminarne
- odvoji komunikaciju prema korisnicima od tehničkih dokaza
- sačuvaj bitna obaveštenja, odgovore provajdera i vremena kao dokaze incidenta

### Trijaža obaveštavanja

Utvrdi da li incident može da obuhvata:

- lične podatke
- autentikacione kredencijale
- podatke platnih kartica ili checkout-a
- zdravstvene, obrazovne, finansijske ili druge regulisane informacije
- korisnički sadržaj ili poverljive poslovne podatke
- distribuciju malware-a ili zloupotrebu third-party infrastrukture

Ne daj pravne zaključke specifične za jurisdikciju bez potvrđene jurisdikcije i aktuelnih pravnih izvora. Zabeleži ko je vlasnik odluka o obaveštavanju pravnog tima, osiguravača, regulatora, policije, payment provajdera i korisnika.

