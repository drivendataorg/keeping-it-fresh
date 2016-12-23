![Banner Image](https://s3.amazonaws.com/drivendata/comp_images/tileimage.jpg)
# Keeping it Fresh: Predict Restaurant Inspections - 1st Place
<br> <br>
# Entrant Background and Submission Overview

### Mini-bio
I am presently a data scientist.  I've been involved in the development of a machine-learning-as-a-service platform, and also in financial forecasting, web traffic fraud detection and text analysis related projects. Before this I was a data and text mining specialist.

I have an MSc in Electrical and Computer Engineering, and my thesis work was focused on pattern detection in electrophysiological signals, using unsupervised learning methods. I'm going back to college soon, as I have recently enrolled in an Astronomy certification programme.

### High Level Summary of Submission
With regards to data representation, I used three types of variables to represent each restaurant inspection:

1. Variables related to the restaurant's past inspections record: e.g. number of inspections, number of violations of each type, ratios of number of violations etc. The hypothesis here was that the past inspections, especially the two or three most recent, would be good indicators of the outcome of the current inspection.

2. Variables related to the restaurant's location and characteristics: e.g. neighborhood and type of food served. These were derived from the files originally provided by DrivenData/Yelp. I left out some of the characteristics available because I noticed that by including them, the models would have a worse performance.

3. Variables extracted from the universe of Yelp reviews for each restaurant: these include 	     the mean/median/deviation of review scores and also:

    * Sentiment analysis based features: the hypothesis here is that the “aggregated” sentiment conveyed by these features is correlated with the number of health violations, that is, for example, restaurants with very negative reviews will tend to have a higher number of violations.

    * Topic modeling based features: instead of taking individual words or expressions as features, I felt that topic modeling would be a better candidate in the sense that it can characterize a piece of text as a mixture of several groups of related words, pertaining to different topics. The approach here was to build a single topic model from the labelled reviews with 5 topics, where each topic corresponds to a review label (that is, its score) from 1 (bad) to 5 (excellent).

The end result of the feature extraction steps is 122 variables and 3 targets (one for each type of health violation). Please check the file dd_dictionary.csv included in the documentation bundle, it contains a brief description of each variable.

For the learning stage, I averaged the predictions of a random forest and a gradient boosted model. I tried a number of regression algorithms and combinations, but RF and GBM seemed to yield the best performances. Averaging their predictions is a bit of a naïve approach, but I hoped this way the predictions would “even out”, so to speak.

### Omitted Work
Among the things I tried that were left out in the end were:
* Variables based on the Yelp “tips”

* Variables related to the reviewers themselves.

* Additional variables related to the restaurant’s characteristics: “parking available”, “type of credit cards accepted” and so on.

* Other topic models, like “standard” topic models built from the reviews without using the scores as classification labels.

I opted not to include them in the final model because I noticed that for some, when they were added up to the data’s representation space, the model performance would be worse. Others just had a really high percentage of unknown values (especially some restaurant characteristics) so I left them out.

I also experimented a number of different implementations and regression algorithms and combinations thereof, but the aforementioned averaging of GBM and RF seemed to yield the best model.

### Model Evaluation
I used the conventional RMSE in addition to the competition metric.

### Potentially Helpful Features
I feel that the crucial features, that is, the results and dates of previous inspections, are already well represented in the data. Additional variables that might help to improve further analysis could be related to additional information on the inspections (for example, some sort of identification of the inspector or team of inspectors or other aspects relevant to the inspection itself) and demographic information related to the location (i.e., neighbourhood) where the restaurants operate.

What could have been really helpful would be information on the restaurant's ownership, such as: do they own other restaurants, on which date they assumed ownership of the restaurant, number of staff at time or prior to the inspection, estimated number of clients, estimated revenue, etc. But I do realize this must be very hard to obtain.

### Notes About the Model
The feature building code is not the most efficient, I have to admit this was my first real effort at coding in R, so there’s a lot of space to improve there. The algorithm implementations I used can also consume a good deal of memory. Running the whole thing might take up to a day.

### Future Steps
I would try to fine tune a different model for each of the three targets, instead of using the same algorithms, with the same parameter values.  I also feel there’s a lot to be done feature wise, in terms of extracting meaningful information from the reviews’ text. I did not explore sentiment and topic modeling as well as I’d like, also I did not have the chance to explore syntactic patterns.

With regards to the topic modeling step, I opted to build a single topic model based on all available reviews due to time constraints. It might have been more correct to build several topic models, for several points in time (that is, using only reviews dating prior to those time points).

Other alternative setup for topic modeling would be building a topic model for each type of violation, using their number as a classification label instead of the review score.

<br><br>
# Replicating the Submission

### Summary

This README describes the requirements and steps needed to recreate the winning submission of the data science competition "Keeping it Fresh: Predict Restaurant Inspections" organized by DrivenData and supported by Yelp and the City of Boston.

The code was originally implemented on a Windows 7 64bit installation, with a AMD Phenom II 6 core processor and 8Gb of RAM.

The requirements versions listed below are merely indicative, it is possible that earlier versions work just as well.

### Requirements

1. R setup (mandatory)
    * R version >= 3.2.0
    * R packages
        * randomForest: version >= 4.6.10
        * jsonlite: version >= 0.9.16
        * h2o: version >= 2.8.4.4
        * plyr: version >= 1.8.1
        * stringr: version >= 0.6.2

2. Java setup (optional): only needed if the user wishes to recreate the topic model
    * 1.6 or higher
    * Mallet:
        * unzip the mallet.rar file included in this distribution
        * create a %MALLET_HOME% environment variable, setting its value to the directory where Mallet resides (e.g. "C:\\mallet").

3. Mandatory data files
    * AllViolations.csv: as originally provided by the competition organizers
    * restaurant_ids_to_yelp_ids.csv: as originally provided by the competition organizers
    * yelp_academic_dataset_business.json: as originally provided by the competition organizers
    * yelp_academic_dataset_review.json: as originally provided by the competition organizers
    * review_sentiscored.csv: contains reviews scored using sentiment analysis methods, for more details read the subsection of this README titled "Sentiment Analysis Features".
    * docsAsTopicsProbs_noStopwords.txt: contains reviews represented as topic probability vectors, for more details read the subsection of this README titled "Topic Modeling Features".

4. Optional data files
    * yelp.stops: contains a stopwords list useful to build a topic model from the reviews, for more details read the subsection of this README titled "Topic Modeling Features".
    * rev_tm.txt: contains all the reviews and the respective scores in a format suitable to build a topic model from them, for more details read the subsection of this README titled "Topic Modeling Features".
    * negative-words.txt: a list of words associated to negative sentiment [1][2], for more details read the subsection of this README titled "Sentiment Analysis Features".
    * positive-words.txt: a list of words associated to positive sentiment [1][2], for more details read the subsection of this README titled "Sentiment Analysis Features".

5. Mandatory scripts
    * run.R: main point of entry to recreate the winning model, is dependent on the data files listed in point 3 and on the following scripts:
        * feature_eng.R: all the feature engineering/extraction takes place here.
        * learning_final.R: all the predictive modeling takes place here.

6. Optional scripts/code
    + sentiment_script.R: used to recreate the optional *review_sentiscored.csv*.
    + build_rev_tm.R: used to recreate the optional *rev_tm.txt* file.
    + mallet.rar: used to recreate the topic model.

### Quick Run

* Install the R packages detailed in the previous section by executing the code
```{r eval=FALSE}
library(jsonlite)
library(randomForest)
library(h2o)
```

* Change the working directory in the first line of the script run.R to point to the folder that contains all files listed in points 3 and 5 of the previous section.

* Run the script run.R:
    * this file will invoke the scripts that perform feature engineering and predictive modeling. The final outcome consists on a csv file similar to the one submitted to the DrivenData competition named *sub_2_PhaseII_h20*.
    * set the 'final_date' parameter in the learning_stage function to the be the last day of inspections in yyyy-MM-dd (e.g. "2015-08-19")
    * set the maximum size of the memory allocation pool to h2o by setting the value of the max_mem_size_h2o parameter (e.g. "4g")

For a more detailed description of the different steps in the modeling workflow, read the following sections.

### Feature Engineering Stage

The bulk of the feature engineering stage is contained in the *feature_eng.R* script. The final outcome of this script consists of two csv files, *features_train_phase2.csv* and *features_test_phase2.csv*. The former is used to train a predictive model, which in turn will use the second file to generate the competition submission.

Each of the two files has 126 columns, being that each column is a variable that represents some characteristic of the restaurant being inspected. For a brief description of each variable, check the dictionary file *dd_dictionary.csv*.

##### 1. Sentiment Analysis Features

The sentiment analysis variables contained in *review_sentiscored.csv* were generated with the *sentiment_script.R* file prior to the overall modeling workflow described in the section "Quick Run" and **do not need to be recreated** in order to generate the model and submission file.

Follow these steps **only** if you wish to recreate the sentiment analysis features present in the *review_sentiscored.csv* file.

1. Change the first line of the *sentiment_script.R* to point to the right directory and run the script. The code implemented here was based on [3].

##### 2. Topic Modeling Features

The topic modelling variables contained in the *docsAsTopicsProbs_noStopwords.txt* were generated prior to overall modeling workflow described in the section "Quick Run" and **do not need to be recreated** in order to generate the model and submission file.

Follow these steps **only** if you wish to recreate the topic model based features present in the *docsAsTopicsProbs_noStopwords.txt* file.

1. Change the first line of the *build_rev_tm.R* script to point to the right directory and
run the script. The outcome is the text file *rev_tm.txt* where each line contains a review about a restaurant and the respective score as a number between 1 and 5.

2. Ensure that you have the correct Java/Mallet setup as detailed in point 2 of the "Requirements" section.

3. Place the *rev_tm.txt* file and the *yelp.stops* file inside the Mallet directory (e.g "C:\Mallet").

4. Using the command line, run the following commands from inside the mallet directory [4]
>{r eval=FALSE}
> bin\mallet import-file --input rev_tm.txt --output yelp-short.seq --stoplist-file yelp.stops --label-as-features --keep-sequence
> bin\mallet run cc.mallet.topics.LabeledLDA --input yelp-short.seq --output-topic-keys yelp-llda.keys --output-doc-topics docsAsTopicsProbs_noStopwords.txt

    * These commands will generate a topic model with 5 topics, one for each review score between 1 (bad) and 5 (excellent). This way we can represent the reviews as a probabilistic mixture of five topics. Note that topic is defined as a set of related terms. The *yelp.stops* file is a stopwords list, built from a conventional english stopwords list to which a small number of terms were added (like "boston" and "restaurant").

5. The final outcome is the *docsAsTopicsProbs_noStopwords.txt* file, where each row corresponds to a review and the last five columns correspond to each topic. The values in these columns are the probability/weight that the corresponding topic has when characterizing its text as a mixture of topics.

Check [4] for more details.

#### Learning Stage

The modeling is done in the *learning_final.R* script. All inspections that have a number of violations of type "Minimum" equal or higher to 10 are treated as outliers and removed prior to running the learning algorithms.

Two models are built for each of the three target types, a random forest and a gradient boosted model using the R package "h2o" implementation. The predictions for the inspections in the submission file are obtained by running both models on the previously unseen inspections and averaging them.

#### References

[1] Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing and Comparing Opinions on the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.


[2] http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html


[3] https://github.com/benmarwick/AAA2011-Tweets/blob/master/AAA2011.R


[4] http://www.mimno.org/articles/labelsandpatterns/
