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

HOST_DATABASE = os.environ.get('HOST_DATABASE')

def StoreRecords(data, table, progress_bar=False, verbose=False):
  '''Store records in a PostgreSQL database.'''

  # #
  # # Available schemas.
  # #
  # database = LoadConfig('dev.json')['database']
  # schemas = {}
  # for schema in database:
  #   field_names = []
  #   for field in schema['fields']:
  #     field_names.append(field['field_name'])

  #   schemas[schema['name']] = field_names


  # try:
  #   schema = schemas[table]

  # except Exception as e:
  #   if verbose is True:
  #     print "%s select one of the following tables: %s." % (item('prompt_error'), ", ".join(schemas.keys()))
  #     print e

  #   print '%s Could not find schema.' % item('prompt_error')
  #   return False


  #
  # TODO: add environment variables
  # to these default values.
  #
  conn = psycopg2.connect(host=HOST_DATABASE, dbname='rolltime', user='rolltime', password='rolltime')
  cur = conn.cursor()

  try:
    for record in data:

      c = 'INSERT INTO {table} ({columns}) '.format(table=table, columns=",".join(record.keys()))
      v = 'VALUES ({values})'.format(values="'" + "','".join(str(v) for v in record.values()) + "'")
      cur.execute(c + v)

    #
    # Commit all records.
    # And close connection.
    #
    conn.commit()
    cur.close()
    conn.close()


  except Exception as e:
    print "%s Failed to store record in database." % item('prompt_error')
    print e
    return False
