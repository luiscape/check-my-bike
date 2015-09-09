#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import mock
import unittest
from mock import patch

from scripts.status import send as Send

class TestNodeWatchNotifier(unittest.TestCase):
  '''Testing that the collector sends data correclty to Node Watch.'''

  def test_request_doesnt_fail(self):
    assert Send.SendStatus('ok') != False
    assert Send.SendStatus('error') != False

  def test_request_fails(self):
    assert Send.SendStatus(address='http://foo.bar.baz') == False


