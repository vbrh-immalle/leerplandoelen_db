import sqlite3
import models

db_filename = '../leerplandoelen_db.sqlite3'


def get_competenties():
    conn = sqlite3.connect(db_filename)    
    cs = []
    for row in conn.execute("SELECT * FROM Competenties"):
        c = models.Competentie()
        c.nummer = row[0]
        c.omschrijving = row[1]
        cs.append(c)
    return cs

def get_deelcompetenties():
    conn = sqlite3.connect(db_filename)
    ds = []
    for row in conn.execute("SELECT * FROM Deelcompetenties"):
        d = models.Deelcompetentie()
        d.nummer = row[0]
        d.omschrijving = row[1]
        d.competentie = row[2]
        ds.append(d)
    return ds
