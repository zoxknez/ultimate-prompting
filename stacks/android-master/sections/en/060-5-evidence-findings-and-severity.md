## 5. Evidence, Findings And Severity

### 5.1 Finding Schema

For every finding record:

```text
ID
severity: P0 | P1 | P2 | P3
status: OPEN | FIXED | CONTAINED | ACCEPTED | REJECTED | UNVERIFIED
component and module
build type, flavor and environment
device, API level, ABI and form factor
entry point and user journey
preconditions and trigger
reproduction steps
expected result
actual result
evidence status
evidence location
root cause
impact and blast radius
recommended repair
implemented change, if any
verification and regression test
rollback or containment
residual risk
owner and deadline, if known
```

### 5.2 Android-Specific Severity Model

Use the shared severity model, plus these minimum interpretations:

- `P0`: production credential or signing-key disclosure; confirmed auth or tenant bypass; destructive or unrecoverable data corruption; release crash loop; remote code execution; exploitable exported component with critical impact; broken production update path; complete critical playback or business-flow outage.
- `P1`: frequent crash or ANR; practical deep-link or intent abuse; race causing duplicate or inconsistent writes; migration failure with user-data loss risk; uncontrolled foreground service or battery drain; critical TV focus trap; insecure WebView or file exposure; release-only failure; serious permission, privacy, or policy breach.
- `P2`: measurable jank, startup, memory, energy, lifecycle, accessibility, offline, error-state, observability, testability, or maintainability weakness with real user or operational impact.
- `P3`: low-impact cleanup, naming, documentation, non-blocking consistency, or optional modernization.

Severity depends on impact, reachability, frequency, recovery, and evidence, not on the number of violated style rules.

### 5.3 Command, Build And Device Log

For every executed command, test, benchmark, or device session, record:

```text
run ID
repository revision and dirty state
command or action
working directory
Android Studio / AGP / Gradle / JDK / Kotlin / SDK / NDK versions
variant, flavor, build type and task
emulator or physical device model
Android version, API level, ABI, page size and form factor
start and end time
exit status
warnings and errors
result summary
artifact, report, trace, screenshot or log location
execution environment: local | container | CI | device-lab | staging | production-read-only
```

Do not summarize a red build as green because one unrelated task passed.

