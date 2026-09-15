import sqlite3


class DatabaseClient:

    def __init__(self, database_path):
        self.database_path = database_path
        self.initialize_database()

    def connect(self):
        return sqlite3.connect(self.database_path)

    def initialize_database(self):

        connection = self.connect()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            """)

            cursor.execute("""
                INSERT OR IGNORE INTO users
                (id, username, email)
                VALUES (1, 'phani', 'phani@example.com')
            """)

            cursor.execute("""
                INSERT OR IGNORE INTO users
                (id, username, email)
                VALUES (2, 'ravi', 'ravi@example.com')
            """)

            connection.commit()

        finally:
            connection.close()

    def fetch_one(self, query, params=None):

        connection = self.connect()
        cursor = connection.cursor()

        try:
            cursor.execute(
                query,
                params or ()
            )

            return cursor.fetchone()

        finally:
            connection.close()

    def fetch_all(self, query, params=None):

        connection = self.connect()
        cursor = connection.cursor()

        try:
            cursor.execute(
                query,
                params or ()
            )

            return cursor.fetchall()

        finally:
            connection.close()

    def execute(self, query, params=None):

        connection = self.connect()
        cursor = connection.cursor()

        try:
            cursor.execute(
                query,
                params or ()
            )

            connection.commit()

            return cursor.rowcount

        finally:
            connection.close()