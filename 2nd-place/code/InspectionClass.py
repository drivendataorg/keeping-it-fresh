'''
This file defines the inspection class. It contains mostly dates and violation metrics. Again, many of its variables are not used in the final train or test data sets.
Date: August 28, 2015
'''

from datetime import datetime

class InspectionClass(object):

    inspection_id = 0
    date = ""
    days = 0
    restaurant_id = ""
    one_star = 0
    two_star = 0
    three_star = 0
    violation_types = []
    num_prior_two_year = 0
    one_star_prior_two_year = 0
    two_star_prior_two_year = 0
    three_star_prior_two_year = 0
    avg_prior_two_year = 0
    avg_one_star_prior_two_year = 0
    avg_two_star_prior_two_year = 0
    avg_three_star_prior_two_year = 0
    num_prior_one_year = 0
    one_star_prior_one_year = 0
    two_star_prior_one_year = 0
    three_star_prior_one_year = 0
    avg_one_star_prior_one_year = 0
    avg_two_star_prior_one_year = 0
    avg_three_star_prior_one_year = 0
    is2007 = "0"
    is2008 = "0"
    is2009 = "0"
    is2010 = "0"
    is2011 = "0"
    is2012 = "0"
    is2013 = "0"
    is2014 = "0"
    is2015 = "0"
    isJan = "0"
    isFeb = "0"
    isMar = "0"
    isApr = "0"
    isMay = "0"
    isJun = "0"
    isJul = "0"
    isAug = "0"
    isSep = "0"
    isOct = "0"
    isNov = "0"
    isDec = "0"
    isMon = "0"
    isTue = "0"
    isWed = "0"
    isThu = "0"
    isFri = "0"

    is_train = False
    is_first_in_set = False
    is_second_in_set = False
    is_later_in_set = False
    related_inspection = ",,,"

    def __init__(self, inspection_id, date, restaurant_id, one_star, two_star, three_star, violation_types, is_train):
        self.inspection_id = inspection_id
        self.date = date
        self.days = self.days_between("2006-01-01", date)
        self.restaurant_id = restaurant_id
        self.one_star = one_star
        self.two_star = two_star
        self.three_star = three_star
        self.violation_types = violation_types
        self.is_train = is_train
        d1 = datetime.strptime(date, "%Y-%m-%d")
        if d1.year == 2007:
            self.is2007 = "1"
        elif d1.year == 2008:
            self.is2008 = "1"
        elif d1.year == 2008:
            self.is2009 = "1"
        elif d1.year == 2010:
            self.is2010 = "1"
        elif d1.year == 2011:
            self.is2011 = "1"
        elif d1.year == 2012:
            self.is2012 = "1"
        elif d1.year == 2013:
            self.is2013 = "1"
        elif d1.year == 2014:
            self.is2014 = "1"
        elif d1.year == 2015:
            self.is2015 = "1"
        if d1.month == 1:
            self.isJan = "1"
        elif d1.month == 2:
            self.isFeb = "1"
        elif d1.month == 3:
            self.isMar = "1"
        elif d1.month == 4:
            self.isApr = "1"
        elif d1.month == 5:
            self.isMay = "1"
        elif d1.month == 6:
            self.isJun = "1"
        elif d1.month == 7:
            self.isJul = "1"
        elif d1.month == 8:
            self.isAug = "1"
        elif d1.month == 9:
            self.isSep = "1"
        elif d1.month == 10:
            self.isOct = "1"
        elif d1.month == 11:
            self.isNov = "1"
        elif d1.month == 12:
            self.isDec = "1"
        if d1.weekday() == 0:
            self.isMon = "1"
        elif d1.weekday() == 1:
            self.isTue = "1"
        elif d1.weekday() == 2:
            self.isWed = "1"
        elif d1.weekday() == 3:
            self.isThu = "1"
        elif d1.weekday() == 4:
            self.isFri = "1"

    def days_between(self, d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)
