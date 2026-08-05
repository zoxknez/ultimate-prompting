## Model dokaza

| Nivo | Znacenje | Dozvoljen zakljucak |
| --- | --- | --- |
| E0 | Pretpostavka, secanje, tvrdnja dobavljaca ili nedokumentovana izjava. | Bez zatvaranja nalaza i bez readiness tvrdnje. |
| E1 | Inspekcija schema-e, source-a, migracije ili konfiguracije. | Samo namera i moguci rizik. |
| E2 | Catalog, staticka analiza, dependency, plan ili backup metadata. | Jaci dokaz, ali ne i runtime dokaz. |
| E3 | Ponovljiv test na deklarisanom engine-u i dataset-u. | Ponasanje u tom deklarisanom okruzenju. |
| E4 | Production-like podaci, concurrency, migration, failover ili restore test. | Jak release dokaz sa navedenim ogranicenjima. |
| E5 | Posmatran kontrolisan produkcioni rollout, failover, reconciliation ili izolovani restore. | Produkcioni zakljucak u posmatranom scope-u. |

