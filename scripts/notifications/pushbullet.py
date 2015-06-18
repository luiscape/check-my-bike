#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import requests as r

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item

def SendPushbulletNotification(payload, verbose=False):
  '''Send push notification via the Pushbullet API.'''

  config_path = os.path.join(os.path.split(dir)[0], 'config', 'secrets.json')

  #
  # Defining credentials.
  #
  with open(config_path, "r") as f:
    config = json.loads(f.read())

  headers = {'content-type': 'application/json', "Authorization": "Bearer " + config['pushbullet_key'] }

  #
  # Default Pusbullet type.
  #
  payload['type'] = 'note'

  #
  # Send notifications via POST.
  #
  try:
    print '%s Sending Pushbullet notification.' % item('prompt_bullet')
    res = r.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(payload), headers=headers)

    if not res.ok:
       print '%s %s' % (item('prompt_error'), res.json()['error']['message'])
       return False

    print '%s Pushbullet notification sent successfully.' % item('prompt_success')
    return True


  except Exception as e:
    print '%s Failed to send Pushbullet notification.' % item('prompt_error')
    if verbose:
      print e
    return False


if __name__ == '__main__':
  payload = { 'title': 'TEST', 'body': 'yet another test' }
  SendPushbulletNotification(payload)
