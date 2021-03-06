#!/usr/bin/python3
"""a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

""" after each request is done, close storage session"""


@app.teardown_appcontext
def close_session(exception):
    """close storage"""
    storage.close()

""" Route: /states_list """


@app.route('/states_list', strict_slashes=False)
def state_list():
    state_list = storage.all("State")
    state_arr = state_list.values()
    sorted_arr = []
    for state in sorted(state_arr, key=lambda k: k.name):
        sorted_arr.append(state)
    return render_template('7-states_list.html', state_list=sorted_arr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
