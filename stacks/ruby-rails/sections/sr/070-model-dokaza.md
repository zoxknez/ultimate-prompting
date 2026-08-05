## Model Dokaza

| Nivo | Znacenje | Dozvoljen zakljucak |
| --- | --- | --- |
| E0 | Pretpostavka, secanje ili nedokumentovana tvrdnja. | Bez zatvaranja nalaza i bez readiness tvrdnje. |
| E1 | Pregled source-a ili konfiguracije. | Samo namera implementacije. |
| E2 | Staticka alatka, dependency, schema ili build analiza. | Potencijalni problem ili compatibility dokaz. |
| E3 | Reproduktivno lokalno ili CI izvrsavanje u deklarisanom okruzenju. | Ponasanje samo u tom okruzenju. |
| E4 | Production-like release artefakt, realni podaci, concurrency i failure testiranje. | Jak release dokaz sa navedenim ogranicenjima. |
| E5 | Posmatrano production ponasanje, kontrolisani rollout, telemetry, rollback ili izolovani restore. | Production tvrdnja u posmatranom scope-u. |

