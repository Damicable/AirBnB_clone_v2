#!/usr/bin/python3
"""Flask web application to display cities by state"""

from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities_by_states():
    """Display a list of states and their cities"""
    states = storage.all(State)
    states_list = []
    for state_id, state in states.items():
        state_dict = {
            "id": state.id,
            "name": state.name,
            "cities": sorted(
                [
                    {"id": city.id, "name": city.name}
                    for city in state.cities
                ],
                key=lambda x: x["name"]
            )
        }
        states_list.append(state_dict)

    a_s = sorted(states_list, key=lambda x: x["name"])
    return render_template('8-cities_by_states.html', a_s=a_s)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
