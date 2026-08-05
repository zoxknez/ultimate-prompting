## 21. Accessibility, Adaptive UI, And Localization

### 21.1 Accessibility
- Test screen readers, focus order, labels, roles, states, hints, live regions, grouping, headings, modals, errors, and custom gestures.
- Test keyboard, switch control, external input, D-pad, pointer, TV focus, and hardware-key navigation where supported.
- Verify large text, font scaling, Dynamic Type, bold text, display zoom, contrast, color independence, reduced motion, transparency, and animation settings.
- Test loading, empty, offline, permission-denied, validation, partial failure, destructive confirmation, and success states.
- Ensure custom Fabric views, native views, charts, maps, media controls, and WebViews expose usable accessibility semantics.
- Use automated checks as a supplement to manual assistive-technology testing on both platforms.

### 21.2 Adaptive Layout And Localization
- Test supported phones, tablets, foldables, resizable windows, split screen, orientation, safe areas, keyboard, cutouts, and external displays.
- Use measured adaptive breakpoints and content priorities instead of device-name assumptions.
- Test LTR and RTL layout, bidirectional text, locale switching, long translations, plural rules, grammatical variants, and fallback locale.
- Audit date, time, calendar, timezone, number, currency, decimal precision, rounding, units, phone number, address, and sorting behavior.
- Verify persisted values are locale-independent and migrations do not reinterpret formatted display strings as canonical data.
- Test locale and timezone changes while the application is installed, backgrounded, offline, or running a long operation.

