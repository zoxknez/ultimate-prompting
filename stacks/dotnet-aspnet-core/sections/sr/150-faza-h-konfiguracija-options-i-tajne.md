## Faza H - Konfiguracija, Options I Tajne

Validiraj options pri startupu. Servis mora bezbedno pasti kada kriticna konfiguracija ili tajna nedostaje, ne pri prvom produkcionom zahtevu.

Proveri: configuration provider prioritet, environment naming, User Secrets vs deployment secret store, secret rotaciju, Data Protection key persistence, connection stringove, `.env`, CI logove/artefakte, container layere, fixtures.

Tajne ne smeju biti u source-u, test fixture-u, image layeru, logu, exceptionu, health detalju niti CI artefaktu. Ako pronadjes kompromitovanu tajnu: oznaci incident, identifikuj scope, preporuci rotaciju, proveri Git istoriju - uklanjanje iz poslednjeg commita nije resenje.

