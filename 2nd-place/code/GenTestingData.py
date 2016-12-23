'''
This file takes the data provided by Yelp and the contest hosts and builds a testing data set used in LearnTest.py for making predictions
Date: August 28, 2015
'''

import json
import csv
import codecs
from BusinessClass import BusinessClass
from InspectionClass import InspectionClass
from ReviewClass import ReviewClass
import math

#create a dictionary of businesses using the yelp data set of businesses
businesses = {}
with open("yelp_boston_academic_dataset/yelp_academic_dataset_business.json") as f:
    for line in f:
        businessInfo = json.loads(line)
        business = BusinessClass(businessInfo["city"], businessInfo["review_count"], businessInfo["name"], businessInfo["neighborhoods"],
                            businessInfo["type"], businessInfo["business_id"], businessInfo["full_address"], businessInfo["hours"],
                            businessInfo["state"], businessInfo["longitude"], businessInfo["stars"], businessInfo["latitude"],
                            businessInfo["attributes"], businessInfo["open"], businessInfo["categories"])
        businesses[business.business_id] = business

#create a hash map that maps restaurant id to businesses id in order to merge business information with the inspection data set
restaurant_to_yelp = {}
with open("restaurant_ids_to_yelp_ids.csv", "rb") as csvfile:
    mergeReader = csv.reader(csvfile, delimiter=',')
    mergeReader.next()
    for r in mergeReader:
        restaurant_to_yelp[r[0]] = r[1]

#note that there are some restaurant ids that have multiple business ids mapping to it.
#I manually created a file that collapsed the multiple business ids into the first business id listed in the restaurant_ids_to_yelp_ids file
#the code below creates a hash from that file so that the second or third etc business id information are treated to have the first business id for that business.
#I think this only matters for the review data, not completely sure though.
yelp_duplicate_ids = {}
with open("yelp_duplicate_ids.csv", "rb") as csvfile:
    dupReader = csv.reader(csvfile, delimiter=',')
    dupReader.next()
    for d in dupReader:
        yelp_duplicate_ids[d[1]] = d[0]

#load the training inspection data set (AllViolations.csv)
#generate a dictionary of inspections with restaurant_id as the key
#note that it is necessary to use the training inspection data because many of the variables used in the test data requires the training inspections to build (e.g., num_violations)
train_inspections = {}
with open("AllViolations.csv", "rb") as csvfile:
    inspectionReader = csv.reader(csvfile, delimiter=',')
    inspectionReader.next()
    for inspectionInfo in inspectionReader:
        inspection = InspectionClass(inspectionInfo[0], inspectionInfo[1], inspectionInfo[2], inspectionInfo[3], inspectionInfo[4], inspectionInfo[5], inspectionInfo[6:95], True)
        businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections.append(inspection)
        businesses[restaurant_to_yelp[inspection.restaurant_id]].restaurant_id = inspection.restaurant_id
        #if the inspection's restaurant_id is already in the dictionary simply append onto the list
        #else create a new list for that restaurant_id and add this inspection into it
        if inspection.restaurant_id in train_inspections:
            train_inspections[inspection.restaurant_id].append(inspection)
        else:
            train_inspections[inspection.restaurant_id] = [inspection]

