from app import mysql

def findUsers():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM contato")
    if users > 0:
        userDetails = cur.fetchall()
    return userDetails