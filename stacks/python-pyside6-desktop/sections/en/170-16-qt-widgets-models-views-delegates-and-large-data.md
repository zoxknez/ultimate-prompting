## 16. Qt Widgets, Models, Views, Delegates, And Large Data

### 16.1 Audit Scope

1. Inventory windows, dialogs, stacked pages, dock widgets, actions, shortcuts, forms, tables, trees, lists, proxy models, delegates, and custom painting.
2. Review layout ownership, duplicate layout assignment, widget parenting, focus chains, tab order, modality, geometry persistence, and multi-monitor behavior.
3. For every model, verify index validity, parent/child relationships, row and column notifications, persistent indexes, reset semantics, sorting, filtering, and thread ownership.
4. Assess lazy loading, pagination, virtualization, fetch-more behavior, image/icon caching, large text, drag/drop, clipboard, and undo/redo.
5. Review delegate editors, validation, commit/close ordering, stale indexes, selection state, and concurrent model updates.
6. Distinguish presentation formatting from domain values, permissions, validation, persistence, and business invariants.

### 16.2 Required Verification

1. Exercise empty, small, large, malformed, rapidly changing, filtered, sorted, reordered, and concurrently refreshed datasets.
2. Use model testers, assertions, focused unit tests, and UI automation to validate notification order and index safety.
3. Measure scroll, resize, selection, editing, filtering, painting, and memory behavior at realistic maximum data sizes.
4. Test keyboard-only navigation, screen reader names/states, high DPI, text scaling, localization expansion, and right-to-left layouts.
5. Ensure model changes are marshalled to the GUI thread and stale asynchronous results cannot mutate a replaced model or selection.

