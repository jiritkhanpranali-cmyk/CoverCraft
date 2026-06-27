import sqlite3

conn = sqlite3.connect(
    "database/users.db"
)

cursor = conn.cursor()

users = cursor.execute(
    "SELECT * FROM users"
).fetchall()

for user in users:
    print(user)

conn.close()