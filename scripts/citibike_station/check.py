#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item
from utilities.store_records import StoreRecords


def FetchLatestStationData(verbose=False):
  '''Fetch latest station data from CitiBike's API'''

  print '%s Fetching station list.' % item('prompt_bullet')

  u = 'http://www.citibikenyc.com/stations/json'
  r = requests.get(u)

  if not r.ok:
    print '%s Something went wrong checking for data.' % item('prompt_error')
    return False

  else:
    data = r.json()

    record_array = []
    for record in data['stationBeanList']:
      record['executionTime'] = data['executionTime']
      record_array.append(record)

    StoreRecords(data=record_array, table='station', verbose=True)
