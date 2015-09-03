#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from status.send import SendStatus
from utilities.prompt_format import item
from citibike_station.fetch import FetchLatestStationData


def Main():
  '''Wrapper.'''

  try:
    status = FetchLatestStationData()

  except Exception as e:
    print '%s Failed to fetch data from the CitiBike API.' % item('prompt_error')
    print e
    return False

  if status != False:
    print '%s Collection worked successfully.' % item('prompt_success')
    return True

  else:
    print '%s Failed to fetch data from the CitiBike API.' % item('prompt_error')
    return False


if __name__ == '__main__':

  if Main() == False:
    SendStatus('error')

  else:
    SendStatus('ok')