#the code below determines whether each inspection is part of a set of multiple inspections
#this was necessary in phase 1 because a large number of the inspections were follow-ups from initial failures
#this information was not used in phase 2 because being a part of a set of multiple inspections requires first having a failure, which we cannot predict ahead of time
#nevertheless this code is left in for the sake of completeness
#note that so far only training inspections are included
for key in businesses.keys():
    business = businesses[key]
    business.sortInspections()
    # see if inspection is first within a set
    for i in range(0, len(business.inspections)):
        # it is initialized to false unless otherwise specified as true below
        if i == 0 and len(business.inspections) > 1 and business.inspections[i+1].days - business.inspections[i].days <= 42:
            # if it's the first inspection and there is another inspection within 40 days after
            business.inspections[i].is_first_in_set = True
            business.inspections[i].related_inspection = "," + business.inspections[i+1].one_star + "," + business.inspections[i+1].two_star + "," + business.inspections[i+1].three_star
        if i > 0 and len(business.inspections) > i+1 and business.inspections[i].days - business.inspections[i-1].days > 42 and business.inspections[i+1].days - business.inspections[i].days <= 42:
            # if it's not the first inspection, but there is no inspection within 40 days before and there is another inspection within 40 days after
            business.inspections[i].is_first_in_set = True
            business.inspections[i].related_inspection = "," + business.inspections[i+1].one_star + "," + business.inspections[i+1].two_star + "," + business.inspections[i+1].three_star

    # see if inspection is second within a set
    for i in range(1, len(business.inspections)):
        if business.inspections[i-1].is_first_in_set and business.inspections[i].days - business.inspections[i-1].days <= 42:
            business.inspections[i].is_second_in_set = True
            business.inspections[i].related_inspection = "," + business.inspections[i-1].one_star + "," + business.inspections[i-1].two_star + "," + business.inspections[i-1].three_star

    # see if inspection is third within a set
    for i in range(1, len(business.inspections)):
        if business.inspections[i-1].is_second_in_set and business.inspections[i].days - business.inspections[i-1].days <= 42:
            business.inspections[i].is_later_in_set = True

    # see if inspection is fourth or further within a set
    for i in range(1, len(business.inspections)):
        if not (business.inspections[i-1].is_second_in_set or business.inspections[i-1].is_first_in_set) and business.inspections[i].days - business.inspections[i-1].days <= 42:
            business.inspections[i].is_later_in_set = True

#the code below makes guesses on some of the test inspections
#note that due to the fact that failed inspections (i.e., high violation counts) are re-inspected and the re-inspection results are coded incorrectly, it is almost always the case that the second inspection following a failed inspection (usually within a month) has the exact same number of violations. Therefore in this case instead of predicting, simply setting the predicted result equal to the previous failed inspection is better
#basically, if in the test data the observation meets the "guessing" criteria, we "guess" the outcome and save into the test_guess_final.csv file. Otherwise we do prediction later
test_inspections = {}
with open("PhaseIISubmissionFormat_test.csv", "rb") as csvfile:
    inspectionReader = csv.reader(csvfile, delimiter=',')
    inspectionReader.next()
    for inspectionInfo in inspectionReader:
        inspection = InspectionClass(inspectionInfo[0], inspectionInfo[1], inspectionInfo[2], "", "", "", inspectionInfo[6:95], False)
        if (len(businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections) > 0) and inspection.days - businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections[-1].days <= 42 and not businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections[-1].is_second_in_set and not businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections[-1].is_later_in_set:
            inspection.one_star = businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections[-1].one_star
            inspection.two_star = businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections[-1].two_star
            inspection.three_star = businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections[-1].three_star
        else:
            inspection.one_star = ""
            inspection.two_star = ""
            inspection.three_star = ""
        businesses[restaurant_to_yelp[inspection.restaurant_id]].inspections.append(inspection)
        businesses[restaurant_to_yelp[inspection.restaurant_id]].restaurant_id = inspection.restaurant_id
        if inspection.restaurant_id in test_inspections:
            test_inspections[inspection.restaurant_id].append(inspection)
        else:
            test_inspections[inspection.restaurant_id] = [inspection]

