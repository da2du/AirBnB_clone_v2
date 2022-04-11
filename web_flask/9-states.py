#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def state(id=None, strict_slashes=False):
    states = storage.all(State).values()
    return render_template('9-states.html', id=id, states=states)


@app.teardown_appcontext
def tear(exception):
    """removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
