## 16. Phase K - Background Work, Services, Notifications And Scheduling

1. Inventory WorkManager, services, foreground services, alarms, JobScheduler, FCM, receivers, exact alarms, and app-start triggers.
2. Verify each background mechanism is necessary and matches current platform restrictions.
3. Verify WorkManager uniqueness, constraints, tags, input limits, progress, retries, backoff, cancellation, chaining, and idempotency.
4. Prevent duplicate workers after process death, app update, boot, login, or repeated user actions.
5. Verify foreground-service type, permission, user-visible purpose, notification timing, stop behavior, and timeout.
6. Verify the app does not start restricted background work illegally.
7. Verify exact alarms are truly user-facing and policy-eligible.
8. Verify boot receivers, rescheduling, time-zone changes, daylight saving, clock changes, and device reboot.
9. Verify notifications have correct channels, importance, grouping, actions, PendingIntents, privacy, localization, permission handling, and deep links.
10. Prevent stale, duplicate, misleading, sensitive, or cross-account notifications.
11. Verify FCM token rotation, duplicate messages, collapse behavior, data versus notification payloads, and server authorization.
12. Measure wakeups, network, CPU, location, and battery impact.
13. Test Doze, App Standby, Battery Saver, background restriction, OEM process killing, offline, and low storage.

