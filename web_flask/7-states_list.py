#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    return render_template("7-states_list.html", data=storage.all(State))


@app.teardown_appcontext
def tear(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
