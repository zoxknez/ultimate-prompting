## 12. Phase G - Adaptive UI And Device Classes

### 12.1 Phones, Tablets, Foldables And Desktop-Like Modes

1. Test compact, medium, and expanded window sizes, not only device names or orientation.
2. Verify resize, split-screen, freeform, multi-window, fold posture, hinge, desktop mode, keyboard, mouse, trackpad, and stylus where supported.
3. Avoid orientation locks and resizability restrictions unless the use case and policy justify them.
4. Verify list-detail, navigation, dialogs, sheets, grids, media, and forms adapt without stretching phone UI blindly.
5. Test cutouts, insets, edge-to-edge, status and navigation bars, IME, gesture navigation, and display density.
6. Verify focus order, keyboard navigation, hover, context menus, shortcuts, and selection for larger devices.
7. Test state continuity when resizing or moving between displays.
8. Verify screenshots and sensitive content behavior in recents and external displays.

### 12.2 Android TV And D-Pad

1. Map focus traversal for every screen, rail, row, dialog, overlay, player, search, and empty or error state.
2. Verify a visible focused state, deterministic initial focus, focus restoration, and no focus traps.
3. Test D-pad, back, play, pause, seek, channel, menu, long press, and manufacturer remote variations.
4. Verify overscan-safe layout, readable distance, target size, contrast, and motion.
5. Verify lazy lists retain focus correctly when data changes, pages load, filters change, or items disappear.
6. Verify player controls, active audio, multiview, buffering, retry, parental gates, and screen-on behavior.
7. Test TV launcher intent, banners, recommendations, preview channels, media sessions, and background playback where applicable.
8. Verify touch-only assumptions are removed from TV flows.
9. Test low-memory TV devices and slower storage or network conditions.

### 12.3 Wear OS, Automotive And Other Device Surfaces

1. Apply only if present and use current platform-specific quality guidance.
2. Verify rotary input, ambient mode, tiles, complications, small-screen navigation, and battery constraints for Wear OS.
3. Verify driver-distraction, parked versus driving state, templates, media, messaging, and manifest declarations for Android Auto or Automotive.
4. Verify companion-device association, cross-device state, permissions, and disconnect recovery.
5. Separate device-specific code and policy without duplicating core business logic unnecessarily.

