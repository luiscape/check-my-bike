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

#
# Install R dependencies.
#
printf "Now run in R: install.packages(c('sqldf', 'dplyr', 'devtools', 'ggplot2', 'httpuv')) \n"
