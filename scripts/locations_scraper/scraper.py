#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import requests
import schedule
from datetime import datetime

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from bs4 import BeautifulSoup
from utilities.prompt_format import item
from utilities.load_config import LoadConfig
from utilities.store_records import StoreRecords


def ScrapeMotivateWebsite(verbose=True):
  '''Scrapes the Motivate website for information about their bike sharing programs.'''

  print "%s Scraping Motivate's website for program metadata." % item('prompt_bullet')

  #
  # Load config data.
  #
  location_data = LoadConfig('locations.json')
  if location_data == False:
    return False

  try:

    #
    # Download data from Motivate's website.
    #
    u = 'http://www.motivateco.com/locations'
    r = requests.get(u)

    #
    # Find data with BeautifulSoup.
    #
    soup = BeautifulSoup(r.content, 'html.parser')
    tables = soup.findAll("table")
    city_list = ["seattle", "toronto", "columbus", "bay_area", "chicago", "new_york", "chattanooga", "boston", "washington", "melbourne" ]
    i = 0
    for table in tables:

      #
      # Add output to the location data.
      #
      location_data[i]['bikes'] = int(table.findAll('td')[0].string.replace(',', ''))
      location_data[i]['stations'] = int(table.findAll('td')[0].string.replace(',', ''))

      i += 1


    #
    # Find links with BeautifulSoup.
    #
    links = soup.find_all("div", class_="content")
    i = 0
    for link in links:
      location_data[i]['program_website'] = link.find('a').get('href')
      location_data[i]['company_logo_url'] = 'http://www.motivateco.com' + link.findAll('img')[0].get('src')
      location_data[i]['bike_image_url'] = 'http://www.motivateco.com' + link.findAll('img')[0].get('src')

      #
      # Get current time.
      #
      d = datetime.now()
      location_data[i]['information_last_updated'] = str(d.strftime('%Y-%m-%d %H:%M'))

      i += 1


    return location_data


  except Exception as e:
    print "%s Failed to scrape data from Motivate's website" % item('prompt_error')
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

  else:
    if StoreRecords(data=data, table='location', verbose=True) == False:
      return False

    print '%s Scraped program / location data successfully.\n' % item('prompt_success')

