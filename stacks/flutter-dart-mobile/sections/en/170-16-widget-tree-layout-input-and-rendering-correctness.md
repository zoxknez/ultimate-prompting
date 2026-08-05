## 16. Widget Tree, Layout, Input, And Rendering Correctness

Review UI behavior across constraints, devices, input modes, text scales, and lifecycle changes.

- Audit widget identity, keys, list reuse, reorder behavior, focus retention, form state, scroll position, hero tags, overlays, and portal-like content.
- Check constraints, unbounded layouts, overflow, intrinsic measurement, nested scrolling, slivers, large lists, grids, tables, dialogs, sheets, and keyboard insets.
- Verify touch, mouse, trackpad, stylus, keyboard, gamepad, remote control, hover, drag/drop, context menus, text selection, and IME behavior where applicable.
- Test minimum and extreme sizes, orientation, split-screen, fold/posture changes, desktop resize, multiple displays, safe areas, system bars, and display cutouts.
- Inspect animation controllers, ticker ownership, reduced-motion behavior, route transitions, loading indicators, skeletons, and interruption handling.
- Verify image decode, caching, placeholders, error states, large images, animated formats, vector assets, color profiles, and memory pressure.
- Detect unnecessary rebuilds, layout thrashing, saveLayer use, opacity/clipping cost, shader compilation issues, raster cache misuse, and platform-view composition cost.
- Require visual, golden, semantic, focus, and interaction tests where regressions have meaningful user impact.

