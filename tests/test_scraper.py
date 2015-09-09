# #!/usr/bin/python
# # -*- coding: utf-8 -*-

import os
import sys
import mock
import unittest
from mock import patch

from scripts.utilities import load_config as Config
from scripts.locations_scraper import scraper as Scraper


class CheckMotivateScraper(unittest.TestCase):
  '''Tests that the scraper to Motivate's website works as expected.'''

  def test_wrapper_function_doesnt_fail(self):
    assert Scraper.ScrapeMotivateWebsite() != False


