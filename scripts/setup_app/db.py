#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import scraperwiki

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

  if 'name' not in database.keys():
    print '%s Database name not available in config file.' % item('promtp_error')
    return False

  #
  # Construct SQL statement.
  #
  table_sql = ""
  for f in database['fields']:
    s = '%s %s, ' % (f['field_name'], f['type'])
    table_sql += s

  statement = 'CREATE TABLE IF NOT EXISTS %s(%sPRIMARY KEY (%s))' % (database['name'], table_sql, ", ".join(database['primary_key']))

  #
  # Make statements to the database.
  #
  try:
    scraperwiki.sqlite.execute(statement)
    scraperwiki.sqlite._State.new_transaction()
    print "%s table `%s` created." % (item('prompt_bullet'), str(database['name']))

  except Exception as e:
    print '%s Table `%s` could not be created.' % (item('prompt_error'), database['name'])
    if verbose:
      print e
    return False


if __name__ == '__main__':
  CreateDbAndTable()
