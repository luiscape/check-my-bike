#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from datetime import datetime
from utilities.prompt_format import item

def FormatDate(s, verbose=True):
  '''Format a single date entry into the desired Rolltime format.'''

  try:
    d = datetime.strptime(s, '%Y-%m-%d %X %p')
    return d.strftime('%Y-%m-%d %H:%M')

  except Exception as e:
    if verbose:
      print '%s Failed to convert date: %s' % (item('prompt_error'), s)
      print e
      return s

def CalculateRatios():
  '''Calculates the three basic rations we are currently using.'''

  print 'nothing yet'
