## 6. Source-To-Installed-Runtime Identity Chain

Do not assume that the repository, CI artifact, uploaded package, downloaded installer, installed application, running process, and update payload are the same thing. Prove the chain or explicitly identify the break.

| Stage | Required evidence | Question |
| --- | --- | --- |
| Source identity | Commit, tag, dirty state, submodules, generated source, lock files, build inputs | Can another engineer reproduce exactly which source was used? |
| Resolved graph | npm/pnpm/yarn/Bun lock, Cargo.lock, native dependencies, plugins, tool versions | Does the resolved graph match policy and the claimed release? |
| Build identity | Builder image/host, environment, flags, feature sets, target triple, generated files | Is the build deterministic enough to explain artifact differences? |
| Package identity | App ID/bundle ID, product name, version, build number, channel, package type, architecture | Can the package be tied to the source and intended channel? |
| Integrity identity | Hashes, ASAR integrity, embedded resources, SBOM, provenance, signature, timestamp, notarization | Can modification or substitution be detected? |
| Distribution identity | Release record, store listing, CDN object, update manifest, feed response | Is the user receiving the reviewed artifact? |
| Installed identity | Install path, package manager/store registration, binary signature, resources, permissions | Does installed state match the reviewed artifact? |
| Runtime identity | Executable path, process tree, loaded modules/libraries, WebView/runtime versions, channel, profile | Is the running process the expected installed release? |

### 6.1 Required Identity Checks

1. Compare source version declarations with generated package metadata, executable metadata, installer metadata, store metadata, and update feed metadata.
2. Verify application ID, bundle identifier, executable name, publisher identity, protocol scheme, file associations, data directory, keychain/credential namespace, and update channel continuity.
3. Verify that CI promotes an immutable artifact instead of rebuilding independently for test, signing, staging, and release.
4. Verify that symbols, source maps, dSYM/PDB/debug files, SBOM, provenance, and release notes correspond to the exact shipped artifact.
5. Inspect the installed application, not only the unpacked staging directory.
6. Verify runtime-loaded native libraries, sidecars, and system WebView/runtime components where they affect behavior.
7. Document every unsupported identity link as a release blocker or explicit residual risk.

