#!/usr/bin/python3
"""starts a Flask web application and list states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(error):
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html",
                           state_list=storage.all("State"))


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    return render_template("8-cities_by_states.html",
                           state_list=storage.all("State"),
                           city_list=storage.all("City"))


@app.route("/states/<state_id>", strict_slashes=False)
def states_select(state_id):
    stateObjs = storage.all("State").values()
    for state in stateObjs:
        if state.id == state_id:
            return render_template("9-states.html",
                                   state=state)
    return render_template("9-states.html", state=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
