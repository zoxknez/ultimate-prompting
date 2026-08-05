## 8. Python runtime, ABI, GIL, free-threaded režim i JIT

### 8.1 Obim audita

1. Zabeleži tačnu CPython verziju, vendor, build flag-ove, arhitekturu, debug/release status, ABI tag, `SOABI`, Unicode konfiguraciju, OpenSSL i platformski runtime.
2. Identifikuj da li build koristi tradicionalni GIL, free-threaded režim, eksperimentalni JIT, debug allocator, sanitizer-e ili prilagođene interpreter patch-eve.
3. Mapiraj svaku C/C++/Rust ekstenziju, limited-API/abi3 wheel, ctypes/cffi binding, Shiboken wrapper i native biblioteku na podržane Python i platformske ABI-je.
4. Pregledaj vlasništvo referenci, finalizer-e, weak reference-e, cyclic GC, shutdown redosled, exception hook-ove, import hook-ove i signal handling.
5. Proceni subinterpreter-e, embedded Python, isolated mode, virtual environment-e, zip import-e, frozen module i user-site ponašanje ako je primenljivo.
6. Razlikuj thread safety na nivou jezika od safety-ja ekstenzija, Qt-a, baze, fajlova i poslovne konkurentnosti.

### 8.2 Obavezna verifikacija

1. Pokreni zapakovanu aplikaciju pod tačnim podržanim interpreter režimom i vežbaj native ekstenzije, shutdown, izuzetke i konkurentnost.
2. Za free-threaded režim zahtevaj eksplicitne compatibility dokaze za PySide6, svaku native zavisnost, globalno stanje, callback-ove, životne vekove referenci i third-party biblioteke.
3. Za JIT ili non-default build-ove uporedi ispravnost, startup, memoriju, dijagnostiku, pakovanje, crash ponašanje i rollback sa podržanim baseline-om.
4. Koristi debug build-ove, faulthandler, tracemalloc, sanitizer-e ili platformske debugger-e gde je prikladno za istragu native crash-eva i lifetime defekata.
5. Odbaci upgrade interpretera kada potrebni wheel paketi, Qt binding-i, packaging alati, native biblioteke ili OS ciljevi nisu podržani.

