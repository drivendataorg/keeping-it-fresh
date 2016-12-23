![Banner Image](https://s3.amazonaws.com/drivendata/comp_images/tileimage.jpg)
# Keeping it Fresh: Predict Restaurant Inspections - 3rd Place
<br> <br>
# Entrant Background and Submission Overview

### Mini-bio
I am an advanced analytics professional with an academic background in Operations Research and about ten years industry experience. I am currently managing a team of data scientists working in the aviation sector.

### High Level Summary of Submission
I normalized all the data structures in the different json files and imported those flattened structures into a Postgresql database. I then joined up the different structures together to get a richer view of each data source e.g. when a user submitted a review, I also had info on that user from their profile, alongside check-in information about how other people checked-in to the restaurant that was being reviewed, alongside static information about that restaurant like neighborhood, category, etc. This approach allowed me to create rich features about users, reviews, restaurants, etc.

I also supplemented these features with historic (recent and longer-term trends) violations data for the restaurant being inspected.

I then built four models for each target (random forest, extra random trees, gradient boosting machine, l2 logistic regression) and blended the predictions from these models to get my final submission.

### Omitted Work
I looked at creating various features from the text reviews using bag-of-words and TFIDF approaches but these didn't add much to my models, so I discarded them. I also tried to look at a social network element e.g. look at users who recently reviewed a restaurant, look at their friends and the levels of recent violations in the restaurants that their friends had reviewed and use that as a predictor but this did not add a lot in the end.

### Model Evaluation
I looked at unweighted RMSLE and lots of scatterplots of actual vs predicted values.

### Potentially Helpful Features
I would ask the inspectors themselves to provide more data - submit verbatims on any restaurants inspected & the nature of any violations found. I would also talk to them and ask them what their experiences taught them about key risk factors - potentially there is domain expertise that could be captured that we have not thought of and captured in our models.

Any sensor data that could be captured from restaurants too (e.g. from refrigeration units, from ovens, from dishwashers, etc.) could also be really great, if albeit, not a short-term option.

And I would guess that maybe weather data could be interesting - it would be easy to get your hands on and try anyway.

### Notes About the Model
I use SQL and scikit-learn and both are pretty robust.  The only watch-out that I flagged previously is that a key predictor is recent and historic violations. So you need to make sure that the most recent violations and the history are available to the model at time of scoring.

### Future Steps
I would also build multiple models for predicting different points in the future e.g. a model for predicting the likely violators tomorrow, another model for predicting likely violators 2 days from now, another for three days from now, etc. I say this because I deliberately handicapped my model to not use any data from within seven weeks of the date being predicted because the test approach dictated that. I'd guess that I could predicted earlier dates in the test period better if I had had a dedicated model that used data right up to the predicted date.

I would also look for groups within the different violations levels - maybe within three star violations, there are cleanliness / hygiene violations, violations related to the way food is stored, violations related to machinery used... I don't really know but maybe the violations target is currently a mixture of circumstances that are easier predicted when separated and predicted by different models?

<br><br>
# Replicating the Submission

### Install Requirements
* PostgreSQL 9.4.4+
    * Exact details of installation used in this application - "PostgreSQL 9.4.4 on x86_64-unknown-linux-gnu, compiled by gcc (Ubuntu 4.9.2-10ubuntu13) 4.9.2, 64-bit"


* PgadminIII for easy interaction with postgresql
    * Exact details of installation used in this application - "pgAdmin PostgreSQL Tools Version 1.20.0 Beta 2 (Oct 25 2014, rev:REL-1_18_0-116-gd4910ef)"


* Python
    * Exact details of installation used in this application - "Python 2.7.9 (default, Apr  2 2015, 15:33:21) [GCC 4.9.2]"
    * Packages:
        * numpy==1.9.2
        * pandas==0.15.2
        * psycopg2==2.5.4
        * python-dateutil==2.4.0
        * scikit-learn==0.16.0
        * scipy==0.15.1
        * SQLAlchemy==1.0.4

### Setup Database
Once PostgreSQL and pgAdminIII are installed, you should register a new server
(See http://www.pgadmin.org/docs/dev/connect.html for instructions).

Suggested values:
* In the field for "Name", please add a name for the server that you would like to use e.g. "yelp".

* In the field for "Username", please add the username that you would like to use e.g. "shane".

* In the field for "Password", please specifiy a password that you would like to use e.g. "terenure".

* In the field for Port, I suggest that you enter 5433, as the default (5432) can sometimes be problematic.

* In the field for Host, I suggest that you leave this blank - this will default to "localhost" as Host in later steps, and this works well.

Please note the above Username, Password, Port and Host values, as they will be needed in subsequent steps.

When the new server is registered, please click on the plus sign beside the server name in pgAdminIII to expand the drop-down.

Right-click on the database option and choose "New Database".  In the dialog box that appears, please enter a name for the new database e.g. "dd_db".  All other values can be left at the defaults

### Run Step_3.py

### Run Step_4.py
