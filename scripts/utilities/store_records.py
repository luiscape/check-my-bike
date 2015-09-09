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

HOST_DATABASE = os.environ.get('POSTGRES_PORT_5432_TCP_ADDR')

def StoreRecords(data, table, progress_bar=False, verbose=False):
  '''Store records in a PostgreSQL database.'''

  #
  # TODO: add environment variables
  # to these default values.
  #
  conn = psycopg2.connect(host=HOST_DATABASE, dbname='rolltime', user='rolltime', password='rolltime')
  cur = conn.cursor()

  try:
    for record in data:

      #
      # Check no NULL values are passed.
      #
      for key in record.keys():
        if record.get(key) is None:
          record.pop(key)

      #
      # TODO: Check that the upsert statement
      # is supported by PostgreSQL 9.5
      #
      c = 'INSERT INTO {table} ({columns}) '.format(table=table, columns=",".join(record.keys()))
      # v = 'VALUES ({values}) ON CONFLICT UPDATE'.format(values="'" + "','".join(str(v) for v in record.values()) + "'")
      v = 'VALUES ({values})'.format(values="'" + "','".join(str(v) for v in record.values()) + "'")
      cur.execute(c + v)

    #
    # Commit all records.
    # And close cursor and connection.
    #
    conn.commit()
    cur.close()
    conn.close()

  except Exception as e:
    if e.pgcode == '23505':
      print '%s Record already exists. Skipping.' % item('prompt_warn')
      return

    else:
      if verbose:
        print "%s Failed to store record in database." % item('prompt_error')
        print 'PosgreSQL error code: %s' % e.pgcode
      return False
