## 13. Faza I - Agent Orkestracija I Ispravnost Workflow-a

1. Modeluj agenta kao state machine sa eksplicitnim stanjima, tranzicijama, vlasnistvom i failure handling-om.
2. Definisi maksimalne korake, wall time, tokene, cost, tool pozive, retry, recursion, subagente i paralelizam.
3. Implementiraj stop condition, loop detection, sprecavanje duplog rada, cancellation i ponasanje pri iscrpljenju budget-a.
4. Proveri da planner, executor, critic, router i subagent granice ne prosiruju ovlascenja.
5. Proveri da delegirani zadaci nose least-privilege identitet, tenant kontekst, budget-e i provenance.
6. Testiraj stale state, konfliktne paralelne akcije, duplicate event-e, out-of-order result, retry i partial completion.
7. Za dugotrajne ili spolja vidljive akcije zahtevaj durable workflow semantiku.
8. Razdvoji at-least-once delivery od exactly-once poslovnog efekta.
9. Obezbedi rollback ili compensating action za multi-step side effect-e.
10. Preferiraj deterministicke workflow-e za poznate procese i koristi modele samo gde su potrebni procena ili jezicke sposobnosti.
11. Proveri da zavrsni odgovor tacno odrazava zavrsene, neuspele, preskocene i pending akcije.

