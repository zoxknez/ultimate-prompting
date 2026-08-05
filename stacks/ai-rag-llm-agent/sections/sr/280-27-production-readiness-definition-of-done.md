## 27. Production Readiness Definition Of Done

Svaku primenjivu stavku oznaci kao `CONFIRMED`, `UNVERIFIED` ili `NOT_APPLICABLE` uz dokaz.

Sistem ne moze biti `ready` osim ako:

1. Workspace, kredencijali, podaci i produkcioni sistemi su bili zasticeni tokom audita.
2. Stvarna arhitektura, modeli, promptovi, retrieval, alati, MCP, memorija i deployment jedinice su popisani.
3. Identity i tenant context su sacuvani kroz ceo lanac.
4. Retrieval, alati, memorija i high-impact akcije sprovode deterministicku resource-level autorizaciju.
5. Nijedan primenjivi P0 nije otvoren.
6. P1 nalazi su popravljeni ili formalno contained sa vlasnikom, rokom, monitoring-om i recovery putem.
7. Kriticni pozitivni, negativni, adversarial, failure, retry i recovery testovi prolaze sa dokazom.
8. Eval dataset-i i pragovi su reprezentativni, verzionisani, reproducibilni i odobreni.
9. Model, prompt, retrieval, tool, policy i provider izmene imaju regression i rollback kontrole.
10. Cost, latencija, capacity, availability i budget limiti su izmereni i prihvatljivi.
11. Osetljivi podaci su zasticeni kroz promptove, providere, retrieval, memoriju, logove, traces, eval-e i export-e.
12. Observability, audit logovi, alert-i, kill switch-evi, incident runbook-i, backup, restore i rollback su testirani.
13. Primenjive pravne, regulatorne, consent, transparency, human-oversight i accessibility praznine su resene ili eksplicitno blokiraju release.
14. Residual risk je eksplicitan i prihvacen od ovlascenog vlasnika.
15. Nijedna materijalna oblast nije proglasena bezbednom samo zato sto nije testirana.

Ako je bilo koja primenjiva blokirajuca stavka nepotpuna, napisi:

> Not fully production-ready.

Zatim navedi tacne blokirajuce uslove.

