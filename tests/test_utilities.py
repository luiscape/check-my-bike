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

  def test_config_files_have_correct_structure(self):
    d = Config.LoadConfig('dev.json')
    p = Config.LoadConfig('prod.json')
    assert 'database' in d.keys()
    assert 'database' in p.keys()

    #
    # Test database config structure.
    #
    assert 'name' in d['database']
    assert 'fields' in d['database']
    assert 'primary_key' in d['database']

    assert 'name' in p['database']
    assert 'fields' in p['database']
    assert 'primary_key' in p['database']
