from flask import Flask, render_template
import leerplandb

app = Flask(__name__)


@app.route('/')
def hello():
    return """
<p>Ga naar:</p> 
<ul>
  <li>
    <a href='/competenties'>Competenties</a>
  </li>
  <li>
    <a href='/deelcompetenties'>Deelcompetenties</a>
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


app.run(host='localhost', port='5001', debug=True)