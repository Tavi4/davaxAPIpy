
from math_service.core.db.connection import get_connection
from math_service.core.utils.publisher import publish_message

import json
import sqlite3

# EDGE CASE DACA FAILUIESTE CONEXIUNEA
def log_operation(operation: str, input_data: dict, result):
    try:
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

    except sqlite3.Error as e:
        print(f"[DB ERROR] Failed to log operation: {e}")

    # trebuie sa dea publish doar daca a reusit sa logheze si in baza de date
    publish_message(operation, input_data, result) # sending the message to rabbitmq


def get_operation_logs(limit: int = 10, operation: str = None):
    """
    Fetch recent operation logs from the database.
    Supports optional filtering by operation name.
    """
    try:
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

    except sqlite3.Error as e:
        print(f"[DB ERROR] Failed to fetch logs: {e}")
        return []
