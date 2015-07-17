#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import requests
import schedule

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from bs4 import BeautifulSoup
from utilities.prompt_format import item


def ScrapeMotivateWebsite(verbose=True):
  '''Scrapes the Motivate website for information about their bike sharing programs.'''

  try:

    #
    # Download data from Motivate's website.
    #
    u = 'http://www.motivateco.com/locations'
    r = requests.get(u)

    #
    # TODO: Load config file.
    #

    #
    # Parse it with beautiful soup.
    #
    soup = BeautifulSoup(r.content, 'html.parser')
    tables = soup.findAll("table")
    city_list = ["seattle", "toronto", "columbus", "bay_area", "chicago", "new_york", "chattanooga", "boston", "washington", "melbourne" ]
    all_city_data = []
    i = 0
    for table in tables:
      #
      # Build output.
      #
      test = {
        'name': city_list[i],
        table.findAll('th')[1].string: table.findAll('td')[0].string,
        table.findAll('th')[2].string: table.findAll('td')[1].string
        }

      i += 1

      all_city_data.append(test)

    print all_city_data




  except Exception as e:
    print "%s Failed to scrape data from Motivate's website" % item('prompt_error')
    print e
    return False


def StoreOutput():
  '''Store the output into the local configuration JSON file.'''

  try:
    print 'nothing yet'

  except Exception as e:
    print '%s Failed to store data in JSON.' % item('prompt_error')
    print e
    return False

def Main():
  '''Wrapper.'''

  try:
    data = ScrapeMotivateWebsite()

  except Exception as e:
    print '%s Motivate scraper failed.' % item('prompt_error')
    print e
    return False

  #
  # Check for failures.
  #
  if data == False:
    print '%s Motivate scraper failed.' % item('prompt_error')
    return False


if __name__ == '__main__':
  Main()
