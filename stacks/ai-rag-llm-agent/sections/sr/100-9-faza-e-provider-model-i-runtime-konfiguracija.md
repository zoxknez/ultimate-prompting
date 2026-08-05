## 9. Faza E - Provider, Model I Runtime Konfiguracija

1. Utvrdi stvarne provider endpoint-e, modele, alias-e, verzije, regione i feature flag-ove u svakom okruzenju.
2. Proveri lifecycle, deprecation, kompatibilnost, ogranicenja model card-a ili system card-a i provider-specific safety smernice iz primarnih izvora.
3. Proveri timeout-e, retry, backoff, rate limit-e, concurrency, kvote, maksimalni output, stop ponasanje, cancellation i mapiranje gresaka.
4. Proveri da deterministicki poslovi ne zavise od nepotrebnih model poziva.
5. Proveri da model routing ne moze precutno sniziti security, privacy, quality, context, tool support ili residency zahteve.
6. Proveri da je fallback ponasanje eksplicitno, vidljivo, testirano i kompatibilno sa policy-jem.
7. Testiraj malformed response, refusal, empty response, partial stream, duplicate event, provider outage i quota exhaustion.
8. Proveri da structured output koristi strict schema gde je prikladno i da se i dalje validira server-side.
9. Proveri da se model-generated confidence ne tretira kao kalibrisana verovatnoca bez dokaza.

