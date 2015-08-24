#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

# Below as a helper for namespaces.
# Looks like a horrible hack.
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

import psycopg2
import progressbar as pb

from utilities.prompt_format import item
from utilities.load_config import LoadConfig

def StoreRecords(data, table, progress_bar=False, verbose=False):
  '''Store records in a PostgreSQL database.'''

  #
  # Available schemas.
  #
  database = LoadConfig('dev.json')['database']
  schemas = {}
  for schema in database:
    field_names = []
    for field in schema['fields']:
      field_names.append(field['field_name'])

    schemas[schema['name']] = field_names


  try:
    schema = schemas[table]

  except Exception as e:
    if verbose is True:
      print "%s select one of the following tables: %s." % (item('prompt_error'), ", ".join(schemas.keys()))
      print e

    print '%s Could not find schema.' % item('prompt_error')
    return False

  try:
    for record in data:

      s = ''
      scraperwiki.sqlite.save(record.keys(), record, table_name=table)

  except Exception as e:
    print "%s Failed to store record in database." % item('prompt_error')
    print e
    return False
