import json


def format_log_entry(entry: dict) -> str:
    try:
        operation = entry.get("operation")
        input_data = json.loads(entry.get("input_data", "{}"))
        result = entry.get("result")
        timestamp = entry.get("timestamp")

        if operation == "power":
            formatted_input = f"{input_data.get('base')} ^ {input_data.get('exponent')}"
        elif operation == "factorial":
            formatted_input = f"{input_data.get('n')}!"
        elif operation == "fibonacci":
            formatted_input = f"{input_data.get('n')}"
        else:
            formatted_input = str(input_data)

        return f"[{timestamp}] {operation}({formatted_input}) = {result}"
    except Exception as e:
        return f"[invalid log entry] {e}"
