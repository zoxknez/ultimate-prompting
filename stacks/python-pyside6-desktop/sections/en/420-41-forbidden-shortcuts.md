## 41. Forbidden Shortcuts

1. Do not declare success because the application starts from source, a unit suite passes, or one unsigned package launches on the developer machine.
2. Do not call `processEvents`, sleep on the GUI thread, move UI work to arbitrary threads, or keep objects globally alive merely to hide lifecycle defects.
3. Do not update widgets or models directly from workers, ignore thread affinity, or assume the GIL makes Qt and business state thread-safe.
4. Do not enable free-threaded mode, JIT, a new Python major, or a new Qt major without native dependency, packaging, platform, and rollback evidence.
5. Do not silence exceptions, Qt warnings, failed futures, unhandled tasks, type errors, linter results, packaging warnings, signature failures, or migration errors without root-cause analysis.
6. Do not add broad `except`, empty handlers, arbitrary sleeps, forced garbage collection, unchecked casts, global mutable state, or blanket suppressions as universal fixes.
7. Do not deserialize untrusted pickle/YAML/object data, execute user input, load arbitrary plugins, or compile untrusted QML/JavaScript/templates.
8. Do not build shell commands from interpolated input, trust localhost automatically, open arbitrary URLs, or search writable paths for code and helpers.
9. Do not disable TLS validation, accept all certificates, store secrets in plain settings, or log tokens, credentials, personal data, or cryptographic material.
10. Do not broaden file, device, plugin, WebChannel, IPC, helper, service, or installer permissions merely to make a feature work.
11. Do not treat PyInstaller/Nuitka/Qt bundling, obfuscation, code signing, antivirus approval, or OS sandboxing as a complete security boundary.
12. Do not auto-migrate or reset data without backup and failure semantics; do not silently delete corrupted profiles or user files.
13. Do not publish mutable or unsigned artifacts, rebuild different bytes per environment without reason, or let untrusted CI access signing and production channels.
14. Do not raise thread, queue, timeout, retry, memory, disk, parser, or transfer limits without capacity and abuse analysis.
15. Do not claim Windows, macOS, Linux, x64, ARM64, high DPI, accessibility, update, rollback, or restore support without applicable packaged evidence.
16. Do not mass-format, delete unrelated files, weaken tests, hide failed checks, or overwrite another person's work.
17. Do not call the application perfect, fully secure, fully tested, or production-ready without satisfying the applicable evidence and recovery requirements.

