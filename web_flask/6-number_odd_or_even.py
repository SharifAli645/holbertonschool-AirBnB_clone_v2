#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_function(text):
    text = text.replace("_", " ")
    return f'C {text}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_function(text="is cool"):
    text = text.replace("_", " ")
    return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def numbers(n):
    return f'{n} is a number'


@app.route("/number_template/<int:number>", strict_slashes=False)
def template(number):
    return render_template("5-number.html", number=number)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        tp = "even"
    else:
        tp = "odd"

    return render_template("6-number_odd_or_even.html", n=n, tp=tp)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)