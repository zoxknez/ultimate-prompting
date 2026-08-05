## Repair I Verification Workflow

1. Registruj nalaz sa dokazom i eksplicitnom invarijantom.
2. Reprodukuj najmanju failure putanju i sacuvaj komandu, input i rezultat.
3. Identifikuj autoritativni sloj koji mora da primeni invarijantu.
4. Dizajniraj najmanju reverzibilnu popravku i navedi odbacene alternative sa razlozima.
5. Dodaj ciljani regression test pre ili zajedno sa popravkom gde je izvodljivo.
6. Pokreni uske testove, zatim pogodjene integration, contract, security, concurrency, load i production-build provere.
7. Pregledaj finalni diff, lockfile, generated output, artefakte, migracije i konfiguraciju radi nenamernih promena.
8. Definisi rollout guardrail-e, abort kriterijume, rollback ili forward repair, monitoring i residual risk.
9. Ne zatvaraj nalaz dok evidence i acceptance kriterijumi nisu ispunjeni.

