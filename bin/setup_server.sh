#!/bin/bash

#
# Download Python and its dependencies.
#
apt-get install python-setuptools python-dev python2.7-dev python-software-properties libpq-dev
apt-get install build-essential libssl-dev libffi-dev python-dev gcc-4.6-base cpp-4.6 libgomp1 libquadmath0 libc6-dev
apt-get install cron
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py
pip install virtualenv


#
# Add cronjob configuration.
#
printf "Installing crontab.\n"
crontab -l | { cat; echo "*/1 * * * * bash ~/check-my-bike/bin/collect_station.sh"; } | crontab -
