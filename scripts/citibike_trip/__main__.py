#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import datetime
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from datetime import date
from utilities.prompt_format import item
from citibike_download.download import DownloadPackageFromCitiBike
from citibike_download.extract import UnzipPackageFromCitiBike
from citibike_download.process import IngestCitiBikeData


def Main():
  '''Wrapper.'''

  #DownloadPackageFromCitiBike(verbose=True)
  #UnzipPackageFromCitiBike(verbose=True)
  IngestCitiBikeData(verbose=True)


if __name__ == '__main__':
  Main()
