#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models import State, Amenity


app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display webpage"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', **locals())

@app.teardown_appcontext
def tr(exception):
    """removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
