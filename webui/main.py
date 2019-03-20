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


app.run(host='localhost', port='5001', debug=True)