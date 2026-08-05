## 25. Migration Overlays

### 25.1 React Native And Expo Upgrade
- Upgrade supported framework and Expo SDK versions incrementally unless evidence justifies a different sequence.
- Before each step freeze baseline behavior, critical journey tests, release artifacts, symbols, source maps, store state, update state, and rollback path.
- Compare native templates, config plugins, generated projects, build tools, permission declarations, lifecycle, Hermes, Metro, Codegen, and third-party support.
- Test release binaries and OTA compatibility at every step; do not rely on Expo Doctor or successful compilation alone.
- Track deprecated APIs, removed behavior, support windows, store requirements, minimum OS changes, and native library replacements.
- Roll out each step independently with telemetry, guardrails, abort, rollback, and retained evidence.

### 25.2 New Architecture And Expo Adoption
- Inventory unsupported libraries, custom native modules, view managers, JSI code, brownfield surfaces, build scripts, and native patches before migration.
- Migrate one boundary at a time with schema, threading, lifecycle, memory, error, and compatibility tests.
- When adopting Expo or CNG define native project ownership, config-plugin coverage, regeneration rules, development-build strategy, EAS linkage, and escape path.
- Do not erase working native behavior with prebuild cleanup until every manual change has an authoritative config-plugin or documented ownership strategy.
- Validate library maintainers, fork plans, patch ownership, future framework support, and rollback from partially migrated state.
- Retire compatibility code only after production evidence proves the replacement across supported platforms and versions.

