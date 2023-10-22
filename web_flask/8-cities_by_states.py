#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """a function that teardown a db session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """a function that renders and html page of  cities in states"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
