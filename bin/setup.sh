#!/bin/bash

#
# Installing Python dependencies.
#
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

#
# Configuring application.
#
python scripts/setup_app/

#
# Collect data about
# different locations.
#
# python scripts/locations_scraper/
