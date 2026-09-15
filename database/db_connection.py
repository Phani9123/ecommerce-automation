import sqlite3


DATABASE_PATH = "database/ecommerce.db"


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


# Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")


# Insert users
cursor.execute("""
    INSERT OR IGNORE INTO users (id, username, email)
    VALUES (1, 'phani', 'phani@example.com')
""")

cursor.execute("""
    INSERT OR IGNORE INTO users (id, username, email)
    VALUES (2, 'ravi', 'ravi@example.com')
""")

cursor.execute("""
    SELECT * FROM users
""")

users = cursor.fetchall()

print("Users:", users)

# Find a specific user
cursor.execute("""
    SELECT username
    FROM users
    WHERE id = 1
""")

user = cursor.fetchone()

print("User:", user)

connection.commit()

connection.close()