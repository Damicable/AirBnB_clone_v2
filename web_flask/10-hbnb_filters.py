#!/usr/bin/python3
"""
Flask web application script that serves an HTML page with filters.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name)


@app.route('/hbnb_filters', strict_slashes = False)
def hbnb_filters():
    """'/hbnb_filters' route that displays for state, city and amenity"""
    states = sorted(list(storage.all(State).values()), key=lambda state: state.name)
    cities = sorted(list(storage.all(City).values()), key=lambda city: city.name)
    amenities = sorted(list(storage.all(Amenity).values()), key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
