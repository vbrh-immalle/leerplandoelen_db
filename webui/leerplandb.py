import sqlite3
import models

db_filename = '../leerplandoelen_db.sqlite3'

conn = sqlite3.connect(db_filename)


def get_competenties():
    global conn
    cs = []
    for row in conn.execute("SELECT * FROM Competenties"):
        c = models.Competentie()
        c.nummer = row[0]
        c.omschrijving = row[1]
        cs.append(c)
    return cs