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
    state_list = storage.all(State)
    string = ""
    for state in state_list:
        string += f'<LI>{state.id}: <B>{state.name}</B></LI>'
    return render_template("7-states_list.html", strg=string)


@app.teardown_appcontext
def tear():
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
