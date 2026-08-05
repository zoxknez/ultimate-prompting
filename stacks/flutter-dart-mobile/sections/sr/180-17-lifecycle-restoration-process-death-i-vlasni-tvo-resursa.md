## 17. Lifecycle, restoration, process death i vlasništvo resursa

Pretpostavi da operativni sistem može suspendovati, odvojiti, ubiti, ponovo kreirati, promeniti veličinu ili obnoviti aplikaciju u nezgodnom trenutku.

- Mapiraj lifecycle aplikacije, view-a, rute, widget-a, engine-a, scene/prozora, isolate-a, servisa i plugin-a za svaku podržanu platformu.
- Proveri redosled inicijalizacije, spremnost zavisnosti, uklanjanje splash-a, obnovu sesije, otvaranje baze, migracije, remote config i first-frame ponašanje.
- Testiraj backgrounding, foregrounding, inactive/hidden/detached stanja, memory pressure, zaključavanje uređaja, prekid, promene dozvola i terminaciju procesa.
- Proveri obnovu navigacije, formi, draft-ova, playback-a, download-a, upload-a, paginacije, neposlatih akcija i conflict stanja bez izlaganja drugog naloga ili tenant-a.
- Dispose-uj controller-e, focus node-ove, animation controller-e, stream subscription-e, timer-e, port-ove, database watcher-e, plugin listener-e, texture-e, kamere, player-e i native handle-ove tačno jednom.
- Obradi hot restart i development-only ponašanje odvojeno od production lifecycle tvrdnji.
- Testiraj prekinutu migraciju, prekinut upis, prekinuto plaćanje, prekinut transfer fajla, prekinut update i obnovu nakon low-memory terminacije.
- Zahtevaj state restoration i process-death testove na stvarnim ili production-equivalent uređajima za kritične tokove.

