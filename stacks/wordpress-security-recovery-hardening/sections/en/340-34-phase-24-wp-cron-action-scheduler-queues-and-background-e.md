## 34. Phase 24 - WP-Cron, Action Scheduler, Queues And Background Execution

Background execution can preserve malware, replay unwanted actions or reintroduce modified files after an apparently successful cleanup.

### Execution inventory

- WordPress cron option and all registered hooks
- system cron calling `wp-cron.php`, WP-CLI or custom scripts
- disabled internal WP-Cron and alternate cron configurations
- Action Scheduler pending, in-progress, failed and completed actions
- plugin-specific queue tables and async request endpoints
- backup, migration, update, cache-warming, email and webhook jobs
- host-panel scheduled tasks and one-click maintenance jobs
- external schedulers, uptime services and CI webhooks that trigger application actions

### Required checks

- map every hook/action to the owning component and callable
- identify unknown callbacks, encoded arguments, suspicious recurrence and newly created events
- preserve malicious action records before cancellation
- inspect failed actions for payloads and stack traces
- prevent duplicate execution during maintenance and worker restart
- validate idempotency of payment, email, order, user and external API jobs
- verify old workers or cron runners cannot execute removed code
- test scheduler recovery after database restore, timezone change and daylight-saving transition
- monitor re-created events after cleanup as a persistence indicator

