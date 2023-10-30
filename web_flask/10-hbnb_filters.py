#!/usr/bin/python3
""" a script that starts a Flask web application """

from flask import Flask, render_template
from models import *
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """a function that renders an HTML page"""
    states = storage.all(State).values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """a function that closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
