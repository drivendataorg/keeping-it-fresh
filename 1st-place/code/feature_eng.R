

feature_building <- function() {
  
  set.seed(998)
  
  message("Loading data files...","\r")
  
  
  matching <- read.csv("restaurant_ids_to_yelp_ids.csv",sep=",",encoding="UTF-8")
  business <- fromJSON(sprintf("[%s]", paste(readLines('yelp_academic_dataset_business.json'), collapse=",")))
  review <- fromJSON(sprintf("[%s]", paste(readLines('yelp_academic_dataset_review.json'), collapse=",")))
  review$date <- strptime(x = as.character(review$date), tz="US/Eastern", format = "%Y-%m-%d")
  
  train.labels <- read.csv("AllViolations.csv",sep=",",encoding="UTF-8")
  train.labels$date <- strptime(x = as.character(train.labels$date), tz="US/Eastern", format = "%Y-%m-%d")
  train.labels <- train.labels[order(train.labels$date),]
  train.labels$year <- train.labels$date$year+1900
  train.labels$quarter <-  as.factor(quarters(train.labels$date))
  train.labels$month <- train.labels$date$mon
  
  dates <- train.labels$date
  ids <- train.labels$id
  train.labels$id <- NULL
  
  submission <- read.csv("PhaseIISubmissionFormat.csv",sep=",")
  submission$date <- strptime(x = as.character(submission$date), tz="US/Eastern", format = "%Y-%m-%d")
  submission$id <- NULL
  submission$X. <- NULL
  submission$X.. <- NULL
  submission$X... <- NULL
  submission$year <- submission$date$year+1900
  submission$quarter <-  as.factor(quarters(submission$date))
  submission$month <- submission$date$mon
  
  
  # Join some variables of business to train.label
  train.labels$city <- train.labels$latitude <- train.labels$longitude <- 
    train.labels$review_count <- train.labels$open <- rep(NaN, nrow(train.labels))
  
  # Variables from review scores
  train.labels$mean.stars <- train.labels$median.stars <- 
    train.labels$sd.stars <- train.labels$max.score <- 
    train.labels$min.score <- rep(NaN, nrow(train.labels))
  train.labels$mean.review.length <- train.labels$sd.review.length <- rep(0, nrow(train.labels))
  
  # Infraction statistics
  train.labels$meanMin <- train.labels$meanMed <- train.labels$meanSev <- train.labels$medianMin <- 
    train.labels$medianMed <- train.labels$medianSev <- train.labels$sdMin <- train.labels$sdMed <- 
    train.labels$sdSev <- train.labels$lastMin <- train.labels$lastMed <- train.labels$lastSev <- rep(NaN, nrow(train.labels))
  
  # Restaurant characteristics
  train.labels$isRestaurant <- train.labels$isFood <- 
    train.labels$isPizza <- train.labels$isBars <-
    train.labels$isPubs <- train.labels$isSandwiches <- 
    train.labels$isChinese <- train.labels$isDelis <- 
    train.labels$isItalian <- train.labels$isCoffeeTea <-
    train.labels$isMexican <- train.labels$isNightlife <-
    train.labels$isAmericanTrad <- train.labels$isBB <-
    train.labels$isAmericanNew <- train.labels$isSeafood <-
    train.labels$isIceCream <- train.labels$isJapanese <-
    train.labels$isFastFood <- train.labels$isDonuts <-
    train.labels$isBurgers <- train.labels$isSushiBars <-
    train.labels$isThai <- train.labels$isLounges <-
    train.labels$isFrench <- train.labels$isBakeries <-
    train.labels$isIndian <- train.labels$isLatinAmerican <-
    train.labels$isSteakhouses <- train.labels$isMiddleEastern <-
    train.labels$isCaterers <- train.labels$isEventPlanning <-
    train.labels$isVietnamese <- train.labels$isAsianFusion <-
    train.labels$isDanceClubs <- train.labels$isSportsBars <-
    train.labels$isArts <- train.labels$isDiveBars <-rep("no", nrow(train.labels))
  
  # Restaurant location
  train.labels$isChinatown <- train.labels$Dorchester <- train.labels$Downtown <- 
    train.labels$JamaicaPlain <- train.labels$SouthEnd <- train.labels$BeaconHill <- 
    train.labels$Waterfront <- train.labels$SouthBoston <- train.labels$FinancialDistrict <- 
    train.labels$NorthEnd <- train.labels$EastBoston <- train.labels$BackBay <- 
    train.labels$Roslindale <- train.labels$WestRoxburyCenter <- train.labels$WestRoxbury <- 
    train.labels$AllstonBrighton <- train.labels$HydePark <- train.labels$DudleySquare <- 
    train.labels$UphamsCorner <- train.labels$MissionHill <- train.labels$FieldsCorner <- 
    train.labels$Mattapan <- train.labels$LeatherDistrict <- train.labels$Charlestown <- 
    train.labels$Fenway <- train.labels$EglestonSquare <- rep(0, nrow(train.labels))
  
  # Sentiment analysis features
  scored.review <- read.csv("review_sentiscored.csv", sep=",")
  train.labels$av.senti.diff <- train.labels$av.senti.ratio <- 
    train.labels$av.senti.positive <- train.labels$av.senti.negative <- 
    train.labels$max.senti.positive <- train.labels$min.senti.negative <- rep(NaN, nrow(train.labels))
  
  message("Building train set features based on restaurant characteristics and review scores...This might take a while.")
  pb   <- txtProgressBar(1, nrow(train.labels), style=3)
  
  for(i in 1:nrow(train.labels) ){  
    
    
    b_id <- match(train.labels$restaurant_id[i], matching[,1])
    b_id <- matching[b_id,2]
    
    train.labels$city[i] <- business$city[match(b_id, business$business_id)]
    train.labels$latitude[i] <- business$latitude[match(b_id, business$business_id)]
    train.labels$longitude[i] <- business$longitude[match(b_id, business$business_id)]
    train.labels$open[i] <- business$open[match(b_id, business$business_id)]
    
    # Extract variables from categories
    cats <- business$categories[match(b_id, business$business_id)]
    for(j in 1:length(cats[[1]])) {
      if(cats[[1]][j] == "Restaurants")
        train.labels$isRestaurant[i] = "yes"
      if(cats[[1]][j] == "Food")
        train.labels$isFood[i] = "yes"
      if(cats[[1]][j] == "Pizza")
        train.labels$isPizza[i] = "yes"
      if(cats[[1]][j] == "Bars")
        train.labels$isBars[i] = "yes"
      if(cats[[1]][j] == "Pubs")
        train.labels$isPubs[i] = "yes"
      if(cats[[1]][j] == "Sandwiches")
        train.labels$isSandwiches[i] = "yes"
      if(cats[[1]][j] == "Chinese")
        train.labels$isChinese[i] = "yes"
      if(cats[[1]][j] == "Delis")
        train.labels$isDelis[i] = "yes"
      if(cats[[1]][j] == "Italian")    
        train.labels$isItalian[i] = "yes"
      if(cats[[1]][j] == "Coffee & Tea")
        train.labels$isCoffeeTea[i] = "yes"
      if(cats[[1]][j] == "Mexican")
        train.labels$isMexican[i] = "yes"
      if(cats[[1]][j] == "Nightlife")
        train.labels$isNightlife[i] = "yes"
      if(cats[[1]][j] == "American (Traditional)")
        train.labels$isAmericanTrad[i] = "yes"
      if(cats[[1]][j] == "Breakfast & Brunch")
        train.labels$isBB[i] = "yes"
      if(cats[[1]][j] == "American (New)")
        train.labels$isAmericanNew[i] = "yes"
      if(cats[[1]][j] == "Seafood")
        train.labels$isSeafood[i] = "yes"
      if(cats[[1]][j] == "Ice Cream & Frozen Yogurt")
        train.labels$isIceCream[i] = "yes"
      if(cats[[1]][j] == "Japanese")
        train.labels$isJapanese[i] = "yes"
      if(cats[[1]][j] == "Fast Food")
        train.labels$isFastFood[i] = "yes"
      if(cats[[1]][j] == "Donuts")
        train.labels$isDonuts[i] = "yes"
      if(cats[[1]][j] == "Burgers")
        train.labels$isBurgers[i] = "yes"
      if(cats[[1]][j] == "Sushi Bars")
        train.labels$isSushiBars[i] = "yes"
      if(cats[[1]][j] == "Thai")
        train.labels$isThai[i] = "yes"
      if(cats[[1]][j] == "Lounges")
        train.labels$isLounges[i] = "yes"
      if(cats[[1]][j] == "French")
        train.labels$isFrench[i] = "yes"
      if(cats[[1]][j] == "Bakeries")
        train.labels$isBakeries[i] = "yes"
      if(cats[[1]][j] == "Indian")
        train.labels$isIndian[i] = "yes"
      if(cats[[1]][j] == "Latin American")
        train.labels$isLatinAmerican[i] = "yes"
      if(cats[[1]][j] == "Steakhouses")
        train.labels$isSteakhouses[i] = "yes"
      if(cats[[1]][j] == "Middle Eastern")
        train.labels$isMiddleEastern[i] = "yes"
      if(cats[[1]][j] == "Caterers")
        train.labels$isCaterers[i] = "yes"
      if(cats[[1]][j] == "Event Planning & Services")
        train.labels$isEventPlanning[i] = "yes"
      if(cats[[1]][j] == "Vietnamese")
        train.labels$isVietnamese[i] = "yes"
      if(cats[[1]][j] == "Asian Fusion")
        train.labels$isAsianFusion[i] = "yes"
      if(cats[[1]][j] == "Dance Clubs")
        train.labels$isDanceClubs[i] = "yes"
      if(cats[[1]][j] == "Sports Bars")
        train.labels$isSportsBars[i] = "yes"
      if(cats[[1]][j] == "Arts & Entertainment")
        train.labels$isArts[i] = "yes"
      if(cats[[1]][j] == "Dive Bars")
        train.labels$isDiveBars[i] = "yes"
    }
    
    # Get reviews for this restaurant that have a date prior to this inspection
    sub <- review[which(review$business_id == b_id),]
    sub_review <- subset(sub, sub$date <= train.labels$date[i])
    train.labels$review_count[i] <- nrow(sub_review)
    
    if(nrow(sub_review) > 0) {      
      train.labels$mean.stars[i] <- mean(sub_review$stars)
      train.labels$median.stars[i] <- median(sub_review$stars)
      train.labels$sd.stars[i] <- sd(sub_review$stars)
      train.labels$max.score[i] <- max(sub_review$stars)
      train.labels$min.score[i] <- min(sub_review$stars)
      train.labels$mean.review.length[i] <- mean(log(nchar(sub_review$review)+1))
      train.labels$sd.review.length[i] <- sd(log(nchar(sub_review$review)+1))
      
      sub_scored <- subset(scored.review, scored.review$review_id %in% sub_review$review_id)
      train.labels$av.senti.diff[i] <- mean(sub_scored$sentiscores.sum)
      train.labels$av.senti.ratio[i] <- mean(sub_scored$sentiscores.ratio)  
      train.labels$av.senti.positive[i] <- mean(sub_scored$sentiscores.positive)
      train.labels$av.senti.negative[i] <- mean(sub_scored$sentiscores.negative)
      train.labels$max.senti.positive[i] <- exp(max(sub_scored$sentiscores.positive)) 
      train.labels$min.senti.negative[i] <- exp(min(sub_scored$sentiscores.negative))
    }
    
    neighbs <- business$neighborhoods[match(b_id, business$business_id)]
    if(length(neighbs[[1]]) > 0) {
      
      for(j in 1:length(neighbs[[1]])) {
        if(neighbs[[1]][j] == "Chinatown")
          train.labels$isChinatown[i] <- 1
        if(neighbs[[1]][j] == "Dorchester")
          train.labels$Dorchester[i] <- 1
        if(neighbs[[1]][j] == "Downtown")
          train.labels$Downtown[i] <- 1
        if(neighbs[[1]][j] == "Jamaica Plain")
          train.labels$JamaicaPlain[i] <- 1
        if(neighbs[[1]][j] == "South End")
          train.labels$SouthEnd[i] <- 1
        if(neighbs[[1]][j] == "Beacon Hill")
          train.labels$BeaconHill[i] <- 1
        if(neighbs[[1]][j] == "Waterfront")
          train.labels$Waterfront[i] <- 1
        if(neighbs[[1]][j] == "South Boston")      
          train.labels$SouthBoston[i] <- 1
        if(neighbs[[1]][j] == "Financial District")
          train.labels$FinancialDistrict[i] <- 1
        if(neighbs[[1]][j] == "North End")
          train.labels$NorthEnd[i] <- 1
        if(neighbs[[1]][j] == "East Boston")
          train.labels$EastBoston[i] <- 1
        if(neighbs[[1]][j] == "Back Bay")
          train.labels$BackBay[i] <- 1
        if(neighbs[[1]][j] == "Roslindale" ||neighbs[[1]][j] == "Roslindale Village" )
          train.labels$Roslindale[i] <- 1
        if(neighbs[[1]][j] == "West Roxbury Center")
          train.labels$WestRoxburyCenter[i] <- 1
        if(neighbs[[1]][j] == "West Roxbury")
          train.labels$WestRoxbury[i] <- 1
        if(neighbs[[1]][j] == "Allston/Brighton")
          train.labels$AllstonBrighton[i] <- 1
        if(neighbs[[1]][j] == "Hyde Park")
          train.labels$HydePark[i] <- 1
        if(neighbs[[1]][j] == "Dudley Square")
          train.labels$DudleySquare[i] <- 1
        if(neighbs[[1]][j] == "Uphams Corner")
          train.labels$UphamsCorner[i] <- 1
        if(neighbs[[1]][j] == "Mission Hill")
          train.labels$MissionHill[i] <- 1
        if(neighbs[[1]][j] == "Fields Corner")
          train.labels$FieldsCorner[i] <- 1
        if(neighbs[[1]][j] == "Mattapan")
          train.labels$Mattapan[i] <- 1
        if(neighbs[[1]][j] == "Leather District")
          train.labels$LeatherDistrict[i] <- 1
        if(neighbs[[1]][j] == "Charlestown")
          train.labels$Charlestown[i] <- 1
        if(neighbs[[1]][j] == "Fenway")
          train.labels$Fenway[i] <- 1
        if(neighbs[[1]][j] == "Egleston Square")
          train.labels$EglestonSquare[i] <- 1
      }
    }
    
    sub <- subset(train.labels, train.labels$restaurant_id == train.labels$restaurant_id[i]
                  & train.labels$date < train.labels$date[i])
    
    if(nrow(sub) > 0) {      
      sub <- sub[order(sub$date),]
      
      train.labels$meanMin[i] <- mean(sub$X.)
      train.labels$meanMed[i] <- mean(sub$X..)
      train.labels$meanSev[i] <- mean(sub$X...)
      train.labels$medianMin[i] <- median(sub$X.)
      train.labels$medianMed[i] <- median(sub$X..)
      train.labels$medianSev[i] <- median(sub$X...)
      train.labels$sdMin[i] <- sd(sub$X.)
      train.labels$sdMed[i] <- sd(sub$X..)
      train.labels$sdSev[i] <- sd(sub$X...)
      train.labels$lastMin[i] <- sub$X.[nrow(sub)]
      train.labels$lastMed[i] <- sub$X..[nrow(sub)]
      train.labels$lastSev[i] <- sub$X...[nrow(sub)]
    }
    
    setTxtProgressBar(pb, i)
  }
  
  
  message("Building train set features based on previous inspections...")  
  pb   <- txtProgressBar(1, nrow(train.labels)-2, style=3)
  train.labels$TotalInf <- train.labels$lastMin + train.labels$lastMed + train.labels$lastSev
  train.labels$timeSinceLastInspection <- rep(NaN,nrow(train.labels))
  train.labels$numberInspections <- rep(0,nrow(train.labels))
  train.labels$ratioLastBeforeLastMin <- rep(NaN,nrow(train.labels))
  for(i in nrow(train.labels):2 ){  
    
    coiso <- train.labels[1:i-1,]
    sub <- subset(coiso, coiso$restaurant_id %in% train.labels$restaurant_id[i])
    
    if(nrow(sub) > 0) {
      
      train.labels$numberInspections[i] <- nrow(sub)
      train.labels$timeSinceLastInspection[i] <-  train.labels$date[i] - sub$date[length(sub$date)]
      
      if(nrow(sub) >=2) {
        #print(i)
        train.labels$ratioLastBeforeLastMin[i] <- log( (1+sub$lastMin[length(sub$lastMin)]) / (1+sub$lastMin[length(sub$lastMin)-1]) )
        train.labels$ratioLastBeforeLastMed[i] <- log( (1+sub$lastMed[length(sub$lastMed)]) / (1+sub$lastMed[length(sub$lastMed)-1]) )
        train.labels$ratioLastBeforeLastSev[i] <- log( (1+sub$lastSev[length(sub$lastSev)]) / (1+sub$lastSev[length(sub$lastSev)-1]) )
      }
    }  
    setTxtProgressBar(pb, nrow(train.labels) - i)
  }
  
  # Variables from topic modeling
  message("Building train set features based on a topic model...")  
  pb   <- txtProgressBar(1, nrow(train.labels), style=3)
  
  tops <- read.table("docsAsTopicsProbs_noStopwords.txt")
  tops$V1 <- NULL
  train.labels$mean.topic1 <- train.labels$mean.topic2 <- 
    train.labels$mean.topic3 <- train.labels$mean.topic4 <- 
    train.labels$mean.topic5 <- train.labels$sd.topic1 <- 
    train.labels$sd.topic2 <- train.labels$sd.topic3 <- 
    train.labels$sd.topic4 <- train.labels$sd.topic5 <- rep(0,nrow(train.labels))
  for(i in 1:nrow(train.labels) ){  
    
    #print(i)
    b_id <- match(train.labels$restaurant_id[i], matching[,1])
    b_id <- matching[b_id,2]
    
    sub <- review[which(review$business_id == as.character(b_id)),]
    sub_review <- subset(sub, sub$date < train.labels$date[i])
    
    t <- subset(tops, tops$V2 %in% sub_review$review_id)
    
    train.labels$mean.topic1[i] <- mean(t$V3)
    train.labels$mean.topic2[i] <- mean(t$V4)
    train.labels$mean.topic3[i] <- mean(t$V5)
    train.labels$mean.topic4[i] <- mean(t$V6)
    train.labels$mean.topic5[i] <- mean(t$V7)
    
    train.labels$sd.topic1[i] <- sd(t$V3)
    train.labels$sd.topic2[i] <- sd(t$V4)
    train.labels$sd.topic3[i] <- sd(t$V5)
    train.labels$sd.topic4[i] <- sd(t$V6)
    train.labels$sd.topic5[i] <- sd(t$V7)
    setTxtProgressBar(pb, i)
  }
  
  # Repeat the whole thing for the test set  
  # Join some variables of business to train.label
  submission$city <- submission$latitude <- submission$longitude <- 
    submission$review_count <- submission$open <- rep(NaN, nrow(submission))
  
  # From reviews
  submission$mean.stars <- submission$median.stars <- 
    submission$sd.stars <- submission$max.score <- 
    submission$min.score <- rep(NaN, nrow(submission))
  submission$mean.review.length <- submission$sd.review.length <- rep(0, nrow(submission))
  # Infraction statistics
  submission$meanMin <- submission$meanMed <- submission$meanSev <- 
    submission$medianMin <- submission$medianMed <- submission$medianSev <- 
    submission$sdMin <- submission$sdMed <- submission$sdSev <- 
    submission$lastMin <- submission$lastMed <- submission$lastSev <- rep(NaN, nrow(submission))
  
  submission$isRestaurant <- submission$isFood <- submission$isPizza <- submission$isBars <-
    submission$isPubs <- submission$isSandwiches <- submission$isChinese <-
    submission$isDelis <- submission$isItalian <- submission$isCoffeeTea <-
    submission$isMexican <- submission$isNightlife <- submission$isAmericanTrad <-
    submission$isBB <- submission$isAmericanNew <- submission$isSeafood <-
    submission$isIceCream <- submission$isJapanese <-submission$isFastFood <-
    submission$isDonuts <- submission$isBurgers <- submission$isSushiBars <-
    submission$isThai <- submission$isLounges <- submission$isFrench <-
    submission$isBakeries <- submission$isIndian <- submission$isLatinAmerican <-
    submission$isSteakhouses <- submission$isMiddleEastern <- submission$isCaterers <-
    submission$isEventPlanning <- submission$isVietnamese <- submission$isAsianFusion <-
    submission$isDanceClubs <- submission$isSportsBars <- submission$isArts <-
    submission$isDiveBars <-rep("no", nrow(submission))
  
  submission$isChinatown <- submission$Dorchester <- submission$Downtown <- 
    submission$JamaicaPlain <- submission$SouthEnd <- submission$BeaconHill <- 
    submission$Waterfront <- submission$SouthBoston <- submission$FinancialDistrict <- 
    submission$NorthEnd <- submission$EastBoston <- submission$BackBay <- 
    submission$Roslindale <- submission$WestRoxburyCenter <- submission$WestRoxbury <- 
    submission$AllstonBrighton <- submission$HydePark <- submission$DudleySquare <- 
    submission$UphamsCorner <- submission$MissionHill <- submission$FieldsCorner <- 
    submission$Mattapan <- submission$LeatherDistrict <- submission$Charlestown <- 
    submission$Fenway <- submission$EglestonSquare <- rep(0, nrow(submission))
  
  submission$av.senti.diff <- submission$av.senti.ratio <- 
    submission$av.senti.positive <- submission$av.senti.negative <- 
    submission$max.senti.positive <- submission$min.senti.negative <- rep(NaN, nrow(submission))
  
  message("Building test set features based on restaurant characteristics and review scores...This might take a while.")
  pb   <- txtProgressBar(1, nrow(submission), style=3)
  for(i in 1:nrow(submission) ){  
    
    b_id <- match(submission$restaurant_id[i], matching[,1])
    b_id <- matching[b_id,2]
    
    submission$city[i] <- business$city[match(b_id, business$business_id)]
    submission$latitude[i] <- business$latitude[match(b_id, business$business_id)]
    submission$longitude[i] <- business$longitude[match(b_id, business$business_id)]
    submission$open[i] <- business$open[match(b_id, business$business_id)]
    
    # Extract variables from categories
    cats <- business$categories[match(b_id, business$business_id)]
    for(j in 1:length(cats[[1]])) {
      if(cats[[1]][j] == "Restaurants")
        submission$isRestaurant[i] = "yes"
      if(cats[[1]][j] == "Food")
        submission$isFood[i] = "yes"
      if(cats[[1]][j] == "Pizza")
        submission$isPizza[i] = "yes"
      if(cats[[1]][j] == "Bars")
        submission$isBars[i] = "yes"
      if(cats[[1]][j] == "Pubs")
        submission$isPubs[i] = "yes"
      if(cats[[1]][j] == "Sandwiches")
        submission$isSandwiches[i] = "yes"
      if(cats[[1]][j] == "Chinese")
        submission$isChinese[i] = "yes"
      if(cats[[1]][j] == "Delis")
        submission$isDelis[i] = "yes"
      if(cats[[1]][j] == "Italian")    
        submission$isItalian[i] = "yes"
      if(cats[[1]][j] == "Coffee & Tea")
        submission$isCoffeeTea[i] = "yes"
      if(cats[[1]][j] == "Mexican")
        submission$isMexican[i] = "yes"
      if(cats[[1]][j] == "Nightlife")
        submission$isNightlife[i] = "yes"
      if(cats[[1]][j] == "American (Traditional)")
        submission$isAmericanTrad[i] = "yes"
      if(cats[[1]][j] == "Breakfast & Brunch")
        submission$isBB[i] = "yes"
      if(cats[[1]][j] == "American (New)")
        submission$isAmericanNew[i] = "yes"
      if(cats[[1]][j] == "Seafood")
        submission$isSeafood[i] = "yes"
      if(cats[[1]][j] == "Ice Cream & Frozen Yogurt")
        submission$isIceCream[i] = "yes"
      if(cats[[1]][j] == "Japanese")
        submission$isJapanese[i] = "yes"
      if(cats[[1]][j] == "Fast Food")
        submission$isFastFood[i] = "yes"
      if(cats[[1]][j] == "Donuts")
        submission$isDonuts[i] = "yes"
      if(cats[[1]][j] == "Burgers")
        submission$isBurgers[i] = "yes"
      if(cats[[1]][j] == "Sushi Bars")
        submission$isSushiBars[i] = "yes"
      if(cats[[1]][j] == "Thai")
        submission$isThai[i] = "yes"
      if(cats[[1]][j] == "Lounges")
        submission$isLounges[i] = "yes"
      if(cats[[1]][j] == "French")
        submission$isFrench[i] = "yes"
      if(cats[[1]][j] == "Bakeries")
        submission$isBakeries[i] = "yes"
      if(cats[[1]][j] == "Indian")
        submission$isIndian[i] = "yes"
      if(cats[[1]][j] == "Latin American")
        submission$isLatinAmerican[i] = "yes"
      if(cats[[1]][j] == "Steakhouses")
        submission$isSteakhouses[i] = "yes"
      if(cats[[1]][j] == "Middle Eastern")
        submission$isMiddleEastern[i] = "yes"
      if(cats[[1]][j] == "Caterers")
        submission$isCaterers[i] = "yes"
      if(cats[[1]][j] == "Event Planning & Services")
        submission$isEventPlanning[i] = "yes"
      if(cats[[1]][j] == "Vietnamese")
        submission$isVietnamese[i] = "yes"
      if(cats[[1]][j] == "Asian Fusion")
        submission$isAsianFusion[i] = "yes"
      if(cats[[1]][j] == "Dance Clubs")
        submission$isDanceClubs[i] = "yes"
      if(cats[[1]][j] == "Sports Bars")
        submission$isSportsBars[i] = "yes"
      if(cats[[1]][j] == "Arts & Entertainment")
        submission$isArts[i] = "yes"
      if(cats[[1]][j] == "Dive Bars")
        submission$isDiveBars[i] = "yes"
    }
    
    
    sub <- review[which(review$business_id == b_id),]
    sub_review <- subset(sub, sub$date <= submission$date[i])
    submission$review_count[i] <- nrow(sub_review)
    
    if(nrow(sub_review) > 0) {      
      submission$mean.stars[i] <- mean(sub_review$stars)
      submission$median.stars[i] <- median(sub_review$stars)
      submission$sd.stars[i] <- sd(sub_review$stars)
      submission$max.score[i] <- max(sub_review$stars)
      submission$min.score[i] <- min(sub_review$stars)
      submission$mean.review.length[i] <- mean(log(nchar(sub_review$review)+1))
      submission$sd.review.length[i] <- sd(log(nchar(sub_review$review)+1))
      
      sub_scored <- subset(scored.review, scored.review$review_id %in% sub_review$review_id)
      submission$av.senti.diff[i] <- mean(sub_scored$sentiscores.sum)
      submission$av.senti.ratio[i] <- mean(sub_scored$sentiscores.ratio)  
      submission$av.senti.positive[i] <- mean(sub_scored$sentiscores.positive)
      submission$av.senti.negative[i] <- mean(sub_scored$sentiscores.negative)
      submission$max.senti.positive[i] <- exp(max(sub_scored$sentiscores.positive)) 
      submission$min.senti.negative[i] <- exp(min(sub_scored$sentiscores.negative))
    }
    
    neighbs <- business$neighborhoods[match(b_id, business$business_id)]
    if(length(neighbs[[1]]) > 0) {
      
      for(j in 1:length(neighbs[[1]])) {
        if(neighbs[[1]][j] == "Chinatown")
          submission$isChinatown[i] <- 1
        if(neighbs[[1]][j] == "Dorchester")
          submission$Dorchester[i] <- 1
        if(neighbs[[1]][j] == "Downtown")
          submission$Downtown[i] <- 1
        if(neighbs[[1]][j] == "Jamaica Plain")
          submission$JamaicaPlain[i] <- 1
        if(neighbs[[1]][j] == "South End")
          submission$SouthEnd[i] <- 1
        if(neighbs[[1]][j] == "Beacon Hill")
          submission$BeaconHill[i] <- 1
        if(neighbs[[1]][j] == "Waterfront")
          submission$Waterfront[i] <- 1
        if(neighbs[[1]][j] == "South Boston")      
          submission$SouthBoston[i] <- 1
        if(neighbs[[1]][j] == "Financial District")
          submission$FinancialDistrict[i] <- 1
        if(neighbs[[1]][j] == "North End")
          submission$NorthEnd[i] <- 1
        if(neighbs[[1]][j] == "East Boston")
          submission$EastBoston[i] <- 1
        if(neighbs[[1]][j] == "Back Bay")
          submission$BackBay[i] <- 1
        if(neighbs[[1]][j] == "Roslindale" ||neighbs[[1]][j] == "Roslindale Village" )
          submission$Roslindale[i] <- 1
        if(neighbs[[1]][j] == "West Roxbury Center")
          submission$WestRoxburyCenter[i] <- 1
        if(neighbs[[1]][j] == "West Roxbury")
          submission$WestRoxbury[i] <- 1
        if(neighbs[[1]][j] == "Allston/Brighton")
          submission$AllstonBrighton[i] <- 1
        if(neighbs[[1]][j] == "Hyde Park")
          submission$HydePark[i] <- 1
        if(neighbs[[1]][j] == "Dudley Square")
          submission$DudleySquare[i] <- 1
        if(neighbs[[1]][j] == "Uphams Corner")
          submission$UphamsCorner[i] <- 1
        if(neighbs[[1]][j] == "Mission Hill")
          submission$MissionHill[i] <- 1
        if(neighbs[[1]][j] == "Fields Corner")
          submission$FieldsCorner[i] <- 1
        if(neighbs[[1]][j] == "Mattapan")
          submission$Mattapan[i] <- 1
        if(neighbs[[1]][j] == "Leather District")
          submission$LeatherDistrict[i] <- 1
        if(neighbs[[1]][j] == "Charlestown")
          submission$Charlestown[i] <- 1
        if(neighbs[[1]][j] == "Fenway")
          submission$Fenway[i] <- 1
        if(neighbs[[1]][j] == "Egleston Square")
          submission$EglestonSquare[i] <- 1
      }
    }
    
    sub <- subset(train.labels, train.labels$restaurant_id == as.character(submission$restaurant_id[i])
                  & train.labels$date < submission$date[i])
    
    if(nrow(sub) > 0) {
      #print(i)
      sub <- sub[order(sub$date),]
      
      submission$meanMin[i] <- mean(sub$X.)
      submission$meanMed[i] <- mean(sub$X..)
      submission$meanSev[i] <- mean(sub$X...)
      submission$medianMin[i] <- median(sub$X.)
      submission$medianMed[i] <- median(sub$X..)
      submission$medianSev[i] <- median(sub$X...)
      submission$sdMin[i] <- sd(sub$X.)
      submission$sdMed[i] <- sd(sub$X..)
      submission$sdSev[i] <- sd(sub$X...)
      submission$lastMin[i] <- sub$X.[nrow(sub)]
      submission$lastMed[i] <- sub$X..[nrow(sub)]
      submission$lastSev[i] <- sub$X...[nrow(sub)]
    }
    setTxtProgressBar(pb, i)
  }
  
  submission$TotalInf <- submission$lastMin + submission$lastMed + submission$lastSev
  submission$timeSinceLastInspection <- rep(NaN,nrow(submission))
  submission$numberInspections <- rep(0,nrow(submission))
  submission$ratioLastBeforeLastMin <- rep(NaN,nrow(submission))
  submission$ratioLastBeforeLastMed <- rep(NaN,nrow(submission))
  submission$ratioLastBeforeLastSev <- rep(NaN,nrow(submission))
  message("Building test set features based on previous inspections...")  
  pb   <- txtProgressBar(1, nrow(submission), style=3)
  for(i in nrow(submission):1 ){  
    
    
    sub <- subset(train.labels, train.labels$restaurant_id == as.character(submission$restaurant_id[i])
                  & train.labels$date < submission$date[i])
    
    if(nrow(sub) > 0) {
      
      submission$numberInspections[i] <- nrow(sub)
      submission$timeSinceLastInspection[i] <-  submission$date[i] - sub$date[length(sub$date)]
      
      if(nrow(sub) >=2) {
        #print(i)
        if(!is.na(sub$lastMin[length(sub$lastMin)]) & !is.na(sub$lastMin[length(sub$lastMin)-1]))
          submission$ratioLastBeforeLastMin[i] <- log( (1+sub$lastMin[length(sub$lastMin)]) / (1+sub$lastMin[length(sub$lastMin)-1]) )
        if(!is.na(sub$lastMed[length(sub$lastMed)]) & !is.na(sub$lastMed[length(sub$lastMed)-1]))
          submission$ratioLastBeforeLastMed[i] <- log( (1+sub$lastMed[length(sub$lastMed)]) / (1+sub$lastMed[length(sub$lastMed)-1]) )
        if(!is.na(sub$lastSev[length(sub$lastSev)]) & !is.na(sub$lastSev[length(sub$lastSev)-1]))
          submission$ratioLastBeforeLastSev[i] <- log( (1+sub$lastSev[length(sub$lastSev)]) / (1+sub$lastSev[length(sub$lastSev)-1]) )
      }
    }
    setTxtProgressBar(pb, nrow(submission) - i)
  }
  
  submission$mean.topic1 <- submission$mean.topic2 <- submission$mean.topic3 <- 
    submission$mean.topic4 <- submission$mean.topic5 <- submission$sd.topic1 <- 
    submission$sd.topic2 <- submission$sd.topic3 <- submission$sd.topic4 <- 
    submission$sd.topic5 <- rep(0,nrow(submission))
  message("Building test set features based on a topic model...")  
  pb   <- txtProgressBar(1, nrow(submission), style=3)
  for(i in 1:nrow(submission) ){  
    
    #print(i)
    b_id <- match(submission$restaurant_id[i], matching[,1])
    b_id <- matching[b_id,2]
    
    sub <- review[which(review$business_id == as.character(b_id)),]
    sub_review <- subset(sub, sub$date < submission$date[i])
    
    t <- subset(tops, tops$V2 %in% sub_review$review_id)
    
    submission$mean.topic1[i] <- mean(t$V3)
    submission$mean.topic2[i] <- mean(t$V4)
    submission$mean.topic3[i] <- mean(t$V5)
    submission$mean.topic4[i] <- mean(t$V6)
    submission$mean.topic5[i] <- mean(t$V7)
    
    submission$sd.topic1[i] <- sd(t$V3)
    submission$sd.topic2[i] <- sd(t$V4)
    submission$sd.topic3[i] <- sd(t$V5)
    submission$sd.topic4[i] <- sd(t$V6)
    submission$sd.topic5[i] <- sd(t$V7)
    setTxtProgressBar(pb, i)
  }
  
  
  message("Let's add some additional features based on reviews and past inspections...")  
  pb   <- txtProgressBar(1, nrow(train.labels), style=3)
  # Additional features based on reviews
  train.labels$review.total.votes <- rep(0,nrow(train.labels))
  train.labels$review.mean.votes <- rep(0,nrow(train.labels))
  for(i in 1:nrow(train.labels) ){  
    
    
    b_id <- match(train.labels$restaurant_id[i], matching[,1])
    b_id <- matching[b_id,2]
    
    sub <- review[which(review$business_id == b_id),]
    sub_review <- subset(sub, sub$date <= train.labels$date[i])
    
    if(nrow(sub_review) > 0) {         
      train.labels$mean.review.length[i] <- mean(log(sum(nchar(sub_review$text))+1))
      train.labels$sd.review.length[i] <- mean(log(sum(nchar(sub_review$text))+1))
      train.labels$review.total.votes[i] <- sum(sub_review$votes$funny) + sum(sub_review$votes$useful) + sum(sub_review$votes$cool)
      train.labels$review.mean.votes[i] <- train.labels$review.total.votes[i] / nrow(sub_review)
    }  
    setTxtProgressBar(pb, i)
  }
  
  submission$review.total.votes <- rep(0,nrow(submission))
  submission$review.mean.votes <- rep(0,nrow(submission))
  pb   <- txtProgressBar(1, nrow(submission), style=3)
  for(i in 1:nrow(submission) ){    
    b_id <- match(submission$restaurant_id[i], matching[,1])
    b_id <- matching[b_id,2]
    
    sub <- review[which(review$business_id == b_id),]
    sub_review <- subset(sub, sub$date <= submission$date[i])
    
    if(nrow(sub_review) > 0) {         
      submission$mean.review.length[i] <- mean(log(sum(nchar(sub_review$text))+1))
      submission$sd.review.length[i] <- mean(log(sum(nchar(sub_review$text))+1))
      submission$review.total.votes[i] <- sum(sub_review$votes$funny) + sum(sub_review$votes$useful) + sum(sub_review$votes$cool)
      submission$review.mean.votes[i] <- submission$review.total.votes[i] / nrow(sub_review)
    }  
    setTxtProgressBar(pb, i)
  }
  
  # Additional features based on past inspections
  train.labels$secondLastMin <- train.labels$secondLastMed <- 
    train.labels$secondLastSev <- train.labels$thirdLastMin <- 
    train.labels$thirdLastMed <- train.labels$thirdLastSev <- rep(0,nrow(train.labels))
  pb   <- txtProgressBar(1, nrow(train.labels)-2, style=3)
  for(i in nrow(train.labels):2 ){  
    
    coiso <- train.labels[1:i-1,]
    sub <- subset(coiso, coiso$restaurant_id == as.character(train.labels$restaurant_id[i]))
    
    if(nrow(sub) >=2) {
      train.labels$secondLastMin[i] <- sub$lastMin[length(sub$lastMin)-1]
      train.labels$secondLastMed[i] <- sub$lastMed[length(sub$lastMed)-1]
      train.labels$secondLastSev[i] <- sub$lastSev[length(sub$lastSev)-1]
      
      if(nrow(sub) >2) {
        train.labels$thirdLastMin[i] <- sub$lastMin[length(sub$lastMin)-2]
        train.labels$thirdLastMed[i] <- sub$lastMed[length(sub$lastMed)-2]
        train.labels$thirdLastSev[i] <- sub$lastSev[length(sub$lastSev)-2]
      }
    }  
    setTxtProgressBar(pb, nrow(train.labels) - i)
  }

  
  submission$secondLastMin <- submission$secondLastMed <- 
    submission$secondLastSev <- submission$thirdLastMin <- 
    submission$thirdLastMed <- submission$thirdLastSev <- rep(0,nrow(submission))
  pb   <- txtProgressBar(1, nrow(submission), style=3)  
  for(i in 1:nrow(submission)){  
    
    sub <- subset(train.labels, train.labels$restaurant_id == as.character(submission$restaurant_id[i])
                  & train.labels$date < submission$date[i])
    
    if(nrow(sub) >=2) {
      
      submission$secondLastMin[i] <- sub$lastMin[length(sub$lastMin)-1]
      submission$secondLastMed[i] <- sub$lastMed[length(sub$lastMed)-1]
      submission$secondLastSev[i] <- sub$lastSev[length(sub$lastSev)-1]
      
      if(nrow(sub) >2) {    
        
        submission$thirdLastMin[i] <- sub$lastMin[length(sub$lastMin)-2]
        submission$thirdLastMed[i] <- sub$lastMed[length(sub$lastMed)-2]
        submission$thirdLastSev[i] <- sub$lastSev[length(sub$lastSev)-2]
      }
    }  
    setTxtProgressBar(pb, i)
  }  
  
  write.csv(train.labels,"features_train_phase2.csv",row.names=FALSE)
  write.csv(submission,"features_test_phase2.csv",row.names=FALSE)
  
}