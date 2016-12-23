'''
This file takes the training data to build random forest models and then makes predictions for the test data
Date: August 28, 2015
'''

import pandas as pd
import numpy as np
import csv
import time
import codecs
from sklearn.ensemble import RandomForestRegressor

t0 = time.time()

'''
Note that the violations have already been converted into a single value through the following: 1 * number of one star violations + 2 * number of two star violations + 5 * number of three star violations
'''
#load the training and testing data
df_train = pd.read_csv('train_data_final.csv', header=1)
df_test = pd.read_csv('test_data_final.csv', header=1)

#drop the first 5 columns (inspection_id, date, restaurant_id, name, part_of_set)
df_train.drop(df_train.columns[[0, 1, 2, 4, 5]], axis=1, inplace=True)

#drop the first 6 columns (inspection_id, date, restaurant_id, violations, name, part_of_set)
df_test.drop(df_test.columns[[0, 1, 2, 3, 4, 5]], axis=1, inplace=True)

#randomize the training data for each run
df_train = df_train.reindex(np.random.permutation(df_train.index))

train_data = df_train.values
test_data = df_test.values

#log transform the violations column (response variable)
#this is done because the evaluation criteria is RMSLE and the scikit-learn implementation of random forests minimizes squared error
train_data[0::, 0] = np.log(train_data[0::, 0] + 1)

#train and predict via random forests
RF = RandomForestRegressor(n_estimators = 1001, max_features = 600, n_jobs = 8, oob_score = True)
RF = RF.fit(train_data[0::, 1::], train_data[0::, 0])
output1 = RF.predict(test_data)

#transform the predicted results back by exponentiating and then subtracting by 1
output1 = np.exp(output1) - 1

#not sure why I did this...
output1 = output1 + 1

#just in case any predictions are negative, set equal to 0 as we cannot have negative violations
output1[output1 < 0] = 0

#create two rows of 0s for submission purposes, since the final submission requires 3 columns of violations
output2 = np.multiply(0, output1)
output3 = np.multiply(0, output1)

output1.tolist()
output2.tolist()
output3.tolist()

#below I put together the results from guessing and predicting for generating the submission file
predict_inspections = {}

#first take the guesses we made and put into hash with inspection_id as the key
with open("test_guess_final.csv", "rb") as csvfile:
    guessReader = csv.reader(csvfile, delimiter=',')
    guessReader.next()
    for guessInfo in guessReader:
        predict_inspections[guessInfo[0]] = [int(guessInfo[3]), 0, 0]

#next take the predictions from the test data and put them into the hash with inspection_id as the key
#note that I'm not so fluent with pandas so I noticed that I was always missing the first row when I loaded in for prediction purposes so I included a dummy first row of data (after the column titles). That's why there are two dataReader.next calls below
with open("test_data_final.csv", "rb") as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    dataReader.next()
    dataReader.next()

    count = 0
    for dataInfo in dataReader:
        predict_inspections[dataInfo[0]] = [int(round(output1[count])), int(round(output2[count])), int(round(output3[count]))]
        count += 1

total_error = 0

#write out the predictions in the order specified by the PhaseIISubmissionFormat
#must manually copy and paste the predictions into the PhaseIISubmissionFormat file (the inspections are already in the correct order)
f = codecs.open("test_result_final.csv","w",'utf-8')
for key in sorted(predict_inspections.keys()):
    f.write(key + "," + str(predict_inspections[key][0]) + "," + str(predict_inspections[key][1]) + "," + str(predict_inspections[key][2]) + "\n")
print time.time() - t0, "seconds wall time"
