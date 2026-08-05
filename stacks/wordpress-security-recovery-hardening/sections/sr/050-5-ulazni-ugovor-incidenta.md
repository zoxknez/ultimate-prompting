## 5. Ulazni Ugovor Incidenta

Koristi sledeće podatke. Nedostajuće vrednosti označi kao `NEPOZNATO`; nikada ih ne popunjavaj nagađanjem.

```yaml
incident:
  domain: "[DOMAIN]"
  business_function: "[BLOG / ECOMMERCE / MEMBERSHIP / CORPORATE / OTHER]"
  owner_authorization: "[CONFIRMED / UNCONFIRMED]"
  mode: "[AUDIT_ONLY / CONTAIN_AND_RECOVER / HARDEN_ONLY / FORENSICS_ONLY]"
  first_observed_at: "[ISO-8601 SA VREMENSKOM ZONOM / NEPOZNATO]"
  symptoms:
    - "[REDIRECT / SEO SPAM / 500 / WSOD / ADMIN LOCKOUT / WEBSHELL / SKIMMER / NEPOZNATO]"
  known_events:
    - "[DOGAĐAJ]"
  suspected_data_exposure: "[DA / NE / NEPOZNATO]"
  payment_processing: "[DA / NE / NEPOZNATO]"

environment:
  hosting_type: "[CPANEL / PLESK / MANAGED_WP / VPS / CONTAINER / SHARED / OTHER]"
  os: "[VREDNOST / NEPOZNATO]"
  web_server: "[APACHE / NGINX / LITESPEED / OTHER / NEPOZNATO]"
  php_sapi: "[FPM / APACHE_MODULE / CGI / OTHER / NEPOZNATO]"
  php_version: "[VREDNOST / NEPOZNATO]"
  wordpress_version: "[VREDNOST / NEPOZNATO]"
  database: "[MYSQL / MARIADB / OTHER / NEPOZNATO]"
  database_version: "[VREDNOST / NEPOZNATO]"
  multisite: "[DA / NE / NEPOZNATO]"
  document_root: "[PUTANJA / NEPOZNATO]"
  timezone: "[IANA VREMENSKA ZONA / NEPOZNATO]"

access:
  ssh: "[DA / NE]"
  sftp_or_ftp: "[SFTP / FTP / NE]"
  hosting_panel: "[DA / NE]"
  wp_admin: "[DA / NE]"
  database: "[DA / NE]"
  logs: "[DA / NE / DELIMIČNO]"
  backups: "[DA / NE / NEPOZNATO]"
  dns: "[DA / NE]"
  registrar: "[DA / NE]"
  cdn_waf: "[DA / NE]"
  search_console: "[DA / NE]"

constraints:
  maximum_downtime: "[TRAJANJE / NEPOZNATO]"
  evidence_retention: "[TRAJANJE / NEPOZNATO]"
  maintenance_window: "[VREDNOST / NEPOZNATO]"
  prohibited_actions:
    - "[AKCIJA]"
```

