#!/usr/bin/python3
"""starts a Flask web application and list states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(error):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html",
                           state_list=storage.all("State"))

if __name__ == "__main__":
    storage.close()
    app.run(host='0.0.0.0', port=5000)
