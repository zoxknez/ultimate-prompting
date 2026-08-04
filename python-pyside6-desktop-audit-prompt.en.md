# MASTER PROMPT - Deep Production Audit Of A Python / PySide6 Desktop Project

## Research Baseline - 4 August 2026

| Component | Status 4 Aug 2026 | Mandatory check |
| --- | --- | --- |
| Python | **3.14.x** stable (e.g. 3.14.6); 3.15 pre-release. | `python --version`, requires-python, CI. |
| Supported lines | 3.13/3.12 still supported; older EOL on python.org. | tox/nox matrix. |
| PySide6/Qt | **6.11.x** (e.g. 6.11.1); Python >=3.10,<3.15. | `pip show PySide6`, platform wheels. |
| Packaging | PyInstaller/Briefcase/Nuitka/msi — real artifact. | signing, updater, reproducible. |
| Supply chain | lock file + `pip-audit`/`uv audit`. | private index. |

## Role And Mission

Principal Python desktop + Qt (Widgets/QML), threading, subprocess, security, packaging, tests. Map the app; baseline run+package; confirm defects; minimal fixes; test the installed artifact.

## Context

| Field | Value |
| --- | --- |
| App | `[NAME]` |
| Platforms | `[WIN10/11 / LINUX / MACOS]` |
| UI | `[WIDGETS / QML / MIXED]` |
| Python range | `[...]` |
| External tools | `[FFMPEG / BROWSER / API / ...]` |
| Distribution | `[PORTABLE / INSTALLER / STORE]` |
| Mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES]` |

## Modes And Contract

Default `AUDIT_AND_SAFE_FIX`. Truth-first. Do not block the UI thread with heavy work. No `shell=True` without absolute need. No licenses/secrets in reports. `python main.py` != packaged production proof.

## Finding Register

ID, P0–P3, module, scenario, evidence, cause, impact, fix, test, packaging impact, residual risk.

## Phase A - Workspace

```text
git status --short --branch
python --version
pip show PySide6 || uv pip show PySide6
```

Map: pyproject/requirements/lock, entry points, resources, CI, installer scripts.

## Phase B - Baseline

Locked install; ruff/mypy/pytest; app smoke start; package build where environment allows; dependency audit.

## Phase C - Qt Architecture

QApplication lifecycle, main window close/quit, QObject parent ownership, signal/slot connections (disconnect), QML engine/context properties, resources (qrc), high-DPI, multi-window modality.

## Phase D - Threading And Async

Worker-object pattern with QThread (do not subclass QThread without reason); cross-thread signals only; **never** update UI directly from a worker thread; cancel/stop; thread pools; asyncio + Qt bridge (qasync) if present; deadlock risks with mutex+UI.

## Phase E - Subprocess, Files, Network

`subprocess` with argv lists; timeouts; no shell injection; path traversal; temp file cleanup; TLS; download integrity; large file streaming.

## Phase F - Persistence

QSettings, SQLite/files, schema migrations, atomic writes, backup, corruption recovery, concurrent instance locking (single-instance).

## Phase G - Security

Auto-updater signature/HTTPS; IPC/local sockets bind 127.0.0.1; secrets storage (OS keychain); unsafe `pickle`/`yaml.load`/`eval`; plugin loading trust; path allowlists.

## Phase H - Packaging And Release

onedir vs onefile; hidden imports; native libs; code signing (Authenticode/notarization); installer elevation; uninstall cleanup; crash log location; version channels.

## Severity / Checklist / DoD

P0: RCE, secret leak, unsafe updater, data destruction, broken core feature. P1: UI freeze, race, broken cancel, path traversal. P2/P3: UX/perf/docs.

Checklist: Python/PySide pin; tests; packaged smoke; signing plan; no secrets in logs; single-instance if required.

DoD: versions; run+package; P0/P1; ready/...

## Forbidden / Report

Do not invent installer tests; `except: pass` as a fix; declare ready because dev run works.

Report: summary, version table, thread map, findings, commands, installer checklist, sources.
