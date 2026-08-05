## 27. Phase 17 - WordPress Bootstrap And WP-CLI Trust Boundaries

Treat the WordPress bootstrap as potentially hostile until core, configuration, MU plugins, drop-ins and early-loading code are examined.

### Bootstrap execution map

Trace and verify:

- web-server rewrite and front-controller path
- `index.php`, `wp-blog-header.php`, `wp-load.php`, `wp-config.php` and `wp-settings.php`
- files included before or from `wp-config.php`
- `auto_prepend_file` and `auto_append_file` from PHP, pool, vhost and per-directory configuration
- `advanced-cache.php`, `object-cache.php`, `db.php`, `sunrise.php`, `maintenance.php` and other drop-ins
- MU plugins and their loader files
- Composer autoloaders, custom bootstrap files and vendor code
- environment-based secret loaders and hosting-provider bootstrap code
- OPcache and preload configuration that may retain old executable code

### WP-CLI safety rules

- identify whether a command runs before WordPress loads or executes the full compromised bootstrap
- `wp core verify-checksums` is useful because the documented command runs before WordPress loading, but it still proves only core-file integrity
- do not assume `--skip-plugins --skip-themes` neutralizes MU plugins, drop-ins, `wp-config.php`, PHP auto-prepend code or host-level persistence
- prefer an evidence copy or isolated forensic clone for commands that load WordPress
- run with the least-privileged OS and database account available
- never run WP-CLI as root merely to bypass permissions
- capture command, working directory, effective user, WP-CLI version, exit code and output hash
- treat unexpected output, network calls, process creation or file changes during a read-only command as an indicator requiring investigation

### Direct inspection fallback

When WordPress bootstrap cannot be trusted:

- inspect files directly with OS tools
- use read-only database access and explicit SQL queries
- obtain inventory from package manifests, filesystem metadata and clean vendor packages
- compare against an isolated known-good WordPress installation
- defer application-level commands until the bootstrap trust boundary is restored

