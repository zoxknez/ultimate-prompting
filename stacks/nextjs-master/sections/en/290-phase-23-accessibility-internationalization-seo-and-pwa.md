## Phase 23 - Accessibility, Internationalization, SEO, And PWA

Verify critical journeys for users, assistive tech, locales, crawlers, offline states, and multiple tabs.

### Audit Requirements

- Use semantic HTML, correct names/roles, labels, focus order, keyboard behavior, contrast, target size, reduced motion, and zoom.
- Test loading, error, empty, validation, optimistic, modal, menu, table, virtualized, drag/drop, media, and notification states.
- Verify locale routing, fallback, RTL, pluralization, collation, timezone, date, number, currency, and hydration stability.
- Audit metadata, canonical, hreflang, robots, sitemap, status codes, redirects, structured data, social previews, and soft 404.
- Inventory service worker, browser storage, offline mutation queues, push, account switch, logout, and multi-tab coordination.
- Never cache private HTML, RSC, API, export, or file data without proven identity binding and invalidation.

### Required Evidence

- Accessibility matrix with automated and manual evidence.
- Locale/RTL/timezone/currency matrix for critical journeys.
- Rendered metadata, status, canonical, robots, sitemap, and structured-data captures.
- Browser storage, service-worker, offline queue, and push lifecycle inventory.

### Mandatory Failure And Acceptance Tests

- Complete journeys using keyboard, screen reader, 200 percent zoom, reduced motion, and high contrast.
- Switch locale, RTL, timezone, currency, and font size during server/client navigation.
- Crawl direct and client-navigated pages and compare status, metadata, and visible content.
- Log out and switch account offline across multiple tabs and verify no data or mutation leakage.

