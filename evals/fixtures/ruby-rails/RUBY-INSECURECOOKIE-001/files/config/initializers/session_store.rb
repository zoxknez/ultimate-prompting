# Vulnerable: the session cookie is issued with no `secure` or `httponly`
# flag. Without `secure: true`, the browser will happily send the session
# cookie over a plain HTTP connection (e.g. a stray http:// link, a
# downgrade on a hostile network), exposing it to interception. Without
# `httponly: true`, any JavaScript running on the page - including from a
# successful XSS elsewhere in the app or a compromised third-party script -
# can read document.cookie and steal the session directly.
Rails.application.config.session_store :cookie_store, key: "_app_session"
