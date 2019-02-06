# Leerplandoelen_db

`parser.py` maakt gebruik van **regular expressions** om de input-file `leerplandoelen_text.txt` te parsen.
Er werden Model-classes aangemaakt zodat de parser-code gescheiden kon blijven van de database-code.

Als oef. kan je:

- deze Model-classes verwijderen en rechtstreeks in de parser de database aanspreken
- i.p.v. regular expressions, kan je ook de standaard string-functies van Python gebruiken


# Opmerkingen

In (X)Ubuntu:

- `sudo apt install sqlite` om nadien de gemaakte database te kunnen testen met `sqlite3`
- `python3` om `create_db.py` uit te voeren (er wordt geen gebruikt gemaakt van `pip` omdat enkel standard libraries gebruikt worden)


# SQL

Als oef. kan je:

- extra queries schrijven om test-data toe te voegen
- een query schrijven die alle antwoorden van een bepaald leerplandoel opvraagt
- een query schrijven die alle antwoorden van een bepaalde gebruiker opvraagt
- ...
