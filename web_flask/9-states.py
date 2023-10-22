#!/usr/bin/python3
"""Flask web application containing list_state route"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def fetch_states():
    """Fetch states function definition"""
    states_list = []
    all_states = storage.all(State)
    for st in all_states:
        states_list.append(all_states[st])
    a_s = sorted(states_list, key=lambda x: x.name)
    return render_template('7-states_list.html', a_s=a_s)


@app.route("/states/<id>", strict_slashes=False)
def fetch_state_id(id):
    """This defines and fetch /states/<id> route function"""
    all_states = storage.all(State)
    all_cities = storage.all(City)
    for st in all_states:
        if all_states[st].id == id:
            id_f = True
            a_s_d = {}
            ct_list = []
            for ct in all_cities:
                if all_cities[ct].state_id == id:
                    tmp = {}
                    tmp['name'] = all_cities[ct].name
                    tmp['id'] = all_cities[ct].id
                    ct_list.append(tmp)
            a_s_d['name'] = all_states[st].name
            a_s_d['id'] = all_states[st].id
            sorted_cts = sorted(ct_list, key=lambda x: x['name'])
            a_s_d['cts'] = sorted_cts
            a_s_d['flag'] = True
            return render_template('9-states.html', states=a_s_d)
    a_s_d = {'flag': False}
    return render_template('9-states.html', states=a_s_d)


@app.teardown_appcontext
def app_teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
