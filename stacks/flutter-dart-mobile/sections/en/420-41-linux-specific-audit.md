## 41. Linux-Specific Audit

Define and prove the supported distribution, desktop, packaging, sandbox, and library matrix.

- Audit compiler, CMake/Ninja, GTK, glibc and system libraries, plugins, generated registrant, dynamic linkage, rpaths, architecture, and reproducible build environment.
- Declare tested distributions, versions, desktop environments, display servers, architectures, package formats, sandbox/store runtimes, and support policy.
- Verify desktop file, MIME/protocol handlers, icons, AppStream metadata, single-instance behavior, DBus, portals, notifications, keyring, and file chooser.
- Audit package signature, repository trust, update path, dependency resolution, bundled versus system libraries, permissions, sandbox interfaces, and rollback.
- Test X11 and Wayland where claimed, HiDPI, multiple monitors, keyboard layouts, IME, accessibility stack, screen readers, clipboard, drag/drop, suspend/resume, and session restart.
- Audit filesystem permissions, XDG paths, temporary files, symlinks, removable media, keyring unavailability, headless/remote sessions, and enterprise restrictions.
- Verify crash symbols, core dump privacy, logs, package metadata, license notices, uninstall cleanup, and user-data preservation.
- Test clean/minimal environments, supported old/new distributions, offline launch, missing optional library, restricted user, low disk, update, rollback, and restore.

