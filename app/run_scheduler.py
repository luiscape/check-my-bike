#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import schedule

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(os.path.join(dir, 'scripts'))

from scheduler import scheduler

def RunScheduler():
  '''Running scheduler.'''

  scheduler.Main()
