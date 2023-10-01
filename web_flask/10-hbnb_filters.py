#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    return render_template("10-hbnb_filters.html",
                           data_state=storage.all(State),
                           data_city=storage.all(City),
                           data_ameni=storage.all(Amenity))


@app.teardown_appcontext
def tear(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
