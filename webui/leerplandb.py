import sqlite3
import models
from flask import g

db_filename = '../leerplandoelen_db.sqlite3'

def get_db():
    if 'conn' not in g:
        g.conn = sqlite3.connect(db_filename)    
    return g.conn

def get_competenties():
    conn = get_db()
    cs = []
    for row in conn.execute("SELECT * FROM Competenties"):
        c = models.Competentie()
        c.nummer = row[0]
        c.omschrijving = row[1]
        cs.append(c)
    return cs

def get_deelcompetenties():
    conn = get_db()
    ds = []
    for row in conn.execute("SELECT * FROM Deelcompetenties"):
        d = models.Deelcompetentie()
        d.nummer = row[0]
        d.omschrijving = row[1]
        d.competentie = row[2]
        ds.append(d)
    return ds
