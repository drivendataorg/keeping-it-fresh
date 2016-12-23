![Banner Image](https://s3.amazonaws.com/drivendata/comp_images/tileimage.jpg)
# Keeping it Fresh: Predict Restaurant Inspections - 2nd Place
<br> <br>
# Entrant Background and Submission Overview

### Mini-bio
I have just started as a PhD student in data science and I've also just started work as a consultant.

### High Level Summary of Submission
My approach was focused almost strictly on feature engineering. I used scikit-learn’s implementation of random forests in Python. Perhaps the most unique aspect of my approach is that I used almost no text information from the Yelp reviews. Instead I focused on feature engineering with the business and inspection information. Finally, I noticed something tricky with the data where following a failed inspection there would be another inspection within around 1-4 weeks that had the exact same violations. This observation allowed me to implement specifically a guess to some of the test inspections that were within a few weeks of failures. However this only applied to a very small subset of the phase 2 test data as it comes far into the future. This method worked especially well during phase 1 though.

### Omitted Work
I tried using the text information in the Yelp reviews but did not succeed. I also tried many different variables from my feature engineering, such as the number of recent violations or ratings of recent reviews. These variables did not improve performance for my personal test set and therefore I didn’t include them.

### Model Evaluation
 I created my own train/validation set and evaluated my model using only the provided metric.

### Potentially Helpful Features
I wouldn’t really know what data would be useful without having tried it in some form of prediction first. Throughout this competition there were many variables that I thought would be useful which turned out not to be. One type of information that’s lacking which I think is important is information on the person who performed the inspection and other info involved with the inspection such as the exact time of inspection. We all know that humans can be biased in many ways, and therefore if the inspector was in a good mood during the inspection he or she may be less willing to assign violations. Ultimately, inspections are two-way interactions involving both the restaurant and the inspector. I would expect that having information on the inspectors would improve prediction performance significantly.

### Notes About the Model
I’m not an expert with Python and have written my code in a way that’s more familiar to Java developers so please forgive me if the code may see more difficult to read or understand. Other than that, I don’t think there are any quirks in particular.

### Future Steps
First of all, I would try gradient boosted trees which I only learned of after the competition. I would also try to mind some useful information out of the text data, maybe via some form of blending or stacking (again, I learned of this after the competition).

<br><br>
# Replicating the Submission

This package contains the files necessary to reproduce the predictions for the Yelp Keeping It Fresh Competition for DrivenData. The files should not be moved in order to generate the predictions, the following steps will detail what needs to be done in order to make the predictions.

I used Mac OS X Yosemite and used the LiClipse IDE for all of the programming tasks.

### Install Python
* Packages:
    * pandas
    * numpy
    * scipy
    * scikit-learn

Please follow the steps below to reproduce my prediction submission:

1. The first step required is to put the Yelp data .json files into the directory yelp_boston_academic_dataset. All of my code assumes that the .json files are contained in this directory which is contained in this package. I did not include the .json files because they’re too large to be emailed and also it’s specified that I do not need to submit them.

2. The second step required is to produce the yelp_duplicate_ids.csv file. In the restaurant_ids_to_yelp_ids.csv file given to us by the competition host are some restaurants that are mapped to multiple Yelp IDs. I did not take this into consideration at first and only realized it towards the end of the competition so I decided to manually create the yelp_duplicate_ids.csv file. This is done by deleting all rows from the restaurant_ids_to_yelp_ids.csv that have only one mapping between restaurant ID and Yelp ID.

3. Run the file GenLearningData.py. This takes some of the JSON and CSV files in this package and outputs the train_data_final.csv file which is the training dataset that will be used for my prediction model.

4. In order to have the proper testing data, the PhaseIISubmissionFormat_test.csv file must be created. This file is essentially the same as the PhaseIISubmissionFormat file provided by the competition host except the inspection ID has been changed to be ordered by row of the file. This is so that when generating the testing data, the ordering of the rows can be maintained for later submission. To create the PhaseIISubmissionFormat_test.csv file, simply take the original PhaseIISubmissionFormat.csv file and set the id column to 200001 for the first row, 200002 for the second row, until the very end. I’ve included the file in this submission package for convenience.

5. Run the file GenTestingData.py. This takes some of the JSON and CSV files in this package and outputs the test_guess_final.csv and test_data_final.csv files which are the testing dataset that will be used for my prediction model. Note that there are two output files. The test_guess_final.csv is the result of a trick that I thought of from personally analyzing the data.

6. Run the file LearnTest.py. This builds a random forest model using the training dataset from train_data_final.csv and makes predictions on the testing dataset from test_data_final.csv. The results are then combined with the “guesses” made in test_guess_final.csv and outputted into a file called test_result_final.csv. My final submission was the average predictions of 7 runs of LearnTest.py. There are only minor discrepancies between each run, and the final average was rounded to the nearest integer.

7. Finally, the prediction result (averaged or not) must be copied and pasted into the PhaseIISubmissionFormat.csv file provided. Only the violation predictions should be copied and pasted, not the inspection id. Order is already correct so all of the data could be copied and pasted at once.

8. My submission for the competition should be the file PhaseIISubmissionFormat_final.csv which I included into this package. Please compare the output to this file for reproduction.
