## 6. Faza B - Arhitektura, Data Flow I Trust Boundaries

1. Nacrtaj stvarni request i state flow, ukljucujuci asinhrone i retry putanje.
2. Oznaci svaki trust boundary, data store, spoljnu zavisnost i prelaz privilegija.
3. Klasifikuj ulaze kao trusted, authenticated-but-untrusted, third-party, model-generated, retrieved ili operator-controlled.
4. Prati tenant i user identitet kroz ceo lanac, ukljucujuci queue-ove, cache, traces, tool pozive i background job-ove.
5. Identifikuj gde se kontekst spaja, skracuje, sumira, kesira ili cuva.
6. Razdvoji control-plane i data-plane funkcije.
7. Dokazi gde se izvrsavaju deterministicka validacija, autorizacija, policy enforcement i output encoding.
8. Oznaci svaku granicu koja se oslanja samo na poslusnost modela.

