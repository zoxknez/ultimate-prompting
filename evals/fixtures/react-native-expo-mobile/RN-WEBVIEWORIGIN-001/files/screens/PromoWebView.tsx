import React from "react";
import { WebView } from "react-native-webview";
import { useRoute } from "@react-navigation/native";

// Vulnerable: the WebView loads whatever URL arrives via the deep-link
// param with JavaScript enabled and no origin restriction. A crafted deep
// link (myapp://promo?url=https://attacker.example/phish) opens arbitrary
// attacker-controlled pages with full JS execution and access to whatever
// the WebView's injected bridge exposes - there is no allowlist checking
// that url actually points at this app's own promo domain.
export default function PromoWebView() {
  const route = useRoute();
  const { url } = route.params as { url: string };

  return (
    <WebView
      source={{ uri: url }}
      javaScriptEnabled={true}
      originWhitelist={["*"]}
    />
  );
}
