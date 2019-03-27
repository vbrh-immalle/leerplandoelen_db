from flask import Flask, render_template
import leerplandb

app = Flask(__name__)


@app.route('/')
def hello():
    return """
<p>Ga naar:</p> 
<ul>
  <li>
    <a href='/competenties'>Alle competenties</a>
  </li>
  <li>
    <a href='/deelcompetenties'>Alle deelcompetenties</a>
  </li>
  <li>
    <a href='/leerplandoelen'>Alle leerplandoelen</a>
  </li>
  <li>
    <a href='/users'>Alle users</a>
  </li>
</ul>
"""

@app.route('/competenties')
def competenties():
    cs = leerplandb.get_competenties()
    return render_template("competenties.html", competenties=cs)

@app.route('/deelcompetenties')
def deelcompetenties():
    ds = leerplandb.get_deelcompetenties()
    return render_template("deelcompetenties.html", deelcompetenties=ds)

@app.route('/competentie/<nummer>')
def competentie(nummer):
    ds = leerplandb.get_deelcompetenties_voor_competentie(nummer)
    return render_template("deelcompetentie.html", competentienummer=nummer, deelcompetenties=ds)

@app.route('/leerplandoelen')
def leerplandoelen():
    ls = leerplandb.get_leerplandoelen()
    return render_template("leerplandoelen.html", leerplandoelen=ls)

@app.route('/users')
def users():
    us = leerplandb.get_users()
    return render_template("users.html", users=us)

@app.route('/user/<user_id>')
def user(user_id):
    u = leerplandb.get_user(user_id)
    if u is None:
        return f"User met id {user_id} niet gevonden!"
    antwoorden = leerplandb.get_antwoorden_from_user(user_id)
    return render_template("user_details.html", user=u, antwoorden=antwoorden)

app.run(host='localhost', port='5001', debug=True)