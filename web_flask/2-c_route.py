#!/usr/bin/python3
"""Display flask web application route module"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This defines the root route for Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def lone_hbnb():
    """The defines the /hbnb route for HBNB."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def arg_hbnb(text):
    """This defines the /c/<text> route"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
