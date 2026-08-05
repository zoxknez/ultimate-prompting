## 43. Performance, Capacity, Battery, And Resource Audit

Profile release/profile builds on representative hardware before optimizing.

- Define budgets for cold/warm startup, first frame, time to interactive, route transition, input latency, frame build/raster time, memory, CPU, battery, network, disk, and artifact size.
- Capture DevTools timelines, frame charts, CPU profiles, allocation profiles, heap snapshots, network traces, shader/raster behavior, platform traces, and backend metrics.
- Measure low-end devices, old supported devices, large datasets, slow storage, constrained memory, thermal pressure, battery saver, poor network, and long sessions.
- Audit startup dependency chain, synchronous I/O, plugin initialization, database migration, remote config, authentication restoration, font/image decode, and first-route work.
- Detect rebuild and relayout hotspots, expensive paint, platform-view cost, large object churn, image/cache leaks, stream/listener leaks, isolate overhead, and background wakeups.
- Test burst, soak, pagination, huge list, rapid navigation, repeated login/logout, account switch, offline queue, reconnect, upload/download, media, and notification storms.
- Correlate client behavior with API rate, retry amplification, websocket connections, push registration, storage growth, cache hit rate, and cloud cost.
- Require before/after measurements, statistical context, device matrix, workload definition, visual correctness, and rollback for performance changes.

