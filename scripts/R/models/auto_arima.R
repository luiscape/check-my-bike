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

FitArimaModel <- function(production_model=FALSE, forecast_minutes=30) {

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

  #
  # Making the model.
  #
  if (production_model) {
    time_series_data <- ts(model_data, start(1))
    bikes_arima <- auto.arima(time_series_data)
    forecast_bikes <- forecast.Arima(bikes_arima, h=forecast_minutes)

    #
    # Making plot
    #
    return(forecast_bikes)
  }

  #
  # Returning the model for train sets only.
  #
  else {
    time_series_data <- ts(model_data, start(1))
    train_data <- window(time_series_data, start=1, end=round(nrow(time_series_data) * .80))
    test_data <- window(time_series_data, start=round(nrow(time_series_data) * .80) + 1)
    bikes_arima <- auto.arima(train_data)
    forecast_bikes <- forecast.Arima(bikes_arima, h=forecast_minutes)
    arima_rmse <- accuracy(forecast_children, test_data)[,2]

  }

  return(data.frame(arima_rmse))

}
