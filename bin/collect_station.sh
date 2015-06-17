#!/bin/bash

#
# Collect CitiBike station data every minute.
#
cd ~/check-my-bike/
source venv/bin/activate
python scripts/citibike_station/
