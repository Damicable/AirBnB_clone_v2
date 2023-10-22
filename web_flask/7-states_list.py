#!/usr/bin/python3
"""
Simple Flask web application script that displays a list of states.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name)


@app.route('/states_list', strict_slashes = False)
    """This is /states_list route that a list of states."""
    tates_list = []
    all_states = storage.all(State)
    for st in all_states:
        states_list.append(all_states[st])
    states = sorted(states_list, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
