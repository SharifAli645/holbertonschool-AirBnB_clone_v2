#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states():
    return render_template("8-cities_by_states.html",
                           data_state=storage.all(State),
                           data_city=storage.all(City))


@app.teardown_appcontext
def tear(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
