import psycopg2


def export_table(connection, table_name: str, row_limit: int):
    """Admin utility: dump the first `row_limit` rows of a caller-chosen table.

    Vulnerable: table_name cannot be passed as a bind parameter (identifiers
    aren't parameterizable in SQL), so it is string-formatted directly into
    the query with no allowlist or quoting. A table_name of
    "users; DROP TABLE users; --" or "pg_shadow" lets the caller run
    arbitrary SQL or read tables never intended to be exported.
    """
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name} LIMIT {row_limit}"
    cursor.execute(query)
    return cursor.fetchall()
