#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import csv

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item
from utilities.store_records import StoreRecords

def IngestCitiBikeData(db_table='historic', verbose=False):
  '''Adds the CitiBike historical data to a database.'''

  #
  # Iterate over every CSV.
  #
  data_dir = os.path.join('data', 'historic')
  for file in os.listdir(data_dir):
    if file.endswith(".csv"):

      print '%s Processing data for `%s`' % (item('prompt_bullet'), file)

      #
      # Storing GAUL on database.
      #
      try:
        with open(os.path.join(data_dir, file)) as csv_file:
          data = csv.DictReader(csv_file)
          records = []
          for row in data:
            records.append(row)

          #
          # Store records in DB.
          #
          StoreRecords(records, db_table, verbose=True)

      except Exception as e:
        print "%s Failed to store records from %s in DB." % (item('prompt_error'), file)
        if verbose:
          print e
        return False
