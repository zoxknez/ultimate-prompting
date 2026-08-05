package com.example.app

import com.example.payments.sdk.PaymentsSDK

object PaymentsClient {
    // Vulnerable: a live payments-provider secret key compiled directly into
    // the app. Anyone who downloads the APK can extract this string with a
    // decompiler (no obfuscation defeats a plain string constant) and use it
    // to call the payments provider's server-side API directly, outside the
    // app's own rate limits and validation.
    private const val PAYMENTS_SECRET_KEY = "PAYMENTS-LIVE-SECRET-DO-NOT-SHIP-IN-CLIENT-CODE-0000000000"

    fun init() {
        PaymentsSDK.initialize(secretKey = PAYMENTS_SECRET_KEY)
    }
}
