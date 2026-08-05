## 29. Phase 19 - WordPress Persistence Matrix

Use a persistence matrix and mark every row `EXAMINED`, `NOT PRESENT`, `CONFIRMED`, `UNVERIFIED` or `OUT OF SCOPE`.

### Filesystem and bootstrap persistence

- modified root/core files
- MU plugins and hidden loader files
- drop-ins and cache loaders
- active and inactive plugin/theme files
- executable uploads and polyglot media
- `.htaccess`, Nginx/LiteSpeed rules and custom error documents
- `.user.ini`, `php.ini`, PHP-FPM pool directives and auto-prepend files
- backup, cache, language, upgrade and temporary directories
- parent directories, sibling sites and user home startup files
- OPcache preload files and stale bytecode

### WordPress and database persistence

- administrator, editor and service accounts
- role/capability changes in user metadata
- application passwords and session tokens
- `active_plugins`, network-active plugins and theme settings
- cron option entries and plugin-specific scheduled-action tables
- malicious options, transients, widgets, menus, block content and reusable patterns
- injected posts, pages, revisions, comments and metadata
- site URL, home URL, upload path, admin email and redirect-related settings
- database triggers, events, routines, unexpected users and grants
- object-cache values capable of restoring stale or malicious application state

### Host and external persistence

- user/system cron, systemd timers and startup hooks
- SSH keys, shell profiles and authorized command restrictions
- control-panel users, tokens and one-click installer jobs
- DNS records, nameservers, registrar delegates and domain forwarding
- CDN workers, rules, redirects, origin overrides and cache keys
- Git deploy keys, CI secrets, webhooks and build artifacts
- email forwarding, mailbox rules, SMTP credentials and API tokens
- Search Console/Bing ownership tokens and unauthorized verified owners

Do not declare persistence eradicated until every applicable row has evidence and a verification method.

