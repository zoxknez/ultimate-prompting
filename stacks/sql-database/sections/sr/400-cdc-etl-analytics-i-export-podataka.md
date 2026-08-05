## CDC, ETL, analytics i export podataka

- Mapiraj snapshot, log poziciju, schema verziju, ordering, duplicate i delete semantiku za svaki pipeline.
- Testiraj schema evolution, backfill overlap, replay, consumer lag i poison record-e.
- Proveri da se analytics ili search store-ovi ne tretiraju kao autoritativni za write ili autorizaciju.
- Zastiti export-e autorizacijom, tenant scope-om, row limitima, enkripcijom, expiry-jem i auditom.
- Usaglasi source i destination broj redova, agregate, checksum-e gde imaju smisla i kriticne invarijante.
- Definisi cutover i rollback ponasanje kada je pipeline deo migracije.

