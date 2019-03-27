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

def get_deelcompetenties_voor_competentie(nummer):
    conn = get_db()
    ds = []
    for row in conn.execute("SELECT * FROM Deelcompetenties WHERE competentie = ?", (nummer,)):
        d = models.Deelcompetentie()
        d.nummer = row[0]
        d.omschrijving = row[1]
        d.competentie = row[2]
        ds.append(d)
    return ds


def get_leerplandoelen():
    conn = get_db()
    ls = []
    for row in conn.execute("SELECT * FROM Leerplandoelen"):
        l = models.Leerplandoel()
        l.nummer = row[0]
        l.omschrijving = row[1]
        l.competentie = row[2]
        l.deelcompetentie = row[3]
        ls.append(l)
    return ls


def get_users():
    conn = get_db()
    users = []
    for row in conn.execute("SELECT * FROM Users"):
        u = models.User()
        u.id = row[0]
        u.achternaam = row[1]
        u.voornaam = row[2]
        users.append(u)
    return users


def get_user(id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM Users WHERE id = ?", (id,))
    row = cursor.fetchone()
    if not row:
        return None
    u = models.User()
    u.id = row[0]
    u.achternaam = row[1]
    u.voornaam = row[2]
    return u


def get_antwoorden(leerplannummer):
    conn = get_db()
    antwoorden = []
    for row in conn.execute("SELECT * FROM Antwoorden WHERE leerplan = ?", (leerplannummer,)):
        a = models.Antwoord()
        a.leerplandoel = row[2]
        a.inhoud = row[3]
        a.tijdstip = row[4]
        antwoorden.append(a)
    return antwoorden


def get_antwoorden_from_user(user_id):
    conn = get_db()
    antwoorden = []
    for row in conn.execute("SELECT * FROM Antwoorden WHERE user_id = ?", (user_id,)):
        a = models.Antwoord()
        a.leerplandoel = row[2]
        a.inhoud = row[3]
        a.tijdstip = row[4]
        antwoorden.append(a)
    return antwoorden
