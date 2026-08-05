<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class ReportController extends Controller
{
    public function byCustomer(Request $request)
    {
        $customerId = $request->input('customer_id');

        // Vulnerable: user-controlled value concatenated directly into raw SQL.
        $rows = DB::select("SELECT id, total, created_at FROM orders WHERE customer_id = " . $customerId);

        return response()->json($rows);
    }
}
