#!/usr/bin/python3
"""Module containing cities by state route"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def fetch_states():
    """Fetch states function definition"""
    states_list = []
    all_states = storage.all(State)
    all_cities = storage.all(City)
    for st in all_states:
        a_s_d = {}
        ct_list = []
        for ct in all_cities:
            if all_cities[ct].state_id == all_states[st].id:
                tmp = {}
                tmp['name'] = all_cities[ct].name
                tmp['id'] = all_cities[ct].id
                ct_list.append(tmp)
        a_s_d = all_states[st].__dict__
        a_s_d['name'] = all_states[st].name
        a_s_d['id'] = all_states[st].id
        sorted_cts = sorted(ct_list, key=lambda x: x['name'])
        a_s_d['cts'] = sorted_cts
        states_list.append(a_s_d)
    a_s = sorted(states_list, key=lambda x: x['name'])
    return render_template('8-cities_by_states.html', a_s=a_s)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
