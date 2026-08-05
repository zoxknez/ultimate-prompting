## 1. Current Research Baseline - Re-Check Before Every Audit

This baseline reflects primary-source information available on 5 August 2026. It is a starting point only. Re-check current releases, support windows, Python ABI, wheel availability, Qt platform requirements, packaging-tool support, operating-system policies, security advisories, and distribution rules before recommending or changing anything.

| Area | Baseline on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| Python stable | Python 3.14.7 is the current stable bugfix release on 5 August 2026; Python 3.15 remains pre-release. | Exact interpreter patch, vendor, architecture, ABI, build flags, free-threaded status, JIT status, extension compatibility, and support policy. |
| Python execution modes | Free-threaded Python is officially supported but optional; experimental JIT binaries exist on some platforms and are not a default production recommendation. | Whether the application and every native dependency support the selected GIL/free-threaded/JIT mode under realistic concurrency and packaging. |
| PySide6 stable | PySide6 6.11.1 is the current stable package at the baseline and declares CPython 3.10 through 3.14 support. | Exact PySide6, shiboken6, Qt libraries, wheel tags, bundled plugins, licensing, packaging support, and OS deployment requirements. |
| Qt for Python | Qt for Python follows the Qt 6 release family and ships platform-specific wheels and deployment tooling. | Project-supported Qt line, exact patch, module availability, platform plugin deployment, graphics backend, WebEngine support, and compatibility matrix. |
| Packaging | PyInstaller, Nuitka, Briefcase, pyside6-deploy, cx_Freeze, installers, and stores have independent support and security behavior. | Exact tool and plugin versions, hooks, hidden imports, native libraries, reproducibility, signing order, updater model, and clean-machine installation. |

