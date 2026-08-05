## Workflow popravke i verifikacije

1. Reprodukuj ili ustanovi nalaz najsnažnijim dostupnim dokazom i sačuvaj minimalni failing case.
2. Identifikuj root cause, pogođenu trust granicu, invarijantu, tip procesa, podatke, tenant-a, release i failure prozor.
3. Dizajniraj najmanju kompletnu popravku koja uklanja uzrok bez skrivanja simptoma ili slabljenja druge kontrole.
4. Dodaj determinističke regression, negative, concurrent, failure, migration ili recovery testove primerene riziku.
5. Ponovo pokreni ciljane provere, zatim relevantne framework, integration, security, load, migration i packaging suite-ove.
6. Izgradi produkcioni artifact iz clean checkout-a i proveri njegov digest, sadržaj, runtime kompatibilnost i release metadata.
7. Deploy-uj kroz namenjenu putanju sa canary ili staged guardrail-ima, kompletnom zamenom procesa i telemetry korelacijom.
8. Proveri user-visible ponašanje, invarijante, autorizaciju, tenant izolaciju, side effect-e, queue-ove, podatke, health i rollback uslove.
9. Ažuriraj zapis nalaza dokazom, residual risk-om, owner-om, operativnom akcijom, expiry-jem i finalnim statusom.

