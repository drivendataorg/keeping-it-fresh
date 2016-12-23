setwd("<set dir here>\\scripts and data")
set.seed(998)
require(jsonlite)
review <- fromJSON(sprintf("[%s]", paste(readLines('yelp_academic_dataset_review.json'), collapse=",")))

rev_tm <- NULL
rev_tm$id <- review$review_id
rev_tm$score <- review$stars
rev_tm$text <- gsub("[\r\n]", " ", review$text)
rev_tm <- as.data.frame(rev_tm)

write.csv(rev_tm,"rev_tm.txt",row.names=FALSE)
