## 24. Phase 14 - Verification And Reinfection Watch

Verification must include independent evidence, not only the absence of visible symptoms.

### Technical verification

- repeat core and repository-plugin checksum checks
- repeat filesystem inventory and compare deltas
- re-scan all executable and script locations
- verify users, application passwords, cron, systemd, SSH keys, DB triggers/events and CDN rules
- verify no PHP execution in prohibited directories
- verify log collection and alerts
- test from authenticated and unauthenticated sessions
- test multiple user agents and referrers for conditional malware/SEO spam
- test direct origin and CDN paths where authorized
- check Search Console and public search results
- validate payment pages for unauthorized scripts and network requests

### Monitoring windows

Define monitoring by risk rather than using 24-72 hours as a guarantee:

- intensive watch: first 24-72 hours
- elevated watch: 7-14 days
- normal long-term monitoring: ongoing

Monitor file changes, privileged logins, failed logins, new users, plugin/theme changes, cron changes, outbound mail spikes, WAF events, unusual POST requests, PHP errors, DNS/CDN changes and search-index anomalies.

