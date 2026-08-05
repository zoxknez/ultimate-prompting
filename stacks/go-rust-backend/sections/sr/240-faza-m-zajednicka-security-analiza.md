## Faza M - Zajednicka Security Analiza

Trust granice: public API, internal API, admin, worker, DB, broker, filesystem, cloud metadata, FFI.

AuthN/AuthZ: token/session validacija, object-level authorization, tenant isolation, service-to-service auth. Testiraj BOLA/IDOR.

Input: injection (SQL/command/path), SSRF, deserialization bomb, path traversal, zip-slip, XSS ako ima HTML, header injection.

Command execution: allowlist, bez shell-a gde je moguce, env scrubbing.

Filesystem: root confinement, permissions, symlink, temp file.

TLS/crypto: verifikacija lanaca, min version, cipher, certificate pin gde treba, key storage, zabranjeno iskljucivanje TLS verify u production putanji.

Tajne: ne u source/log/image/artefakt; rotacija; incident ako su kompromitovane (bez prikazivanja pune vrednosti).

Debug: pprof, metrics, admin, reflection - ne javno bez zastite.

