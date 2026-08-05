## 44. Application Size, Symbols, Obfuscation, And Reverse Engineering

Reduce size and information exposure without sacrificing diagnosability or pretending the client can keep secrets.

- Measure per-platform release size, download size, installed size, split size, web transfer size, native libraries, fonts, assets, localization, and duplicate resources.
- Use size analysis and diffs per release; assign ownership and budget for significant growth.
- Verify tree shaking, deferred loading where appropriate, asset variants, image formats, font subsetting, native stripping, debug artifact exclusion, and package-level contributors.
- If Dart obfuscation is used, preserve exact symbol maps per artifact and verify crash deobfuscation and retention.
- Preserve Android mapping/native symbols, Apple dSYM, Windows PDB, macOS/Linux symbols, web source maps, and native plugin symbols with access controls.
- Do not claim obfuscation protects API secrets, authorization logic, encryption keys, business rules, or personal data.
- Review runtime strings, logs, error messages, manifest metadata, endpoints, feature flags, test credentials, certificates, and assets for unintended disclosure.
- Test symbol upload, crash decoding, source-map privacy, retention, access, incident availability, and artifact-to-symbol identity.

