#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import psycopg2

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item
from utilities.load_config import LoadConfig


def CreateDbAndTable(config_file='dev.json', verbose=True):
  '''Creating tables in SQLite database.'''

  #
  # Loading database information
  # from config file.
  #
  database = LoadConfig(config_file)['database']

  #
  # TODO: add environment variables
  # to these default values.
  #
  conn = psycopg2.connect(host='HOSTNAME_HERE', dbname='rolltime', user='rolltime', password='rolltime')
  cur = conn.cursor()

  #
  # Build each table.
  #
  for table in database:

    #
    # Construct SQL statement.
    #
    table_sql = ""
    for f in table['fields']:
      s = '%s %s, ' % (f['field_name'], f['type'])
      table_sql += s

    statement = 'CREATE TABLE IF NOT EXISTS %s(%sPRIMARY KEY (%s))' % (table['name'], table_sql, ", ".join(table['primary_key']))

    #
    # Make statements to the database.
    #
    try:
      cur.execute(statement)
      conn.commit()
      print "%s table `%s` created." % (item('prompt_bullet'), str(table['name']))

    except Exception as e:
      print '%s Table `%s` could not be created.' % (item('prompt_error'), table['name'])
      if verbose:
        print e
      return False

  #
  # Close communication.
  #
  cur.close()
  conn.close()


if __name__ == '__main__':
  CreateDbAndTable()
