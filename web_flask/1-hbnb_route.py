#!/usr/bin/python3
"""This is Flask web application module"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This displays "Hello HBNB!" when the root URL is accessed."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def lone_hbnb():
    """This displays "HBNB" when '/hbnb' URL is accessed."""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
