## Posebni target overlay-i

### CLI, daemon i system service

- Proveri stdin/stdout/stderr ugovore, exit code-ove, obradu signala, detekciju terminala, non-interactive režim, prioritet konfiguracije, atomske upise fajla, lock fajlove, spuštanje privilegija, readiness za service manager, restart politiku i ownership logova.
- Obezbedi da skripte i automatizacija razlikuju validation, delimičan uspeh, retryable failure, permanent failure i prekinuto izvršavanje.

### WebAssembly, plugin i embedded target-i

- Proveri host import-e, capability model, limite linearne memorije, allocator i panic ponašanje, serialization granicu, browser ili WASI podršku, determinističke pretpostavke, sandbox escape površinu i pregovaranje verzije.
- Za plugin-e proveri ABI/API stabilnost, loading putanju, potpise, version kompatibilnost, izolaciju, ownership resursa, panic/crash containment, hot reload i opoziv.
- Za embedded ili ograničene target-e proveri dostupnost allocator-a, interrupt i concurrency model, no-std pretpostavke, watchdog, nestanak napajanja, habanje flash-a, atomskost persistent stanja, potpisivanje firmware-a, update recovery i hardware-in-the-loop testove.

