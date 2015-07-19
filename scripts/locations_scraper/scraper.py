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


def ScrapeMotivateWebsite(verbose=True):
  '''Scrapes the Motivate website for information about their bike sharing programs.'''

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
    all_city_data = []
    i = 0
    for table in tables:
      #
      # Build output.
      #
      iterator = {
        'name': city_list[i],
        table.findAll('th')[1].string: int(table.findAll('td')[0].string.replace(',', '')),
        table.findAll('th')[2].string: int(table.findAll('td')[1].string.replace(',', ''))
        }

      i += 1

      all_city_data.append(iterator)

    #
    # Find links with BeautifulSoup.
    #
    links = soup.find_all("div", class_="content")
    i = 0
    for link in links:
      all_city_data[i]['program_website'] = link.find('a').get('href')
      all_city_data[i]['company_logo_url'] = 'http://www.motivateco.com' + link.findAll('img')[0].get('src')
      all_city_data[i]['bike_image_url'] = 'http://www.motivateco.com' + link.findAll('img')[0].get('src')

      #
      # Get current time.
      #
      d = datetime.now()
      all_city_data[i]['information_last_updated'] = str(d.strftime('%Y-%m-%d %H:%M'))

      i += 1


    return all_city_data


  except Exception as e:
    print "%s Failed to scrape data from Motivate's website" % item('prompt_error')
    print e
    return False


def StoreOutput(data, json_path, verbose=True):
  '''Store the output into the local configuration JSON file.'''

  try:
    with open(json_path, 'w') as out_file:
       json.dump(data, out_file)

    print '%s Stored data in JSON successfully.\n' % item('prompt_success')

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

  else:
    StoreOutput(data, 'test.json')

if __name__ == '__main__':
  Main()
