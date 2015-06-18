#
# Run the model on an API.
#
#
# Author: Luis Capelo | luiscape@gmail.com
#


library(rapier)

r <- rapier('scripts/R/model.R')
r$run(port=8000)
