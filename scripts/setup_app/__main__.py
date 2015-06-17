#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from setup_app import db as Db
from utilities.prompt_format import item

def Main():
  '''Wrapper.'''
  try:
    Db.CreateDbAndTable(table_name='historic')

  except Exception as e:
    print '%s Database configuration failed' % item('prompt_error')


  print '%s Database configured successfully.\n' % item('prompt_success')



if __name__ == '__main__':
  Main()
