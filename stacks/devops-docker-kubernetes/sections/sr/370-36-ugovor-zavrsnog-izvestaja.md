## 36. Ugovor zavrsnog izvestaja

### 36.1 Obavezni redosled izvestaja

1. Naslov, datum audita, verzija, rezim, auditori, opseg, autorizacija i ogranicenje nivoa dokaza.
2. Izvrsni verdict i najvaznije poslovne, bezbednosne, reliability i recovery odluke.
3. Pregled sistema, trust boundary-ja, okruzenja, identiteta, data flow-a i vlasnistva.
4. Procena integriteta od izvora do produkcije i live drift-a.
5. Nalazi poređani po severity-ju, zatim verovatnoci eksploatacije ili otkaza i poslovnom uticaju.
6. Implementirane izmene sa diff-ovima, odobrenjima, verifikacijom, posmatranjem, rollback-om i rezidualnim rizikom.
7. Matrica testova i dokaza ukljucujuci blokirane, neuspesne, nepokrenute i neprimenljive provere.
8. Rezimei bezbednosti, supply-chain-a, pouzdanosti, performansi, observability-ja, backup-a, restore-a, DR-a, incidenta i troska.
9. Prioritizovan remediation roadmap sa vlasnicima, zavisnostima, trudom, smanjenjem rizika, rollout-om i verifikacijom.
10. Prihvaceni rizici, nerazresene pretpostavke, praznine dokaza, rokovi odluka i obavezan follow-up.
11. Zavrsni verdict i tacni uslovi potrebni da se promeni.

### 36.2 Pravila verdict-a

| Verdict | Obavezno znacenje |
| --- | --- |
| `ready` | Nema nerazresenog P0 ili P1 nalaza, kriticne putanje su potvrđene, identitet od izvora do produkcije dokazan, recovery demonstriran, vlasnistvo uspostavljeno i nivo dokaza dovoljan. |
| `ready-with-conditions` | Nema neprihvatljivog neposrednog blokera, ali ostaju eksplicitni ograniceni uslovi, vlasnici, rokovi, monitoring i rollback. |
| `not-ready` | Bilo koji nerazresen P0, neprihvatljiv P1, nedostajuci kriticni restore, neproverljiv produkcioni artefakt, nekontrolisana privileged putanja, nebezbedna release putanja ili nedovoljan dokaz za materijalnu tvrdnju. |

### 36.3 Masinski citljiv rezime

```json
{
  "audit_id": "...",
  "baseline_date": "2026-08-05",
  "scope": ["..."],
  "verdict": "ready | ready-with-conditions | not-ready",
  "evidence_ceiling": "...",
  "findings": {"P0": 0, "P1": 0, "P2": 0, "P3": 0},
  "coverage": {"passed": 0, "failed": 0, "blocked": 0, "not_applicable": 0},
  "production_artifact_verified": false,
  "restore_verified": false,
  "open_conditions": ["..."],
  "accepted_risks": ["..."],
  "next_decision_date": "YYYY-MM-DD"
}
```

