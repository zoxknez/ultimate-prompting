## 23. Phase 13 - Hardening Baseline

Apply according to environment and business requirements. Avoid cargo-cult settings.

### WordPress

- update core, plugins and themes to maintained compatible versions
- remove unused plugins/themes and unknown code
- restrict administrator count and use named accounts
- enable MFA for privileged accounts
- disable dashboard file editing with `DISALLOW_FILE_EDIT`
- consider `DISALLOW_FILE_MODS` only when deployments and updates are managed externally
- restrict application passwords and remove unused credentials
- restrict registration and role assignment
- review REST/XML-RPC exposure based on legitimate use
- secure WP-Cron or replace it with a controlled system scheduler when appropriate
- minimize plugin count and require provenance/maintenance ownership
- enable security/audit logging with protected remote retention where possible

### Filesystem and PHP

- least-privilege ownership and permissions
- no world-writable executable paths
- deny script execution in uploads and cache directories where architecture permits
- protect `wp-config.php`, backups, logs and environment files
- ensure temporary and session directories are not web-accessible
- disable PHP version exposure
- configure PHP error display off in production and secure error logging on
- review dangerous functions based on application need, not as a substitute for patching
- review `open_basedir` only where it provides real containment and compatibility is tested
- set secure upload limits and MIME handling
- maintain supported PHP and extensions

### Web server and transport

- enforce HTTPS and HSTS only after HTTPS is correct on all required subdomains
- set appropriate security headers with compatibility testing
- prevent access to hidden/config/backup files
- disable directory listing
- restrict admin paths with rate limiting, WAF, VPN or IP controls where practical
- preserve real client IP configuration correctly behind CDN/proxy
- configure request/body limits and timeouts defensibly

### Database

- unique least-privilege WordPress database user
- no remote database exposure unless explicitly required and restricted
- supported database version
- secure backups and encrypted transport where applicable
- monitor privileged users, grants, triggers and events

### Host and operations

- supported OS and packages
- SSH keys, MFA/provider controls and no shared admin accounts
- separate sites/accounts where possible to limit lateral movement
- patch management with staging and rollback
- offsite, immutable or versioned backups
- documented restore tests
- centralized logs and alerting
- file-integrity monitoring with a known baseline
- vulnerability inventory and maintenance ownership
- incident runbook and contact list

### CDN, DNS and third parties

- MFA and least privilege
- registrar lock and recovery review
- DNS change alerts
- origin lock-down and authenticated origin where supported
- review workers, page rules, redirects and transform rules
- restrict payment/API/webhook credentials
- inventory third-party scripts and tag-manager permissions

