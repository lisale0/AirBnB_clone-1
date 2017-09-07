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
    """remove the session to see what happened"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    return render_template('10-hbnb_filters.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
