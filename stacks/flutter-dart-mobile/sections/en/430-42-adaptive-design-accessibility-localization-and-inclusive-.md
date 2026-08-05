## 42. Adaptive Design, Accessibility, Localization, And Inclusive UX

Accessibility and adaptation are correctness requirements, not final polish.

- Define supported window classes, breakpoints, orientation, posture, input modes, navigation patterns, information density, and feature parity by platform.
- Test text scaling beyond common defaults, bold text, display zoom, high contrast, color filters, dark mode, reduced motion, reduced transparency, and system font changes.
- Verify semantic labels, roles, values, states, actions, traversal order, live regions, headings, grouping, error association, and hidden decorative content.
- Test TalkBack, VoiceOver, browser screen readers, Narrator, VoiceOver on macOS, and supported Linux accessibility tools with critical journeys.
- Verify keyboard-only and switch access, visible focus, focus trapping, restoration, shortcuts, escape/back semantics, touch target size, gesture alternatives, and timeout extensions.
- Audit contrast, non-color cues, flashing, animation, autoplay, captions, transcripts, audio descriptions, haptics, and error recovery.
- Verify locale resolution, fallback, plural/gender rules, RTL, bidirectional text, date/time, timezone, numbers, currency, names, addresses, sorting, search, and Unicode normalization.
- Detect hard-coded user text, concatenated translations, clipped strings, missing keys, stale generated localizations, untranslated native UI, and unsafe server text.
- Require automated semantics checks plus manual assistive-technology and locale matrix testing for critical flows.

