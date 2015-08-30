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


def FetchLatestStationData(verbose=True):
  '''Fetch latest station data from CitiBike's API'''

  if verbose:
    print '%s Fetching station data.' % item('prompt_bullet')

  #
  # TODO: make this URL relative.
  #
  u = 'http://www.citibikenyc.com/stations/json'

  #
  # At times, server returns wrong encoding.
  # This makes sure that the server doesn't
  # crash.
  #
  try:
    r = requests.get(u)

  except Exception as e:
    print '%s Something went wrong checking for data.' % item('prompt_error')
    return False

  if not r.ok:
    print '%s Something went wrong checking for data.' % item('prompt_error')
    return False

  else:
    data = r.json()

    def _none_check(v):
      '''Checks for None values. Inserts 0 instead.'''
      print 'None'

    #
    # Schema of the database
    # has to be defined properly.
    # Right now everything is text
    # and thigs are, as expected, not
    # working as planned.
    #
    record_array = []
    for record in data['stationBeanList']:

      #
      # Filtering record for
      # data of interest.
      #
      record = {
         'id': int(record['id']),
         'totalDocks': int(record['totalDocks']),
         'availableDocks': int(record['availableDocks']),
         'availableBikes': int(record['availableBikes']),
         'lastCommunicationTime': str(record['lastCommunicationTime'])
         }

      #
      # Adding additional data.
      #
      record['week'] = Process.CalculateWeekNumber(data['executionTime'])
      record['weekDay'] = Process.CalculateWeekDayNumber(data['executionTime'])
      record['day'] = Process.FormatDay(data['executionTime'])
      record['executionTime'] = Process.FormatDate(data['executionTime'])
      record['lastCommunicationTime'] = Process.FormatDate(record['lastCommunicationTime'])
      record['availableDocksRatio'] = Process.CalculateRatio(record['availableDocks'], record['totalDocks'])
      record['availableBikesRatio'] = Process.CalculateRatio(record['availableBikes'], record['totalDocks'])

      #
      # Append results to an array.
      #
      record_array.append(record)

    if StoreRecords(data=record_array, table='metric', verbose=True) == False:
      return False


if __name__ == '__main__':
  FetchLatestStationData()
