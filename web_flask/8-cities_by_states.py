#!/usr/bin/python3
"""starts a Flask web application and list states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(error):
    """Tear down process when app stops running"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Lists states in database"""
    return render_template("7-states_list.html",
                           state_list=storage.all("State"))


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Lists states in database"""
    return render_template("8-cities_by_states.html",
                           state_list=storage.all("State"),
                           city_list=storage.all("City"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
