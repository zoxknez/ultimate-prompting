## 30. Accessibility, Localization, Visual Correctness, And Error UX

### 30.1 Audit Scope

1. Inventory supported languages, scripts, locales, time zones, calendars, numbering, currencies, units, plural rules, input methods, themes, contrast modes, and motion preferences.
2. Review accessible names, roles, states, descriptions, relationships, live updates, focus order, keyboard operation, shortcuts, mnemonics, and screen-reader output.
3. Assess text scaling, high DPI, fractional scaling, long translations, right-to-left layout, bidirectional text, emoji, combining marks, truncation, and font fallback.
4. Review color contrast, non-color indicators, focus visibility, target size, reduced motion, flashing, animation cancellation, and graphics alternatives.
5. Map user-visible error states for validation, permission denial, offline, timeout, partial failure, cancellation, corrupted data, update failure, and recovery.
6. Ensure errors are actionable without exposing secrets, stack traces, internal paths, identifiers, or misleading success states.

### 30.2 Required Verification

1. Test critical journeys with keyboard only, screen readers, high contrast, 200 percent or policy-required text scaling, RTL, long translations, and reduced motion.
2. Run packaged builds on each platform because native accessibility bridges, fonts, menus, dialogs, and shortcuts differ from source tests.
3. Verify focus and announcements during asynchronous progress, validation failure, modal dialogs, notifications, page replacement, and error recovery.
4. Test locale and time-zone changes, ambiguous dates, daylight-saving transitions, Unicode filenames, and mixed-script input.
5. Require screenshots or recordings for visual regressions and accessibility evidence where automation is insufficient.

