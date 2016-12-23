'''
This file defines the review class. It contains mostly dates, text and rating metrics.
Date: August 28, 2015
'''

from datetime import datetime

class ReviewClass(object):

    review_id = 0
    user_id = 0
    stars = 0
    weighted_stars = 0
    date = ""
    days = 0
    text = ""
    business_id = ""
    has_poison = 0
    has_unclean = 0
    has_health = 0
    has_violation = 0
    length = 0

    def __init__(self, review_id, user_id, stars, weighted_stars, date, text, business_id):
        self.review_id = review_id
        self.date = date
        self.days = self.days_between("2006-01-01", date)
        self.user_id = user_id
        self.stars = stars
        self.weighted_stars = weighted_stars
        self.text = text
        self.business_id = business_id
        if "poison" in text:
            self.has_poison = 1
        if "unclean" in text or "Unclean" in text:
            self.has_unclean = 1
        if " health " in text or " Health " in text:
            self.has_health = 1
        self.length = len(text)

    def days_between(self, d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)