#the code below re-performs the earlier code which determines whether each inspection is part of a set of multiple inspections
#the reason this is done is because the earlier code did not include the test inspections
#again, this was necessary in phase 1 but not in phase 2
for key in businesses.keys():
    business = businesses[key]
    business.sortInspections()
    # see if inspection is first within a set
    for i in range(0, len(business.inspections)):
        # it is initialized to false unless otherwise specified as true below
        if i == 0 and len(business.inspections) > 1 and business.inspections[i+1].days - business.inspections[i].days <= 42:
            # if it's the first inspection and there is another inspection within 40 days after
            business.inspections[i].is_first_in_set = True
            business.inspections[i].related_inspection = "," + business.inspections[i+1].one_star + "," + business.inspections[i+1].two_star + "," + business.inspections[i+1].three_star
        if i > 0 and len(business.inspections) > i+1 and business.inspections[i].days - business.inspections[i-1].days > 42 and business.inspections[i+1].days - business.inspections[i].days <= 42:
            # if it's not the first inspection, but there is no inspection within 40 days before and there is another inspection within 40 days after
            business.inspections[i].is_first_in_set = True
            business.inspections[i].related_inspection = "," + business.inspections[i+1].one_star + "," + business.inspections[i+1].two_star + "," + business.inspections[i+1].three_star

    # see if inspection is second within a set
    for i in range(1, len(business.inspections)):
        if business.inspections[i-1].is_first_in_set and business.inspections[i].days - business.inspections[i-1].days <= 42:
            business.inspections[i].is_second_in_set = True
            business.inspections[i].related_inspection = "," + business.inspections[i-1].one_star + "," + business.inspections[i-1].two_star + "," + business.inspections[i-1].three_star

    # see if inspection is third within a set
    for i in range(1, len(business.inspections)):
        if business.inspections[i-1].is_second_in_set and business.inspections[i].days - business.inspections[i-1].days <= 42:
            business.inspections[i].is_later_in_set = True

    # see if inspection is fourth or further within a set
    for i in range(1, len(business.inspections)):
        if not (business.inspections[i-1].is_second_in_set or business.inspections[i-1].is_first_in_set) and business.inspections[i].days - business.inspections[i-1].days <= 42:
            business.inspections[i].is_later_in_set = True

#get the average stars for each user
users = {}
with open("yelp_boston_academic_dataset/yelp_academic_dataset_user.json") as f:
    for line in f:
        userInfo = json.loads(line)
        users[userInfo["user_id"]] = userInfo["average_stars"]

#get the yelp review data: review_id, user_id, stars, de-meaned stars, date, text, business_id
with open("yelp_boston_academic_dataset/yelp_academic_dataset_review.json") as f:
    for line in f:
        reviewInfo = json.loads(line)
        review = ReviewClass(reviewInfo["review_id"], reviewInfo["user_id"], reviewInfo["stars"], reviewInfo["stars"] - users[reviewInfo["user_id"]], reviewInfo["date"],
                             reviewInfo["text"], reviewInfo["business_id"])
        if review.business_id in businesses.keys():
            businesses[review.business_id].reviews.append(review)
        else:
            businesses[yelp_duplicate_ids[review.business_id]].reviews.append(review)
#sort the reviews for each business by date
#calculate some metrics for the reviews for each business
for key in businesses.keys():
    businesses[key].sortReviews()
    businesses[key].calculateReviews()

#generate a list of business categories by going through all of the categories of each business
categories = {}
for key in businesses:
    for i in businesses[key].categories:
        if i not in categories.keys():
            categories[i.replace(",", "")] = 1
print categories.keys()

#generate a list of business neighborhoods by going through all of the neighborhood of each business
neighborhoods = {}
for key in businesses:
    for i in businesses[key].neighborhoods:
        if i not in neighborhoods.keys():
            neighborhoods[i.replace(",", "")] = 1
print neighborhoods.keys()

#generate a list of business attributes by going through all of the attributes of each business
attributes = {}
for key in businesses:
    for i in businesses[key].attributes:
        if i not in attributes.keys():
            attributes[i.replace(",", "")] = 1
print attributes.keys()

#generate a list of business ambiences by going through all of the ambiences of each business
ambiences = {}
for key in businesses:
    if "Ambience" in businesses[key].attributes.keys():
        for i in businesses[key].attributes["Ambience"]:
            if i not in ambiences.keys():
                ambiences[i.replace(",", "")] = 1
print ambiences.keys()

#generate a list of businesses with 5 or more inspections to include as dummy variables
k_keys = {}
for key in businesses:
    c = 0
    for i in businesses[key].inspections:
        if i.days < 3463:
            c += 1
        if c > 4:
            k_keys[key] = 1
            break

