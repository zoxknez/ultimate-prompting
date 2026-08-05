## 26. Faza 16 - Kompromitacija Hosting Naloga, Susednih Sajtova I Kontrolnih Ravni

WordPress sajt nije izolovan asset kada deli hosting korisnika, kontrolni panel, FTP nalog, PHP pool, database server, deployment kredencijal ili upisivi direktorijum sa drugim sajtovima.

### Scope celog naloga

Popiši i pregledaj:

- svaki domen, poddomen, addon domen, parkirani domen i document root pod hosting nalogom
- staging, development, arhivirane i zaboravljene instalacije
- susedne WordPress, Joomla, Drupal, custom PHP i statičke sajtove
- deljene upload, cache, backup, privremene i session direktorijume
- symlink-ove, bind mount-ove i alias-e koji prelaze granice sajtova
- deljene FTP/SFTP korisnike, SSH ključeve, panel korisnike i API tokene
- deljene database korisnike, Redis/Memcached instance, SMTP kredencijale i deployment ključeve
- nalaze host-level malware skenera i istoriju karantina
- cron poslove na nivou naloga, PHP handler-e, nasleđivanje `.user.ini` i environment promenljive

### Dokazi kontrolne ravni

Prikupi, kada su dostupni:

- istoriju prijava i audita hosting panela
- događaje kreiranja korisnika, resetovanja lozinke, API tokena i delegiranog pristupa
- DNS, nameserver, certificate i redirect izmene
- aktivnosti file manager-a, restore-a backup-a i one-click instalera
- FTP/SFTP/SSH autentikacione logove
- support impersonation ili administrativne akcije provajdera
- snapshot-e, istoriju image-a i migracije naloga

Ako je kompromitacija celog naloga ili slaba tenant izolacija verovatna, prednost daj migraciji na novo provisionovan nalog ili host umesto čišćenju samo sajta na mestu. Svaki nepregledani susedni asset dokumentuj kao rizik ponovne infekcije.

