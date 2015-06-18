#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import schedule

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from citibike_station.check import FetchLatestStationData
from utilities.prompt_format import item

#
# Schedule
#
schedule.every(1).minutes.do(FetchLatestStationData)


def Main():
  '''Wrapper to run all the scheduled tasks.'''

  print '%s Running scheduler.' % item('prompt_bullet')
  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
    Main()
