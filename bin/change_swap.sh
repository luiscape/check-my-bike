#!/bin/bash

#
# R is in need of more swap memory.
# The solution was found here:
# https://github.com/wcyuan/data-science-courses
#

# make the swap.  this will only last until the machine is rebooted
sudo /bin/dd if=/dev/zero of=/swapfile bs=1024 count=256k
sudo /sbin/mkswap /swapfile

# results in:
# Setting up swapspace version 1, size = 262140 KiB
# no label, UUID=2193e5eb-0482-420c-9a7d-53558084fd06

sudo /sbin/swapon /swapfile

# To turn off the swap, run:
# sudo /sbin/swapoff /swapfile

# To make it use this swap every time the machine is started
# Add this to /etc/fstab:
/swapfile swap swap defaults 0 0
