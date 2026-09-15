import sqlite3


class DatabaseClient:

    def __init__(self, database_path):
        self.database_path = database_path

    def connect(self):
        return sqlite3.connect(
            self.database_path
        )

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