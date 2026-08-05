## 11. Faza 1 - Čuvanje Dokaza

Pre čišćenja:

1. Napravi snapshot sajta i hosta kada je to tehnički i ugovorno moguće.
2. Odvojeno sačuvaj WordPress fajlove, konfiguraciju, database export i relevantne logove.
3. Hash-uj evidence pakete koristeći SHA-256.
4. Sačuvaj metadata, ACL i extended attributes kada su podržani.
5. Zabeleži sinhronizaciju vremena i podešavanje vremenske zone.
6. Kada host pristup dozvoljava, sačuvaj listu procesa, otvorene network listenere i aktivne sesije.
7. Sačuvaj volatile evidence pre reboot-a/restart-a kada je relevantno.
8. Čuvaj dokaze van kompromitovanog web root-a uz ograničen pristup.
9. Rediguj tajne u radnim izveštajima, ali originale čuvaj u kontrolisanom evidence storage-u.

### Bezbedni primeri prikupljanja

Prilagodi putanje i komande stvarnom okruženju. Ne prikazuj primer izlaza kao stvarni izlaz.

```bash
# Vreme i platforma
date --iso-8601=seconds
date -u --iso-8601=seconds
uname -a
id

# Verzije
php -v
wp core version --path=/putanja/do/sajta --skip-plugins --skip-themes
mysql --version
nginx -v
apachectl -v

# Metadata i hash fajla
stat /putanja/do/sumnjivog-fajla.php
sha256sum /putanja/do/sumnjivog-fajla.php
find /putanja/do/sajta -xdev -type f -printf '%TY-%Tm-%TdT%TH:%TM:%TS %u %g %m %s %p\n' > filesystem-inventory.txt

# Primer evidence arhive - koristi destinaciju van web root-a
tar --acls --xattrs --numeric-owner -cpf /secure-evidence/site-files.tar /putanja/do/sajta
sha256sum /secure-evidence/site-files.tar > /secure-evidence/site-files.tar.sha256
```

Nikada ne prepisuj jedinu kopiju sumnjivog fajla.

