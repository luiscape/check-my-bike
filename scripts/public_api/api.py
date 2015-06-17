#!/usr/bin/python
# -*- coding: utf-8 -*-

import flask
import flask.ext.sqlalchemy
import flask.ext.restless

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///scraperwiki.sqlite'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

# Create your Flask-SQLALchemy models as usual but with the following two
# (reasonable) restrictions:
#   1. They must have a primary key column of type sqlalchemy.Integer or
#      type sqlalchemy.Unicode.
#   2. They must have an __init__ method which accepts keyword arguments for
#      all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
#      supplies such a method, so you don't need to declare a new one).

class station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stationName = db.Column(db.Unicode, unique=False)
    availableDocks = db.Column(db.Unicode, unique=False)
    totalDocks = db.Column(db.Unicode, unique=False)
    latitude = db.Column(db.Unicode, unique=False)
    longitude = db.Column(db.Unicode, unique=False)
    statusValue = db.Column(db.Unicode, unique=False)
    statusKey = db.Column(db.Unicode, unique=False)
    availableBikes = db.Column(db.Unicode, unique=False)
    stAddress1 = db.Column(db.Unicode, unique=False)
    stAddress2 = db.Column(db.Unicode, unique=False)
    city = db.Column(db.Unicode, unique=False)
    postalCode = db.Column(db.Unicode, unique=False)
    location = db.Column(db.Unicode, unique=False)
    altitude = db.Column(db.Unicode, unique=False)
    testStation = db.Column(db.Unicode, unique=False)
    lastCommunicationTime = db.Column(db.Unicode, unique=False)
    landMark = db.Column(db.Unicode, unique=False)
    executionTime = db.Column(db.Unicode, unique=False)

# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(station, methods=['GET', 'POST', 'DELETE'])

# start the flask loop
app.run()
