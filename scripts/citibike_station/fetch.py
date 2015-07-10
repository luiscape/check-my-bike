#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

import process as Process
from utilities.prompt_format import item
from utilities.store_records import StoreRecords


def FetchLatestStationData(verbose=False):
  '''Fetch latest station data from CitiBike's API'''

  if verbose:
    print '%s Fetching station list.' % item('prompt_bullet')

  u = 'http://www.citibikenyc.com/stations/json'
  r = requests.get(u)

  if not r.ok:
    print '%s Something went wrong checking for data.' % item('prompt_error')
    return False

  else:
    data = r.json()

    #
    # Schema of the database
    # has to be defined properly.
    # Right now everything is text
    # and thigs are, as expected, not
    # working as planned.
    #
    record_array = []
    for record in data['stationBeanList']:
      record['weekDay'] = Process.CalculateWeekNumber(data['executionTime'])
      record['executionTime'] = Process.FormatDate(data['executionTime'])
      record['lastCommunicationTime'] = Process.FormatDate(record['lastCommunicationTime'])
      record['availableDocksRatio'] = str(Process.CalculateRatio(record['availableDocks'], record['totalDocks']))
      record['availableBikesRatio'] = str(Process.CalculateRatio(record['availableBikes'], record['totalDocks']))

      record_array.append(record)

    StoreRecords(data=record_array, table='station', verbose=True)


if __name__ == '__main__':
  FetchLatestStationData()
