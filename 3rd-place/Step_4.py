#############################################################################################
#### What is the flow of the code? ######################################################
#############################################################################################
# (0) specify parameters needed to connect to the db, find the necessary input files and run the models -- THIS IS THE ONLY SECTION THAT NEEDS TO BE UPDATED FOR THE CODE TO RUN
# (1) clear out any old values that might be in the tables in the PostgreSQL database from previous runs
# (2) import CSV files needed from the competition dataset. Append any new violations data to "AllViolations.csv" as "recent violations" is a key input into the model
# (3) pull in the json files and prep them into flat tabular CSV files that can be imported into tables in PostgreSQL
# (4) import the above prepped CSV files into PostgreSQL
# (5) delete the CSV files created during the json prep process, just to keep things tidy
# (6) build indexes on the tables in PostgreSQL for query efficiency
# (7) pull all the imported data together into a table for modelling through the pre-built views in PostgreSQL
# (8) load the pickled models and predict each of the targets
# (9) blend each of the models for each target
# (10) generate a scores file with scores for the three targets in it
#####################################################


#############################################################################################
#### (0) Specify parameters needed to run the model #########################################
#### The parameters needed to connect to PostgreSQL. These should be the same as the ########
#### values used in the previous one-off step to create the tables and views ################
#############################################################################################
pg_hostname = "localhost" # the hostname of the PostgreSQL server. FYI, if this field was left blank when the server was registered, pg_hostname should be declared as localhost
pg_user = "shane" # the username needed to log into PostgreSQL database
pg_password = "terenure" # the password needed to log into PostgreSQL database
pg_port = 5433
pg_db_name = "dd_db" # the name of the PostgreSQL database created
#############################################################################################


#############################################################################################
#### (0) Specify parameters needed to run the model #########################################
#### Parameters needed to pick up the necesary input files  #################################
#############################################################################################
json_data_folder = "/home/shane/Documents/Kaggle/Boston/1. Raw Data/Phase II/" # which folder are the new json files in? NB! Please end this string with a slash e.g. "C:/test/" is good. "C:/test" is bad
json_checkin_file = "yelp_academic_dataset_checkin.json" # in the competition dataset supplied, this file was called yelp_academic_dataset_checkin.json
json_review_file = "yelp_academic_dataset_review.json" # in the competition dataset supplied, this file was called yelp_academic_dataset_review.json
json_tip_file = "yelp_academic_dataset_tip.json" # in the competition dataset supplied, this file was called yelp_academic_dataset_tip.json
json_user_file = "yelp_academic_dataset_user.json" # in the competition dataset supplied, this file was called yelp_academic_dataset_user.json
json_business_file = "yelp_academic_dataset_business.json" # in the competition dataset supplied, this file was called yelp_academic_dataset_business.json


csv_data_folder = "/home/shane/Documents/Kaggle/Boston/1. Raw Data/Phase II/" # which folder are the CSV files from the competition dataset in? NB! Please end this string with a slash e.g. "C:/test/" is good. "C:/test" is bad
csv_map_ids_file = "restaurant_ids_to_yelp_ids.csv" # in the competition dataset supplied, this file was called restaurant_ids_to_yelp_ids.csv
csv_labelled_cases = "AllViolations.csv" # in the competition dataset supplied, this file was called AllViolations.csv
csv_non_labelled_cases = "PhaseIISubmissionFormat.csv" # in the competition dataset supplied, this file was called PhaseIISubmissionFormat.csv

model_source_folder = "/home/shane/Documents/Kaggle/Boston/1. Raw Data/Phase II/" # the folder where the pickled model files are stored
#############################################################################################


#############################################################################################
#### (0) Specify parameters needed to run the model #########################################
#### Parameters around where the final scores file should be stored  ########################
#############################################################################################
scores_output_folder = "/home/shane/Documents/Kaggle/Boston/1. Raw Data/Phase II/" # which folder should the scores be written to
scores_output_file = "20151004.csv" # what should the output CSV file be called
#############################################################################################





##########################################################################################################
##########################################################################################################
#### From here down, the code should run unaltered each time the scores are refreshed ####################
##########################################################################################################
##########################################################################################################




#####################################################
#### Import packages ################################
#####################################################
import psycopg2 as pgs
import pandas as pd
import numpy as np
import os

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
#####################################################


