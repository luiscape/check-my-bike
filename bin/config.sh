#!/bin/bash


source venv/bin/activate

#
# Configuring application.
#
python scripts/setup_app/

#
# Collect data about
# different locations.
#
python scripts/locations_scraper/
