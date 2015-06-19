#
# Process CitiBike station data in order to model
# more effectively its predictions.
#
#
# Author: Luis Capelo | luiscape@gmail.com
#

library(dplyr)
library(sqldf)
library(lubridate)


source('scripts/R/helper/read_table.R')
source('scripts/R/helper/write_table.R')

#
# Prepare data for modeling.
#
CleanData <- function(df=NULL) {

  #
  # Select variables of interest.
  #
  s = select(df, id, availableDocks, totalDocks, statusValue, availableBikes, lastCommunicationTime, executionTime)

  #
  # Transforming numeric types.
  #
  s$totalDocks <- as.numeric(s$totalDocks)
  s$availableDocks <- as.numeric(s$availableDocks)
  s$availableBikes <- as.numeric(s$availableBikes)

  #
  # Transforming time.
  #
  s$executionTime <- as.POSIXct(s$executionTime)
  s$lastCommunicationTime <- as.POSIXct(s$lastCommunicationTime)
  s$week <- week(s$executionTime)
  s$weekDay <- wday(s$executionTime)

  #
  # Adding ratios.
  #
  s$availableDocksRatio <- s$availableDocks / s$totalDocks
  s$availableBikesRatio <- s$availableBikes / s$totalDocks
  s$availabilityRatio <- s$availableDocksRatio + s$availableBikesRatio
  s$usageRatio <- 1 - (s$availableDocksRatio + s$availableBikesRatio)

  return(s)
}

#
# Wrapper.
#
ProcessData <- function() {

  cat('----------------------------\n')
  cat('Preparing data for model.\n')
  cat('----------------------------\n')
  #
  # Load.
  #
  cat('Loading data | ')
  data <- ReadTable('station', deploy=FALSE)
  cat('DONE.\n')

  #
  # Process.
  #
  cat('Processing data | ')
  processed_data <- CleanData(data)
  cat('DONE.\n')

  #
  # Store.
  #
  cat('Storing processed data in database | ')
  WriteTable(processed_data, 'station_processed', overwrite=TRUE)
  cat('DONE.\n')
  
  cat('----------------------------\n')
}
