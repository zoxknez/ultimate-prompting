## 29. Incident response, forenzika i supply-chain kompromitovanje

**Cilj:** Pripremi ogranicavanje, istragu, uklanjanje uzroka, oporavak i ucenje bez unistavanja dokaza.

### 29.1 Obavezne provere

1. Definisi incident uloge, severity, komandanta, komunikacije, legal i privacy escalation, vendor kontakte, cuvare dokaza, poslovne odluke i odgovornosti javnog statusa.
2. Pripremi playbook-ove za kompromitovan CI, runner, source nalog, paket, action, base image, registry, signing identitet, cluster kredencijal, workload, node, KMS kljuc, secret manager, DNS ili cloud nalog.
3. Sacuvaj logove, audit tragove, artefakte, image-e, provenance, potpise, workflow run-ove, istoriju kontrolera, cloud event-e, runtime metadata, memory ili disk dokaze i chain of custody.
4. Ogranici incident najmanjom efektivnom akcijom: opozovi identitet, blokiraj digest, stavi workload u karantin, pauziraj promociju, izoluj nalog ili namespace, onemoguci rutu ili ogranici egress.
5. Izbegni siroko brisanje, rebuild, termination noda, ciscenje logova, rotaciju kljuceva ili redeployment dok se ne razmotre dokazi i uticaj zavisnosti.
6. Isprati blast radius kroz artefakte, okruzenja, identitete, podatke, korisnike, regione, zavisnosti, backup-e i recovery sisteme.
7. Rebuild-uj iz trusted izvora i builder-a, rotiraj po redosledu zavisnosti, potvrdi ciste artefakte, bezbedno restore-uj, prati ponavljanje i sacuvaj rollback.
8. Izvedi tabletop ili tehnicku vezbu i pretvori lekcije u izmene sa vlasnikom i rokom.

### 29.2 Minimalni dokazi

- Plan incident ovlascenja, kontakata, severity-ja i rukovanja dokazima.
- Playbook-ovi supply-chain i credential kompromitovanja.
- Timeline vezbe, odluke, dokazi, praznine i dodeljena poboljsanja.

### 29.3 Kriterijumi izlaza

1. Organizacija moze opozvati, staviti u karantin, rebuild-ovati, redeploy-ovati i potvrditi kriticne komponente bez oslanjanja na kompromitovanu putanju.
2. Odgovornosti cuvanja dokaza i komunikacije su jasne.
3. Nalazi vezbe imaju vlasnike, rokove, verifikaciju i vidljivost rukovodstva.

