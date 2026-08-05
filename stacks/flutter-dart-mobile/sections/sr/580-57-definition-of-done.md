## 57. Definition of Done

1. Ovlašćeni scope je potpuno povezan sa dokazima, nalazima, izmenama, testovima, artefaktima, rollout-om i oporavkom.
2. Nijedna materijalna tvrdnja se ne oslanja samo na dokumentaciju, debug režim, emulator/simulator ponašanje, analyzer uspeh ili nepotpisan artefakt.
3. Svaki potvrđen problem ima root cause, minimalnu remedijaciju, regresionu pokrivenost, platformski scope, vlasnika i dokaz provere.
4. Svaki nerešen problem navodi granicu dokaza, bloker, rizik, potrebnog vlasnika i sledeći tačan korak provere.
5. Svi primenljivi release artefakti su reproduktivni, pregledani, potpisani, instalabilni, dijagnostikabilni i povezani sa tačnim source-om i simbolima.
6. Kritični tokovi prolaze normalne, nevalidne, neovlašćene, offline, duplicate, concurrent, interrupted, upgrade, rollback, restore i accessibility scenarije.
7. Production telemetrija i support signali dokazuju da release zadovoljava odobrene gate-ove ili release ostaje blokiran.
8. P0/P1 nalazi su zatvoreni ili formalno prihvaćeni sa istekom; nijedan skriveni bloker nije pretvoren u zeleni status.
9. Rollback, forward-fix, backup restore, key/store recovery i trusted rebuild imaju imenovane vlasnike i testirane procedure.
10. Završni izveštaj je interno konzistentan, dovoljno sažet za izvršenje, dovoljno detaljan za reprodukciju i iskren o neizvesnosti.

