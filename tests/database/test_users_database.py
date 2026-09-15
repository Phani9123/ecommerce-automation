from database.database_client import DatabaseClient


DATABASE_PATH = "database/ecommerce.db"


def test_user_exists():

    db = DatabaseClient(
        DATABASE_PATH
    )

    user = db.fetch_one("""
        SELECT username
        FROM users
        WHERE id = ?
    """, (1,))

    assert user[0] == "phani"
    
def test_users_exist():

    db = DatabaseClient(
        DATABASE_PATH
    )

    users = db.fetch_all("""
        SELECT username
        FROM users
        WHERE id IN (1, 2)
    """)

    assert len(users) == 2
    
def test_insert_user():

    db = DatabaseClient(
        DATABASE_PATH
    )

    db.execute(
        """
        INSERT INTO users (id, username, email)
        VALUES (?, ?, ?)
        """,
        (100, "test_user", "test@example.com")
    )

    user = db.fetch_one(
        """
        SELECT username, email
        FROM users
        WHERE id = ?
        """,
        (100,)
    )

    assert user == (
        "test_user",
        "test@example.com"
    )

    db.execute(
        """
        DELETE FROM users
        WHERE id = ?
        """,
        (100,)
    )
    
def test_update_user():

    db = DatabaseClient(
        DATABASE_PATH
    )

    db.execute(
        """
        INSERT OR REPLACE INTO users (id, username, email)
        VALUES (?, ?, ?)
        """,
        (101, "update_user", "old@example.com")
    )

    db.execute(
        """
        UPDATE users
        SET email = ?
        WHERE id = ?
        """,
        ("new@example.com", 101)
    )

    user = db.fetch_one(
        """
        SELECT email
        FROM users
        WHERE id = ?
        """,
        (101,)
    )

    assert user[0] == "new@example.com"

    db.execute(
        """
        DELETE FROM users
        WHERE id = ?
        """,
        (101,)
    )
    
def test_delete_user():

    db = DatabaseClient(
        DATABASE_PATH
    )

    db.execute(
        """
        INSERT OR REPLACE INTO users (id, username, email)
        VALUES (?, ?, ?)
        """,
        (102, "delete_user", "delete@example.com")
    )

    user = db.fetch_one(
        """
        SELECT username
        FROM users
        WHERE id = ?
        """,
        (102,)
    )

    assert user[0] == "delete_user"

    rows_deleted = db.execute(
        """
        DELETE FROM users
        WHERE id = ?
        """,
        (102,)
    )

    assert rows_deleted == 1

    user = db.fetch_one(
        """
        SELECT username
        FROM users
        WHERE id = ?
        """,
        (102,)
    )

    assert user is None