## Work Modes

Default: `AUDIT_AND_SAFE_FIX`.

| Mode | Allowed |
| --- | --- |
| `AUDIT_ONLY` | No source/lock/signing/EAS channel/store changes. |
| `AUDIT_AND_SAFE_FIX` | Low-risk fixes + tests; plan for native/OTA/data. |
| `FULL_IMPLEMENTATION` | Small steps; do not publish build/OTA without approval. |
| `FIX_CONFIRMED_ISSUES` | Confirmed only. |
| `SECURITY_AUDIT` | Auth, tokens, deep links, WebView, native/JSI, storage, network, OTA trust, signing. |
| `PERFORMANCE_AUDIT` | Startup, Hermes, JS/UI thread, Fabric, lists, memory, images, JSI, DB, battery; release profile. |
| `NEW_ARCHITECTURE_MIGRATION` | Legacy inventory, Turbo/Fabric/Codegen/JSI, threading, rollback. |
| `EXPO_MIGRATION` | bare/CNG/SDK, Router, EAS, config plugins, dev clients. |
| `RELEASE_AND_OTA_AUDIT` | Native build, runtimeVersion, channels, signing, rollout, local-data, store. |

