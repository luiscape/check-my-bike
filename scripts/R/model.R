#
# Model what time I would have to
# leave to catch a bike or a dock.
#
#
# Author: Luis Capelo | luiscape@gmail.com
#

library(dplyr)

source('scripts/R/models/auto_arima.R')
source('scripts/R/helpers/read_table.R')

#' @get /status
ShowCurrentStatus <- function(station_id=445, deploy_api=FALSE) {

  #
  # Sanity check.
  #
  if (is.null(id)) stop('Provide an id.')

  #
  # Load data.
  #
  data <- ReadTable('station_processed', deploy=FALSE)

  #
  # Show current status of prefered station.
  #
  preferred_station <- data %>%
    filter(executionTime == max(executionTime)) %>%
    filter(id == station_id)

  list(preferred_station)

}



#
# Generate forecast data.
#

#' @get /forecast
GenerateForecastOutput <- function() {

  #
  # Load original data.
  #
  data <- ReadTable('station_processed', deploy=FALSE)

  #
  # Forecast table.
  #
  forecast_data <- data.frame(FitArimaModel(production_model=TRUE))

  #
  # Creating school children plot.
  #
  list(head(forecast_data))

}
