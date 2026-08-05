## 17. Phase 7 - Database Analysis

Use a read-only database account for analysis where practical.

Inspect:

- unexpected users, administrators and privileged `usermeta`
- user creation and password-change timing
- application passwords and session tokens
- `siteurl`, `home`, `active_plugins`, `cron`, rewrite and autoloaded options
- unexpected option names, large autoloaded values and encoded payloads
- injected posts, pages, templates, widgets, menus and comments
- SEO spam, hidden links and conditional content
- malicious JavaScript in content, options or page-builder data
- serialized data integrity
- multisite network admins, sites and network options
- database triggers, scheduled events, users and grants where supported
- unexpected tables and recently modified records where audit data exists

### Database safety rules

- Dump before mutation and hash the dump.
- Do not place raw dumps in a public or repository path.
- Avoid manual string replacement in serialized values.
- Use transaction-safe and reversible changes where supported.
- Record every modified row/table and the reason.
- Validate table prefixes instead of assuming `wp_`.
- Distinguish WordPress-level compromise from database-server compromise.

