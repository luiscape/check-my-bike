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
# Installing R.
#
apt-get install libcurl4-gnutls-dev
apt-get install libxml2 libxml2-dev
codename=$(lsb_release -c -s)
echo "deb http://cran.fhcrc.org/bin/linux/ubuntu $codename/" | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
sudo add-apt-repository ppa:marutter/rdev
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install r-base r-base-dev
printf "Now run in R: install.packages(c('sqldf', 'dplyr', 'devtools', 'ggplot2', 'httpuv')) \n"

#
# Add cronjob configuration.
#
printf "Installing crontab.\n"
crontab -l | { cat; echo "*/1 * * * * bash ~/check-my-bike/bin/collect_station.sh"; } | crontab -
