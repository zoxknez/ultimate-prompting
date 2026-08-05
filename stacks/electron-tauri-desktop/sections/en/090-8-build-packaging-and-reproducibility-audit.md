## 8. Build, Packaging, And Reproducibility Audit

### 8.1 Build Graph And Configuration

1. Map every build entry point, workspace filter, environment, feature flag, target, architecture, bundle variant, and platform-specific override.
2. Resolve the effective configuration after environment variables, CLI flags, generated files, merge rules, defaults, and conditional code are applied.
3. Compare development, test, staging, production, store, enterprise, portable, and update builds. Treat unexplained differences as risk.
4. Verify that development servers, debug menus, devtools, source-map servers, hot reload, test endpoints, mock data, verbose logging, and bypass flags cannot enter production artifacts unintentionally.
5. Verify deterministic versioning and build numbering across package manifests, Rust crates, executables, installers, stores, and update feeds.
6. Check locale, path, case sensitivity, time, network, CPU count, signing availability, and host-specific behavior that can make builds non-reproducible.
7. Record all generated configuration and compare it to the source template. Review generated diffs before release.
8. Build from a clean clone with network and credential access minimized. Explain every difference from the existing release artifact.

### 8.2 Package Content Inspection

1. List every file in the packaged application and installer. Classify executable code, resources, configuration, licenses, symbols, source maps, user templates, native libraries, sidecars, and unused files.
2. Search the final artifact for secrets, tokens, private URLs, test credentials, signing material, internal certificates, source repositories, absolute paths, usernames, and sensitive fixtures.
3. Verify that only intended native modules, crates, plugins, codecs, locales, and architectures are shipped.
4. Check file permissions, ownership, ACLs, executable bits, quarantine attributes, entitlements, capabilities, and installer-created directories.
5. Verify compression, archive extraction paths, symlink behavior, and unpacked files. Do not assume archive packaging prevents reading or modification.
6. Verify that runtime-writable content is outside signed/read-only application resources and cannot replace executable code on restart.
7. Compare package size and content against a known-good release. Explain significant additions, removals, or duplicate runtimes.
8. Scan the actual artifact with appropriate malware, reputation, package, and signature tools, recording false-positive handling without disabling controls globally.

