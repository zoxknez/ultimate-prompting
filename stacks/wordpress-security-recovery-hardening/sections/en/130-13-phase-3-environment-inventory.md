## 13. Phase 3 - Environment Inventory

Build a complete asset map before drawing conclusions.

### WordPress inventory

- WordPress version, locale and update channel
- single-site or multisite
- active/inactive plugins with versions and provenance
- active/inactive themes with versions and provenance
- MU plugins
- drop-ins: `advanced-cache.php`, `db.php`, `db-error.php`, `install.php`, `maintenance.php`, `object-cache.php`, `sunrise.php`
- custom code, code snippets, child themes and vendor packages
- administrators, editors and privileged service accounts
- application passwords
- WP-Cron events and schedules
- REST routes, XML-RPC use and externally exposed endpoints
- active plugins stored in database options
- uploads structure and executable file presence
- object cache, page cache and CDN integration
- security, backup and migration plugins
- payment, SMTP, analytics, tag manager and SSO integrations

### Host inventory

- OS, kernel, hosting account and isolation model
- web server and virtual-host configuration
- PHP version, SAPI, pool configuration and extensions
- document roots, aliases, symlinks and additional domains/subdomains
- filesystem ownership, permissions, ACLs and immutable flags
- SSH users, keys, shell history availability and SFTP/FTP accounts
- cPanel/Plesk users, API tokens and delegated users
- user and system crontabs, `/etc/cron*`, systemd timers and startup scripts
- `/tmp`, `/var/tmp`, home directories and adjacent web roots
- log locations, rotation and retention
- backups, snapshots and restore points
- outbound mail configuration
- Redis/Memcached/object-cache services
- containers, deployment pipelines and mounted volumes where applicable

### Edge and external inventory

- registrar account and nameservers
- DNS records and recent changes
- CDN/WAF zones, workers, rules, redirects and origin settings
- TLS certificates and origin certificates
- Search Console/Bing Webmaster Tools
- payment provider webhooks and API credentials
- Git repositories, CI/CD systems and deployment keys
- transactional email provider
- monitoring and uptime services

