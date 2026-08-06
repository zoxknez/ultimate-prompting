import { NextRequest, NextResponse } from "next/server";

// Vulnerable: callbackUrl comes straight from the query string and is used
// as the redirect target with no check that it points back at this app's
// own origin. A crafted link like
// "https://real-app.example/api/auth/callback?callbackUrl=https://attacker.example/login"
// looks legitimate (it starts with the real domain) but redirects the user
// straight to a phishing page immediately after they authenticate -
// classic open-redirect-enabled phishing.
export async function GET(request: NextRequest) {
  const callbackUrl = request.nextUrl.searchParams.get("callbackUrl") ?? "/dashboard";
  return NextResponse.redirect(callbackUrl);
}
