#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import scraperwiki

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item

def CreateDbAndTable(table_name=None, verbose=True):
  '''Creating tables in SQLite database.'''

  if table_name == None:
    print '%s Please provide table name.' % item('promtp_error')
    return False

  #
  # This creates a 'generic' schema in which
  # all fields are text. Better schemas
  # should be provided in the config files.
  #
  schema = ["'tripduration'","'starttime'","'stoptime'","'start station id'","'start station name'","'start station latitude'","'start station longitude'","'end station id'","'end station name'","'end station latitude'","'end station longitude'","'bikeid'","'usertype'","'birth year'","'gender'"]
  statement = " TEXT, ".join(schema)
  statement = 'CREATE TABLE IF NOT EXISTS %s(%s TEXT)' % (table_name, statement)

  try:
    scraperwiki.sqlite.execute(statement)
    scraperwiki.sqlite._State.new_transaction()
    print "%s table `%s` created." % (item('prompt_bullet'), str(table_name))

  except Exception as e:
    print '%s Table `%s` could not be created.' % (item('prompt_error'), table_name)
    if verbose:
      print e
    return False

