## 26. Phase 16 - Hosting Account, Neighbor Site And Control-Plane Compromise

A WordPress site is not an isolated asset when it shares a hosting user, control panel, FTP account, PHP pool, database server, deployment credential or writable directory with other sites.

### Account-wide scope

Inventory and inspect:

- every domain, subdomain, addon domain, parked domain and document root under the hosting account
- staging, development, archived and forgotten installations
- sibling WordPress, Joomla, Drupal, custom PHP and static sites
- shared upload, cache, backup, temporary and session directories
- symlinks, bind mounts and aliases crossing site boundaries
- shared FTP/SFTP users, SSH keys, panel users and API tokens
- shared database users, Redis/Memcached instances, SMTP credentials and deployment keys
- host-level malware scanner findings and quarantine history
- account-level cron jobs, PHP handlers, `.user.ini` inheritance and environment variables

### Control-plane evidence

Collect, when available:

- hosting-panel login and audit history
- user creation, password reset, API token and delegated-access events
- DNS, nameserver, certificate and redirect changes
- file-manager, backup-restore and one-click installer activity
- FTP/SFTP/SSH authentication logs
- support impersonation or provider-side administrative actions
- snapshots, image history and account migration events

If account-wide compromise or weak tenant isolation is credible, prefer migration to a newly provisioned account or host over an in-place site-only cleanup. Document any sibling asset that remains unexamined as a reinfection risk.

