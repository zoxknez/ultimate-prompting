## 12. Faza H - Alati, Plugini I MCP

### 12.1 Tool Ugovori I Izvrsavanje

1. Popisi svaku capability, vlasnika, caller-a, scope, side effect, podatke kojima pristupa i reverzibilnost.
2. Koristi strict argument schema i deterministicku server-side validaciju.
3. Ponovo autorizuj svaki tool poziv prema autentifikovanom akteru, tenant-u, resursu i trenutnom stanju.
4. Primeni allowlist-e za alate, komande, putanje, hostove, protokole, destinacije i klase podataka.
5. Izoluj filesystem, process, browser, network i code execution.
6. Spreci SSRF, DNS rebinding, credential forwarding, pristup lokalnoj mrezi, metadata servisima, path traversal, command injection i unsafe deserialization.
7. Sprovedi timeout-e, output-size limite, rate limit-e, concurrency limite i cost budget-e.
8. Koristi idempotency key-eve za retry side effect-a i compensating action za partial failure.
9. Validiraj i sanitizuj tool output pre ulaska u promptove, logove, UI, shell, SQL, HTML, template-e ili downstream API-je.
10. Loguj invocation intent, authorization decision, argumente u redigovanom obliku, result status, odobrenje i side effect-e.

### 12.2 Ljudsko Odobrenje I High-Impact Akcije

1. Klasifikuj alate prema uticaju i reverzibilnosti.
2. Zahtevaj ljudsku potvrdu za payment, deployment, delete, publication, account ili permission promene, external communication, sensitive export, shell i druge materijalne side effect-e osim kada postoji formalno odobrena automation policy.
3. Pre odobrenja prikazi korisniku tacan preview akcije i destinaciju.
4. Ponovo trazi odobrenje kada se promene parametri, resurs, iznos, primalac, okruzenje ili smisao akcije.
5. Ne izvodi odobrenje iz ranije konverzacione izjave koja nije vezana za tacnu akciju.
6. Testiraj cancellation, timeout, duplicate approval, stale approval i race condition-e.

### 12.3 MCP-Specific Kontrole

1. Utvrdi MCP specification verziju koja je stvarno implementirana i razdvoji stable od draft ili release-candidate funkcija.
2. Proveri OAuth i authorization ponasanje prema aktuelnoj normativnoj specifikaciji.
3. Validiraj token audience i zabrani token passthrough.
4. Spreci confused-deputy ponasanje, privilege escalation, session hijacking i cross-client state leakage.
5. Validiraj identitet servera, redirect URI-jeve, origin-e, transport security, local binding i poverenje u remote endpoint.
6. Tool opis, resource content, promptove, sampling request-eve, elicitation i server metadata tretiraj kao untrusted.
7. Detektuj capability promene i zahtevaj review pre izlaganja novih ili prosirenih mogucnosti.
8. Pinuj, verifikuj, popisi i nadgledaj MCP server pakete, image-e, binarne fajlove i zavisnosti.
9. Testiraj malicious ili compromised MCP servere, poisoned tool metadata, oversized response, invalid schema, disconnect, retry i partial result.
10. Dokumentuj svako koriscenje experimental ekstenzija i rollback put.

