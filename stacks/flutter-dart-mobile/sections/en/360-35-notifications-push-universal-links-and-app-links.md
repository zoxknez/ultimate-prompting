## 35. Notifications, Push, Universal Links, And App Links

Push delivery is untrusted, duplicated, delayed, and platform-dependent.

- Inventory FCM/APNs/web push providers, tokens, topics, channels/categories, background handlers, notification service extensions, actions, badges, and local notifications.
- Verify token registration, rotation, deletion, environment separation, account/tenant binding, logout cleanup, device replacement, and server-side authorization.
- Treat payload fields as untrusted; validate type, size, route, object identifier, actor, tenant, freshness, signature where used, and current authorization.
- Test foreground, background, terminated, force-stopped, offline, duplicate, delayed, reordered, revoked-session, wrong-account, and app-upgrade delivery.
- Avoid sensitive notification content on locked screens unless policy and user choice permit it; handle preview settings and platform redaction.
- Verify app links, universal links, custom schemes, asset association files, domain ownership, fallback pages, multiple apps, and hijack resistance.
- Make notification actions idempotent and server-authorized; prevent repeated taps from duplicating payments, orders, messages, or destructive changes.
- Measure delivery, open rate, duplicate rate, invalid token rate, action failure, deep-link failure, and notification-to-backend amplification.

