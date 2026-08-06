const express = require("express");
const router = express.Router();
const userSettings = require("../lib/userSettings");

function deepMerge(target, source) {
  for (const key of Object.keys(source)) {
    if (source[key] && typeof source[key] === "object" && !Array.isArray(source[key])) {
      target[key] = target[key] || {};
      deepMerge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}

// Vulnerable: deepMerge recurses into the request body with no check for
// "__proto__", "constructor", or "prototype" keys. A body like
// {"__proto__": {"isAdmin": true}} walks up the prototype chain and adds
// isAdmin to Object.prototype itself - every plain object in the running
// process, across every request and every user, now has isAdmin: true
// unless explicitly overridden. This is prototype pollution, and depending
// on how other code reads that property it can become a privilege
// escalation or, with the right gadget elsewhere in the app, remote code
// execution.
router.patch("/settings", async (req, res) => {
  const current = await userSettings.get(req.user.id);
  const merged = deepMerge(current, req.body);
  await userSettings.save(req.user.id, merged);
  res.json(merged);
});

module.exports = router;
