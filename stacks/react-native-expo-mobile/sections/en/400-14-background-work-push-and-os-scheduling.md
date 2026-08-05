## 14. Background Work, Push, And OS Scheduling

### 14.1 Background Execution
- Inventory TaskManager tasks, background fetch, location, geofencing, uploads, downloads, media, headless JavaScript, native services, BGTaskScheduler, and Android jobs.
- Verify registration timing, unique task identity, duplicate registration, versioning, persisted options, permission dependencies, and unregister behavior.
- Design for best-effort scheduling, OS throttling, battery restrictions, network constraints, process death, reboot, and vendor-specific behavior.
- Bound execution time, memory, data volume, retries, wakeups, and concurrency; checkpoint durable progress.
- Test old background code with new backend, new JavaScript with old native scheduler state, and queued work across app upgrades.
- Expose success, failure, timeout, cancellation, next schedule, last completion, and user-visible stale-data state.

### 14.2 Push Notifications And Actions
- Inventory APNs, FCM, Expo Push Service, direct provider integration, notification service extensions, categories, channels, and background handlers.
- Treat payload as untrusted input and validate type, version, size, sender context, deep link, resource ownership, and expiration.
- Do not place secrets or unnecessary personal data in payloads, notification text, analytics, or device logs.
- Test duplicate, delayed, reordered, expired, malformed, tenant-mismatched, logged-out, account-switched, and revoked-resource notifications.
- Verify tap, dismiss, quick action, text input, foreground, background, terminated, and restored behavior separately.
- Define token registration, rotation, invalidation, logout cleanup, account deletion, environment separation, and delivery observability.

