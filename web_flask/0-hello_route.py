#!/usr/bin/python3
"""Declaration of route in web application module"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """This is function definition hello HBNB"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
