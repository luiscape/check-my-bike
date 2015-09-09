#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

import json
import requests
from datetime import datetime
from utilities.prompt_format import item

#
# Scope variables.
#
NOW = datetime.now().isoformat(str('T'))
NODE_ID = os.getenv('NODE_ID', None)
# NODE_WATCH_ADDR = os.getenv('NODE_WATCH_PORT_27017_TCP_ADDR', 'http://localhost:9000')
NODE_WATCH_ADDR = 'http://node_watch:9000'  # Experimenting with Docker variables.

def SendStatus(status=None, id=NODE_ID, time=NOW, address=NODE_WATCH_ADDR):
  '''Sending status to the node watching service.'''

  if status == 'error':
    message = 'Failed to collect data.'

  if status == 'ok':
    message = 'Data collection successful.'

  payload = {
    'id': id,
    'status': status,
    'time': time,
    'message': message
  }

  print '%s Sending notification to Node Watch.' % item('prompt_ping')

  try:
    r = requests.post(address, data=payload)
    if r.json()['success'] == False:
      print r.json()

  except Exception as e:
    print '%s Could not send notification to Node Watch.'
    print payload
    print e
    return False
