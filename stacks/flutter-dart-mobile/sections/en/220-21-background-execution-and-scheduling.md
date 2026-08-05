## 21. Background Execution And Scheduling

Background work is platform-controlled and cannot be guaranteed by a Dart timer.

- Inventory WorkManager, foreground services, background fetch, BGTaskScheduler, silent push, isolates, desktop services, scheduled tasks, and browser background capabilities.
- Document platform eligibility, execution window, quotas, battery/network constraints, user-visible requirements, permission, and termination behavior.
- Make tasks idempotent, resumable, bounded, observable, and safe after duplicate scheduling, delayed execution, process death, reboot, upgrade, logout, or account switch.
- Verify background entrypoint initialization, plugin registration, storage access, authentication refresh, tenant context, and conflict handling.
- Prevent background jobs from leaking data after logout, continuing revoked uploads, reviving deleted state, or sending stale notifications.
- Test restricted battery modes, no network, metered network, low storage, reboot, force stop, OS upgrade, app upgrade, and missed schedule recovery.
- Measure success, delay, retries, duplicate execution, duration, resource use, queue age, and backend load.
- Provide a degraded-mode product behavior when the platform cannot or will not run work on the desired schedule.

