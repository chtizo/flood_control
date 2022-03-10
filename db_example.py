import sqlite3

conn = sqlite3.connect("login_data.db")
cursor = conn.cursor()
cursor.execute("SELECT 1 FROM USERS USERNAME = ? AND PASS
print(cursor.fetchall())
