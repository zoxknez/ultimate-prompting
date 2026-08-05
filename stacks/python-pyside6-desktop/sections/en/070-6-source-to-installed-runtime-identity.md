## 6. Source-To-Installed-Runtime Identity

### 6.1 Audit Scope

1. Inventory repository roots, submodules, generated directories, build outputs, vendor folders, installer projects, update metadata, scripts, and ownership.
2. Record commit, dirty state, branch/tag, source archive hash, build host, CI run, environment lock, and every external input that can alter delivered bytes.
3. Distinguish developer interpreter, test interpreter, build interpreter, packaging interpreter, embedded interpreter, helper interpreter, and system Python.
4. Map source modules to generated code, bytecode, extension modules, resources, Qt plugins, executable, installer, update package, and installed files.
5. Record executable, package, installer, manifest, SBOM, signature, timestamp, and update metadata hashes.
6. Connect the installed process, loaded modules, Qt libraries, plugin paths, configuration, schema, feature flags, and telemetry release identity to the intended artifact.

### 6.2 Required Verification

1. Perform a clean environment resolve and build; compare dependency, generated-code, resource, and artifact manifests with CI and release records.
2. Inspect packaged and installed files, import origins, `sys.executable`, `sys.path`, `sys.prefix`, Qt library paths, plugin paths, and loaded native modules.
3. Verify that no writable search path, current directory, user plugin path, or stale file can shadow trusted Python or Qt components.
4. Launch the installed application on a clean machine or VM and record exact binary, command line, environment, working directory, libraries, and release identifiers.
5. Test update and rollback identity so the reported version, code, data schema, resources, and telemetry cannot disagree silently.

