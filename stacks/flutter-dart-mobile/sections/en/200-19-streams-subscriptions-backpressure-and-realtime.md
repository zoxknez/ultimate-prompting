## 19. Streams, Subscriptions, Backpressure, And Realtime

Review streams as long-lived resource and ordering contracts.

- Inventory single-subscription and broadcast streams, controllers, subjects, database watchers, sockets, SSE, platform event channels, and push-derived streams.
- Verify subscription ownership, pause/resume, cancellation, close, error handling, done semantics, replay, buffering, and lifecycle binding.
- Audit event ordering, duplicates, gaps, reconnection, resume cursor, snapshots plus deltas, clock skew, stale cache, and version conflict handling.
- Define backpressure, bounded queues, dropping/coalescing policy, slow-consumer behavior, and memory limits for high-volume streams.
- Prevent duplicate listeners after rebuild, navigation, reconnect, hot reload, account switching, and background/foreground transitions.
- Verify sensitive events are filtered by current identity, tenant, resource ownership, and revocation state before state mutation or display.
- Test disconnect storms, duplicate frames, malformed messages, server restart, resume-token expiry, and long offline periods.
- Measure event lag, queue depth, dropped/coalesced events, reconnect rate, memory growth, and server pressure.

