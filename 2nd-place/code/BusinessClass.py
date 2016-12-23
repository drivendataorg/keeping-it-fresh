'''
This file defines the business class. A business contains a list of review and inspection objects. Some of the variables in this class were not used to generate the training or testing data sets, although I have tried all of them.
Date: August 28, 2015
'''
class BusinessClass(object):
    city = ""
    review_count = 0
    name = 0
    neighborhoods = []
    business_type = ""
    business_id = ""
    restaurant_id = ""
    full_address = ""
    hours = {}
    state = ""
    longitude = 0
    stars = 0
    latitude = 0
    attributes = {}
    business_open = False
    categories = []
    inspections = []
    reviews = []
    percent_1star = 0
    percent_2star = 0
    percent_3star = 0
    percent_4star = 0
    percent_5star = 0
    is_chain = "0"

    def __init__(self, city, review_count, name, neighborhoods, business_type, business_id,
                 full_address, hours, state, longitude, stars, latitude, attributes, business_open, categories):
        self.city = city
        self.review_count = review_count
        self.name = name.replace(',', '')
        self.neighborhoods = neighborhoods
        self.business_type = business_type
        self.business_id = business_id
        self.full_address = full_address
        self.hours = hours
        self.state = state
        self.longitude = longitude
        self.stars = stars
        self.latitude = latitude
        self.attributes = attributes
        self.business_open = business_open
        self.categories = categories
        self.inspections = []
        self.reviews = []
        self.review_words = ""
        self.restaurant_id = ""

    def sortReviews(self):
        self.reviews.sort(key=lambda r: r.days, reverse=False)

    def sortInspections(self):
        self.inspections.sort(key=lambda i: i.days, reverse=False)

    def calculateReviews(self):
        num_one_star = 0
        num_two_star = 0
        num_three_star = 0
        num_four_star = 0
        num_five_star = 0
        for r in self.reviews:
            if r.stars == 1:
                num_one_star += 1
            elif r.stars == 2:
                num_two_star += 1
            elif r.stars == 3:
                num_three_star += 1
            elif r.stars == 4:
                num_four_star += 1
            elif r.stars == 5:
                num_five_star += 1
        self.percent_one_star = num_one_star / float(len(self.reviews))
        self.percent_two_star = num_two_star / float(len(self.reviews))
        self.percent_three_star = num_three_star / float(len(self.reviews))
        self.percent_four_star = num_four_star / float(len(self.reviews))
        self.percent_five_star = num_five_star / float(len(self.reviews))
