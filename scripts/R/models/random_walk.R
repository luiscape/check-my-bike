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

FitRandomWalkModel <- function(production_model=FALSE, forecast_minutes=30) {

  #
  # Load data.
  #
  data <- ReadTable('station_processed', deploy=deploy_api)

  #
  # Organizing the model data.frame
  #
  model_data <- data.frame(
    available_bike_ratio = data$availableBikesRatio
  )

  if (production_model) {
    #
    # Calculate model.
    #
    time_series_data <- ts(lm_data$children_pop, start(1950))
    random_walk_forecast <- rwf(time_series_data, h=25, drift=FALSE)

    #
    # Generate plot.
    #
    return(random_walk_forecast)
  }

  else {
    time_series_data <- ts(model_data, start(1))
    train_data <- window(time_series_data, start=1, end=round(nrow(time_series_data) * .80))
    test_data <- window(time_series_data, start=round(nrow(time_series_data) * .80) + 1)
    random_walk_forecast <- rwf(train_data, h=forecast_minutes, drift=FALSE)
    forecast_bikes <- forecast(random_walk_forecast, h=forecast_minutes)
    random_walk_rmse <- accuracy(forecast_bikes, test_data)[,2]
  }

  return(data.frame(random_walk_rmse))
}
