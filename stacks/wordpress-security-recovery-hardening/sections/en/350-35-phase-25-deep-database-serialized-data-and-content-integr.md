## 35. Phase 25 - Deep Database, Serialized Data And Content Integrity Audit

Use the discovered table prefix and actual schema. Never assume `wp_` or a single-site layout.

### High-value data domains

Inspect, as applicable:

- users, user metadata, roles, capabilities, sessions and application passwords
- options, site options, transients, autoloaded values and cron data
- posts, pages, revisions, templates, patterns, navigation, attachments and metadata
- comments and comment metadata
- terms, taxonomies and relationships
- plugin-specific tables for forms, snippets, redirects, SEO, cache, security, backups and commerce
- WooCommerce orders, customers, webhooks and scheduled actions
- multisite global and per-site tables
- database users, grants, routines, triggers, events and definers

### Serialized and encoded data rules

- identify PHP serialized values before mutation
- use serialization-aware tooling for replacements
- preserve exact byte lengths and object structure
- treat unserialization of untrusted objects as code-execution risk
- search for suspicious URLs, domains, script fragments, iframes, event handlers, encoded blobs and unexpected PHP without blindly decoding or executing content
- perform expensive pattern searches on a copy or replica when production impact is uncertain
- record query, row count, primary key/object ID and before/after hash for every mutation
- use transactions or tested reversible batches where supported

### Content integrity and reconciliation

- compare critical settings with known-good configuration or owner-approved values
- identify unexpected administrators, role changes and ownership transfers
- verify published content, revisions and attachments around the incident window
- reconcile orders, users, form submissions and other business records against external systems
- identify gaps caused by restoring an older backup
- document data that cannot be trusted and the business owner responsible for disposition

