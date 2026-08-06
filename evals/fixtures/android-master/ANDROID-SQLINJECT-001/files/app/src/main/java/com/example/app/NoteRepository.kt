package com.example.app

import android.database.sqlite.SQLiteDatabase

class NoteRepository(private val db: SQLiteDatabase) {

    // Vulnerable: the caller-supplied search term is concatenated directly
    // into the raw SQL string instead of using a parameterized query
    // (rawQuery's selectionArgs, or Room's @Query with bound parameters).
    // A search term like "' OR '1'='1" returns every note regardless of
    // owner, and a term like "'; DROP TABLE notes; --" can destroy the
    // local table - reachable by anything that can influence this search
    // field, including a value restored from a backup or shared via intent.
    fun searchNotes(term: String): List<String> {
        val cursor = db.rawQuery(
            "SELECT title FROM notes WHERE owner_id = ? AND title LIKE '%$term%'",
            arrayOf(currentUserId())
        )
        val results = mutableListOf<String>()
        while (cursor.moveToNext()) {
            results.add(cursor.getString(0))
        }
        cursor.close()
        return results
    }

    private fun currentUserId(): String = "user-1"
}
