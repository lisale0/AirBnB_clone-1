#!/usr/bin/python3
"""a script that starts a Flask web application """


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import operator
app = Flask(__name__)

""" after each request is done, close storage session"""


@app.teardown_appcontext
def close_session(exception):
    """ close storage"""
    storage.close()

""" Route: /states """


@app.route('/states', strict_slashes=False)
def state():
    states = storage.all("State")
    state_values = states.values()
    state_list = []
    for s in sorted(state_values, key=lambda k: k.name):
        state_list.append([s, s.cities])
    return render_template('9-states.html', condition="state_list",
                           state_list=state_list)

""" Route: /states/<id>"""


@app.route('/states/<string:state_id>', strict_slashes=False)
def state_id(state_id):
    states = storage.all("State").values()
    sorted_city_state = []
    sorted_cities = []
    try:
        for state in states:
            if state.id == state_id:
                state_name = state.name
                sorted_city_state.append([state, state.cities])

        for i in range(0, len(sorted_city_state[0][1])):
            sorted_cities.append({'name': sorted_city_state[0][1][i].name,
                                  'id': sorted_city_state[0][1][i].id})

        sorted_cities = sorted(sorted_cities, key=lambda k: k['name'])
        return render_template('9-states.html', condition="state_id",
                               sorted_cities=sorted_cities,
                               state_name=state_name)
    except:
        return render_template('9-states.html', condition="not_found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
