## Research Baseline - 5 August 2026

This baseline is a starting point, not permission to upgrade blindly. Re-check official Ruby, Rails, RubyGems, Bundler, Puma and project-specific sources immediately before recommendations or changes.

| Component | Verified status on 5 August 2026 | Mandatory audit check |
| --- | --- | --- |
| Ruby CRuby | 4.0.6 is the latest stable patch in the 4.0 line; 3.4 remains in normal maintenance, 3.3 in security maintenance, and 3.2 is EOL. | Verify `ruby -v`, `RUBY_ENGINE`, patch, build, platform, image and process. |
| Rails | 8.1.3.1 is the latest security release in the current 8.1 line. | Verify `Gemfile.lock`, actual loaded gem versions, maintenance window and security advisories. |
| Rails support policy | Bug fixes are generally provided for one year and security fixes for two years after a minor series starts. | Calculate dates from the actual series release and re-check policy. |
| Bundler | 4.0.17 is the current stable release. | Verify Bundler, RubyGems, lockfile format, platforms, checksums and deployment mode. |
| Puma | 8.0.2 is the current release; supported applications may intentionally remain on another maintained line. | Verify Rack compatibility, server config, parser/proxy behavior, workers, threads and graceful restart. |
| Solid Queue | Rails 8 uses Solid Queue as the default production Active Job backend; current gem line must be verified from the lockfile. | Do not transfer Sidekiq semantics to Solid Queue. Verify database, dispatcher, worker, scheduler and concurrency behavior. |
| Ruby execution models | CRuby, JRuby and TruffleRuby have different concurrency, GC, native extension and deployment properties. | Never generalize GVL or native gem assumptions across runtimes. |

Do not mix source declarations, local development, CI, image build, web process, job process, console, scheduler and one-off task state. Each is a separate evidence boundary.

