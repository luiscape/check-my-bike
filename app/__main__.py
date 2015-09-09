# #!/usr/bin/python
# # -*- coding: utf-8 -*-

import sys
import run_scheduler
from termcolor import colored as color

__version__ = "v.0.2.2"

#
# Run the scheduler.
#
if __name__ == '__main__':

  print '--------------------------'
  print '|    %s    |' % color("ROLLTIME COLLECT", "blue", attrs=['bold'])
  print '|       [ %s ]      |' % color(__version__, "yellow", attrs=['bold'])
  print '--------------------------'

  run_scheduler.RunScheduler()
