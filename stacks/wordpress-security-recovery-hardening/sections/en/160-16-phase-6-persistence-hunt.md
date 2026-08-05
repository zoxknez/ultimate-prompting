## 16. Phase 6 - Persistence Hunt

Treat persistence as a separate workstream. Check:

- MU plugins and WordPress drop-ins
- `wp-config.php` includes and constants
- `auto_prepend_file` and `auto_append_file`
- `.user.ini`, `php.ini`, PHP-FPM pool configuration and vhost configuration
- `.htaccess` and Nginx/LiteSpeed includes
- WordPress scheduled events
- system/user cron and systemd timers
- startup scripts and shell profile files
- SSH `authorized_keys`
- hosting panel users and API tokens
- database users, grants, triggers and events
- rogue WordPress administrators and application passwords
- malicious options, transients, widgets and serialized payloads
- Redis/object-cache persistence and stale cache
- CDN workers, transform rules, redirects and edge functions
- DNS/registrar access
- CI/CD deploy keys, secrets and compromised build artifacts
- modified backup or migration packages that can reintroduce malware

A recovered site that retains an unexamined persistence path is not production-safe.

