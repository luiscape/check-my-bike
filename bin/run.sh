#!/bin/bash

#
# Run defaults in dev mode.
#
export HOST_DATABASE='192.168.59.103'

#
# Run the application.
#
source venv/bin/activate
python app/
