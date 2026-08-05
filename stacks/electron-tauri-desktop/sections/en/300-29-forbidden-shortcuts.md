## 29. Forbidden Shortcuts

1. Do not declare success because the app starts in development mode, builds on one machine, passes browser tests, or produces an installer.
2. Do not enable Node integration, disable context isolation/sandbox/web security, broaden a Tauri capability, grant a default plugin permission, or expose generic IPC/commands merely to make a feature work.
3. Do not validate only in the renderer/frontend. Privileged boundaries must validate and authorize independently.
4. Do not silence TypeScript, Rust, compiler, linter, packaging, signing, notarization, installer, updater, or security warnings without root-cause analysis.
5. Do not add `any`, unchecked casts, `unwrap`, `expect`, broad `unsafe`, empty catch blocks, ignored promises/results, or blanket suppressions as universal fixes.
6. Do not use shell execution with interpolated input, arbitrary external-open URLs, unrestricted filesystem scopes, writable executable paths, or unauthenticated localhost services.
7. Do not disable TLS or certificate checks, accept all origins, log secrets, store long-lived tokens in frontend storage, or ship private keys.
8. Do not treat ASAR, obfuscation, minification, Rust, code signing, a sandbox, or capabilities as a complete security boundary by itself.
9. Do not auto-run destructive migrations, reset corrupted data silently, remove user data without policy, or install updates during unsafe critical work.
10. Do not publish mutable artifacts, rebuild separately per promotion stage without explanation, sign unreviewed bytes, or let untrusted CI access release credentials.
11. Do not raise memory, queue, timeout, retry, process, or file-size limits without capacity and abuse analysis.
12. Do not migrate Electron to Tauri, Tauri to Electron, rewrite the frontend, replace the database, or change installer technology merely for popularity or binary-size claims.
13. Do not delete another person's changes, mass-format the repository, hide unrelated diffs, skip failing tests, or weaken tests so a pipeline passes.
14. Do not claim cross-platform support without packaged install/runtime/update evidence on the supported platform matrix.
15. Do not call the application perfect, fully secure, or production-ready without satisfying the applicable evidence and recovery requirements.

