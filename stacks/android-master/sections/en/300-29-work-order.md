## 29. Work Order

Execute in this order unless evidence requires a safer sequence:

```text
protect workspace, data, signing and secrets
-> freeze repository and inventory modules, variants and artifacts
-> verify toolchain and dependency compatibility
-> establish debug and release build baselines
-> inspect R8, signing, packaging, native libraries and 16 KB support
-> map architecture, lifecycle, state, navigation and data flow
-> audit Compose, Views, adaptive UI and target devices
-> audit storage, sync, network, security, privacy and permissions
-> audit background work, notifications, media and hardware APIs
-> measure performance, memory, startup, ANR, energy and accessibility
-> execute risk-based tests and device matrix
-> inspect observability, CI/CD, supply chain, rollout and incident controls
-> apply safe fixes with regression tests
-> re-run release verification, record residual risk and issue final verdict
```

Stop or contain immediately if a confirmed P0 could cause ongoing harm.

