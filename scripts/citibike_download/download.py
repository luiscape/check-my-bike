#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile
import datetime
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from datetime import date
from utilities.prompt_format import item


def DownloadPackageFromCitiBike(from_date=None, verbose=False):
  '''Downloads a data package from CitiBike based on a date input.
     If no specific date is provided it will attempt to download
     all the packages available.'''

  if from_date is None:
    if verbose:
      print '%s No from date provided. Downloading all data packages.' % item('prompt_warn')
  else:
    print "%s Downloading package from date %s from CitiBike." % (item('prompt_bullet'), from_date)
  #
  # Build url list.
  #
  # 2013
  url_list = []
  for n in range(7, 12):
    if len(str(n)) == 1:
      n = '0' + str(n)
    m = '2013%s' % n
    u = 'https://s3.amazonaws.com/tripdata/%s-citibike-tripdata.zip' % m
    url_list.append(u)

  # 2014
  for n in range(1, 12):
    if len(str(n)) == 1:
      n = '0' + str(n)
    m = '2014%s' % n
    u = 'https://s3.amazonaws.com/tripdata/%s-citibike-tripdata.zip' % m
    url_list.append(u)

  # 2015
  c = date.today().month
  for n in range(1, c):
    if len(str(n)) == 1:
      n = '0' + str(n)
    m = '2015%s' % n
    u = 'https://s3.amazonaws.com/tripdata/%s-citibike-tripdata.zip' % m
    url_list.append(u)

  if verbose:
    print "%s URL list assembled. Downloading %s packages." % (item('prompt_bullet'), str(len(url_list)))

  #
  # Downloading.
  #
  try:
    for url in url_list:
      file_name = os.path.join('data', 'historic', os.path.split(url)[1])
      with open(file_name, 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
          print "%s Attempt to download resource %s failed." % (item('prompt_error'), url)
          os.remove(file_name)  # removing problematic file.
          return

        for block in response.iter_content(1024):
          if not block:
            break

          handle.write(block)

        print '%s %s done downloading.' % (item('prompt_bullet'), os.path.split(file_name)[1])

  except Exception as e:
    print '%s There was an error downlaoding the file.' % item('prompt_error')
    if verbose:
      print e
    return False


