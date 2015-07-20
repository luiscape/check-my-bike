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

    #
    # Test base structure.
    #
    d = Config.LoadConfig('dev.json')
    assert 'database' in d.keys()

    p = Config.LoadConfig('prod.json')
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

  def test_config_file_cities_have_right_structure(self):

    #
    # Load config files.
    #
    c = Config.LoadConfig('locations.json')

    #
    # Make sure that all the
    # city fields
    #
    expected_fields = ["city", "state", "country", "bikes", "stations", "company_name", "company_logo_url", "bike_image_url", "information_last_updated", "program_website"]
    for city in c:
      for f in expected_fields:
        assert f in city.keys()




