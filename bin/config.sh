#!/bin/bash


source venv/bin/activate

#
# Configuring application.
#
python scripts/setup_app/

#
# Collect data from
# different location programs.
#
python scripts/locations_scraper/


#
# Run application.
#
python app/
