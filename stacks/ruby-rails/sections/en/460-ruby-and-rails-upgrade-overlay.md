## Ruby And Rails Upgrade Overlay

1. Patch the current supported Ruby and Rails lines first when urgent security fixes exist.
2. Upgrade Ruby separately from Rails where possible and compare interpreter, native-gem, GC, YJIT and performance behavior.
3. Eliminate deprecations and blocking gems before changing the Rails minor or major line.
4. Run `app:update` in a reviewable branch and inspect every config and default change.
5. Review `config.load_defaults` deliberately; do not copy a new application configuration blindly.
6. Test framework components independently: Active Record, Active Job, Action Cable, Active Storage, Action Mailer, Hotwire and assets.
7. Prove mixed-version deployment, database compatibility, queued payload compatibility and rollback before production cutover.
8. Advance one supported step at a time and retain a measured before-and-after baseline.

