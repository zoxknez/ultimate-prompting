## 28. Phase 18 - Plugin, Theme And Integration Supply-Chain Provenance

Every executable component must have a documented origin. Popularity, an update notification or a familiar filename is not provenance.

### Required component record

For each plugin, theme, MU plugin, drop-in, code-snippet package and bundled library record:

- slug and human-readable name
- installed version and filesystem path
- active, inactive, network-active or orphaned status
- source: WordPress.org, vendor portal, Git repository, internal build or unknown
- package URL or repository commit/tag
- acquisition timestamp and operator
- expected hash, signature or vendor checksum when available
- license and maintenance owner
- last update and last known use
- supported WordPress/PHP range
- known vulnerability and abandonment status
- whether the component can modify files, users, roles, cron, redirects, checkout, SMTP, DNS/CDN or external scripts

### Verification requirements

- verify WordPress.org checksums when available, but record unavailable or unverifiable packages separately
- for premium/custom code, compare with a package obtained through a trusted vendor or an internally reproduced build
- inspect package contents before installation, including installer scripts, bundled binaries, obfuscated code and unexpected domains
- compare repository source, built distribution and installed files
- review Composer/npm dependency lockfiles inside plugins/themes when present
- verify update source, update-server URL, certificate validation and signing behavior
- identify plugins removed from directories, ownership-transferred projects, abandoned packages and nulled/pirated distributions
- treat automatic update status as configuration, not proof that the update succeeded or was timely
- inspect filters, constants and provider policies that disable or defer forced security updates

### Third-party script and connector inventory

Include:

- tag managers, analytics, chat, ads, consent tools and optimization scripts
- payment gateway SDKs and remotely loaded checkout JavaScript
- SMTP, CRM, backup, storage, AI/provider connector and webhook credentials
- OAuth applications, API keys and application passwords
- CDN workers, edge includes and script-rewrite features
- browser extensions or workstation deployment tools used by administrators

A component may be clean on disk while its update channel, remote script, vendor account or CI release process is compromised. Scope the trust chain, not only the ZIP file.