#############################################################################################
#### (1) clear out any old values from the tables in PostgreSQL #############################
#### Connect to PostgreSQL and run delete statements on all tables ##########################
#############################################################################################
con = pgs.connect(dbname = pg_db_name, user = pg_user, host = pg_hostname, password = pg_password, port = pg_port)
con.set_isolation_level(pgs.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()

cur.execute("DELETE FROM tbl_users;")
cur.execute("DELETE FROM tbl_tips;")
cur.execute("DELETE FROM tbl_reviews;")
cur.execute("DELETE FROM tbl_checkins;")
cur.execute("DELETE FROM tbl_business;")
cur.execute("DELETE FROM tbl_map_ids;")
cur.execute("DELETE FROM tbl_labelled_cases;")
cur.execute("DELETE FROM tbl_non_labelled_cases;")
print ("Completed (1) clear out any old values from the tables in PostgreSQL")
#############################################################################################


#############################################################################################
#### (2) import CSV files needed from the competition dataset ###############################
#### import CSV files needed to map yelp to business IDs ####################################
#############################################################################################
df_id_map = pd.read_csv(csv_data_folder + csv_map_ids_file)

ls_rows = []
for row in df_id_map.index:
    ls_this_row = []
    boston_id = df_id_map["restaurant_id"][row]
    
    for yelp_id in df_id_map.columns[1:]:
        if not pd.isnull(df_id_map[yelp_id][row]):
			ls_rows.append([boston_id, df_id_map[yelp_id][row]])

ls_header = ["restaurant_id", "yelp_id"]
df_ids = pd.DataFrame(ls_rows, columns = ls_header)
df_ids.to_csv(csv_data_folder + "map_ids_final.csv", index = False, encoding = 'utf-8', header = False)
print ("Completed (2) import CSV files needed from the competition dataset - import CSV files needed to map yelp to business IDs")
#############################################################################################


#############################################################################################
#### (2) import CSV files needed from the competition dataset ###############################
#### import the labelled training cases used to train the models ############################
#############################################################################################
df_labelled_cases = pd.read_csv(csv_data_folder + csv_labelled_cases, index_col = None)

l_colnames = ["id", "date", "restaurant_id", "one_star", "two_star", "three_star"]
df_labelled_cases.columns = l_colnames

df_labelled_cases.to_csv(csv_data_folder + "labelled_cases_final.csv", index = False, encoding = 'utf-8', header = False)
print ("Completed (2) import CSV files needed from the competition dataset - import the labelled training cases used to train the models")
#############################################################################################


#############################################################################################
#### (2) import CSV files needed from the competition dataset ###############################
#### import the unlabelled cases that are to be scored in this run ##########################
#############################################################################################
df_non_labelled_cases = pd.read_csv(csv_data_folder + csv_non_labelled_cases, index_col = None)

l_colnames = ["id", "date", "restaurant_id", "one_star", "two_star", "three_star"]
df_non_labelled_cases.columns = l_colnames

df_non_labelled_cases.to_csv(csv_data_folder + "non_labelled_cases_final.csv", index = False, encoding = 'utf-8', header = False)
print ("Completed (2) import CSV files needed from the competition dataset - import the unlabelled cases that are to be scored in this run")
#############################################################################################


#############################################################################################
#### (3) pull in new json files and convert them to flat tabular structures #################
#### Prep the checkins json file ############################################################
#############################################################################################
with open(json_data_folder + json_checkin_file, 'r') as checkins_file:
	checkins_json = '[' + ','.join(checkins_file.readlines()) + ']'

df_checkins_all = pd.read_json(checkins_json)

col = "checkin_info"

s_json = "["
for row in df_checkins_all.index:
	s_json = s_json + str(df_checkins_all[col][row]) + ","
s_json = s_json[:-1] + "]"

s_json = s_json.replace("u'", "\"")
s_json = s_json.replace("'", "\"")

df_json = pd.read_json(s_json)
df_json.fillna(0, inplace = True)

ls_columns = []
for cl in df_json.columns:
	ls_columns.append(col + "_" + cl.replace("-", "_"))
df_json.columns = ls_columns

df_checkins_final = pd.concat([df_checkins_all.business_id, df_json], axis = 1)
df_checkins_final.to_csv(json_data_folder + "checkins_final.csv", index = False, encoding = 'utf-8', header = False)
print ("Completed (3) pull in new json files and convert them to flat tabular structures - Prep the checkins json file")
#############################################################################################


#############################################################################################
#### (3) pull in new json files and convert them to flat tabular structures #################
#### Prep the reviews json file #############################################################
#############################################################################################
with open(json_data_folder + json_review_file, 'r') as reviews_file:
	reviews_json = '[' + ','.join(reviews_file.readlines()) + ']'

df_reviews_all = pd.read_json(reviews_json)
df_reviews_all.reset_index("review_id", inplace = True)

ls_flat_columns = ["business_id", "date", "stars", "user_id"]
df_reviews_tmp = df_reviews_all[ls_flat_columns]

ls_nested_numeric_columns = ["votes"]
for col in ls_nested_numeric_columns:

	#print col

	s_json = "["
	for row in df_reviews_all.index:
		s_json = s_json + str(df_reviews_all[col][row]) + ","
	s_json = s_json[:-1] + "]"

	s_json = s_json.replace("u'", "\"")
	s_json = s_json.replace("'", "\"")
	
	df_json = pd.read_json(s_json)
	df_json.fillna(0, inplace = True)
	
	ls_column_names = []
	for nested_col in df_json.columns:
		ls_column_names.append(col + "_" + nested_col)
	df_json.columns = ls_column_names
	df_json.index = df_reviews_tmp.index
	#print df_json.shape
	df_reviews_tmp = df_reviews_tmp.join(df_json)
	#print df_reviews_tmp.shape

counter = 0
df_reviews_tmp["review_len"] = 0
for row in df_reviews_all.index:
	counter = counter + 1
	df_reviews_tmp.loc[row, "review_len"] = len(df_reviews_all.text[row])
#print df_reviews_tmp.shape

df_reviews_tmp.to_csv(json_data_folder + "reviews_final.csv", index = False, encoding = 'utf-8', header = False)
print ("Completed (3) pull in new json files and convert them to flat tabular structures - Prep the reviews json file")
#############################################################################################


#############################################################################################
#### (3) pull in new json files and convert them to flat tabular structures #################
#### Prep the tips json file ################################################################
#############################################################################################
with open(json_data_folder + "yelp_academic_dataset_tip.json", 'r') as tips_file:
	tips_json = '[' + ','.join(tips_file.readlines()) + ']'

df_tips_all = pd.read_json(tips_json)

ls_flat_columns = ["user_id", "date", "business_id", "likes"]

df_tips_flat = df_tips_all[ls_flat_columns]
df_tips_flat.to_csv(json_data_folder + "tips_final.csv", index = False, encoding = 'utf-8', header = False)
print ("Completed (3) pull in new json files and convert them to flat tabular structures - Prep the tips json file")
#############################################################################################


#############################################################################################
#### (3) pull in new json files and convert them to flat tabular structures #################
#### Prep the users json file ###############################################################
#############################################################################################
with open(json_data_folder + "/yelp_academic_dataset_user.json", 'r') as users_file:
	users_json = '[' + ','.join(users_file.readlines()) + ']'

df_users_all = pd.read_json(users_json)
df_users_all.set_index("user_id", inplace = True)
print df_users_all.shape

ls_flat_columns = ["yelping_since", "review_count", "fans", "average_stars"]
df_users_tmp = df_users_all[ls_flat_columns]
print df_users_tmp.shape

counter = 0
df_users_tmp["num_friends"] = 0
for row in df_users_all.index:
	if counter % 100 == 0:
		print counter
	counter = counter + 1
	df_users_tmp.loc[row, "num_friends"] = len(df_users_all.friends[row])
print df_users_tmp.shape

ls_nested_numeric_columns = ["votes", "compliments"]
for col in ls_nested_numeric_columns:

	print col

	s_json = "["
	for row in df_users_all.index:
		s_json = s_json + str(df_users_all[col][row]) + ","
	s_json = s_json[:-1] + "]"

	s_json = s_json.replace("u'", "\"")
	s_json = s_json.replace("'", "\"")
	
	df_json = pd.read_json(s_json)
	df_json.fillna(0, inplace = True)
	
	ls_column_names = []
	for nested_col in df_json.columns:
		ls_column_names.append(col + "_" + nested_col)
	df_json.columns = ls_column_names
	df_json.index = df_users_tmp.index
	print df_json.shape
	df_users_tmp = df_users_tmp.join(df_json)
	print df_users_tmp.shape


ls_nested_categorical_columns = ["elite"]
for col in ls_nested_categorical_columns:

	print col

	ls_unique_values = []

	for row in df_users_all.index:
		for vl in df_users_all[col][row]:
			if vl not in ls_unique_values:
				ls_unique_values.append(vl)

	ls_rows = []
	ls_header = ["elite_2005", "elite_2006", "elite_2007", "elite_2008", "elite_2009", "elite_2010", "elite_2011", "elite_2012", "elite_2013", "elite_2014", "elite_2015"]
	for row in df_users_all.index:
		ls_this_row = []
		for vl in sorted(ls_unique_values):
			if vl in df_users_all[col][row]:
				ls_this_row.append(1)
			else:
				ls_this_row.append(0)
		ls_rows.append(ls_this_row)

	df_elite = pd.DataFrame(ls_rows, columns = ls_header, index = df_users_tmp.index)
	print df_elite.shape
	df_elite["sum_years_elite"] = df_elite.sum(axis = 1)
	print df_elite.shape
	df_users_tmp = df_users_tmp.join(df_elite)
	print df_users_tmp.shape

df_users_tmp.yelping_since = pd.to_datetime(df_users_tmp.yelping_since)

df_users_tmp.to_csv(json_data_folder + "users_final.csv", index = True, encoding = 'utf-8', header = False)
print ("Completed (3) pull in new json files and convert them to flat tabular structures - Prep the users json file")
#############################################################################################


#############################################################################################
#### (3) pull in new json files and convert them to flat tabular structures #################
#### Prep the business json file ############################################################
#############################################################################################
with open(json_data_folder + "/yelp_academic_dataset_business.json", 'r') as business_file:
	business_json = '[' + ','.join(business_file.readlines()) + ']'

df_business_all = pd.read_json(business_json)

df_business_all = df_business_all.drop(["type", "state", "name"], axis = 1)
df_business_all.set_index("business_id", inplace = True)

ls_flat_columns = ["latitude", "longitude", "review_count", "stars"]
df_business_wip = df_business_all[ls_flat_columns]
print df_business_wip.shape

ls_nested_list_categorical_columns = ["neighborhoods", "categories"]
for col in ls_nested_list_categorical_columns:

	print col
	ls_unique_values = []
	for row in df_business_all.index:
		for vl in df_business_all[col][row]:
			if vl not in ls_unique_values:
				ls_unique_values.append(vl)
	ls_unique_values = sorted(ls_unique_values)

	ls_rows = []
	ls_header = []
	ls_chars_to_replace = [" ", "/", "'", "-", "(", ")", ",", "&", "__"]
	for vl in ls_unique_values:
		for c in ls_chars_to_replace:
			vl = str(vl).replace(c, "_")
		ls_header.append(col + "_" + str(vl))

	for row in df_business_all.index:
		ls_this_row = []
		for vl in sorted(ls_unique_values):
			if vl in df_business_all[col][row]:
				ls_this_row.append(1)
			else:
				ls_this_row.append(0)
		ls_rows.append(ls_this_row)

	df_business_tmp = pd.DataFrame(ls_rows, columns = ls_header, index = df_business_wip.index)

	df_business_tmp[col + "_sum"] = df_business_tmp.sum(axis = 1)

	for col in df_business_tmp.columns:
		i_this_col = np.sum(df_business_tmp[col])
		if i_this_col <= 5:
			df_business_tmp.drop(col, axis = 1, inplace = True)
			#print col + " was dropped"

	print df_business_tmp.shape
	df_business_wip = df_business_wip.join(df_business_tmp)
	print df_business_wip.shape


ls_nested_categorical_columns = ["city"]
for col in ls_nested_categorical_columns:

	print col
	ls_unique_values = sorted(np.unique(df_business_all[col]))

	ls_rows = []
	ls_header = []
	for vl in ls_unique_values:
		ls_chars_to_replace = [" ", "/", "'", "-", "(", ")", ",", "&", "__"]
		for c in ls_chars_to_replace:
			vl = str(vl).replace(c, "_")
		ls_header.append(col + "_" + str(vl))
	print ls_header

	for row in df_business_all.index:
		ls_this_row = []
		for vl in sorted(ls_unique_values):
			if vl in df_business_all[col][row]:
				ls_this_row.append(1)
			else:
				ls_this_row.append(0)
		ls_rows.append(ls_this_row)

	df_business_tmp = pd.DataFrame(ls_rows, columns = ls_header, index = df_business_wip.index)

	df_business_tmp[col + "_sum"] = df_business_tmp.sum(axis = 1)

	for col in df_business_tmp.columns:
		i_this_col = np.sum(df_business_tmp[col])
		if i_this_col <= 5:
			df_business_tmp.drop(col, axis = 1, inplace = True)
			#print col + " was dropped"

	print df_business_tmp.shape
	df_business_wip = df_business_wip.join(df_business_tmp)
	print df_business_wip.shape


ls_nested_boolean_columns = ["open"]
for col in ls_nested_boolean_columns:

	print col

	ls_rows = []
	ls_header = [col + "_True"]

	for row in df_business_all.index:
		ls_this_row = []
		if df_business_all[col][row]:
			ls_this_row.append(1)
		else:
			ls_this_row.append(0)
		ls_rows.append(ls_this_row)

	df_business_tmp = pd.DataFrame(ls_rows, columns = ls_header, index = df_business_wip.index)
	print df_business_tmp.shape
	df_business_wip = df_business_wip.join(df_business_tmp)
	print df_business_wip.shape


ls_nested_json_categorical_columns = ["attributes"]
ls_chars_to_replace = [" ", "/", "'", "-", "(", ")", "&", "__"]
ls_descr = []
ls_values = []
ls_idx = []

df_business_all.reset_index(inplace = True)
for rw in df_business_all.index:
	if rw % 100 == 0:
		print str(rw)
	s_business_id = df_business_all.business_id[rw]
	s_json_test = str(df_business_all.attributes[rw])[1:-1]

	s_json_test = s_json_test.replace(" u'", "")
	s_json_test = s_json_test.replace("u'", "")
	s_json_test = s_json_test.replace("': ", ":")
	s_json_test = s_json_test.replace("':", ":")
	s_json_test = s_json_test.replace("' ,", ",")
	s_json_test = s_json_test.replace("',", ",")
	s_json_test = s_json_test.replace("{}", "False")

	ls_json_test = s_json_test.split(",")
	for cnt in np.arange(len(ls_json_test)):
		ls_json_test[cnt] = ls_json_test[cnt].lstrip()

	ls_json_pairs = []
	for vl in ls_json_test:
		ls_json_pairs.append(vl.split(":"))

	i_lvl = 0
	ls_str_lvl = [] 
	ls_str_lvl.append("")
	if s_json_test != "":
		for vl in ls_json_pairs:
			ls_idx.append(s_business_id)
			if "{" in vl[1]:
				i_lvl = i_lvl + 1
				if i_lvl >= len(ls_str_lvl):
					ls_str_lvl.append(vl[0])
					ls_descr.append(ls_str_lvl[i_lvl] + "_" + str(vl[1].split(",")[0][1:]))
					ls_values.append(str(vl[2]))
				else:
					ls_str_lvl[i_lvl] = vl[0]
					ls_descr.append(ls_str_lvl[i_lvl] + "_" + str(vl[1].split(",")[0][1:]))
					ls_values.append(str(vl[2]))
			elif "}" in vl[1]:
				ls_descr.append(ls_str_lvl[i_lvl] + "_" + str(vl[0]))
				ls_values.append(str(vl[1][:-1]))
				i_lvl = i_lvl - 1
			else:
				if i_lvl > 0:
					ls_descr.append(ls_str_lvl[i_lvl] + "_" + str(vl[0]))
					ls_values.append(str(vl[1]))
				else:
					ls_descr.append(str(vl[0]))
					ls_values.append(str(vl[1]))

	for cnt in np.arange(len(ls_descr)):
		for c in ls_chars_to_replace:
			ls_descr[cnt] = ls_descr[cnt].replace(c, "_").lower()

	for cnt in np.arange(len(ls_values)):
		if str(type(ls_values[cnt])) == "<type 'str'>":
			if "'" in ls_values[cnt]:
				ls_values[cnt] = ls_values[cnt].replace("'", "")

		if ls_values[cnt] == "True":
			ls_values[cnt] = 1
		elif ls_values[cnt] == "False":
			ls_values[cnt] = 0
		elif unicode(str(ls_values[cnt]), "utf-8").isnumeric():
			ls_values[cnt] = float(ls_values[cnt])

ls_combined = zip(ls_idx, ls_descr, ls_values)

df_stacked = pd.DataFrame(ls_combined, columns = ["business_id", "metric", "value"])
df_stacked["check"] = df_stacked.business_id + df_stacked.metric
df_stacked["row_counter"] = np.arange(df_stacked.shape[0])

df_de_duped = df_stacked.groupby(["check"]).min()
df_de_duped["check"] = df_de_duped.business_id + df_de_duped.metric
df_de_duped["check"].value_counts()

df_pivoted = df_de_duped.pivot(index = "business_id", columns = "metric", values = "value")

df_pivoted.replace(["True}", "False}"], 0, inplace = True)
df_pivoted.replace([" True"], 1, inplace = True)
df_pivoted.replace([" False"], 0, inplace = True)

ls_columns_to_drop = []
ls_columns_numeric = []
ls_columns_others = []

for col in df_pivoted.columns:
	if (len(np.unique(df_pivoted[col].fillna(0))) == 1):
		ls_columns_to_drop.append(col)
	elif (len(np.unique(df_pivoted[col].fillna(0))) == 2):
		if ((np.unique(df_pivoted[col].fillna(0))[0]) == float(0.0)) & ((np.unique(df_pivoted[col].fillna(0))[1]) == float(1.0)):
			ls_columns_numeric.append(col)
	else:
		ls_columns_others.append(col)

df_pivoted.drop(ls_columns_to_drop, axis = 1, inplace = True)

for cols in ls_columns_numeric:
	df_pivoted[cols].fillna(0, inplace = True)

min_num_cases = 5
for col in ls_columns_others:
	tmp_df = pd.get_dummies(df_pivoted[col])
	tmp_list = list(tmp_df.columns)
	for cntr in np.arange(len(tmp_list)):
		tmp_list[cntr] = col + "_" + str(tmp_list[cntr])
	tmp_df.columns = tmp_list

	df_pivoted = df_pivoted.join(tmp_df)
	df_pivoted = df_pivoted.drop(col, axis = 1)
	for new_col in tmp_df.columns:
		this_col_sum = np.sum(tmp_df[new_col])
		if min_num_cases > this_col_sum:
			df_pivoted = df_pivoted.drop(new_col, axis = 1)

for col in df_pivoted.columns:
	i_this_col = np.sum(df_pivoted[col])
	if i_this_col <= 5:
		df_pivoted.drop(col, axis = 1, inplace = True)
		print col
print df_pivoted.shape

df_business_wip = df_business_wip.join(df_pivoted)
print df_business_wip.shape
df_business_wip.fillna(0, inplace = True)

df_business_wip.to_csv(json_data_folder + "business_final.csv", index = True, encoding = 'utf-8', header = False)
print ("Completed (3) pull in new json files and convert them to flat tabular structures - Prep the business json file")
#############################################################################################


#############################################################################################
#### (4) push the above prepped tabular structures into PostgreSQL ##########################
#### Connect to PostgreSQL and run copy statements to import the prepped CSVs ###############
#############################################################################################
s_users_sql = "COPY tbl_users FROM '" + json_data_folder + "users_final.csv' DELIMITER ',' CSV;"
s_tips_sql = "COPY tbl_tips FROM '" + json_data_folder + "tips_final.csv' DELIMITER ',' CSV;"
s_reviews_sql = "COPY tbl_reviews FROM '" + json_data_folder + "reviews_final.csv' DELIMITER ',' CSV;"
s_checkins_sql = "COPY tbl_checkins FROM '" + json_data_folder + "checkins_final.csv' DELIMITER ',' CSV;"
s_business_sql = "COPY tbl_business FROM '" + json_data_folder + "business_final.csv' DELIMITER ',' CSV;"
cur.execute(s_users_sql)
cur.execute(s_tips_sql)
cur.execute(s_reviews_sql)
cur.execute(s_checkins_sql)
cur.execute(s_business_sql)

s_map_ids_sql = "COPY tbl_map_ids FROM '" + csv_data_folder + "map_ids_final.csv' DELIMITER ',' CSV;"
s_labelled_cases = "COPY tbl_labelled_cases FROM '"+ csv_data_folder + "labelled_cases_final.csv' DELIMITER ',' CSV;"
s_non_labelled_cases = "COPY tbl_non_labelled_cases FROM '" + csv_data_folder + "non_labelled_cases_final.csv' DELIMITER ',' CSV;"
cur.execute(s_map_ids_sql)
cur.execute(s_labelled_cases)
cur.execute(s_non_labelled_cases)

s_all_cases_step_1 = "INSERT INTO tbl_all_cases SELECT id, date, restaurant_id, one_star, two_star, three_star, 'train' as dataset FROM tbl_labelled_cases;"
s_all_cases_step_2 = "INSERT INTO tbl_all_cases SELECT id, date, restaurant_id, one_star, two_star, three_star, 'phase_II' as dataset FROM tbl_non_labelled_cases;"
cur.execute(s_all_cases_step_1)
cur.execute(s_all_cases_step_2)

s_tidy_up_rogue_dates_in_labelled_cases = "DELETE FROM tbl_labelled_cases WHERE date IN ('2012-12-30', '2013-12-30');"
s_tidy_up_rogue_dates_in_all_cases = "DELETE FROM tbl_all_cases WHERE date IN ('2012-12-30', '2013-12-30');"
cur.execute(s_tidy_up_rogue_dates_in_labelled_cases)
cur.execute(s_tidy_up_rogue_dates_in_all_cases)
print ("Completed (4) push the above prepped tabular structures into PostgreSQL - Connect to PostgreSQL and run copy statements to import the prepped CSVs")
#############################################################################################


#############################################################################################
#### (5) tidy up any files created during the prep process ##################################
#### Delete the prepped CSVs to keep the folder and process tidy ############################
#############################################################################################
os.remove(json_data_folder + "users_final.csv")
os.remove(json_data_folder + "tips_final.csv")
os.remove(json_data_folder + "reviews_final.csv")
os.remove(json_data_folder + "checkins_final.csv")
os.remove(json_data_folder + "business_final.csv")

os.remove(json_data_folder + "map_ids_final.csv")
os.remove(json_data_folder + "labelled_cases_final.csv")
os.remove(json_data_folder + "non_labelled_cases_final.csv")
print ("Completed (5) tidy up any files created during the prep process - Delete the prepped CSVs to keep the folder and process tidy")
#############################################################################################


#############################################################################################
#### (6) re-build indexes on the tables in PostgreSQL #######################################
#### To make the views run efficiently, re-build the indexes on the tables in PostgreSQL ####
#############################################################################################
cur.execute("CREATE INDEX ON tbl_all_cases (date);")
cur.execute("CREATE INDEX ON tbl_all_cases (restaurant_id);")
cur.execute("CREATE INDEX ON tbl_all_cases (dataset);")

cur.execute("CREATE INDEX ON tbl_labelled_cases (date);")
cur.execute("CREATE INDEX ON tbl_labelled_cases (restaurant_id);")

cur.execute("CREATE INDEX ON tbl_non_labelled_cases (date);")
cur.execute("CREATE INDEX ON tbl_non_labelled_cases (restaurant_id);")

cur.execute("CREATE INDEX ON tbl_business (business_id);")

cur.execute("CREATE INDEX ON tbl_checkins (business_id);")

cur.execute("CREATE INDEX ON tbl_map_ids (restaurant_id);")
cur.execute("CREATE INDEX ON tbl_map_ids (yelp_id);")

cur.execute("CREATE INDEX ON tbl_reviews (business_id);")
cur.execute("CREATE INDEX ON tbl_reviews (date);")

cur.execute("CREATE INDEX ON tbl_tips (user_id);")
cur.execute("CREATE INDEX ON tbl_tips (date);")
cur.execute("CREATE INDEX ON tbl_tips (business_id);")

cur.execute("CREATE INDEX ON tbl_users (user_id);")
print ("Completed (6) re-build indexes on the tables in PostgreSQL - To make the views run efficiently, re-build the indexes on the tables in PostgreSQL")
#############################################################################################


#############################################################################################
#### (7) pull the data into an AMT via the pre-built views in PostgreSQL ####################
#### Run select statement against final view ################################################
#### This will draw data through feeder views which do the feature creation heavy lifting ###
#############################################################################################
outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format("SELECT * FROM vw_amt_20150702_v02 ORDER BY ID ASC")
with open(json_data_folder + "amt.csv", 'w') as f:
    cur.copy_expert(outputquery, f)

cur.close()
con.close()

df_all = pd.read_csv(json_data_folder + "amt.csv", index_col = "id")
print ("Completed (7) pull the data into an AMT via the pre-built views in PostgreSQL")

df_all = pd.read_csv(csv_data_folder + "amt.csv", index_col = "id")

df_train = df_all[df_all.dataset == "train"]
df_phase_II = df_all[df_all.dataset == "phase_II"]

target_columns = ["one_star", "two_star", "three_star"]
df_train_targets = df_train[target_columns]

ls_cols_to_drop = ['restaurant_id', 'date', 'one_star', 'two_star', 'three_star', 'dataset']
df_train_expl = df_train.drop(ls_cols_to_drop, axis = 1)
df_phase_II_expl = df_phase_II.drop(ls_cols_to_drop, axis = 1)
#############################################################################################


#############################################################################################
#### (8) load the pickled models and predict each of the targets ############################
#### models to predict one_star violations ##################################################
#############################################################################################
#clf = GradientBoostingRegressor(learning_rate = 0.05, n_estimators = 500, max_depth = 15, subsample = 0.7, max_features = 250, verbose = 0)
#clf.fit(df_train_expl, np.ravel(pd.DataFrame(df_train_targets["one_star"].values)))
#joblib.dump(clf, model_source_folder + 'mdl_one_star_gbm.pkl')
clf = joblib.load(model_source_folder + 'mdl_one_star_gbm.pkl')
mdl_one_star_gbm_predictions = clf.predict(df_phase_II_expl)

#clf = RandomForestRegressor(n_jobs = -1, max_features = 450, n_estimators = 1200, bootstrap = False, max_depth = 20, min_samples_leaf = 20)
#clf.fit(df_train_expl, pd.DataFrame(df_train_targets["one_star"].values))
#joblib.dump(clf, model_source_folder + 'mdl_one_star_rf.pkl')
clf = joblib.load(model_source_folder + 'mdl_one_star_rf.pkl')
mdl_one_star_rf_predictions = clf.predict(df_phase_II_expl)

#clf = ExtraTreesRegressor(n_jobs = -1, max_features = 300, n_estimators = 1500, max_depth = 32)
#clf.fit(df_train_expl, pd.DataFrame(df_train_targets["one_star"].values))
#joblib.dump(clf, model_source_folder + 'mdl_one_star_ert.pkl')
clf = joblib.load(model_source_folder + 'mdl_one_star_ert.pkl')
mdl_one_star_ert_predictions = clf.predict(df_phase_II_expl)

#clf = Ridge(alpha = 1500)
#clf.fit(df_train_expl, pd.DataFrame(df_train_targets["one_star"].values))
#joblib.dump(clf, model_source_folder + 'mdl_one_star_ridge.pkl')
clf = joblib.load(model_source_folder + 'mdl_one_star_ridge.pkl')
mdl_one_star_ridge_predictions = clf.predict(df_phase_II_expl)
#############################################################################################


#############################################################################################
#### (8) load the pickled models and predict each of the targets ############################
#### models to predict two_star violations ##################################################
#############################################################################################
#clf = GradientBoostingRegressor(learning_rate = 0.05, n_estimators = 500, max_depth = 15, subsample = 0.7, max_features = 250, verbose = 0)
#clf.fit(df_train_expl, np.ravel(pd.DataFrame(df_train_targets["two_star"].values)))
#joblib.dump(clf, model_source_folder + 'mdl_two_star_gbm.pkl')
clf = joblib.load(model_source_folder + 'mdl_two_star_gbm.pkl')
mdl_two_star_gbm_predictions = clf.predict(df_phase_II_expl)

#clf = Ridge(alpha = 5)
#clf.fit(df_train_expl, pd.DataFrame(df_train_targets["two_star"].values))
#joblib.dump(clf, model_source_folder + 'mdl_two_star_ridge.pkl')
clf = joblib.load(model_source_folder + 'mdl_two_star_ridge.pkl')
mdl_two_star_ridge_predictions = clf.predict(df_phase_II_expl)
#############################################################################################


#############################################################################################
#### (8) load the pickled models and predict each of the targets ############################
#### models to predict three_star violations ################################################
#############################################################################################
#clf = GradientBoostingRegressor(learning_rate = 0.05, n_estimators = 500, max_depth = 15, subsample = 0.7, max_features = 250, verbose = 0)
#clf.fit(df_train_expl, np.ravel(pd.DataFrame(df_train_targets["three_star"].values)))
#joblib.dump(clf, model_source_folder + 'mdl_three_star_gbm.pkl')
clf = joblib.load(model_source_folder + 'mdl_three_star_gbm.pkl')
mdl_three_star_gbm_predictions = clf.predict(df_phase_II_expl)

#clf = RandomForestRegressor(n_jobs = -1, max_features = 150, n_estimators = 2000, bootstrap = True, max_depth = 60, min_samples_leaf = 1)
#clf.fit(df_train_expl, pd.DataFrame(df_train_targets["three_star"].values))
#joblib.dump(clf, model_source_folder + 'mdl_three_star_rf.pkl')
clf = joblib.load(model_source_folder + 'mdl_three_star_rf.pkl')
mdl_three_star_rf_predictions = clf.predict(df_phase_II_expl)

#clf = ExtraTreesRegressor(n_jobs = -1, max_features = 275, n_estimators = 2000, max_depth = 40)
#clf.fit(df_train_expl, pd.DataFrame(df_train_targets["three_star"].values))
#joblib.dump(clf, model_source_folder + 'mdl_three_star_ert.pkl')
clf = joblib.load(model_source_folder + 'mdl_three_star_ert.pkl')
mdl_three_star_ert_predictions = clf.predict(df_phase_II_expl)
#############################################################################################


#############################################################################################
#### (9) blend each of the models for each target ###########################################
#############################################################################################
blended_one_star_predictions = (0.3 * mdl_one_star_gbm_predictions) + (0.14 * mdl_one_star_rf_predictions) + (0.45 * mdl_one_star_ert_predictions) + (0.05 * np.ravel(mdl_one_star_ridge_predictions)) + 0.1
blended_two_star_predictions = (1 * mdl_two_star_gbm_predictions) + (0.5 * np.ravel(mdl_two_star_ridge_predictions))
blended_three_star_predictions = (0.5 * mdl_three_star_gbm_predictions) + (0.42 * mdl_three_star_rf_predictions) + (0.42 * mdl_three_star_ert_predictions) - 0.15
#############################################################################################


#############################################################################################
#### # (10) generate a scores file with scores for the three targets in it ##################
#############################################################################################
dict_predictions = {'*': blended_one_star_predictions, '**': blended_two_star_predictions, '***': blended_three_star_predictions}
df_predictions = pd.DataFrame(dict_predictions, index = df_phase_II_expl.index)
df_predictions_int = df_predictions.copy(deep = True)

for col in df_predictions_int.columns:
	for idx in df_predictions_int.index:
		df_predictions_int[col][idx] = round(df_predictions_int[col][idx], 0)

df_predictions_int.to_csv(scores_output_folder + scores_output_file, index = True)
#############################################################################################
