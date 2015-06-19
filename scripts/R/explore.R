#
# Explore the CitiBike station data to get
# familiar with its properties.
#
#
# Author: Luis Capelo | luiscape@gmail.com
#

library(scales)
library(ggplot2)

source('scripts/R/helper/read_table.R')

#
# Load data.
#
data <- ReadTable('station_processed', deploy=FALSE)

#
# Checking ratios
#
qplot(data$availableDocksRatio)
qplot(filter(data, usageRatio > 0)$usageRatio)

#
# Checking bike ratio per
# observation time.
#
ggplot(filter(data, availableBikesRatio > 0)) +
  geom_bar(aes(availableBikesRatio), stat='bin') +
  facet_wrap(~ executionTime)

#
# Checking a time-series of ratios in
# a single dock.
#
CheckTimeSeries <- function(station_id=NULL) {
  
  filtered_data <- filter(data, id == station_id)
  filtered_data$executionTime <- as.POSIXct(filtered_data$executionTime, origin='1970-01-01')
  ggplot(filtered_data) + 
    geom_point(aes(executionTime, availableBikesRatio), color='#FFFFFF', stat='identity', size=1.4) +
    geom_point(aes(executionTime, availableBikesRatio), stat='identity', size=3) +
    geom_bar(aes(executionTime, availableBikesRatio), stat='identity', size=1.3)
  
  ggplot(filtered_data) + 
    #geom_point(aes(executionTime, availableDocks), stat='identity', size=3) +
    geom_bar(aes(executionTime, availableDocks), stat='identity')
}

