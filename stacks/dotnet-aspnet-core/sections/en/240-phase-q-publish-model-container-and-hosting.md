## Phase Q - Publish Model, Container, And Hosting

Determine: framework-dependent vs self-contained, single-file, trimmed, ReadyToRun, Native AOT, IIS, Windows service, systemd, container.

Trimming/AOT: reflection, DI scanning, JSON, model binding, plugins, EF provider, third-party compatibility. Do not suppress trimming warnings without evidence. Native AOT is not a universal JIT replacement.

Container: official .NET image, tag/digest, OS distro, Alpine/musl, ICU/globalization, non-root, ports, read-only FS, signal/shutdown, secrets in layers, SBOM, image scan. Multi-stage: restore layer with project metadata, locked restore, do not copy `.git` or credentials.

