# utils/file_ops.py
import os

def save_log(filename, content):
    """Appends a timestamped log entry or operation result to a text file."""
    try:
        with open(filename, "a") as file:
            file.write(f"{content}\n")
        return True
    except IOError as e:
        print(f"Error saving to file: {e}")
        return False

def read_logs(filename):
    """Reads and displays all records from the log file."""
    if not os.path.exists(filename):
        return "No logs found yet."
    try:
        with open(filename, "r") as file:
            return file.read()
    except IOError as e:
        return f"Error reading file: {e}"