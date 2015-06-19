#
# Wrapper script.
#

library(dplyr)
library(reshape2)

#
# Importing models.
#
source('scripts/R/models/auto_arima.R')
source('scripts/R/models/random_walk.R')
source('scripts/R/helpers/read_table.R')

MeasureModels <- function() {
  
  #
  # Models used.
  #
  models = c(FitRandomWalkModel(), FitArimaModel())
  
  #
  # Generating output
  #
  for (i in 1:length(models)) {
    data <- models[i]
    if (i == 1) out <- data
    else out <- cbind(out, data)
  }
  
  #
  # Comparing
  #
  out$sets <- c("Training set", "Test set")
  out <- as.data.frame(out)
  names(out) <- c('Arima RMSE', 'Random Walk RMSE', 'Sets')
  
  #
  # Selecting the best model
  #
  best_model <-  melt(out, id.vars="Sets") %>%
    group_by(Sets) %>%
    filter(Sets == "Test set") %>%
    filter(value == min(value))
  
  #
  # Running results.
  #
  print(paste('The best model is', best_model$variable))
  return(out)
}