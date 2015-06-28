#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from flask.ext.cors import cross_origin

@app.route('/')
@cross_origin()
def index():
  '''Serve the index file.'''
  return render_template('index.html')


@app.route('/station')
def show_station():
  '''Serves the station page.'''
  return render_template('station.html')
