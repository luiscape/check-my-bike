#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item
from utilities.store_records import StoreRecords

from citibike_station.check import FetchLatestStationData


def Main():
  '''Wrapper.'''

  try:
    FetchLatestStationData()

  except Exception as e:
    return False

  print '%s Collection worked successfully.' % item('prompt_success')

if __name__ == '__main__':
  Main()
