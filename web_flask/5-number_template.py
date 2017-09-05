#!/usr/bin/python3
"""a script that starts a Flask web application """
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'

@app.route('/c/<string:text>', strict_slashes=False)
def display_c(text):
    text = text.replace("_"," ")
    return 'C {}'.format(text)

@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def display_python(text="is cool"):
    text = text.replace("_"," ")
    return 'Python {}'.format(text)
@app.route('/number/<int:num>', strict_slashes=False)
def display_number(num):
    return '{} is a number'.format(num)

@app.route('/number_template/<int:num>', strict_slashes=False)
def display_numbertemp(num):
    return render_template('5-number.html', num=num)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
