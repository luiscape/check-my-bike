#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from datetime import date
from utilities.prompt_format import item


def UnzipPackageFromCitiBike(package=None, verbose=False):
  '''Unzip the packages downloaded from CitiBike.'''

  data_dir = os.path.join('data', 'historic')
  for file in os.listdir(data_dir):
    if file.endswith(".zip"):

      #
      # Unzipping packages.
      #
      zfile = zipfile.ZipFile(os.path.join(data_dir, file))
      print "%s Decompressing %s." % (item('prompt_bullet'), file)

      try:
        zfile.extractall(data_dir)
        os.remove(os.path.join(data_dir, file))  # remove zip if success.

      except Exception as e:
        print '%s Could not unzip file %s.' % (item('prompt_error'), file)
        if verbose:
          print e
