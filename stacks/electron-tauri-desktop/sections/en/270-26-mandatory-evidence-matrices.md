## 26. Mandatory Evidence Matrices

### 26.1 Source-To-Runtime Matrix

| source commit | resolved graph | builder | package | signature | distribution object | installed binary | runtime process | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.2 Window And WebView Privilege Matrix

| window/webview | origin | session/partition | preload/capability | permissions | data/account | navigation | owner | tests | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.3 IPC And Command Matrix

| channel/command | caller | schema | authentication | authorization | scope | side effect | idempotency | limits | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.4 Filesystem And External-Open Matrix

| operation | source | canonicalization | allowed scope | symlink/race defense | permissions | audit | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.5 Local Data And Migration Matrix

| store/path | owner | sensitivity | schema/version | migration | backup | restore | account isolation | deletion | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.6 Network And Local-Service Matrix

| client/listener | endpoint | trust | auth | TLS/peer check | timeout | retry/backpressure | data | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.7 Dependency And Native-Code Matrix

| component | resolved version | source | shipped | privilege | native/build code | advisory | compatibility | owner | action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.8 Artifact, Signing, And Store Matrix

| platform/channel | artifact | hash | package content | signing identity | timestamp/notary | store/repository | verification | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.9 Update And Rollback Matrix

| source version | target | platform/channel | metadata | signature | data migration | failure point | rollback/recovery | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.10 Platform And Installer Matrix

| OS/version | architecture | format | fresh install | upgrade | repair | rollback | uninstall | OS integration | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.11 Performance And Resource Matrix

| journey | device/profile | budget | measured | bottleneck | fix | regression test | residual risk | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.12 Operational Readiness Matrix

| control | owner | evidence | alert | runbook | abort threshold | rollback | last exercise | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

