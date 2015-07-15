#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item

def LoadConfig(config_file, verbose=False):
  '''Load configuration parameters.'''

  config_path = os.path.join('config', config_file)

  try:
    with open(config_path) as json_file:
      config = json.load(json_file)

  except Exception as e:
    print "%s Couldn't load configuration." % item('prompt_error')
    if verbose:
      print e
    return False

  return config
