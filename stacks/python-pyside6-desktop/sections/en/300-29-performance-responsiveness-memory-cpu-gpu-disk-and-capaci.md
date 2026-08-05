## 29. Performance, Responsiveness, Memory, CPU, GPU, Disk, And Capacity

### 29.1 Audit Scope

1. Define budgets for cold/warm startup, first interactive state, critical journey latency, GUI-thread stall, frame time, memory, CPU, GPU, disk, network, package size, and update size.
2. Measure import time, module initialization, resource loading, font and icon loading, QML compilation, database startup, network initialization, and first-window rendering.
3. Profile GUI thread, render thread, Python threads, native threads, event-loop lag, lock waits, queue waits, allocation, object retention, native heap, textures, and handles.
4. Assess large datasets, images, media, documents, caches, histories, undo stacks, background transfers, devices, multiple windows, and long sessions.
5. Review batching, coalescing, pagination, lazy loading, caching, prefetch, compression, worker limits, and degraded modes with correctness constraints.
6. Define supported device classes, minimum hardware, headroom, concurrency, maximum project/data size, disk requirements, and failure thresholds.

### 29.2 Required Verification

1. Run cold, warm, burst, sustained, soak, low-memory, disk-pressure, offline, dependency-slowdown, and multi-window workloads on representative hardware.
2. Capture repeatable before/after measurements with exact artifact, data set, environment, sampling, and statistical summary.
3. Use Python and native profilers, Qt tools, operating-system traces, heap snapshots, handle inspection, and graphics diagnostics as appropriate.
4. Test cancellation and cleanup after large operations so memory, temporary files, threads, queues, and handles return to acceptable baselines.
5. Reject optimizations that weaken validation, authorization, durability, accessibility, diagnostics, or recovery without an explicit approved tradeoff.

