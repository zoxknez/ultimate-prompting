## 11. Phase F - Jetpack Compose, Views And UI Correctness

### 11.1 Compose State And Side Effects

1. Verify state ownership and hoisting are placed as low as possible while preserving a single owner.
2. Detect mutable objects presented as immutable state, unstable collections, and in-place mutation that Compose cannot observe correctly.
3. Review `remember`, `rememberSaveable`, custom savers, keys, and ownership across navigation and configuration changes.
4. Review `LaunchedEffect`, `DisposableEffect`, `SideEffect`, `produceState`, `snapshotFlow`, and `rememberUpdatedState` for correct keys and cleanup.
5. Ensure composables do not launch uncontrolled work or perform I/O during composition.
6. Verify event lambdas are stable where materially beneficial and do not capture stale state.
7. Verify lazy layouts use stable unique keys and correct content types where needed.
8. Check derived state, snapshot reads, nested scrolling, focus, input, animation, and measure policies for correctness.
9. Verify previews, screenshot fixtures, and fake data do not leak into production code.
10. Confirm UI state is deterministic under recomposition and not dependent on incidental call count.

### 11.2 Compose Performance And Stability

1. Measure before optimizing. Use recomposition tooling, compiler reports, traces, Macrobenchmark, and representative release builds.
2. Detect expensive calculations, allocations, sorting, filtering, image processing, formatting, and object creation in hot composition paths.
3. Review stability only where evidence shows unnecessary recomposition or skipped-state problems.
4. Do not add `@Stable` or `@Immutable` to silence reports unless the contract is true.
5. Verify strong skipping and compiler behavior for the actual Kotlin and Compose toolchain.
6. Defer rapidly changing state reads to the narrowest phase where practical.
7. Verify animations, lists, grids, pagers, nested scroll, images, and video do not create measurable jank.
8. Test release mode with R8 because debug performance is not representative.
9. Verify Baseline Profiles cover real critical journeys and are packaged into the release artifact.
10. Record frame timing, jank, startup, allocation, and memory evidence before and after fixes.

### 11.3 Views, Fragments And Interoperability

1. Verify Fragment view bindings are cleared at `onDestroyView` and do not outlive the view lifecycle.
2. Verify observers and collectors use the correct lifecycle owner.
3. Check adapters, DiffUtil identity, stable IDs, recycled state, payloads, listeners, and selection behavior.
4. Verify custom views handle state saving, accessibility, measurement, RTL, font scale, and configuration changes.
5. Verify ComposeView disposal strategy and View-in-Compose lifecycle ownership.
6. Check mixed navigation and state ownership across Fragment, Activity, Compose, and ViewModel boundaries.
7. Detect synthetic view assumptions, deprecated APIs, retained fragments, and callback leaks.
8. Do not rewrite stable Views to Compose without a measurable product or maintenance reason.

