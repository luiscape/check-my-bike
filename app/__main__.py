# #!/usr/bin/python
# # -*- coding: utf-8 -*-

import sys
import server
import run_scheduler

if __name__ == '__main__':

  #
  # If command provided
  # run the collector.
  #
  try:
    command = sys.argv[1]

    if command == 'scheduler':
      run_scheduler.RunScheduler()

  except Exception as e:
    pass

  #
  # If no command
  # provided run API server.
  #
  server.Main()
