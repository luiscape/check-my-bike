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

FitArimaModel <- function(production_model=FALSE, station_id=445, forecast_minutes=30) {

  #
  # Load data.
  #
  data <- ReadTable('station_processed', deploy=FALSE)
  data <- filter(data, id == station_id)
  
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
    time_series_data <- ts(model_data, start(1), frequency=1440)
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
    time_series_data <- ts(model_data, start=1)
    train_data <- window(time_series_data, start=1, frequency=1440, end=round(nrow(time_series_data) * .80))
    test_data <- window(time_series_data, start=round(nrow(time_series_data) * .80) + 1, frequency=1440)
    bikes_arima <- auto.arima(train_data)
    forecast_bikes <- forecast.Arima(bikes_arima, h=forecast_minutes)
    arima_rmse <- accuracy(forecast_bikes, test_data)[,2]

  }

  return(data.frame(arima_rmse))

}
