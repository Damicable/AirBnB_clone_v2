#!/usr/bin/python3
"""Display flask web application route module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This defines the root route for Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def lone_hbnb():
    """The defines the /hbnb route for HBNB."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_arg_hbnb(text):
    """This defines the /c/<text> route"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_arg_hbnb(text):
    """This display /python/<text> route with text = 'is cool'"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_arg_hbnb(n):
    """Displays "n is a number" for /number/<n> route"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_arg_hbnb(n):
    """This displays 'HTML'for /number_template/<int:n> route"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
