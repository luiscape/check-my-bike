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
    assert Config.LoadConfig('dev.json', True) != False

  def test_config_files_have_correct_structure(self):
    d = Config.LoadConfig('dev.json')
    p = Config.LoadConfig('prod.json')
    assert 'database' in d.keys()
    assert 'database' in p.keys()

    #
    # Test database config structure.
    #
    for table in d['database']:
      assert 'name' in table.keys()
      assert 'fields' in table.keys()
      assert 'primary_key' in table.keys()

    for table in p['database']:
      assert 'name' in table.keys()
      assert 'fields' in table.keys()
      assert 'primary_key' in table.keys()
