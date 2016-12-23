learning_stage <- function(final_date = "2015-08-19", max_mem_size_h2o = '4g') {
  
  set.seed(998)
  
  train.data <- read.csv("features_train_phase2.csv",sep=",")
  test.data <- read.csv("features_test_phase2.csv",sep=",")
  
  train.data$date <- strptime(x = as.character(train.data$date), tz="US/Eastern", format = "%Y-%m-%d")
  original.train.date <- train.data$date
  test.data$date <- strptime(x = as.character(test.data$date), tz="US/Eastern", format = "%Y-%m-%d")
  original.test.date <- test.data$date
  
  # There are many variables that should be converted to factors
  tofactors <- c("month","year","isRestaurant","isFood","isPizza","isBars",
                 "isPubs","isSandwiches","isChinese","isDelis","isItalian",
                 "isCoffeeTea","isMexican","isNightlife","isAmericanTrad",
                 "isBB","isAmericanNew","isSeafood","isIceCream","isJapanese",
                 "isFastFood","isDonuts","isBurgers","isSushiBars","isThai",
                 "isLounges","isFrench","isBakeries","isIndian","isLatinAmerican",
                 "isSteakhouses","isMiddleEastern","isCaterers","isEventPlanning",
                 "isVietnamese","isAsianFusion","isDanceClubs","isSportsBars","isArts",
                 "isDiveBars","open","city","SouthBoston","isChinatown","Dorchester",
                 "Downtown","JamaicaPlain","SouthEnd","BeaconHill","Waterfront",
                 "FinancialDistrict","NorthEnd","EastBoston","BackBay","Roslindale",
                 "WestRoxburyCenter","WestRoxbury","AllstonBrighton","HydePark","DudleySquare",
                 "UphamsCorner","MissionHill","FieldsCorner","Mattapan","LeatherDistrict",
                 "Charlestown","Fenway","EglestonSquare")
  
  train.data[,tofactors] <- lapply(train.data[,tofactors], factor)
  train.data$date <- as.POSIXlt(final_date, format="%Y-%m-%d") - as.POSIXlt(train.data$date, format="%Y-%m-%d")
  train.data$date <- as.numeric(train.data$date / 1000) #Scale for factors
  
  test.data[,tofactors] <- lapply(test.data[,tofactors], factor)
  test.data$date <- as.POSIXlt(final_date, format="%Y-%m-%d") - as.POSIXlt(test.data$date, format="%Y-%m-%d")
  test.data$date <- as.numeric(test.data$date / 1000) #Scale for factors
  
  # Generate three training subsets, one for each target, and a test set
  train.data$X <- NULL
  training1 <- subset(train.data, train.data$X. < 10 )
  training1$X.. <- NULL
  training1$X... <- NULL
  
  training2  <- subset(train.data, train.data$X. < 10 )
  training2$X. <- NULL
  training2$X... <- NULL
  
  training3 <- subset(train.data, train.data$X. < 10 )
  training3$X. <- NULL
  training3$X.. <- NULL
  
  testing <- test.data
  
  # Let's transforma the NA values with the roughfix function
  training1 <- na.roughfix(training1)
  training2 <- na.roughfix(training2)
  training3 <- na.roughfix(training3)
  testing <- na.roughfix(testing)
  
  
  localH2O <- h2o.init(nthreads = -1,max_mem_size = max_mem_size_h2o)
  
  message("Converting the data sets to suitable h2o formats...")
  test.hex <- as.h2o(localH2O,testing)
  train1.hex <- as.h2o(localH2O,training1)
  train2.hex <- as.h2o(localH2O,training2)
  train3.hex <- as.h2o(localH2O,training3)
  
  message("Computing gbm model for first target...")
  gbmmodel1 <- h2o.gbm(x=c(1:2, 4:124),y = 3,data = train1.hex, distribution="gaussian",
                       n.trees=10000, shrinkage = 0.01, importance=T)
  
  message("Computing gbm model for second target...")
  gbmmodel2 <- h2o.gbm(x=c(1:2, 4:124),y = 3,data = train2.hex, distribution="gaussian",
                       n.trees=10000, shrinkage = 0.01, importance=T)
  
  message("Computing gbm model for third target...")
  gbmmodel3 <- h2o.gbm(x=c(1:2, 4:124),y = 3,data = train3.hex, distribution="gaussian",
                       n.trees=10000, shrinkage = 0.01, importance=T)
  
  p1 <- as.data.frame(h2o.predict(gbmmodel1,test.hex))
  p2 <- as.data.frame(h2o.predict(gbmmodel2,test.hex))
  p3 <- as.data.frame(h2o.predict(gbmmodel3,test.hex))
  
  message("Computing random forest model for first target...")
  rfmodel1 <- h2o.randomForest(x=c(1:2, 4:124),y = 3,data = train1.hex,
                               mtries=25, ntree=3000, seed=998, classification=FALSE,
                               importance=TRUE, type="BigData" )
  p4 <- as.data.frame(h2o.predict(rfmodel1,test.hex))
  
  message("Computing random forest model for second target...")
  rfmodel2 <- h2o.randomForest(x=c(1:2, 4:124),y = 3,data = train2.hex,
                               mtries=25, ntree=3000, seed=998, classification=FALSE,
                               importance=TRUE, type="BigData")
  p5 <- as.data.frame(h2o.predict(rfmodel2,test.hex))
  
  message("Computing random forest model for third target...")
  rfmodel3 <- h2o.randomForest(x=c(1:2, 4:124),y = 3,data = train3.hex,
                               mtries=25, ntree=3000, seed=998, classification=FALSE,
                               importance=TRUE, type="BigData")
  p6 <- as.data.frame(h2o.predict(rfmodel3,test.hex))
  
  final.submission <- read.csv("PhaseIISubmissionFormat.csv",sep=",")
  
  # Sometimes h2o's gbm predicts negative values, let's set them to zero
  for(i in 1:length(p1[,1])) {
    
    if(p1[i,1] < 0 )
      p1[i,1] = 0
    if(p2[i,1] < 0 )
      p2[i,1] = 0
    if(p3[i,1] < 0 )
      p3[i,1] = 0
  }
  
  final.submission$X. <- round( (p1[,1] + p4[,1])/2 )
  final.submission$X.. <- round( (p2[,1] + p5[,1])/2 )
  final.submission$X... <- round( (p3[,1] + p6[,1])/2 )
  
  message("Writing final submission file sub_2_PhaseII_h20.csv...")
  write.csv(final.submission, "sub_2_PhaseII_h20.csv", row.names=FALSE)
  
  output <- list(gbmmodel1,gbmmodel2,gbmmodel3,rfmodel1,rfmodel2,rfmodel3)
  return(output)
}