import sqlite3


class Database:
    def __init__(self, db_name="employees.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    department TEXT NOT NULL,
                    salary REAL NOT NULL
                )
            """)

    def execute_query(self, query, parameters=()):
        with self.connect() as conn:
            cursor = conn.execute(query, parameters)
            return cursor.lastrowid

    def fetch_all(self, query, parameters=()):
        with self.connect() as conn:
            cursor = conn.execute(query, parameters)
            return cursor.fetchall()
