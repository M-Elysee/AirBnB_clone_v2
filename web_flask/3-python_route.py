#!/user/bin/python3
""" a script that starts a Flask web application and
    give some functionality to some routes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ a function that provide greatings"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ a function that display some words"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """ a function that display a value provided in the url"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pytext(text='is cool'):
    """ a function that display a value provided in the url """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
