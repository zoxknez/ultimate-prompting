## Obavezni adversarial i failure scenariji

Izvrši ili verno simuliraj sve primenljive scenarije. Za svaki preskočeni scenario zabeleži razlog, rizik, owner-a i compensating dokaz.

1. Drugi autentifikovani tenant zahteva, menja, export-uje ili download-uje resurs drugog tenant-a kroz direktne i indirektne identifikatore.
2. Dva klijenta istovremeno šalju istu kritičnu mutation operaciju sa i bez istog idempotency ključa.
3. Proces pada pre database commit-a, tokom commit neizvesnosti i posle commit-a ali pre response-a ili acknowledgement-a poruke.
4. Queue poruka se duplira, reorder-uje, kasni, replay-uje iz DLQ-a i konzumiraju je stare i nove verzije worker-a.
5. Scheduled task se pokreće dva puta, propušta run, gubi lock, premašuje lock TTL i preklapa se kroz replike.
6. Baza postaje spora, odbija konekcije, vraća deadlock-e, gubi primary ili izlaže replica lag tokom kritičnog toka.
7. Redis ili session storage postaje nedostupan, evict-uje ključeve, vraća stale podatke ili failover-uje tokom autentikacije i autorizacije.
8. Spoljni provider timeout-uje, rate-limit-uje, vraća malformed success, duplira webhook, rotira ključeve i kasno potvrđuje side effect.
9. Korisnik se logout-uje ili suspenduje dok sesije, API tokeni, queued job-ovi, signed URL-ovi i dugotrajni export-i još postoje.
10. Dva sekvencijalna zahteva različitih korisnika i tenant-a izvršavaju se na istom dugovečnom worker-u i koriste locale, auth, tracing i singleton stanje.
11. Veliki, duboko ugnježden, kompresovan, malformed ili parser-hostile payload cilja JSON, XML, YAML, archive, image, PDF, CSV i regex putanje.
12. URL importer ili webhook target koristi redirect-e, DNS rebinding, alternativnu IP sintaksu, interne hostname-ove i cloud metadata adrese.
13. Deployment se odvija sa starim FPM child procesima, stale OPcache-om, starim queue worker-ima, zagrejanim novim cache-evima, mixed schema-om i in-flight zahtevima.
14. Tajna, session ključ, webhook ključ, OAuth ključ ili signing ključ se rotira dok stari i novi procesi koegzistiraju.
15. Aplikacija prima SIGTERM tokom HTTP mutation-a, queue side effect-a, scheduled job-a, migracije, konverzije fajla i export-a.
16. Migracija se pauzira, retry-uje, parcijalno primenjuje, rollback-uje na application nivou i zatim sledi forward repair.
17. Cache ključ, session payload, queued poruka ili serializovani object proizveden starim release-om konzumira novi release i obrnuto.
18. Restore se izvršava izolovano iz backup-a i point-in-time logova, zatim se validiraju autorizacija, integritet, queue stanje, fajlovi i search.
19. Detektuje se ranjiva zavisnost, zlonamerni Composer plugin, poisoned CI cache, zamenjen artifact ili kompromitovan deployment kredencijal.
20. Aktivni webshell ili nepoznat executable fajl se otkriva na produkcionom hostu dok su integritet koda, kredencijala i podataka neizvesni.

