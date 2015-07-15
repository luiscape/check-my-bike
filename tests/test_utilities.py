#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import mock
import unittest
import scraperwiki
from mock import patch

from scripts.utilities import load_config as Config



class CheckLoadConfig(unittest.TestCase):
  '''Testing the process of creating a database.'''

  def test_load_config_doesnt_fail(self):
    assert Config.LoadConfig('dev.json') != False

  # def test_tables_exist(self):
  #   tables = scraperwiki.sqlite.show_tables()
  #   assert 'FCS' in tables.keys()
  #   assert 'CSI' in tables.keys()
  #   assert 'Income' in tables.keys()
