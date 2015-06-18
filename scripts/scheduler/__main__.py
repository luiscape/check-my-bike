#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from scheduler import scheduler

def Main():
  '''Wrapper.'''
  scheduler.Main()


if __name__ == '__main__':
  Main()
