## 19. Faza 9 - Identitet, Kredencijali I Sesije

Napravi matricu rotacije kredencijala. Rotiraj redosledom koji sprečava lockout i ponovnu kompromitaciju.

Obuhvati kada je primenljivo:

- registrar i DNS
- CDN/WAF
- hosting panel i provider nalog
- root/sudo/SSH ključeve
- SFTP/FTP naloge
- database korisnike
- WordPress administratore
- WordPress salts i session tokens
- application passwords
- plugin/vendor licence koje omogućavaju API pristup
- SMTP i email provider kredencijale
- object storage i backup kredencijale
- payment gateway ključeve i webhook tajne
- analytics/tag manager naloge
- Git, CI/CD, deployment i package registry tajne
- cloud service account-e i API ključeve

Pravila:

1. Rotaciju radi sa poznatog čistog uređaja.
2. Koristi jedinstvene kredencijale i MFA gde je podržan.
3. Ukloni nepoznate naloge, ključeve, sesije i tokene.
4. Invalidiraj aktivne sesije nakon promene admin lozinki/salts.
5. Proveri recovery email adrese, forwarding pravila i account delegate-e.
6. Ne stavljaj nove tajne u incident report.

