setwd("<set dir here>\\scripts and data")
require(jsonlite)
require(plyr)
require(stringr)

set.seed(998)

review <- fromJSON(sprintf("[%s]", paste(readLines('yelp_academic_dataset_review.json'), collapse=",")))
review$date <- strptime(x = as.character(review$date), tz="US/Eastern", format = "%Y-%m-%d")

pos <- scan('positive-words.txt', what = 'character',comment.char=';')
neg <- scan('negative-words.txt', what = 'character',comment.char= ';')
pos.words <- c(pos)
neg.words <- c(neg)

score.sentiment.sum <- function(sentences, pos.words, neg.words, .progress='none') {
  scores <- laply(sentences, function(sentence, pos.words, neg.words) {
    
    sentence <- gsub('[[:punct:]]', '', sentence)
    sentence <- gsub('[[:cntrl:]]', '', sentence)
    sentence <- gsub('\\d+', '', sentence)
    sentence <- tolower(sentence)
  
    word.list <- str_split(sentence, '\\s+')
    words <- unlist(word.list)
    
    pos.matches <- match(words, pos.words)
    neg.matches <- match(words, neg.words)
    
    pos.matches <- !is.na(pos.matches)
    neg.matches <- !is.na(neg.matches)
    
    score <- sum(pos.matches) - sum(neg.matches)
    
    return(score)
  }, pos.words, neg.words, .progress=.progress )
  
  scores.df <- data.frame(score=scores, text=sentences)
  return(scores.df)
}

score.sentiment.ratio = function(sentences, pos.words, neg.words, .progress='none')
{
  scores = laply(sentences, function(sentence, pos.words, neg.words) {
    
    sentence = gsub('[[:punct:]]', '', sentence)
    sentence = gsub('[[:cntrl:]]', '', sentence)
    sentence = gsub('\\d+', '', sentence)
    sentence = tolower(sentence)
    word.list = str_split(sentence, '\\s+')
    words = unlist(word.list)
    pos.matches = match(words, pos.words)
    neg.matches = match(words, neg.words)
    pos.matches = !is.na(pos.matches)
    neg.matches = !is.na(neg.matches)
    score = sum(pos.matches) / (sum(neg.matches)+1)
    
    return(score)
  }, pos.words, neg.words, .progress=.progress )
  
  scores.df = data.frame(score=scores, text=sentences)
  return(scores.df)
}

score.sentiment.positive = function(sentences, pos.words, neg.words, .progress='none') {

  scores = laply(sentences, function(sentence, pos.words, neg.words) {
    
    sentence = gsub('[[:punct:]]', '', sentence)
    sentence = gsub('[[:cntrl:]]', '', sentence)
    sentence = gsub('\\d+', '', sentence)
    sentence = tolower(sentence)
    word.list = str_split(sentence, '\\s+')
    words = unlist(word.list)
    
    pos.matches = match(words, pos.words)
    pos.matches = !is.na(pos.matches)
    score = sum(pos.matches) / (length(words)+1)
    
    return(score)
  }, pos.words, neg.words, .progress=.progress )
  
  scores.df = data.frame(score=scores, text=sentences)
  return(scores.df)
}

score.sentiment.negative = function(sentences, pos.words, neg.words, .progress='none')
{
  scores = laply(sentences, function(sentence, pos.words, neg.words) {
    
    sentence = gsub('[[:punct:]]', '', sentence)
    sentence = gsub('[[:cntrl:]]', '', sentence)
    sentence = gsub('\\d+', '', sentence)
    sentence = tolower(sentence)
    word.list = str_split(sentence, '\\s+')
    words = unlist(word.list)
    neg.matches = match(words, neg.words)
    neg.matches = !is.na(neg.matches)
    score = sum(neg.matches) / (length(words)+1)
    
    return(score)
  }, pos.words, neg.words, .progress=.progress )
  
  scores.df = data.frame(score=scores, text=sentences)
  return(scores.df)
}

aaa.text <- review$text 
aaa.scores.sum <- score.sentiment.sum(aaa.text,pos.words,neg.words,.progress='text') 
aaa.scores.ratio <- score.sentiment.ratio(aaa.text,pos.words,neg.words,.progress='text') 
aaa.scores.positive <- score.sentiment.positive(aaa.text,pos.words,neg.words,.progress='text') 
aaa.scores.negative <- score.sentiment.negative(aaa.text,pos.words,neg.words,.progress='text') 

rev_scored <- NULL
rev_scored$review_id <- review$review_id
rev_scored$business_id <- review$business_id
rev_scored$sentiscores.sum <- aaa.scores.sum$score
rev_scored$sentiscores.ratio <- aaa.scores.ratio$score
rev_scored$sentiscores.positive <- aaa.scores.positive$score
rev_scored$sentiscores.negative <- aaa.scores.negative$score

write.csv(rev_scored, "review_sentiscored.csv", row.names=FALSE)

