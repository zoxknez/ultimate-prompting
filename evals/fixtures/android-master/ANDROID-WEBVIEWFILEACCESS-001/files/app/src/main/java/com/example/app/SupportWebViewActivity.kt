package com.example.app

import android.os.Bundle
import android.webkit.WebView
import androidx.appcompat.app.AppCompatActivity

class SupportWebViewActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val webView = WebView(this)
        setContentView(webView)

        // Vulnerable: JavaScript is enabled together with file-URL access
        // from other file URLs. A page loaded in this WebView - including
        // one reached via an open redirect on the support site this screen
        // points at - can use a file:// URL to read arbitrary files
        // readable by the app (SharedPreferences XML, cached auth tokens,
        // internal databases) and exfiltrate them via JavaScript.
        webView.settings.javaScriptEnabled = true
        webView.settings.allowFileAccessFromFileURLs = true
        webView.settings.allowUniversalAccessFromFileURLs = true

        webView.loadUrl("https://support.example.com/help")
    }
}
