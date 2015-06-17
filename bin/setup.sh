#!/bin/bash

#
# Installing Python dependencies.
#
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install requests[security]

#
# Configuring application.
#
python scripts/setup_app/
python scripts/citi_download/
