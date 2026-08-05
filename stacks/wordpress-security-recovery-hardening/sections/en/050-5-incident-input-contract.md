## 5. Incident Input Contract

Use the following data. Mark missing values as `UNKNOWN`; never fill them with guesses.

```yaml
incident:
  domain: "[DOMAIN]"
  business_function: "[BLOG / ECOMMERCE / MEMBERSHIP / CORPORATE / OTHER]"
  owner_authorization: "[CONFIRMED / UNCONFIRMED]"
  mode: "[AUDIT_ONLY / CONTAIN_AND_RECOVER / HARDEN_ONLY / FORENSICS_ONLY]"
  first_observed_at: "[ISO-8601 WITH TIMEZONE / UNKNOWN]"
  symptoms:
    - "[REDIRECT / SEO SPAM / 500 / WSOD / ADMIN LOCKOUT / WEBSHELL / SKIMMER / UNKNOWN]"
  known_events:
    - "[EVENT]"
  suspected_data_exposure: "[YES / NO / UNKNOWN]"
  payment_processing: "[YES / NO / UNKNOWN]"

environment:
  hosting_type: "[CPANEL / PLESK / MANAGED_WP / VPS / CONTAINER / SHARED / OTHER]"
  os: "[VALUE / UNKNOWN]"
  web_server: "[APACHE / NGINX / LITESPEED / OTHER / UNKNOWN]"
  php_sapi: "[FPM / APACHE_MODULE / CGI / OTHER / UNKNOWN]"
  php_version: "[VALUE / UNKNOWN]"
  wordpress_version: "[VALUE / UNKNOWN]"
  database: "[MYSQL / MARIADB / OTHER / UNKNOWN]"
  database_version: "[VALUE / UNKNOWN]"
  multisite: "[YES / NO / UNKNOWN]"
  document_root: "[PATH / UNKNOWN]"
  timezone: "[IANA TIMEZONE / UNKNOWN]"

access:
  ssh: "[YES / NO]"
  sftp_or_ftp: "[SFTP / FTP / NO]"
  hosting_panel: "[YES / NO]"
  wp_admin: "[YES / NO]"
  database: "[YES / NO]"
  logs: "[YES / NO / PARTIAL]"
  backups: "[YES / NO / UNKNOWN]"
  dns: "[YES / NO]"
  registrar: "[YES / NO]"
  cdn_waf: "[YES / NO]"
  search_console: "[YES / NO]"

constraints:
  maximum_downtime: "[DURATION / UNKNOWN]"
  evidence_retention: "[DURATION / UNKNOWN]"
  maintenance_window: "[VALUE / UNKNOWN]"
  prohibited_actions:
    - "[ACTION]"
```

