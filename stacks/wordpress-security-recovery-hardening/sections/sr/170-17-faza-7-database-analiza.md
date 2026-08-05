## 17. Faza 7 - Database Analiza

Za analizu koristi read-only database nalog kada je praktično.

Pregledaj:

- neočekivane korisnike, administratore i privilegovani `usermeta`
- vreme kreiranja korisnika i promene lozinki
- application passwords i session tokens
- `siteurl`, `home`, `active_plugins`, `cron`, rewrite i autoloaded options
- neočekivane option nazive, velike autoloaded vrednosti i encoded payload-e
- injected posts, pages, templates, widgets, menus i comments
- SEO spam, skrivene linkove i conditional content
- zlonamerni JavaScript u content-u, options ili page-builder podacima
- integritet serijalizovanih podataka
- multisite network admine, site-ove i network options
- database triggers, scheduled events, users i grants gde su podržani
- neočekivane tabele i skoro izmenjene zapise kada postoje audit podaci

### Database bezbednosna pravila

- Napravi dump pre izmene i hash-uj dump.
- Ne stavljaj raw dump u javnu putanju ili repozitorijum.
- Izbegavaj ručnu zamenu stringova u serijalizovanim vrednostima.
- Koristi transaction-safe i reverzibilne izmene gde su podržane.
- Zabeleži svaku izmenjenu tabelu/red i razlog.
- Potvrdi table prefix umesto pretpostavke `wp_`.
- Razlikuj WordPress-level kompromitaciju od kompromitacije database servera.

