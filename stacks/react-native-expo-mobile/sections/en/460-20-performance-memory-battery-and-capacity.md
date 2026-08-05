## 20. Performance, Memory, Battery, And Capacity

### 20.1 Measurement Contract
- Define budgets for cold start, warm start, time to interactive, navigation, input response, list scroll, animation, memory, bundle, binary, network, battery, and storage.
- Measure release builds on representative low, medium, and high capability physical devices with realistic data and network conditions.
- Separate JavaScript thread, UI thread, native module, render, GPU, I/O, network, database, image decode, and backend latency.
- Capture p50, p95, p99, maximum, variance, regression threshold, sample size, warmup, and environmental noise.
- Compare before and after every performance change and reject improvements that trade correctness, accessibility, memory, battery, or crash safety.
- Do not close a performance finding from simulator, debug, remote debugger, or microbenchmark evidence alone.

### 20.2 Startup, Lists, Animations, And Images
- Profile module initialization, native SDK startup, synchronous storage, font loading, asset loading, authentication bootstrap, navigation readiness, and first useful content.
- Audit FlatList, SectionList, VirtualizedList, FlashList, custom recyclers, item keys, estimated sizes, windows, clipping, pagination, and nested scrolling.
- Audit Reanimated, Gesture Handler, LayoutAnimation, native animations, shared values, worklets, UI-thread work, cancellation, and stale callbacks.
- Bound image dimensions, cache, prefetch, decode, transformations, animated images, thumbnails, placeholders, and full-resolution retention.
- Test rapid navigation, long lists, repeated media, orientation changes, fold/unfold, low memory, background-resume, and OTA reload.
- Use platform profilers and React Native DevTools together and retain traces linked to release identity.

### 20.3 Memory, Battery, Thermal, And Network Cost
- Measure JavaScript heap, native heap, graphics memory, image memory, database cache, socket buffers, and retained object graphs.
- Detect leaks from listeners, timers, closures, navigation, native modules, Fabric views, media, sensors, WebViews, SDKs, tasks, and caches.
- Audit wakeups, polling, reconnect loops, background location, push processing, animation, media, sync, and network batching for battery impact.
- Test low-memory warnings, memory pressure, thermal throttling, low-power mode, data saver, metered network, and constrained background execution.
- Set capacity and abuse limits for pagination, search, uploads, downloads, offline queues, notifications, media, maps, and realtime events.
- Tie technical resource use to user journey, device class, SLO, infrastructure cost, and store-quality metrics.

