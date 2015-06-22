#!/bin/bash

#
# Installing Python dependencies.
#
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install requests[security]

## Installing sandman from source.
git clone https://github.com/jeffknupp/sandman
cd sandman
python setup.py install
rm -rf sandman

#
# Configuring application.
#
# python scripts/setup_app/
# python scripts/citi_download/
