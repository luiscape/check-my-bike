#!/bin/bash

#
# Collect CitiBike station data every minute.
#
source venv/bin/activate
python app scheduler
