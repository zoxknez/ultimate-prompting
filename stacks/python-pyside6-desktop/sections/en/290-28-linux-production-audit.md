## 28. Linux Production Audit

### 28.1 Audit Scope

1. Review supported distributions, glibc/musl baseline, x86_64/ARM64, desktop environments, Wayland/X11, graphics drivers, portals, and system library assumptions.
2. Inspect ELF architecture, interpreter, RPATH/RUNPATH, bundled/shared libraries, symbol versions, Qt plugins, platform themes, codecs, and license obligations.
3. Assess AppImage, Flatpak, Snap, deb, rpm, tarball, distribution repository, system package, and portable deployment behavior.
4. Review filesystem permissions, XDG paths, Secret Service/KWallet, D-Bus, Unix sockets, udev rules, systemd units, polkit, sandbox permissions, and multi-user isolation.
5. Test Wayland and X11, multiple desktop environments, fractional scaling, remote sessions, screen lock, sleep/resume, accessibility, input methods, and headless failure.
6. Define repository signing, package updates, delta behavior, rollback, dependency removal, uninstall, and retained data.

### 28.2 Required Verification

1. Run dependency and symbol inspection on the final artifact and launch on the minimum supported clean distribution images.
2. Test missing optional libraries, old drivers, Wayland/X11 switching, portal denial, sandbox restrictions, and read-only or noexec locations.
3. Verify package/repository signatures, update metadata, architecture mapping, downgrade behavior, and cross-package-manager conflicts.
4. Exercise standard-user use, another user, locked secret store, system sleep, display changes, screen readers, locale, and IME.
5. Confirm uninstall removes integrations and helpers without deleting user data outside documented policy.

