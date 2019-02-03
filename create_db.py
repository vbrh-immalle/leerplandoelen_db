import sqlite3
import models
import parser
import os

db_filename = 'leerplandoelen_db.sqlite3'

def create_db():
    conn = sqlite3.connect(db_filename)
    
    c = conn.cursor()
    
    c.execute("CREATE TABLE Competenties(nummer text primary key, omschrijving text)")
    c.execute("CREATE TABLE Deelcompetenties(nummer text primary key, omschrijving text, competentie text)")
    c.execute("CREATE TABLE Leerplandoelen(nummer text primary key, omschrijving text, competentie text, deelcompetentie text)")
    
    leerplanonderdelen = parser.parse_leerplandoelentekst()

    for lpo in leerplanonderdelen:
        print(lpo.getInsertCommand())
        c.execute(lpo.getInsertCommand())

    conn.commit()
    c.close()
    

if __name__ == '__main__':
    os.remove(db_filename)
    