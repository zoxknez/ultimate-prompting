## Faza O - Execution planovi i reprezentativni workload-i

Koristi stvarne planove i realne distribucije podataka; nikada ne optimizuj samo iz teksta upita.

- Zabelezi parameterized i reprezentativne vrednosti, procene redova, stvarne redove, loop-ove, timing, buffer-e i wait-ove kada je bezbedno.
- Uporedi cold, warm, common, rare, empty, large-tenant i skewed slucajeve.
- Pregledaj join order, access path, sort, hash, spill, privremene strukture i paralelizam.
- Detektuj parameter sensitivity, nestabilnost plan cache-a i generic/custom plan efekte prepared statement-a.
- Meri aplikativnu end-to-end latenciju, a ne samo vreme izvrsavanja na serveru.
- Sacuvaj before/after planove i odbij regresije u kriticnim klasama upita.

