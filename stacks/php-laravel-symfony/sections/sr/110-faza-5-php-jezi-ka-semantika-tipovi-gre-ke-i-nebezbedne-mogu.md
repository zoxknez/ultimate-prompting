## Faza 5 - PHP jezička semantika, tipovi, greške i nebezbedne mogućnosti

### Cilj

Identifikuj jezičke correctness i compatibility rizike koje uspešan syntax check ne može da dokaže.

### Zahtevi audita

- Audituj strict types granice, scalar coercion, union i intersection tipove, nullable vrednosti, enum-e, readonly stanje, property hook-ove, magic metode i dynamic properties.
- Pregledaj equality, array-key coercion, numeric stringove, integer overflow, floating-point novac, decimale, timezone, DST, locale, Unicode i serialization semantiku.
- Prati exception-e, `Throwable`, error handler-e, shutdown handler-e, warning-e pretvorene u exception-e, fatal error-e, deprecation-e i partial-response ponašanje.
- Pregledaj `eval`, dynamic include, variable variables, reflection, atribute, closure-e, generator-e, fiber-e, weak reference-e, FFI i extension API-je.
- Audituj `serialize` i `unserialize`, object injection, allowed classes, magic metode, Phar metadata i format kompatibilnost.
- Koristi PHPStan ili Psalm, coding standards, mutation ili property testing kada je opravdano, tretirajući output alata kao dokaz, a ne kao istinu.

### Obavezni dokazi

- Compatibility matrica za ciljane PHP linije i kritične ekstenzije.
- Static-analysis baseline sa suppression-ima, vlasnicima, istekom i reachability pregledom.
- Regresioni testovi za svaki materijalni coercion, error, serialization, time, money ili compatibility rizik.

### Kriterijumi prihvatanja

- Nijedna kritična invarijanta ne zavisi od nedokumentovanog coercion-a, magic ponašanja ili version-specific undefined ponašanja.
- Deprecation-i i compatibility blocker-i imaju vlasnike, testove i datume migracije.

