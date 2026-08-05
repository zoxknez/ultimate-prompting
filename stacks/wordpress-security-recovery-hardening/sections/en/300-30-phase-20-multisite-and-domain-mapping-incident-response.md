## 30. Phase 20 - Multisite And Domain-Mapping Incident Response

For WordPress Multisite, scope the network, not only the visibly affected site.

### Multisite inventory

- network type: subdomain, subdirectory or mapped domains
- main site, all sites, archived/spam/deleted sites and orphaned tables
- super administrators and network-level service accounts
- network-active plugins, MU plugins and network-enabled themes
- `sunrise.php`, domain-mapping code and related tables/options
- network settings, registration policy and allowed email domains
- upload paths and per-site media boundaries
- global users and per-site capability metadata
- `wp_blogs`, `wp_site`, `wp_sitemeta`, registration and sign-up records as applicable
- per-site options, posts, metadata and cron entries
- network cache, CDN and certificate coverage

### Multisite-specific checks

- verify that a compromise in one site cannot execute code network-wide through shared plugins/themes
- inspect super-admin assignment and capability changes
- identify site-specific versus network-wide injected content
- verify mapped-domain ownership, redirects and TLS
- test direct access through original and mapped hostnames
- inspect deleted or archived sites for persistence
- evaluate whether shared tables or global users expose other tenants
- rebuild or restore with a network-aware sequence and table-prefix map

A clean main site does not prove that the network is clean.

