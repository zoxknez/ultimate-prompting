const express = require("express");
const router = express.Router();
const db = require("../lib/db");
const { requireAuth } = require("../middleware/auth");

// Vulnerable: requireAuth only checks that a session exists, not that the
// session's account owns the requested invoice. Any authenticated user can
// read any other tenant's invoice by guessing/incrementing the id.
router.get("/invoices/:id", requireAuth, async (req, res) => {
  const invoice = await db.invoices.findById(req.params.id);
  if (!invoice) {
    return res.status(404).json({ error: "not found" });
  }
  res.json(invoice);
});

module.exports = router;
