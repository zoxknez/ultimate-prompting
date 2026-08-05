## 32. Phase 22 - SEO Spam, Redirects And Search-Engine Recovery

SEO spam often combines database content, conditional rendering, redirect logic, cache layers and search-engine ownership abuse.

### SEO and redirect evidence

Check:

- server and CDN redirects
- WordPress canonical, rewrite, template and redirect hooks
- `siteurl`, `home`, permalink and rewrite-rule state
- posts, revisions, post metadata, options, widgets, menus, patterns and theme settings
- sitemap, robots, feeds, structured data and alternate-language links
- hidden pages, doorway content and unexpected taxonomies
- cloaking by user agent, referrer, cookie, IP, geography, time or authentication state
- malicious JavaScript redirects and service workers
- Search Console and Bing verified owners, users, sitemaps and change history
- analytics and tag-manager account ownership
- cached pages at CDN, reverse proxy, browser and search-engine layers

### Recovery sequence

1. remove the root cause and persistence
2. produce a clean canonical response at the origin
3. purge and verify every cache layer
4. regenerate sitemaps and robots content
5. verify Search Console/Bing ownership and remove unauthorized principals
6. request review or removal only after the clean state is stable
7. monitor indexed URLs, crawl errors, manual actions and new spam patterns

URL removal tools hide symptoms temporarily and are not remediation.

