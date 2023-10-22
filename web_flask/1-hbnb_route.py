#!/user/bin/python3
""" a script that starts a Flask web application and
    give some functionality to some routes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ a function that provide greatings on the root URL """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ a function that display some words at a certain URL"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
