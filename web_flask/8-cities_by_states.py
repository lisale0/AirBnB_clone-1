#!/usr/bin/python3
"""a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)

""" after each request is done, close storage session"""


@app.teardown_appcontext
def close_session(exception):
    """remove the session to see what happened"""
    storage.close()

""" Route: /cities_by_states """


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    states = storage.all("State").values()
    city_state = []
    for state in sorted(states, key=lambda k: k.name):
        city_state.append([state, state.cities])
    return render_template('8-cities_by_states.html', city_state = city_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
