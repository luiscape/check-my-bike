#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import app

if __name__ == '__main__':

  if sys.argv[1] == 'scheduler':
    app.RunScheduler()
