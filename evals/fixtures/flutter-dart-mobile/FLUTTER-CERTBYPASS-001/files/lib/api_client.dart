import 'dart:io';
import 'package:http/io_client.dart';

/// Vulnerable: badCertificateCallback unconditionally returns true, which
/// tells the HTTP client to accept ANY TLS certificate for ANY host -
/// expired, self-signed, or presented by an active man-in-the-middle. This
/// completely defeats certificate validation for every request this client
/// makes, including login and payment calls, on any network the device
/// joins (public Wi-Fi, a compromised router, a malicious VPN profile).
HttpClient createApiHttpClient() {
  final httpClient = HttpClient()
    ..badCertificateCallback = (X509Certificate cert, String host, int port) => true;
  return httpClient;
}
