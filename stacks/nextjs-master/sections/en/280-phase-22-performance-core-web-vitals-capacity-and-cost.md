## Phase 22 - Performance, Core Web Vitals, Capacity, And Cost

Optimize from measured user, browser, server, database, cache, network, and cost evidence.

### Audit Requirements

- Measure field and lab LCP, INP, CLS, TTFB, navigation, hydration, RSC payload, JS, CSS, images, fonts, third parties, and long tasks.
- Break latency into queue, cold start, Proxy, auth, cache, database, dependency, rendering, streaming, and network.
- Set budgets for JS, route chunks, RSC payload, images, fonts, third-party work, memory, queries, and external calls.
- Audit image sizing, formats, remote patterns, priority, transforms, cache, cost, and abuse.
- Audit font loading, subset, fallback, variable fonts, preload, shift, privacy, and self-hosting.
- Test cold, warm, burst, sustained, soak, failover, cache-cold, and dependency-brownout scenarios.

### Required Evidence

- Field CWV by route, device, geography, browser, release, and user state.
- Bundle, RSC, image, font, query, call, memory, CPU, and cost profiles.
- Capacity model with saturation, headroom, scaling, and load shedding.
- Before/after evidence for every performance change.

### Mandatory Failure And Acceptance Tests

- Run critical journeys on low-end mobile, desktop, slow network, high latency, and auth states.
- Exceed each budget and prove CI, alerting, or admission catches it.
- Load cold caches and instances while a dependency is degraded.
- Verify load shedding protects critical writes and recovery before saturation.

