# core/db/logger.py

from math_service.core.db.connection import get_connection

import json


def log_operation(operation: str, input_data: dict, result):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO operation_log (operation, input_data, result)
        VALUES (?, ?, ?)
        """,
        (
            operation,
            json.dumps(input_data),
            str(result)
        )
    )

    conn.commit()
    conn.close()


#  function to fetch logs
def get_operation_logs(limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT operation, input_data, result, timestamp
        FROM operation_log
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]