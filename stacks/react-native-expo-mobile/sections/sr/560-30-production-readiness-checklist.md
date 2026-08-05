## 30. Production readiness checklist
- [ ] Autorizacija, opseg, tvrdnje o podrsci i evidence ceiling su zabelezeni.
- [ ] Source-to-runtime identitet je potpun za svaki production artefakt i OTA update.
- [ ] Toolchain, dependency grafovi, generisani projekti i native projekti su reproducibilni i pregledani.
- [ ] New Architecture, Codegen, native modul, Fabric, JSI, ABI i memory granice su verifikovane.
- [ ] Kriticni tokovi, invarijante, autorizacija, tenant izolacija, idempotentnost i reconciliation prolaze.
- [ ] Storage, offline, migracija, backup, restore, promena naloga i ponasanje brisanja prolaze.
- [ ] Mrezni, realtime, background, push, permission, device, file, media i WebView ugovori prolaze.
- [ ] Android release build, pregled artefakta, signing, instalacija, upgrade, uredjaj, performance, accessibility i recovery prolaze.
- [ ] Apple archive, signing, privacy, instalacija, upgrade, uredjaj, performance, accessibility i recovery prolaze.
- [ ] EAS build profili, kredencijali, okruzenje, update runtime, code signing, kanali i rollout su verifikovani.
- [ ] Crash, ANR, hang, source-map, native-symbol, SLI, alert, dashboard i runbook spremnost prolaze.
- [ ] CI/CD trust, SBOM, provenance, immutable promocija artefakta, store submission i approval gate prolaze.
- [ ] Staged rollout, kvantitativni abort kriterijumi, OTA rollback, native rollback, forward fix i kill switch su izvrseni.
- [ ] Izolovani restore, RPO, RTO, data reconciliation, incident containment, opoziv kredencijala i trusted rebuild su izvrseni.
- [ ] Svi P0 i P1 nalazi su zatvoreni ili je odluka NOT_READY ili INCIDENT.
- [ ] Svaki prihvaceni P2 ili P3 rizik ima vlasnika, rok, kompenzacionu kontrolu, monitoring i datum sledece verifikacije.

