#!/usr/bin/python3
"""This is a simple Flask web application script that displays all states."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """This route fetches and lists all states."""
    states = storage.all(State)
    state = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', state=state)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
