#
# Model what time I would have to
# leave to catch a bike or a dock.
#
#
# Author: Luis Capelo | luiscape@gmail.com
#

library(dplyr)

source('scripts/R/helper/read_table.R')

#' @get /status
ShowCurrentStatus <- function(station_id=445) {
  
  #
  # Sanity check.
  #
  if (is.null(id)) stop('Provide an id.')
  
  #
  # Load data.
  #
  data <- ReadTable('station_processed')
  
  #
  # Show current status of prefered station.
  #
  preferred_station <- data %>% 
    filter(executionTime == max(executionTime)) %>%
    filter(id == station_id)
  
  list(preferred_station)
  
  return(preferred_station)
  
}

ShowCurrentStatus()