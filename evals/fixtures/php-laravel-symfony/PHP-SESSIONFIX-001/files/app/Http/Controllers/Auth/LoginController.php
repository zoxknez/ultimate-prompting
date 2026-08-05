<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function login(Request $request)
    {
        $credentials = $request->only('email', 'password');

        if (Auth::attempt($credentials)) {
            // Vulnerable: the session ID from before authentication is kept
            // after login instead of being regenerated. If an attacker fixed
            // the victim's session ID before they logged in (a session
            // fixation attack via a shared/public terminal, a subdomain
            // cookie, or a crafted link on a site that shares the cookie
            // domain), the attacker's pre-known session ID becomes a valid
            // authenticated session for the victim's account.
            return redirect()->intended('dashboard');
        }

        return back()->withErrors(['email' => 'Invalid credentials.']);
    }
}
