setwd("<set dir here>\\scripts and data")

require(jsonlite)
require(randomForest)
require(h2o)

source("feature_eng.R")
feature_building()

source("learning_final.R")
models <- learning_stage(final_date = "2015-08-19", max_mem_size_h2o = '4g')

