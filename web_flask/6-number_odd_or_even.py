#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, escape, render_template


app = Flask(__name__)

@app.route('/',strict_slashes=False)
def hello():
    """display message to user"""
    return "Hello HBNB!"

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    """display message to user"""
    return 'HBNB'

@app.route('/c/<text>',strict_slashes=False)
def c_var(text):
    """display message to user"""
    return 'C %s' % escape(text.replace('_', ' '))

@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>')
def py_var(text,strict_slashes=False):
    """display message to user"""
    return 'Python  %s' % escape(text.replace('_', ' '))

@app.route('/number/<int:n>',strict_slashes=False)
def num_var(n):
    """display message to user"""
    return '%d is a number' % n

@app.route('/number_template/<int:n>',strict_slashes=False)
def nt_var(n):
    """display message to user"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>',strict_slashes=False)
def even_odd(n):
    """display message to user"""
    e=False
    if (n % 2 == 0):
        e = True
    return render_template('6-number_odd_or_even.html', n=n, e=e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
