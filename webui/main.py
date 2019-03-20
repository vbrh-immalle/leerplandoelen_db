from flask import Flask, render_template
import leerplandb

app = Flask(__name__)


@app.route('/')
def hello():
    return "<p>Ga naar <a href='/competenties'>Competenties</a></p>"


@app.route('/competenties')
def competenties():
    cs = leerplandb.get_competenties()
    return render_template("competenties.html", competenties=cs)


app.run(host='localhost', port='5001', debug=True)