#build the testing data set by merging the necessary variables onto each inspection in the testing set
test_learn = {}
test_guess = {}
for key in businesses:
    num_inspections = 0
    num_violations = 0
    num_one_viol = 0
    num_two_viol = 0
    num_three_viol = 0
    for i in businesses[key].inspections:

        #note that a lot of information from the training set is required so different steps are taken for whether the inspection is in train or test
        if not i.is_train:
            violations = ""

            #label if inspection is part of a set
            if i.one_star != "" and ((int(i.three_star) >= 1) or (int(i.one_star) >= 9) or (int(i.two_star) >= 2)):
                violations = str(int(i.one_star) + 2*int(i.two_star) + 5*int(i.three_star))
            part_of_set = "0"
            if i.is_first_in_set or i.is_second_in_set:
                part_of_set = "1"

            num_reviews = 0
            recent_reviews = 0
            stars = 0
            weighted_stars = 0
            recent_stars = 0
            has_poison = 0
            has_unclean = 0
            has_health = 0
            avg_rev_length = 0
            rev_length = 0

            #calculate the number of reviews, total and average review length, total stars, weighted stars, number of "poison", "unclean", "health terms used, and number of recent reviews and stars prior to this inspection
            for r in businesses[key].reviews:
                if i.days - r.days < 0:
                    break
                else:
                    num_reviews += 1
                    rev_length += r.length
                    avg_rev_length = float(rev_length) / num_reviews
                    stars += r.stars
                    weighted_stars += r.weighted_stars
                    if r.has_poison:
                        has_poison += 1
                    if r.has_unclean:
                        has_unclean += 1
                    if r.has_health:
                        has_health += 1
                    if i.days - r.days < 180:
                        recent_reviews += 1
                        recent_stars += r.stars

            #calculate the average stars and weighted stars and recent stars of reviews prior to this inspection
            if num_reviews > 0:
                stars = stars / float(num_reviews)
                weighted_stars = weighted_stars / float(num_reviews)
            else:
                stars = 0
                weighted_stars = 0
            if recent_reviews > 0:
                recent_stars = recent_stars / float(recent_reviews)
            else:
                recent_stars = 0

            #calculate days since last inspection and the number of recent violations
            recent_violations = 0
            days_since_last_insp = 0
            for insp in businesses[key].inspections:
                if i.days - insp.days < 45:
                    break
                if i.days - insp.days < 365 and insp.one_star != "":
                    recent_violations = int(insp.one_star) + 2*int(insp.two_star) + 5*int(insp.three_star)
                days_since_last_insp = i.days - insp.days

            num_neighbor_insps = 0
            num_neighbors = 0
            #calculate the number of businesses within a 1.2 kilometer distance of the business and the number of inspections by the neighbors
            for k in businesses.keys():
                distance = math.sqrt(math.pow((businesses[k].longitude - businesses[key].longitude) * 111, 2) + math.pow((businesses[k].latitude - businesses[key].latitude) * 111, 2))
                if k != key and distance < 1.2:
                    num_neighbors += 1
                    for insp in businesses[k].inspections:
                        if insp.days < i.days:
                            num_neighbor_insps += 1

            #calculate day of most recent inspection (from training set) or review
            for index in range(1, len(businesses[key].inspections)):
                if businesses[key].inspections[-index].is_train:
                    last_insp_review = businesses[key].inspections[-index].days
                    break
            if businesses[key].reviews[-1].days > last_insp_review:
                last_insp_review = businesses[key].reviews[-1].days

            #write a list of the variables that are to be used in the test set
            info = i.inspection_id + "," + i.date + "," + i.restaurant_id + "," + violations + "," + businesses[key].name + "," + part_of_set + "," + str(num_reviews) + "," + str(stars) + "," + str(i.days) + "," + str(num_inspections) + "," + str(num_violations) + "," + str(num_one_viol) + "," + str(num_two_viol) + "," + str(num_three_viol) + "," + str(days_since_last_insp) + "," + str(num_neighbor_insps) + "," + str(has_poison) + "," + str(has_unclean) + "," + str(has_health) + "," + str(businesses[key].longitude) + "," + str(businesses[key].latitude) + "," + str(last_insp_review) + "," + i.is2007 + "," + i.is2008 + "," + i.is2009 + "," + i.is2010 + "," + i.is2011 + "," + i.is2012 + "," + i.is2013 + "," + i.is2014 + "," + i.is2015 + "," + i.isJan + "," + i.isFeb + "," + i.isMar + "," + i.isApr + "," + i.isMay + "," + i.isJun + "," + i.isJul + "," + i.isAug + "," + i.isSep + "," + i.isOct + "," + i.isNov + "," + i.isDec + "," + i.isMon + "," + i.isTue + "," + i.isWed + "," + i.isThu + "," + i.isFri

            #add the dummy values for each business category
            for cat in categories.keys():
                if cat in businesses[key].categories:
                    info = info + ",1"
                else:
                    info = info + ",0"

            #add the dummy values for each business neighborhood
            for neigh in neighborhoods.keys():
                if neigh in businesses[key].neighborhoods:
                    info = info + ",1"
                else:
                    info = info + ",0"

            #attributes are added manually depending on the values specified in the Yelp businesses file
            if "Drive-Thru" in businesses[key].attributes.keys():
                if businesses[key].attributes["Drive-Thru"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Alcohol" in businesses[key].attributes.keys():
                if businesses[key].attributes["Alcohol"] == "full_bar":
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Open 24 Hours" in businesses[key].attributes.keys():
                if businesses[key].attributes["Open 24 Hours"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Noise Level" in businesses[key].attributes.keys():
                n = businesses[key].attributes
                if businesses[key].attributes["Noise Level"] == "quiet":
                    info = info + ",1,0"
                elif businesses[key].attributes["Noise Level"] == "average":
                    info = info + ",2,0"
                elif businesses[key].attributes["Noise Level"] == "loud":
                    info = info + ",3,0"
                elif businesses[key].attributes["Noise Level"] == "very_loud":
                    info = info + ",4,0"
                else:
                    info = info + ",0,1"
            else:
                info = info + ",0,1"

            if "Attire" in businesses[key].attributes.keys():
                if businesses[key].attributes["Attire"] == "dressy":
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Good for Kids" in businesses[key].attributes.keys():
                if businesses[key].attributes["Good for Kids"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Price Range" in businesses[key].attributes.keys():
                if businesses[key].attributes["Price Range"] == 1:
                    info = info + ",1,0"
                elif businesses[key].attributes["Price Range"] == 2:
                    info = info + ",2,0"
                elif businesses[key].attributes["Price Range"] == 3:
                    info = info + ",3,0"
                elif businesses[key].attributes["Price Range"] == 4:
                    info = info + ",4,0"
                else:
                    info = info + ",0,1"
            else:
                info = info + ",0,1"

            if "Caters" in businesses[key].attributes.keys():
                if businesses[key].attributes["Caters"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Delivery" in businesses[key].attributes.keys():
                if businesses[key].attributes["Delivery"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Dogs Allowed" in businesses[key].attributes.keys():
                if businesses[key].attributes["Dogs Allowed"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Coat Check" in businesses[key].attributes.keys():
                if businesses[key].attributes["Coat Check"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Payment Types" in businesses[key].attributes.keys():
                if "cash_only" in businesses[key].attributes["Payment Types"].keys():
                    if businesses[key].attributes["Payment Types"]["cash_only"] == True:
                        info = info + ",2"
                    else:
                        info = info + ",1"
                else:
                    info = info + ",0"
            else:
                info = info + ",0"

            if "Take-out" in businesses[key].attributes.keys():
                if businesses[key].attributes["Take-out"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Ages Allowed" in businesses[key].attributes.keys():
                if businesses[key].attributes["Ages Allowed"] == "21plus":
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "By Appointment Only" in businesses[key].attributes.keys():
                if businesses[key].attributes["By Appointment Only"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Wi-Fi" in businesses[key].attributes.keys():
                if businesses[key].attributes["Wi-Fi"] == "free":
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            if "Order at Counter" in businesses[key].attributes.keys():
                if businesses[key].attributes["Order at Counter"] == True:
                    info = info + ",2"
                else:
                    info = info + ",1"
            else:
                info = info + ",0"

            for ambi in ambiences.keys():
                if "Ambience" in businesses[key].attributes.keys():
                    if ambi in businesses[key].attributes["Ambience"].keys():
                        if businesses[key].attributes["Ambience"][ambi] == True:
                            info = info + ",2"
                        else:
                            info = info + ",1"
                    else:
                        info = info + ",0"
                else:
                    info = info + ",0"

            #add dummy values for which business the inspection falls into
            k_info = ""
            for k in k_keys:
                if key == k:
                    k_info += ",1"
                else:
                    k_info += ",0"
            info = info + k_info

            #if the inspection is in need of prediction (i.e., not guessed earlier) then we include into the prediction test set. Otherwise include into the guessed test set
            if violations == "":
                test_learn[i.inspection_id] = info
            else:
                test_guess[i.inspection_id] = info
        else:

            #if the inspection is a part of the training inspections and not test inspections, we update counters for num_inspections and num_violations
            num_inspections += 1
            num_violations += int(i.one_star) + 2*int(i.two_star) + 5*int(i.three_star)

#write out the prediction test set file
f = codecs.open("test_data_final.csv","w",'utf-8')

#write the variable labels
#note that although unlikely, there may be wrong labels resulting from me forgetting to change them as I was removing and adding variables.
f.write("inspection_id,date,restaurant_id,violations,name,part_of_set,review_count,stars,days,num_inspections,num_violations,num_one_viol,num_two_viol,num_three_viol,days_since_last,num_neighbor_insps,has_poison,has_unclean,has_health,longitude,latitude,last_insp_review,2007,2008,2009,2010,2011,2012,2013,2014,2015,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,Mon,Tue,Wed,Thu,Fri")
for cat in categories.keys():
    f.write("," + cat)
for neigh in neighborhoods.keys():
    f.write("," + neigh)
f.write(",Drive-Thru,Alcohol,Open 24 Hours,Noise Level,Noise Level Unknown,Attire,Good for Kids,Price Range,Price Range Unknown,Caters,Delivery,Dogs Allowed,Coat Check,PaymentTypes,Take-out,Ages Allowed,By Appointment Only,Wi-Fi,Order at Counter")
for ambi in ambiences.keys():
    f.write("," + ambi)
k_count = 1
for key in k_keys:
    f.write("," + str(k_count))
    k_count += 1
f.write("\n")

#write the rows of prediction test set data. Note that the first row is written twice, this is because I'm not fluent with Pandas and was somehow losing the first row during training so I added an extra row to account for that
f.write(test_learn.values()[0] + "\n")
for line in sorted(test_learn.keys()):
    f.write(test_learn[line] + "\n")
f.close()


#write out the guessed test set file
f = codecs.open("test_guess_final.csv","w",'utf-8')

#write the variable labels
#note that although unlikely, there may be wrong labels resulting from me forgetting to change them as I was removing and adding variables.
f.write("inspection_id,date,restaurant_id,violations,name,part_of_set,review_count,stars,days,num_inspections,num_violations,num_one_viol,num_two_viol,num_three_viol,days_since_last,num_neighbor_insps,has_poison,has_unclean,has_health,longitude,latitude,last_insp_review,2007,2008,2009,2010,2011,2012,2013,2014,2015,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,Mon,Tue,Wed,Thu,Fri")
for cat in categories.keys():
    f.write("," + cat)
for neigh in neighborhoods.keys():
    f.write("," + neigh)
f.write(",Drive-Thru,Alcohol,Open 24 Hours,Noise Level,Noise Level Unknown,Attire,Good for Kids,Price Range,Price Range Unknown,Caters,Delivery,Dogs Allowed,Coat Check,PaymentTypes,Take-out,Ages Allowed,By Appointment Only,Wi-Fi,Order at Counter")
for ambi in ambiences.keys():
    f.write("," + ambi)
k_count = 1
for key in k_keys:
    f.write("," + str(k_count))
    k_count += 1
f.write("\n")

#write the rows of guessed test set data
for line in sorted(test_guess.keys()):
    f.write(test_guess[line] + "\n")
f.close()

print("done!")
