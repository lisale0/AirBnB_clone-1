#!/usr/bin/python3
"""a script that starts a Flask web application """


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
import operator
app = Flask(__name__)

""" after each request is done, close storage session"""


@app.teardown_appcontext
def close_session(exception):
    """ close storage """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    city_state = []
    for state in sorted(states, key=lambda k: k.name):
        city_state.append([state, state.cities])

    return render_template('10-hbnb_filters.html',
                           city_state = city_state,
                           amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
