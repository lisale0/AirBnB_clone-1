#!/usr/bin/python3
"""a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

""" after each request is done, close storage session"""
@app.teardown_appcontext
def close_session(exception):
    """remove the session to see what happened"""
    storage.close()

""" Route: /states_list """
@app.route('/states_list', strict_slashes=False)
def even_or_odd():
    state_list = storage.all("State")
    key = []
    state_arr = []
    for state in state_list:
        key.append(state)
    for i in key:
        state_arr.append(state_list[i])
    return render_template('7-states_list.html', state_list=state_arr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
