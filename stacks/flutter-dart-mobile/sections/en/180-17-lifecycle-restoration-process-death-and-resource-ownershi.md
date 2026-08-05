## 17. Lifecycle, Restoration, Process Death, And Resource Ownership

Assume the operating system can suspend, detach, kill, recreate, resize, or restore the application at inconvenient points.

- Map application, view, route, widget, engine, scene/window, isolate, service, and plugin lifecycles for every supported platform.
- Verify initialization ordering, dependency readiness, splash removal, session restoration, database opening, migrations, remote config, and first-frame behavior.
- Test backgrounding, foregrounding, inactive/hidden/detached states, memory pressure, device lock, interruption, permission changes, and process termination.
- Verify restoration of navigation, forms, drafts, playback, downloads, uploads, pagination, unsent actions, and conflict state without exposing another account or tenant.
- Dispose controllers, focus nodes, animation controllers, stream subscriptions, timers, ports, database watchers, plugin listeners, textures, cameras, players, and native handles exactly once.
- Handle hot restart and development-only behavior separately from production lifecycle claims.
- Test interrupted migration, interrupted write, interrupted payment, interrupted file transfer, interrupted update, and restoration after low-memory termination.
- Require state restoration and process-death tests on real or production-equivalent devices for critical flows.

