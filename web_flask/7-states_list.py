#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """ a function that teardown a session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ a function that renders an html page """
    st = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list', st=state_objs)


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0', debug=True)
