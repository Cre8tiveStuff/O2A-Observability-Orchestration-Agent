import sqlite3
import json
from datetime import datetime

DB_PATH = "o2a_log.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""CREATE TABLE IF NOT EXISTS action_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        tool_called TEXT,
        input_data TEXT,
        output_data TEXT,
        verification_status TEXT,
        verification_score REAL
    )""")
    conn.commit()
    conn.close()


def log_action(tool, input_data, output_data, status=None, score=None):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO action_log (timestamp, tool_called, input_data, output_data, verification_status, verification_score) VALUES (?,?,?,?,?,?)",
        (datetime.now().isoformat(), tool, json.dumps(input_data), json.dumps(output_data), status, score)
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    log_action("test_tool", {"query": "hello"}, {"result": "world"}, "PASS", 100.0)
    print("Logged a test action.")