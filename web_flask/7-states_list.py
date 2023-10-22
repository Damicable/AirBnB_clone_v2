#!/usr/bin/python3
"""Simple Flask web application script that displays list of states."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This is /states_list route that a list of states."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
