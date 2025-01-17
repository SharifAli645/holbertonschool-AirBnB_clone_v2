#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    return render_template("9-states.html",
                           d_state=storage.all(State),
                           d_id=None)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    return render_template("9-states.html",
                           d_state=storage.all(State),
                           d_city=storage.all(City),
                           d_id=id)


@app.teardown_appcontext
def tear(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
