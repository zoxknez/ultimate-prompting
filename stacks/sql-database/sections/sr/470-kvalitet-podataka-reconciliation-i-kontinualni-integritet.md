## Kvalitet podataka, reconciliation i kontinualni integritet

Ispravna schema i uspesni upiti ne dokazuju istorijsku ispravnost podataka.

- Definisi data-quality pravila za opsege, reference, uniqueness, hronologiju, totale i state transition-e.
- Napravi ogranicene reconciliation upite koji mogu bezbedno da rade u produkciji ili na replikama.
- Prati odstupanja sa lineage-om, first-seen vremenom, pogodjenim scope-om, vlasnikom i repair statusom.
- Koristi repair skripte koje su pregledane, idempotentne, checkpointed, auditable i reverzibilne gde je moguce.
- Validiraj totale i invarijante nakon migracije, failover-a, restore-a, queue replay-a i incident recovery-ja.
- Alarmiraj na promene trenda, a ne samo na apsolutni broj nevalidnih redova.

