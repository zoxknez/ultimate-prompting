package main

import (
	"log"
	"net/http"
)

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
	})

	// Vulnerable: http.ListenAndServe uses the zero-value http.Server, which
	// has no ReadTimeout, WriteTimeout, ReadHeaderTimeout, or IdleTimeout.
	// A client that opens a connection and sends bytes at 1-per-30-seconds
	// (a classic slowloris pattern), or one that simply never finishes
	// sending its headers, holds a goroutine and a file descriptor open
	// indefinitely. Enough concurrent slow clients exhaust the server's
	// connection pool and deny service to legitimate traffic.
	log.Fatal(http.ListenAndServe(":8080", mux))
}
