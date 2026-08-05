import 'package:shared_preferences/shared_preferences.dart';

/// Vulnerable: the long-lived refresh token is written to SharedPreferences,
/// which on Android backs onto an unencrypted XML file and on iOS onto an
/// unencrypted plist - both readable without root/jailbreak on a device
/// with a file-system backup enabled, or trivially on a rooted/jailbroken
/// device. This should use flutter_secure_storage (Keystore/Keychain)
/// instead, which is designed for exactly this kind of long-lived secret.
class AuthStorage {
  Future<void> saveRefreshToken(String token) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('refresh_token', token);
  }

  Future<String?> getRefreshToken() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString('refresh_token');
  }
}
