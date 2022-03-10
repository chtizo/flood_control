import sqlite3

def register():
    conn = sqlite3.connect("login_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS USERS(USERNAME TEXT NOT NULL PRIMARY KEY, PASSWORD TEXT NOT NULL, NAME TEXT NOT NULL)")

    username = input("Username: ")
    password = input("Password: ")
    name = input("Name: ")
    cursor.execute("SELECT 1 FROM USERS WHERE USERNAME = ?",(username,))

    while len(cursor.fetchall())>0:
        print("Exists enter a new one")
        username = input("Username: ")
        password = input("Password: ")
        name = input("Name: ")
        cursor.execute("SELECT 1 FROM USERS WHERE USERNAME = ?",(username,))
    print("Entered")
    cursor.execute("INSERT INTO USERS(username, password, name) VALUES(?,?,?)", (username, password, name))

    conn.commit()

    cursor.execute("SELECT * FROM USERS")
    print(cursor.fetchall())
    conn.close()

def login():
    conn = sqlite3.connect("login_data.db")
    attempts = 0
    cursor = conn.cursor()

    username = input("Username: ")
    password = input("Password: ")
    #name = input("Name: ")
    attempts = attempts + 1
    cursor.execute("SELECT 1 FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
    print(cursor.fetchall())
    while len(cursor.fetchall()) == 0 and attempts < 3:
        print("Doesn't exist")
        username = input("Username: ")
        password = input("Password: ")
        #name = input("Name: ")
        cursor.execute("SELECT 1 FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        attempts = attempts + 1
        print(cursor.fetchall())
    if attempts >=3:
        print("you are temporarily locked")
        conn.close()
    else:
        print("Logged in")
        conn.close()
##def extractValue(conn):
##    result = conn.execute("SELECT * FROM USERS")
##    print(result)
##    for data in result:
##        print("Username: ", data[0])
##        print("Password: ", data[1])

   


login()


