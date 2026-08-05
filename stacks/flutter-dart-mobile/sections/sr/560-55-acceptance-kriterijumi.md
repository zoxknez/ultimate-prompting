## 55. Acceptance kriterijumi

- Svaka production-relevant tvrdnja ima status, nivo dokaza, scope i eksplicitnu neizvesnost.
- Source, dependency, generisani izlaz, native host, artifact, signing, installation, runtime, telemetry i rollback identiteti su usklađeni.
- Sve kritične poslovne invarijante i serverska authorization pravila imaju pozitivne, negativne, duplicate, concurrent, interrupted i recovery testove.
- Svaka deklarisana platforma ima eksplicitnu support matricu, release build, artifact inspection, install/launch dokaz, testove kritičnih tokova, accessibility pokrivenost, telemetriju i recovery putanju.
- Nijedna tajna se ne oslanja na client confidentiality, nijedna privilegovana akcija samo na UI provere i nijedan osetljiv podatak ne prelazi account ili tenant granice.
- Lifecycle, cancellation, vlasništvo stream-a, isolate/background ponašanje, process death, restoration i cleanup resursa dokazani su za kritične tokove.
- Storage migracije, offline queue-evi, rešavanje konflikata, logout/promena naloga, backup restore, upgrade, rollback i incident recovery čuvaju invarijante.
- Budžeti performansi, veličine, memorije, baterije, mreže, diska, crash-a i accessibility-ja izmereni su na reprezentativnim ciljevima i gate-ovani u isporuci.
- Potpisivanje, provenance, SBOM, simboli, source map-e, store/distribution metapodaci, staged rollout, abort kriterijumi i rollback/forward-fix procedure su provereni.
- Svi P0/P1 nalazi su remedijovani ili formalno prihvaćeni od ovlašćenog vlasnika sa kompenzacionim kontrolama, istekom i monitoring-om.

