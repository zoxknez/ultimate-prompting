## 26. Forbidden Shortcuts

Do not:

1. Declare the app production-ready because `assembleDebug` passes.
2. Disable R8, resource shrinking, lint, tests, TLS validation, signing checks, or permissions to make a build pass.
3. Use debug signing or debug endpoints in production.
4. Add broad keep rules without proving why they are needed.
5. Use `GlobalScope`, unmanaged executors, real sleeps, or swallowed exceptions as fixes.
6. Replace transactions, idempotency, or authorization with UI button disabling alone.
7. Store secrets in source, resources, BuildConfig, assets, native strings, or reversible obfuscation and call them secure.
8. Accept all certificates, disable hostname verification, or enable cleartext globally.
9. Mark exported components, deep links, WebViews, or file providers safe without testing hostile input.
10. Use destructive Room migration fallback for user data without explicit approval and recovery.
11. Claim 16 KB support merely because the app installs on a normal emulator.
12. Treat emulator-only success as proof for codecs, DRM, camera, Bluetooth, TV, OEM, or thermal behavior.
13. Invent command output, test results, profiler metrics, Play Console state, policy eligibility, or source citations.
14. Perform an unrelated mass upgrade or rewrite while fixing one issue.
15. Mark critical areas safe because access or evidence was missing.
16. Ignore release-only, minified, offline, low-memory, process-death, or account-switching behavior.

