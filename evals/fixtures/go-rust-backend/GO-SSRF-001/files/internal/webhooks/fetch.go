package webhooks

import (
	"io"
	"net/http"
)

// FetchPreview downloads a caller-supplied URL to generate a link preview.
//
// Vulnerable: targetURL comes straight from the request with no validation
// against internal/private IP ranges, cloud metadata endpoints, or
// non-HTTP(S) schemes. A caller can pass
// "http://169.254.169.254/latest/meta-data/iam/security-credentials/" (the
// cloud metadata service) or an internal-only admin URL, and this server
// will fetch it on their behalf and return the response - classic SSRF
// turning this service into a proxy into the internal network.
func FetchPreview(targetURL string) ([]byte, error) {
	resp, err := http.Get(targetURL)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	return io.ReadAll(resp.Body)
}
