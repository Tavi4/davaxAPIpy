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
from math_service.core.db.connection import get_connection

def get_operation_logs(limit: int = 10, operation: str = None):
    """
    Fetch recent operation logs from the database.
    Supports optional filtering by operation name.
    """
    conn = get_connection()
    cursor = conn.cursor()

    if operation:
        cursor.execute("""
            SELECT operation, input_data, result, timestamp
            FROM operation_log
            WHERE operation = ?
            ORDER BY timestamp DESC
            LIMIT ?
        """, (operation, limit))
    else:
        cursor.execute("""
            SELECT operation, input_data, result, timestamp
            FROM operation_log
            ORDER BY timestamp DESC
            LIMIT ?
        """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
