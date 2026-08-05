## Zabranjene precice

- Ne dodaj indekse po intuiciji i ne uklanjaj ih samo zato sto brojac kaze da nisu korisceni.
- Ne pokreci `VACUUM FULL`, `OPTIMIZE TABLE`, rebuild, reindex, purge ili shrink kao genericku popravku.
- Ne iskljucuj foreign key-eve, check-ove, row security, strict mode, trajnost ili TLS da bi migracija prosla.
- Ne brisi istoriju migracija, ne menjaj primenjene migracije i ne forsiraj checksum-e bez root-cause analize.
- Ne tretiraj ORM modele, schema dump, repliku, snapshot ili dashboard kao jedinu istinu.
- Ne izvrsavaj produkcioni DDL iz interaktivnog shell-a bez pregledanog artefakta, timeout-a, monitoringa i abort plana.
- Ne tvrdi zero downtime, exactly once, no data loss ili recovery readiness bez failure dokaza.
- Ne kopiraj samo aktivni SQLite glavni fajl u WAL rezimu i ne nazivaj ga proverenim backup-om.

