## 20. Faza P - Observability, Auditability I Incident Response

1. Trace-uj request kroz identity, policy, retrieval, model, tool, workflow, state i output granice.
2. Zabelezi verzije modela, prompta, retrieval-a, alata, policy-ja, dataset-a i deployment-a.
3. Koristi aktuelne OpenTelemetry GenAI konvencije ili eksplicitno dokumentovan ekvivalent gde je prikladno, uz postovanje njihovog stability status-a.
4. Ne loguj pune promptove, completion-e, retrieved dokumente, tool argumente ili memoriju po default-u kada mogu sadrzati osetljive podatke.
5. Implementiraj redaction, sampling, access control, retention i secure export za telemetry.
6. Loguj authorization i approval odluke odvojeno od model reasoning-a.
7. Nadgledaj injection signale, policy violation, neuobicajeno koriscenje alata, exfiltration pattern-e, token spike, loop, latenciju, greske i model ili retrieval drift.
8. Definisi alert-e, vlasnike, escalation, triage, containment, cuvanje dokaza, notification i post-incident review.
9. Testiraj kill switch-eve za modele, alate, retrieval, memory write i autonomne akcije.
10. Proveri backup, restore, replay, rollback i disaster-recovery procedure.
11. Odrzavaj runbook za kompromitovane promptove, poisoned corpus, procurele tajne, malicious MCP servere, provider incidente i nebezbedne model regresije.

