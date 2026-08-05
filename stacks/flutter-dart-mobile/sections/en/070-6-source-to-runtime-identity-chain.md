## 6. Source-To-Runtime Identity Chain

Prove which source and dependencies produced the exact artifact that users execute.

- Record repository URL, commit, branch or tag, dirty state, submodules, Git LFS objects, patches, and generated files.
- Resolve Flutter SDK channel, version, engine revision, Dart version, package manager behavior, and platform toolchains in local and CI environments.
- Capture `pubspec.yaml`, `pubspec.lock`, dependency overrides, workspace configuration, path/git dependencies, plugin platform implementations, and native package locks.
- Trace build-time configuration, `--dart-define`, environment files, flavor, target entrypoint, code-generation options, native build settings, and signing identity.
- Record immutable hashes or IDs for produced APK/AAB, IPA/archive, web bundle, MSIX/installer, app bundle, Linux package, symbols, source maps, and SBOM.
- Verify package name, bundle identifier, application ID, version, build number, channel, signing certificate, provisioning profile, entitlements, and publisher identity.
- Install or deploy the exact artifact and prove runtime version, flavor, backend environment, feature configuration, and loaded native/plugin code.
- Detect rebuilds, mutable artifacts, store reprocessing, environment drift, stale generated files, wrong symbols, wrong source maps, and wrong backend targeting.
- Do not accept a release verdict until source, artifact, signing, installation, runtime, telemetry, and recovery identities are reconciled or explicitly unresolved.

