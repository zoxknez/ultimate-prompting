## 37. Phase 27 - Detection Engineering, Monitoring And Reinfection Canaries

Monitoring must be designed around the observed attack path and remaining uncertainty.

### Minimum detection coverage

- privileged login, password reset, role and capability changes
- new application passwords, API keys and sessions
- plugin/theme/core install, update, activation, deactivation and file edit events
- MU plugin, drop-in, `wp-config.php`, `.htaccess`, `.user.ini` and executable-upload changes
- cron, Action Scheduler, system cron and panel task changes
- DNS, nameserver, CDN worker/rule and certificate changes
- unusual outbound HTTP, mail volume and webhook destinations
- spikes in 404, 403, 5xx, login, XML-RPC, REST and admin-ajax traffic
- suspicious PHP errors, process creation and filesystem writes
- database admin, trigger, event, grant and schema changes
- new Search Console/Bing owners and sitemap submissions
- checkout script, DOM and network-request drift where commerce is present

### Canary and integrity controls

- establish a signed or hashed known-good inventory for critical executable files
- use canary files or directories only when they do not expose secrets or create noise
- alert on PHP creation in uploads/cache/language/backup paths
- monitor unexpected changes to update configuration and security controls
- baseline normal outbound domains and privileged actions
- verify that alerts reach a channel independent of the compromised environment
- test alerts with safe synthetic events and record delivery latency

### Monitoring exit criteria

Do not close elevated monitoring based only on elapsed time. Require:

- no recurrence of incident indicators
- stable file and configuration inventory
- expected privileged activity only
- clean scheduled-task and queue state
- clean search/index and checkout verification where applicable
- functioning alerts and retained logs
- owner acceptance of residual blind spots

