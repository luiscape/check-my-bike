#
# Creating the forecasting model.
#
library(MASS)
library(dplyr)
library(forecast)

#
# Loading helper functions.
#
source('scripts/R/helpers/read_table.R')

FitRandomWalkModel <- function(production_model=FALSE, station_id=445, forecast_minutes=30) {

  #
  # Load data.
  #
  data <- ReadTable('station_processed', deploy=FALSE)
  data <- filter(data, id == station_id)

  #
  # Organizing the model data.frame
  #
  model_data <- data$availableBikesRatio

  if (production_model) {
    #
    # Calculate model.
    #
    time_series_data <- ts(model_data, start=1, frequency=1440)
    random_walk_forecast <- rwf(time_series_data, h=forecast_minutes, drift=FALSE)

    #
    # Generate plot.
    #
    return(random_walk_forecast)
  }

  else {
    time_series_data <- ts(model_data, start=1, frequency=1440)
    train_data <- window(time_series_data, from=1, to=round(length(time_series_data) * .80))
    test_data <- window(time_series_data, from=round(length(time_series_data) * .80) + 1)
    random_walk_forecast <- rwf(train_data, h=forecast_minutes, drift=FALSE)
    forecast_bikes <- forecast(random_walk_forecast, h=forecast_minutes)
    random_walk_rmse <- accuracy(forecast_bikes, test_data)[,2]
  }

  return(data.frame(random_walk_rmse))
}
