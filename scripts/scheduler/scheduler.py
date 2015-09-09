#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import schedule

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from station_collector.fetch import Main as FetchAndStoreData
from utilities.prompt_format import item

#
# Schedule
#
schedule.every(30).seconds.do(FetchAndStoreData)

def Main(verbose=True):
  '''Wrapper to run all the scheduled tasks.'''

  if verbose:
    print '%s Running scheduler.' % item('prompt_bullet')

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
    Main()
