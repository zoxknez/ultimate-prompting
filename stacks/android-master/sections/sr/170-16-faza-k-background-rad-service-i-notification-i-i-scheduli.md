## 16. Faza K - Background Rad, Service-i, Notification-i I Scheduling

1. Inventarisi WorkManager, service-e, foreground service-e, alarm-e, JobScheduler, FCM, receiver-e, exact alarm-e i app-start trigger-e.
2. Proveri da je svaki background mehanizam neophodan i odgovara aktuelnim platform ogranicenjima.
3. Proveri WorkManager uniqueness, constraints, tag-ove, input limite, progress, retry, backoff, cancellation, chaining i idempotency.
4. Spreci duple worker-e nakon process death-a, app update-a, boot-a, login-a ili ponovljenih user akcija.
5. Proveri foreground-service type, permission, user-visible purpose, notification timing, stop ponasanje i timeout.
6. Proveri da aplikacija ne pokrece nedozvoljen restricted background rad.
7. Proveri da su exact alarm-i stvarno user-facing i policy-eligible.
8. Proveri boot receiver-e, rescheduling, promene time zone, daylight saving, promene sata i device reboot.
9. Proveri da notification ima ispravne channel-e, importance, grouping, action-e, PendingIntent-e, privacy, localization, permission handling i deep link.
10. Spreci stale, duplicate, misleading, sensitive ili cross-account notification-e.
11. Proveri FCM token rotation, duplicate message, collapse ponasanje, data naspram notification payload-a i server autorizaciju.
12. Izmeri wakeup, network, CPU, location i battery uticaj.
13. Testiraj Doze, App Standby, Battery Saver, background restriction, OEM process killing, offline i low storage.

