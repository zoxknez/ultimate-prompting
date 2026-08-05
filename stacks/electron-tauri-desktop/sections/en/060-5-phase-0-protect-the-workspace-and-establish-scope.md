## 5. Phase 0 - Protect The Workspace And Establish Scope

### 5.1 Pre-Change Snapshot

1. Record repository root, current branch, commit, remotes, submodules, worktrees, ignored/generated directories, package-manager state, Rust toolchain state, and uncommitted changes.
2. Record host operating system, architecture, shell, locale, time zone, file-system type, security software, and whether the environment is local, VM, CI, container, or remote builder.
3. Inventory existing installers, release artifacts, signing outputs, notarization logs, update manifests, store packages, and crash symbols before generating replacements.
4. Hash or otherwise identify every artifact used as audit evidence. Preserve timestamps and original filenames.
5. Identify directories that contain real user data, production secrets, signing keys, certificates, hardware credentials, browser profiles, or release-channel state; exclude them from destructive tests.
6. Create a narrow change plan and explicit stop conditions before editing.

### 5.2 Initial Command Log

```text
For every command record:
- exact command and arguments;
- working directory;
- environment variables that affect behavior, with secret values redacted;
- framework, Node, package-manager, Rust, Cargo, linker, compiler, packaging, and signing tool versions;
- platform and architecture;
- exit code;
- concise stdout/stderr summary;
- generated or modified files;
- evidence level and conclusion;
- reason if the command was not run.
```

