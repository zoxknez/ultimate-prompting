const express = require("express");
const router = express.Router();
const db = require("../lib/db");
const { sendResetEmail } = require("../lib/mailer");

// Vulnerable: no rate limiting, throttling, or CAPTCHA on this endpoint,
// and the response shape differs depending on whether the account exists.
// An attacker can enumerate every registered email address at unlimited
// speed by watching which requests return "reset email sent" versus
// "no account found", and separately brute-force reset tokens once one is
// issued since there's nothing slowing repeated attempts either.
router.post("/password-reset", async (req, res) => {
  const { email } = req.body;
  const user = await db.users.findByEmail(email);

  if (!user) {
    return res.status(404).json({ error: "No account found with that email." });
  }

  await sendResetEmail(user);
  res.json({ message: "Reset email sent." });
});

module.exports = router;
