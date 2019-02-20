import sqlite3
import os

db_filename = '../leerplandoelen_db.sqlite3'

def query1():
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    c.execute("SELECT * FROM User")
    r = c.fetchone()
    print(r)
    for i in range(0, len(r)):
        print(r[i])
    
    c.close()

def query2():
    pass

if __name__ == '__main__':
    if os.path.isfile(db_filename):
        print("--query 1")
        query1()
        print("--query 2")
        query2()
    else:
        print("database not found!")
    