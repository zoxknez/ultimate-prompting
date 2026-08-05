const { ipcMain } = require("electron");
const fs = require("fs");
const path = require("path");

const ATTACHMENTS_DIR = "/var/app/attachments";

// Vulnerable: the renderer-supplied filename is joined onto the attachments
// directory and read with no check that the resolved path stays inside it.
// A renderer that has been compromised via a loaded remote page (or a
// malicious attachment name itself) can send a filename like
// "../../../../etc/passwd" or "../../.env" and this main-process handler -
// which runs with full Node.js and filesystem access, unlike the sandboxed
// renderer - will read it and return the contents.
ipcMain.handle("read-attachment", async (event, filename) => {
  const filePath = path.join(ATTACHMENTS_DIR, filename);
  return fs.readFileSync(filePath, "utf-8");
});
