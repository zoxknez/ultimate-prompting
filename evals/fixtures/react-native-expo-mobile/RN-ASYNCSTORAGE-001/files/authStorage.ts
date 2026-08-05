import AsyncStorage from "@react-native-async-storage/async-storage";

// Vulnerable: AsyncStorage on Android backs onto an unencrypted SQLite
// database and on iOS onto unencrypted plist/SQLite files - neither is
// designed for secrets. A long-lived refresh token stored here is
// recoverable from a device backup, from an Android app with a targeted
// backup exploit, or trivially on a rooted/jailbroken device. This should
// use expo-secure-store (Keychain/Keystore-backed) instead.
export async function saveRefreshToken(token: string): Promise<void> {
  await AsyncStorage.setItem("refresh_token", token);
}

export async function getRefreshToken(): Promise<string | null> {
  return AsyncStorage.getItem("refresh_token");
}
