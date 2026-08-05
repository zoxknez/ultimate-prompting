## 6. Autorizacija, opseg i cuvanje dokaza

**Cilj:** Uspostavi bezbednu granicu audita pre dodirivanja bilo kog sistema.

### 6.1 Obavezne provere

1. Identifikuj pravnog vlasnika, tehnickog vlasnika, on-call vlasnika, odobravaoca i komunikacioni kanal za svaki produkcioni opseg.
2. Zabelezi naloge, subscription-e, projekte, regione, klastere, namespace-ove, repozitorijume, registre i okruzenja koja jesu i nisu u opsegu.
3. Proveri identitet i nivo dozvola koji se koristi za svaki alat, API, kubeconfig context, cloud sesiju i CI token.
4. Snimi stanje repozitorijuma, deploy-ovane revizije, sync stanje kontrolera, live resource version-e i relevantne prozore za izmene pre mutacije.
5. Definisi pravila rukovanja dokazima, redigovanja, zadrzavanja, sifrovanja, pristupa i brisanja.
6. Uspostavi stop uslove za neocekivani blast radius, degradiran health, zastarele backup-e, nedostajuci rollback ili nejasnu autorizaciju.

### 6.2 Minimalni dokazi

- Potpisana ili zabelezena granica opsega i odobrenja.
- Redigovan inventar identiteta, context-a, naloga i vlasnika.
- Manifest dokaza pre izmene sa hash-evima ili immutable referencama gde je prakticno.

### 6.3 Kriterijumi izlaza

1. Svaka akcija ima poznat identitet, opseg, vlasnika i nivo autorizacije.
2. Osetljivi dokazi su zasticeni i nijedna produkciona izmena nije izvrsena bez odobrenja.
3. Ogranicenja audita i nedostupni sistemi su eksplicitno registrovani.

