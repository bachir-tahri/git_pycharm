from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hallo Welt!</h1>'


@app.route('/kontakt/<name>')
def kontakt(name):
    return '<h2>Ich bin ein kontakttformular für ' + name + '</h2>'


app.run(debug=True, port=9999)
