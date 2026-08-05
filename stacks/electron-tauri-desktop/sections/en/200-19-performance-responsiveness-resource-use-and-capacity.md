## 19. Performance, Responsiveness, Resource Use, And Capacity

### 19.1 Measurement Plan

1. Define budgets for cold/warm startup, first usable window, critical interaction latency, IPC/command latency, update check, memory, CPU, GPU, disk, network, battery, installer size, and package size.
2. Measure on representative minimum and typical hardware, supported operating systems, x64/ARM64, clean and mature profiles, online/offline, and with realistic data volumes.
3. Separate frontend render time, framework bootstrap, native initialization, database migration, credential access, network wait, plugin initialization, sidecar startup, and updater work.
4. Capture traces and profiles before optimizing. Correlate long tasks, main-thread blocking, Rust/Node blocking, lock contention, IPC serialization, database queries, filesystem, GPU, and network.
5. Test idle behavior, hidden/tray mode, minimized windows, background timers, service workers, polling, telemetry, device listeners, and updater cadence.
6. Bound caches and queues. Define eviction, persistence, account isolation, stale-data policy, and memory-pressure behavior.
7. Measure leak behavior across window open/close, navigation, reload, account switch, document open/close, device connect/disconnect, update, and long-running idle.
8. Do not claim performance improvement from microbenchmarks alone; confirm the user journey and resource budget.

### 19.2 Responsiveness And Failure Containment

1. Keep renderer/UI threads responsive. Move CPU-heavy parsing, compression, indexing, media, cryptography, and database work to suitable bounded workers or native processes.
2. Do not block the Electron main process or Tauri event loop with synchronous filesystem, network, crypto, database, child-process, or lock waits.
3. Use backpressure from UI through IPC/commands to workers and external services. Dropping, coalescing, pausing, or rejecting work must be explicit.
4. Prevent one slow window, file, device, network request, tenant/account, or plugin from exhausting global resources.
5. Define timeouts and cancellation for operations that can hang. Ensure cancellation does not leave corrupted files, half-applied migrations, or duplicated side effects.
6. Handle out-of-memory, GPU crash, renderer crash, sidecar crash, WebView failure, database lock, and service outage with bounded recovery.
7. Use crash restart only with limits and state validation. Avoid loops that repeatedly destroy user work or hammer update/network services.
8. Test burst input, huge history, many windows, large files, slow disk, low memory, high DPI, multiple displays, sleep/wake, and prolonged offline mode.

