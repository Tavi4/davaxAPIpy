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
