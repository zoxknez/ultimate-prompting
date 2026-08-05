## Workflow popravke vođen dokazima

1. Zamrzni scope, zaštiti rad i podatke i uspostavi granicu dokaza.
2. Reprodukuj grešku ili dokaži prekršenu invarijantu najmanjim bezbednim scenarijem.
3. Identifikuj root cause kroz source, generisani kod, toolchain, zavisnost, konfiguraciju, podatke, runtime, platformu i operacije.
4. Dizajniraj najmanju bezbednu popravku i eksplicitno odbaci popravke koje samo kriju simptom, šire privilegije, uklanjaju validaciju, isključuju provere ili povećavaju kapacitet bez analize.
5. Dodaj regresioni test plus concurrency, failure, security, migration, compatibility ili recovery pokrivenost primerenu uzroku.
6. Izvrši fokusirane provere, zatim podržanu jezičku, target, tag/feature, integracionu, artifact, load, deployment i rollback matricu.
7. Pregledaj završni diff, dependency i lock promene, generisani izlaz, artefakte, telemetriju, preostali rizik, ownership i operativnu dokumentaciju.

