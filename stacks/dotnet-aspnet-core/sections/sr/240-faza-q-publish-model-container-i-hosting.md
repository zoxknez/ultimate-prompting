## Faza Q - Publish Model, Container I Hosting

Utvrdi: framework-dependent vs self-contained, single-file, trimmed, ReadyToRun, Native AOT, IIS, Windows service, systemd, container.

Trimming/AOT: reflection, DI scanning, JSON, model binding, plugins, EF provider, third-party kompatibilnost. Ne suppression-uj trimming warning bez dokaza. Native AOT nije univerzalna zamena za JIT.

Container: zvanicni .NET image, tag/digest, OS distro, Alpine/musl, ICU/globalization, non-root, ports, read-only FS, signal/shutdown, tajne u layeru, SBOM, image scan. Multi-stage: restore layer sa project metadata, locked restore, ne kopiraj `.git` ni credentials.

