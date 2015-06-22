#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

import scripts
import logging

from app import app
from flask.ext.cors import CORS
from tornado.ioloop import IOLoop
from sandman.model import activate
from sandman import app as application
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from werkzeug.wsgi import DispatcherMiddleware
from scripts.utilities import prompt_format as I


## Configuration.
root = logging.getLogger()
ch = logging.StreamHandler(sys.stderr)
ch.setLevel(logging.WARNING)
root.addHandler(ch)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///scraperwiki.sqlite'
application.config['SANDMAN_GENERATE_PKS'] = True

# Allowing CORS.
cors = CORS(application)
application = DispatcherMiddleware(app, {
    '/api': application,
    })


def CheckLocation():
  '''Checking if the application is on an OpenShift environment.'''

  # print "%s Application not on OpenShift." % I.item('prompt_bullet')
  l = {
    "ip": 'localhost',
    "port": 2368
  }

  return l


def WelcomeMessage(port):
  '''Welcome.'''
  print "%s Server started on port %s." % (I.item('prompt_bullet'), port)


if __name__ == "__main__":
  v = CheckLocation()
  activate(browser=False, admin=False)
  application.debug = True
  WelcomeMessage(v['port'])
  http_server = HTTPServer(WSGIContainer(application))
  http_server.listen(v['port'], v['ip'])
  IOLoop.instance().start()
