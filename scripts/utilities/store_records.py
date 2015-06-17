#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

# Below as a helper for namespaces.
# Looks like a horrible hack.
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

import scraperwiki
import progressbar as pb

from utilities.prompt_format import item

def StoreRecords(data, table, progress_bar=False, verbose = False):
  '''Store records in a ScraperWiki database.'''

  # Available schemas.
  schemas = {
    'trip': ["'tripduration'","'starttime'","'stoptime'","'start station id'","'start station name'","'start station latitude'","'start station longitude'","'end station id'","'end station name'","'end station latitude'","'end station longitude'","'bikeid'","'usertype'","'birth year'","'gender'"],
    'station': ["id", "stationName", "availableDocks", "totalDocks", "latitude", "longitude", "statusValue", "statusKey", "availableBikes", "stAddress1", "stAddress2", "city", "postalCode", "location", "altitude", "testStation", "lastCommunicationTime", "landMark", "executionTime"]
  }

  try:
    schema = schemas[table]

  except Exception as e:

    if verbose is True:
      print "%s select one of the following tables: %s." % (item('prompt_error'), ", ".join(schemas.keys()))
      print e

    print '%s Could not find schema.' % item('prompt_error')
    return False

  try:
    i = 0
    for record in data:
      scraperwiki.sqlite.save(schema, record, table_name=table)

  except Exception as e:
    print "%s Failed to store record in database." % item('prompt_error')
    print e
