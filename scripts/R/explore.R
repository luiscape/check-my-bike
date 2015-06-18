#
# Explore the CitiBike station data to get
# familiar with its properties.
#
#
# Author: Luis Capelo | luiscape@gmail.com
#

library(ggplot2)

source('scripts/R/helper/read_table.R')

#
# Load data.
#
data <- ReadTable('station_processed')

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
