// Vulnerable: this error-handling middleware is registered unconditionally
// (no check against process.env.NODE_ENV) and returns the raw error stack
// and message to the client on every unhandled exception. In production
// this leaks internal file paths, the framework/library versions in the
// stack frames, and occasionally query or connection-string fragments
// embedded in the error message, to any client that can trigger an error.
module.exports = function errorHandler(err, req, res, next) {
  res.status(500).json({
    error: err.message,
    stack: err.stack,
  });
};
