<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AvatarController extends Controller
{
    // Vulnerable: the uploaded file is stored under its original,
    // caller-supplied filename with no extension allowlist, no MIME-type
    // check, and no re-encoding, directly inside the public web root. A
    // file named "shell.php" containing PHP code is stored as-is and is
    // then directly executable by visiting its public URL - a classic
    // unrestricted-file-upload-to-webshell chain.
    public function upload(Request $request)
    {
        $file = $request->file('avatar');
        $filename = $file->getClientOriginalName();
        $file->move(public_path('uploads/avatars'), $filename);

        return response()->json(['path' => "/uploads/avatars/{$filename}"]);
    }
}
