<!-- section:STACK-WORDPRESS-OVERLAY-FOCUS -->
# WordPress Bezbednost, Oporavak & Hardening Overlay

## Obavezne Oblasti Incidenata i Hardening-a

1. **Izolacija Infekcije & Skeniranje Malvera**:
   - Pregledati `wp-config.php`, `.htaccess`, `index.php`, `wp-includes/`, mu-plugins, funkcije tema.
   - Skenirati webshell-ove, base64 obfuskaciju, lažne admin naloge, neovlašćene cron događaje.

2. **Audit Baze Podataka & Privilegija Korisnika**:
   - Auditovati `wp_users` i `wp_usermeta` na neovlašćene administratorske privilegije.
   - Verifikovati prefiks tabela, SQL injekcione vektore i napuštene tabele sa payload-ima.

3. **Kontrole Hardening-a & Oporavka**:
   - Onemogućiti izmenu fajlova (`DISALLOW_FILE_EDIT`), prinudni SSL admin (`FORCE_SSL_ADMIN`).
   - Auditovati lanac snabdevanja dodataka, izloženost REST API-ja, hardening XML-RPC-a i integritet bekap/restore procesa.
