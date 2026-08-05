## 33. Phase 23 - Cache, CDN, OPcache And Stale-Code Consistency

Recovery must account for every layer that can continue serving or executing pre-remediation content.

### Cache and execution layers

Inventory:

- WordPress object cache and object-cache drop-in
- page-cache plugin and advanced-cache drop-in
- Redis or Memcached namespace, authentication and sharing model
- reverse-proxy cache
- CDN cache, workers, transforms, redirects and edge HTML injection
- host-provided cache and optimization layers
- PHP OPcache, preload and PHP-FPM process lifetime
- browser cache and service workers
- DNS resolver and certificate propagation

### Evidence-safe invalidation sequence

- capture relevant cache configuration, keys/metadata and suspicious cached objects before purge when useful
- deploy trusted code and configuration first
- invalidate OPcache or restart the correct PHP process only after evidence capture and with an approved impact plan
- purge object/page/reverse-proxy/CDN caches in a documented order
- verify direct origin and each public edge path
- verify authenticated and unauthenticated variants
- confirm stale workers, containers or PHP children no longer serve old code
- record purge IDs, deployment revisions and verification timestamps

A cache purge before trusted code deployment can repopulate the cache with malicious content. A successful origin test does not prove that every edge is clean.

