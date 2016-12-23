import psycopg2 as pgs

pg_hostname = "localhost" # the hostname of the PostgreSQL server. FYI, if this field was left blank when the server was registered, pg_hostname should be declared as localhost
pg_user = "shane" # the username needed to log into PostgreSQL database
pg_password = "terenure" # the password needed to log into PostgreSQL database
pg_port = 5433
pg_db_name = "dd_db" # the name of the PostgreSQL database created

con = pgs.connect(dbname = pg_db_name, user = pg_user, host = pg_hostname, password = pg_password, port = pg_port)
con.set_isolation_level(pgs.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cur = con.cursor()

s_create_tables_and_views = """
CREATE TABLE tbl_users
(
  user_id character(32),
  yelping_since date,
  review_count integer,
  fans integer,
  average_stars double precision,
  num_friends double precision,
  votes_cool integer,
  votes_funny integer,
  votes_useful integer,
  compliments_cool double precision,
  compliments_cute double precision,
  compliments_funny double precision,
  compliments_hot double precision,
  compliments_list double precision,
  compliments_more double precision,
  compliments_note double precision,
  compliments_photos double precision,
  compliments_plain double precision,
  compliments_profile double precision,
  compliments_writer double precision,
  elite_2005 double precision,
  elite_2006 double precision,
  elite_2007 double precision,
  elite_2008 double precision,
  elite_2009 double precision,
  elite_2010 double precision,
  elite_2011 double precision,
  elite_2012 double precision,
  elite_2013 double precision,
  elite_2014 double precision,
  elite_2015 double precision,
  sum_years_elite double precision
);


CREATE TABLE tbl_tips
(
  user_id character(32),
  date date,
  business_id character(32),
  likes integer
);


CREATE TABLE tbl_reviews
(
  business_id character(32),
  date date,
  stars integer,
  user_id character(32),
  votes_cool double precision,
  votes_funny double precision,
  votes_useful double precision,
  review_len  double precision
);


CREATE TABLE tbl_checkins
(
  business_id character(32),
  checkin_info_0_0 double precision,
  checkin_info_0_1 double precision,
  checkin_info_0_2 double precision,
  checkin_info_0_3 double precision,
  checkin_info_0_4 double precision,
  checkin_info_0_5 double precision,
  checkin_info_0_6 double precision,
  checkin_info_1_0 double precision,
  checkin_info_1_1 double precision,
  checkin_info_1_2 double precision,
  checkin_info_1_3 double precision,
  checkin_info_1_4 double precision,
  checkin_info_1_5 double precision,
  checkin_info_1_6 double precision,
  checkin_info_10_0 double precision,
  checkin_info_10_1 double precision,
  checkin_info_10_2 double precision,
  checkin_info_10_3 double precision,
  checkin_info_10_4 double precision,
  checkin_info_10_5 double precision,
  checkin_info_10_6 double precision,
  checkin_info_11_0 double precision,
  checkin_info_11_1 double precision,
  checkin_info_11_2 double precision,
  checkin_info_11_3 double precision,
  checkin_info_11_4 double precision,
  checkin_info_11_5 double precision,
  checkin_info_11_6 double precision,
  checkin_info_12_0 double precision,
  checkin_info_12_1 double precision,
  checkin_info_12_2 double precision,
  checkin_info_12_3 double precision,
  checkin_info_12_4 double precision,
  checkin_info_12_5 double precision,
  checkin_info_12_6 double precision,
  checkin_info_13_0 double precision,
  checkin_info_13_1 double precision,
  checkin_info_13_2 double precision,
  checkin_info_13_3 double precision,
  checkin_info_13_4 double precision,
  checkin_info_13_5 double precision,
  checkin_info_13_6 double precision,
  checkin_info_14_0 double precision,
  checkin_info_14_1 double precision,
  checkin_info_14_2 double precision,
  checkin_info_14_3 double precision,
  checkin_info_14_4 double precision,
  checkin_info_14_5 double precision,
  checkin_info_14_6 double precision,
  checkin_info_15_0 double precision,
  checkin_info_15_1 double precision,
  checkin_info_15_2 double precision,
  checkin_info_15_3 double precision,
  checkin_info_15_4 double precision,
  checkin_info_15_5 double precision,
  checkin_info_15_6 double precision,
  checkin_info_16_0 double precision,
  checkin_info_16_1 double precision,
  checkin_info_16_2 double precision,
  checkin_info_16_3 double precision,
  checkin_info_16_4 double precision,
  checkin_info_16_5 double precision,
  checkin_info_16_6 double precision,
  checkin_info_17_0 double precision,
  checkin_info_17_1 double precision,
  checkin_info_17_2 double precision,
  checkin_info_17_3 double precision,
  checkin_info_17_4 double precision,
  checkin_info_17_5 double precision,
  checkin_info_17_6 double precision,
  checkin_info_18_0 double precision,
  checkin_info_18_1 double precision,
  checkin_info_18_2 double precision,
  checkin_info_18_3 double precision,
  checkin_info_18_4 double precision,
  checkin_info_18_5 double precision,
  checkin_info_18_6 double precision,
  checkin_info_19_0 double precision,
  checkin_info_19_1 double precision,
  checkin_info_19_2 double precision,
  checkin_info_19_3 double precision,
  checkin_info_19_4 double precision,
  checkin_info_19_5 double precision,
  checkin_info_19_6 double precision,
  checkin_info_2_0 double precision,
  checkin_info_2_1 double precision,
  checkin_info_2_2 double precision,
  checkin_info_2_3 double precision,
  checkin_info_2_4 double precision,
  checkin_info_2_5 double precision,
  checkin_info_2_6 double precision,
  checkin_info_20_0 double precision,
  checkin_info_20_1 double precision,
  checkin_info_20_2 double precision,
  checkin_info_20_3 double precision,
  checkin_info_20_4 double precision,
  checkin_info_20_5 double precision,
  checkin_info_20_6 double precision,
  checkin_info_21_0 double precision,
  checkin_info_21_1 double precision,
  checkin_info_21_2 double precision,
  checkin_info_21_3 double precision,
  checkin_info_21_4 double precision,
  checkin_info_21_5 double precision,
  checkin_info_21_6 double precision,
  checkin_info_22_0 double precision,
  checkin_info_22_1 double precision,
  checkin_info_22_2 double precision,
  checkin_info_22_3 double precision,
  checkin_info_22_4 double precision,
  checkin_info_22_5 double precision,
  checkin_info_22_6 double precision,
  checkin_info_23_0 double precision,
  checkin_info_23_1 double precision,
  checkin_info_23_2 double precision,
  checkin_info_23_3 double precision,
  checkin_info_23_4 double precision,
  checkin_info_23_5 double precision,
  checkin_info_23_6 double precision,
  checkin_info_3_0 double precision,
  checkin_info_3_1 double precision,
  checkin_info_3_2 double precision,
  checkin_info_3_3 double precision,
  checkin_info_3_4 double precision,
  checkin_info_3_5 double precision,
  checkin_info_3_6 double precision,
  checkin_info_4_0 double precision,
  checkin_info_4_1 double precision,
  checkin_info_4_2 double precision,
  checkin_info_4_3 double precision,
  checkin_info_4_4 double precision,
  checkin_info_4_5 double precision,
  checkin_info_4_6 double precision,
  checkin_info_5_0 double precision,
  checkin_info_5_1 double precision,
  checkin_info_5_2 double precision,
  checkin_info_5_3 double precision,
  checkin_info_5_4 double precision,
  checkin_info_5_5 double precision,
  checkin_info_5_6 double precision,
  checkin_info_6_0 double precision,
  checkin_info_6_1 double precision,
  checkin_info_6_2 double precision,
  checkin_info_6_3 double precision,
  checkin_info_6_4 double precision,
  checkin_info_6_5 double precision,
  checkin_info_6_6 double precision,
  checkin_info_7_0 double precision,
  checkin_info_7_1 double precision,
  checkin_info_7_2 double precision,
  checkin_info_7_3 double precision,
  checkin_info_7_4 double precision,
  checkin_info_7_5 double precision,
  checkin_info_7_6 double precision,
  checkin_info_8_0 double precision,
  checkin_info_8_1 double precision,
  checkin_info_8_2 double precision,
  checkin_info_8_3 double precision,
  checkin_info_8_4 double precision,
  checkin_info_8_5 double precision,
  checkin_info_8_6 double precision,
  checkin_info_9_0 double precision,
  checkin_info_9_1 double precision,
  checkin_info_9_2 double precision,
  checkin_info_9_3 double precision,
  checkin_info_9_4 double precision,
  checkin_info_9_5 double precision,
  checkin_info_9_6 double precision
);


CREATE TABLE tbl_business
(
	business_id character(32), 
	latitude double precision,
	longitude double precision,
	review_count double precision,
	stars double precision,
	neighborhoods_Allston_Brighton double precision,
	neighborhoods_Back_Bay double precision,
	neighborhoods_Beacon_Hill double precision,
	neighborhoods_Charlestown double precision,
	neighborhoods_Chinatown double precision,
	neighborhoods_Dorchester double precision,
	neighborhoods_Downtown double precision,
	neighborhoods_Dudley_Square double precision,
	neighborhoods_East_Boston double precision,
	neighborhoods_Fenway double precision,
	neighborhoods_Financial_District double precision,
	neighborhoods_Hyde_Park double precision,
	neighborhoods_Jamaica_Plain double precision,
	neighborhoods_Leather_District double precision,
	neighborhoods_Mattapan double precision,
	neighborhoods_Mission_Hill double precision,
	neighborhoods_North_End double precision,
	neighborhoods_Roslindale double precision,
	neighborhoods_Roslindale_Village double precision,
	neighborhoods_South_Boston double precision,
	neighborhoods_South_End double precision,
	neighborhoods_Waterfront double precision,
	neighborhoods_West_Roxbury double precision,
	neighborhoods_West_Roxbury_Center double precision,
	neighborhoods_sum double precision,
	categories_American_New_ double precision,
	categories_American_Traditional_ double precision,
	categories_Arts__Entertainment double precision,
	categories_Asian_Fusion double precision,
	categories_Bagels double precision,
	categories_Bakeries double precision,
	categories_Barbeque double precision,
	categories_Bars double precision,
	categories_Brazilian double precision,
	categories_Breakfast__Brunch double precision,
	categories_Burgers double precision,
	categories_Cafes double precision,
	categories_Caribbean double precision,
	categories_Caterers double precision,
	categories_Chicken_Wings double precision,
	categories_Chinese double precision,
	categories_Coffee__Tea double precision,
	categories_Dance_Clubs double precision,
	categories_Delis double precision,
	categories_Desserts double precision,
	categories_Dim_Sum double precision,
	categories_Diners double precision,
	categories_Dive_Bars double precision,
	categories_Donuts double precision,
	categories_Event_Planning__Services double precision,
	categories_Fast_Food double precision,
	categories_Food double precision,
	categories_Food_Stands double precision,
	categories_French double precision,
	categories_Gay_Bars double precision,
	categories_Gluten_Free double precision,
	categories_Greek double precision,
	categories_Grocery double precision,
	categories_Halal double precision,
	categories_Hot_Dogs double precision,
	categories_Hotels double precision,
	categories_Hotels__Travel double precision,
	categories_Ice_Cream__Frozen_Yogurt double precision,
	categories_Indian double precision,
	categories_Irish double precision,
	categories_Italian double precision,
	categories_Japanese double precision,
	categories_Jazz__Blues double precision,
	categories_Juice_Bars__Smoothies double precision,
	categories_Korean double precision,
	categories_Latin_American double precision,
	categories_Lounges double precision,
	categories_Mediterranean double precision,
	categories_Mexican double precision,
	categories_Middle_Eastern double precision,
	categories_Music_Venues double precision,
	categories_Nightlife double precision,
	categories_Pizza double precision,
	categories_Pubs double precision,
	categories_Restaurants double precision,
	categories_Salad double precision,
	categories_Sandwiches double precision,
	categories_Seafood double precision,
	categories_Shopping double precision,
	categories_Soul_Food double precision,
	categories_Soup double precision,
	categories_Southern double precision,
	categories_Spanish double precision,
	categories_Specialty_Food double precision,
	categories_Sports_Bars double precision,
	categories_Steakhouses double precision,
	categories_Sushi_Bars double precision,
	categories_Taiwanese double precision,
	categories_Tapas_Bars double precision,
	categories_Tex_Mex double precision,
	categories_Thai double precision,
	categories_Vegan double precision,
	categories_Vegetarian double precision,
	categories_Venues__Event_Spaces double precision,
	categories_Vietnamese double precision,
	categories_Wine_Bars double precision,
	categories_sum double precision,
	city_Allston double precision,
	city_Boston double precision,
	city_Brighton double precision,
	city_Charlestown double precision,
	city_Dorchester double precision,
	city_Dorchester_Center double precision,
	city_East_Boston double precision,
	city_Hyde_Park double precision,
	city_Jamaica_Plain double precision,
	city_Roslindale double precision,
	city_Roxbury double precision,
	city_Roxbury_Crossing double precision,
	city_South_Boston double precision,
	city_West_Roxbury double precision,
	city_sum double precision,
	open_True double precision,
	accepts_credit_cards double precision,
	ambience_casual double precision,
	ambience_classy double precision,
	ambience_divey double precision,
	ambience_hipster double precision,
	ambience_intimate double precision,
	ambience_romantic double precision,
	ambience_touristy double precision,
	ambience_trendy double precision,
	ambience_upscale double precision,
	byob double precision,
	caters double precision,
	coat_check double precision,
	corkage double precision,
	delivery double precision,
	dietary_restrictions_vegan double precision,
	dietary_restrictions_vegetarian double precision,
	dogs_allowed double precision,
	drive_thr double precision,
	good_for_breakfast double precision,
	good_for_brunch double precision,
	good_for_dancing double precision,
	good_for_dessert double precision,
	good_for_dinner double precision,
	good_for_groups double precision,
	good_for_kids double precision,
	good_for_latenight double precision,
	good_for_lunch double precision,
	happy_hour double precision,
	has_tv double precision,
	music_accepts_credit_cards double precision,
	music_background_music double precision,
	music_caters double precision,
	music_corkage double precision,
	music_dj double precision,
	music_good_for_groups double precision,
	music_good_for_kids double precision,
	music_happy_hour double precision,
	music_has_tv double precision,
	music_jukebox double precision,
	music_live double precision,
	music_outdoor_seating double precision,
	music_take_out double precision,
	music_takes_reservations double precision,
	music_video double precision,
	music_waiter_service double precision,
	music_wheelchair_accessible double precision,
	order_at_counter double precision,
	outdoor_seating double precision,
	parking_garage double precision,
	parking_lot double precision,
	parking_street double precision,
	parking_valet double precision,
	parking_validated double precision,
	payment_types_amex double precision,
	payment_types_discover double precision,
	payment_types_mastercard double precision,
	payment_types_visa double precision,
	take_out double precision,
	takes_reservations double precision,
	waiter_service double precision,
	wheelchair_accessible double precision,
	ages_allowed_21plus double precision,
	alcohol_beer_and_wine double precision,
	alcohol_full_bar double precision,
	alcohol_none double precision,
	attire_casual double precision,
	attire_dressy double precision,
	byob_corkage_no double precision,
	byob_corkage_yes_corkage double precision,
	byob_corkage_yes_free double precision,
	music_attire_casual double precision,
	music_byob_corkage_no double precision,
	music_price_range_2 double precision,
	music_smoking_no double precision,
	music_wi_fi_free double precision,
	music_wi_fi_no double precision,
	noise_level_average double precision,
	noise_level_loud double precision,
	noise_level_quiet double precision,
	noise_level_very_loud double precision,
	price_range_1 double precision,
	price_range_2 double precision,
	price_range_3 double precision,
	price_range_4 double precision,
	smoking_no double precision,
	smoking_outdoor double precision,
	smoking_yes double precision,
	wi_fi_free double precision,
	wi_fi_no double precision,
	wi_fi_paid double precision
);


CREATE TABLE tbl_map_ids
(
  restaurant_id character(32),
  yelp_id character(32)
);


CREATE TABLE tbl_all_cases
(
  id integer,
  date date,
  restaurant_id character(32),
  one_star integer,
  two_star integer,
  three_star integer,
  dataset text
);


CREATE TABLE tbl_labelled_cases
(
  id integer,
  date date,
  restaurant_id character(32),
  one_star integer,
  two_star integer,
  three_star integer
);


CREATE TABLE tbl_non_labelled_cases
(
  id integer,
  date date,
  restaurant_id character(32),
  one_star integer,
  two_star integer,
  three_star integer
);


CREATE OR REPLACE VIEW vw_all_ordered_cases AS 
SELECT tbl_all_cases.id,
tbl_all_cases.date,
tbl_all_cases.restaurant_id,
sum(
	CASE
	WHEN tbl_all_cases.dataset = 'train'::text THEN 1
	ELSE 0
END) OVER (PARTITION BY tbl_all_cases.restaurant_id ORDER BY tbl_all_cases.date) AS training_case_label,
tbl_all_cases.one_star,
tbl_all_cases.two_star,
tbl_all_cases.three_star,
tbl_all_cases.dataset
FROM tbl_all_cases;


CREATE OR REPLACE VIEW vw_checkins AS 
 SELECT a.restaurant_id,
    a.sum_checkins,
    a.sum_monday_checkins,
    a.sum_tuesday_checkins,
    a.sum_wednesday_checkins,
    a.sum_thursday_checkins,
    a.sum_friday_checkins,
    a.sum_saturday_checkins,
    a.sum_sunday_checkins,
    a.sum_checkins_0,
    a.sum_checkins_1,
    a.sum_checkins_2,
    a.sum_checkins_3,
    a.sum_checkins_4,
    a.sum_checkins_5,
    a.sum_checkins_6,
    a.sum_checkins_7,
    a.sum_checkins_8,
    a.sum_checkins_9,
    a.sum_checkins_10,
    a.sum_checkins_11,
    a.sum_checkins_12,
    a.sum_checkins_13,
    a.sum_checkins_14,
    a.sum_checkins_15,
    a.sum_checkins_16,
    a.sum_checkins_17,
    a.sum_checkins_18,
    a.sum_checkins_19,
    a.sum_checkins_20,
    a.sum_checkins_21,
    a.sum_checkins_22,
    a.sum_checkins_23,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_0 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_0,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_1 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_1,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_2 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_2,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_3 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_3,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_4 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_4,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_5 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_5,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_6 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_6,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_7 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_7,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_8 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_8,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_9 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_9,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_10 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_10,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_11 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_11,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_12 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_12,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_13 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_13,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_14 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_14,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_15 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_15,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_16 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_16,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_17 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_17,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_18 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_18,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_19 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_19,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_20 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_20,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_21 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_21,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_22 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_22,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_checkins_23 / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_23,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_checkins_0 + a.sum_checkins_1 + a.sum_checkins_2) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_0_2,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_checkins_3 + a.sum_checkins_4 + a.sum_checkins_5) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_3_5,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_checkins_6 + a.sum_checkins_7 + a.sum_checkins_8) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_6_8,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_checkins_9 + a.sum_checkins_10 + a.sum_checkins_11) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_9_11,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_checkins_12 + a.sum_checkins_13 + a.sum_checkins_14) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_12_14,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_checkins_15 + a.sum_checkins_16 + a.sum_checkins_17) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_15_17,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_checkins_18 + a.sum_checkins_19 + a.sum_checkins_20) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_18_20,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_checkins_21 + a.sum_checkins_22 + a.sum_checkins_23) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_21_23,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_monday_checkins / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_monday,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_tuesday_checkins / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_tuesday,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_wednesday_checkins / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_wednesday,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_thursday_checkins / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_thursday,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_friday_checkins / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_friday,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_saturday_checkins / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_saturday,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN a.sum_sunday_checkins / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_sunday,
        CASE
            WHEN a.sum_checkins > 0::double precision THEN (a.sum_saturday_checkins + a.sum_sunday_checkins) / a.sum_checkins
            ELSE 0::double precision
        END AS share_checkins_weekends
   FROM ( SELECT b.restaurant_id,
            sum(a_1.checkin_info_0_0 + a_1.checkin_info_0_1 + a_1.checkin_info_0_2 + a_1.checkin_info_0_3 + a_1.checkin_info_0_4 + a_1.checkin_info_0_5 + a_1.checkin_info_0_6 + a_1.checkin_info_1_0 + a_1.checkin_info_1_1 + a_1.checkin_info_1_2 + a_1.checkin_info_1_3 + a_1.checkin_info_1_4 + a_1.checkin_info_1_5 + a_1.checkin_info_1_6 + a_1.checkin_info_10_0 + a_1.checkin_info_10_1 + a_1.checkin_info_10_2 + a_1.checkin_info_10_3 + a_1.checkin_info_10_4 + a_1.checkin_info_10_5 + a_1.checkin_info_10_6 + a_1.checkin_info_11_0 + a_1.checkin_info_11_1 + a_1.checkin_info_11_2 + a_1.checkin_info_11_3 + a_1.checkin_info_11_4 + a_1.checkin_info_11_5 + a_1.checkin_info_11_6 + a_1.checkin_info_12_0 + a_1.checkin_info_12_1 + a_1.checkin_info_12_2 + a_1.checkin_info_12_3 + a_1.checkin_info_12_4 + a_1.checkin_info_12_5 + a_1.checkin_info_12_6 + a_1.checkin_info_13_0 + a_1.checkin_info_13_1 + a_1.checkin_info_13_2 + a_1.checkin_info_13_3 + a_1.checkin_info_13_4 + a_1.checkin_info_13_5 + a_1.checkin_info_13_6 + a_1.checkin_info_14_0 + a_1.checkin_info_14_1 + a_1.checkin_info_14_2 + a_1.checkin_info_14_3 + a_1.checkin_info_14_4 + a_1.checkin_info_14_5 + a_1.checkin_info_14_6 + a_1.checkin_info_15_0 + a_1.checkin_info_15_1 + a_1.checkin_info_15_2 + a_1.checkin_info_15_3 + a_1.checkin_info_15_4 + a_1.checkin_info_15_5 + a_1.checkin_info_15_6 + a_1.checkin_info_16_0 + a_1.checkin_info_16_1 + a_1.checkin_info_16_2 + a_1.checkin_info_16_3 + a_1.checkin_info_16_4 + a_1.checkin_info_16_5 + a_1.checkin_info_16_6 + a_1.checkin_info_17_0 + a_1.checkin_info_17_1 + a_1.checkin_info_17_2 + a_1.checkin_info_17_3 + a_1.checkin_info_17_4 + a_1.checkin_info_17_5 + a_1.checkin_info_17_6 + a_1.checkin_info_18_0 + a_1.checkin_info_18_1 + a_1.checkin_info_18_2 + a_1.checkin_info_18_3 + a_1.checkin_info_18_4 + a_1.checkin_info_18_5 + a_1.checkin_info_18_6 + a_1.checkin_info_19_0 + a_1.checkin_info_19_1 + a_1.checkin_info_19_2 + a_1.checkin_info_19_3 + a_1.checkin_info_19_4 + a_1.checkin_info_19_5 + a_1.checkin_info_19_6 + a_1.checkin_info_2_0 + a_1.checkin_info_2_1 + a_1.checkin_info_2_2 + a_1.checkin_info_2_3 + a_1.checkin_info_2_4 + a_1.checkin_info_2_5 + a_1.checkin_info_2_6 + a_1.checkin_info_20_0 + a_1.checkin_info_20_1 + a_1.checkin_info_20_2 + a_1.checkin_info_20_3 + a_1.checkin_info_20_4 + a_1.checkin_info_20_5 + a_1.checkin_info_20_6 + a_1.checkin_info_21_0 + a_1.checkin_info_21_1 + a_1.checkin_info_21_2 + a_1.checkin_info_21_3 + a_1.checkin_info_21_4 + a_1.checkin_info_21_5 + a_1.checkin_info_21_6 + a_1.checkin_info_22_0 + a_1.checkin_info_22_1 + a_1.checkin_info_22_2 + a_1.checkin_info_22_3 + a_1.checkin_info_22_4 + a_1.checkin_info_22_5 + a_1.checkin_info_22_6 + a_1.checkin_info_23_0 + a_1.checkin_info_23_1 + a_1.checkin_info_23_2 + a_1.checkin_info_23_3 + a_1.checkin_info_23_4 + a_1.checkin_info_23_5 + a_1.checkin_info_23_6 + a_1.checkin_info_3_0 + a_1.checkin_info_3_1 + a_1.checkin_info_3_2 + a_1.checkin_info_3_3 + a_1.checkin_info_3_4 + a_1.checkin_info_3_5 + a_1.checkin_info_3_6 + a_1.checkin_info_4_0 + a_1.checkin_info_4_1 + a_1.checkin_info_4_2 + a_1.checkin_info_4_3 + a_1.checkin_info_4_4 + a_1.checkin_info_4_5 + a_1.checkin_info_4_6 + a_1.checkin_info_5_0 + a_1.checkin_info_5_1 + a_1.checkin_info_5_2 + a_1.checkin_info_5_3 + a_1.checkin_info_5_4 + a_1.checkin_info_5_5 + a_1.checkin_info_5_6 + a_1.checkin_info_6_0 + a_1.checkin_info_6_1 + a_1.checkin_info_6_2 + a_1.checkin_info_6_3 + a_1.checkin_info_6_4 + a_1.checkin_info_6_5 + a_1.checkin_info_6_6 + a_1.checkin_info_7_0 + a_1.checkin_info_7_1 + a_1.checkin_info_7_2 + a_1.checkin_info_7_3 + a_1.checkin_info_7_4 + a_1.checkin_info_7_5 + a_1.checkin_info_7_6 + a_1.checkin_info_8_0 + a_1.checkin_info_8_1 + a_1.checkin_info_8_2 + a_1.checkin_info_8_3 + a_1.checkin_info_8_4 + a_1.checkin_info_8_5 + a_1.checkin_info_8_6 + a_1.checkin_info_9_0 + a_1.checkin_info_9_1 + a_1.checkin_info_9_2 + a_1.checkin_info_9_3 + a_1.checkin_info_9_4 + a_1.checkin_info_9_5 + a_1.checkin_info_9_6) AS sum_checkins,
            sum(a_1.checkin_info_0_0 + a_1.checkin_info_1_0 + a_1.checkin_info_10_0 + a_1.checkin_info_11_0 + a_1.checkin_info_12_0 + a_1.checkin_info_13_0 + a_1.checkin_info_14_0 + a_1.checkin_info_15_0 + a_1.checkin_info_16_0 + a_1.checkin_info_17_0 + a_1.checkin_info_18_0 + a_1.checkin_info_19_0 + a_1.checkin_info_2_0 + a_1.checkin_info_20_0 + a_1.checkin_info_21_0 + a_1.checkin_info_22_0 + a_1.checkin_info_23_0 + a_1.checkin_info_3_0 + a_1.checkin_info_4_0 + a_1.checkin_info_5_0 + a_1.checkin_info_6_0 + a_1.checkin_info_7_0 + a_1.checkin_info_8_0 + a_1.checkin_info_9_0) AS sum_monday_checkins,
            sum(a_1.checkin_info_0_1 + a_1.checkin_info_1_1 + a_1.checkin_info_10_1 + a_1.checkin_info_11_1 + a_1.checkin_info_12_1 + a_1.checkin_info_13_1 + a_1.checkin_info_14_1 + a_1.checkin_info_15_1 + a_1.checkin_info_16_1 + a_1.checkin_info_17_1 + a_1.checkin_info_18_1 + a_1.checkin_info_19_1 + a_1.checkin_info_2_1 + a_1.checkin_info_20_1 + a_1.checkin_info_21_1 + a_1.checkin_info_22_1 + a_1.checkin_info_23_1 + a_1.checkin_info_3_1 + a_1.checkin_info_4_1 + a_1.checkin_info_5_1 + a_1.checkin_info_6_1 + a_1.checkin_info_7_1 + a_1.checkin_info_8_1 + a_1.checkin_info_9_1) AS sum_tuesday_checkins,
            sum(a_1.checkin_info_0_2 + a_1.checkin_info_1_2 + a_1.checkin_info_10_2 + a_1.checkin_info_11_2 + a_1.checkin_info_12_2 + a_1.checkin_info_13_2 + a_1.checkin_info_14_2 + a_1.checkin_info_15_2 + a_1.checkin_info_16_2 + a_1.checkin_info_17_2 + a_1.checkin_info_18_2 + a_1.checkin_info_19_2 + a_1.checkin_info_2_2 + a_1.checkin_info_20_2 + a_1.checkin_info_21_2 + a_1.checkin_info_22_2 + a_1.checkin_info_23_2 + a_1.checkin_info_3_2 + a_1.checkin_info_4_2 + a_1.checkin_info_5_2 + a_1.checkin_info_6_2 + a_1.checkin_info_7_2 + a_1.checkin_info_8_2 + a_1.checkin_info_9_2) AS sum_wednesday_checkins,
            sum(a_1.checkin_info_0_3 + a_1.checkin_info_1_3 + a_1.checkin_info_10_3 + a_1.checkin_info_11_3 + a_1.checkin_info_12_3 + a_1.checkin_info_13_3 + a_1.checkin_info_14_3 + a_1.checkin_info_15_3 + a_1.checkin_info_16_3 + a_1.checkin_info_17_3 + a_1.checkin_info_18_3 + a_1.checkin_info_19_3 + a_1.checkin_info_2_3 + a_1.checkin_info_20_3 + a_1.checkin_info_21_3 + a_1.checkin_info_22_3 + a_1.checkin_info_23_3 + a_1.checkin_info_3_3 + a_1.checkin_info_4_3 + a_1.checkin_info_5_3 + a_1.checkin_info_6_3 + a_1.checkin_info_7_3 + a_1.checkin_info_8_3 + a_1.checkin_info_9_3) AS sum_thursday_checkins,
            sum(a_1.checkin_info_0_4 + a_1.checkin_info_1_4 + a_1.checkin_info_10_4 + a_1.checkin_info_11_4 + a_1.checkin_info_12_4 + a_1.checkin_info_13_4 + a_1.checkin_info_14_4 + a_1.checkin_info_15_4 + a_1.checkin_info_16_4 + a_1.checkin_info_17_4 + a_1.checkin_info_18_4 + a_1.checkin_info_19_4 + a_1.checkin_info_2_4 + a_1.checkin_info_20_4 + a_1.checkin_info_21_4 + a_1.checkin_info_22_4 + a_1.checkin_info_23_4 + a_1.checkin_info_3_4 + a_1.checkin_info_4_4 + a_1.checkin_info_5_4 + a_1.checkin_info_6_4 + a_1.checkin_info_7_4 + a_1.checkin_info_8_4 + a_1.checkin_info_9_4) AS sum_friday_checkins,
            sum(a_1.checkin_info_0_5 + a_1.checkin_info_1_5 + a_1.checkin_info_10_5 + a_1.checkin_info_11_5 + a_1.checkin_info_12_5 + a_1.checkin_info_13_5 + a_1.checkin_info_14_5 + a_1.checkin_info_15_5 + a_1.checkin_info_16_5 + a_1.checkin_info_17_5 + a_1.checkin_info_18_5 + a_1.checkin_info_19_5 + a_1.checkin_info_2_5 + a_1.checkin_info_20_5 + a_1.checkin_info_21_5 + a_1.checkin_info_22_5 + a_1.checkin_info_23_5 + a_1.checkin_info_3_5 + a_1.checkin_info_4_5 + a_1.checkin_info_5_5 + a_1.checkin_info_6_5 + a_1.checkin_info_7_5 + a_1.checkin_info_8_5 + a_1.checkin_info_9_5) AS sum_saturday_checkins,
            sum(a_1.checkin_info_0_6 + a_1.checkin_info_1_6 + a_1.checkin_info_10_6 + a_1.checkin_info_11_6 + a_1.checkin_info_12_6 + a_1.checkin_info_13_6 + a_1.checkin_info_14_6 + a_1.checkin_info_15_6 + a_1.checkin_info_16_6 + a_1.checkin_info_17_6 + a_1.checkin_info_18_6 + a_1.checkin_info_19_6 + a_1.checkin_info_2_6 + a_1.checkin_info_20_6 + a_1.checkin_info_21_6 + a_1.checkin_info_22_6 + a_1.checkin_info_23_6 + a_1.checkin_info_3_6 + a_1.checkin_info_4_6 + a_1.checkin_info_5_6 + a_1.checkin_info_6_6 + a_1.checkin_info_7_6 + a_1.checkin_info_8_6 + a_1.checkin_info_9_6) AS sum_sunday_checkins,
            sum(a_1.checkin_info_0_0 + a_1.checkin_info_0_1 + a_1.checkin_info_0_2 + a_1.checkin_info_0_3 + a_1.checkin_info_0_4 + a_1.checkin_info_0_5 + a_1.checkin_info_0_6) AS sum_checkins_0,
            sum(a_1.checkin_info_1_0 + a_1.checkin_info_1_1 + a_1.checkin_info_1_2 + a_1.checkin_info_1_3 + a_1.checkin_info_1_4 + a_1.checkin_info_1_5 + a_1.checkin_info_1_6) AS sum_checkins_1,
            sum(a_1.checkin_info_2_0 + a_1.checkin_info_2_1 + a_1.checkin_info_2_2 + a_1.checkin_info_2_3 + a_1.checkin_info_2_4 + a_1.checkin_info_2_5 + a_1.checkin_info_2_6) AS sum_checkins_2,
            sum(a_1.checkin_info_3_0 + a_1.checkin_info_3_1 + a_1.checkin_info_3_2 + a_1.checkin_info_3_3 + a_1.checkin_info_3_4 + a_1.checkin_info_3_5 + a_1.checkin_info_3_6) AS sum_checkins_3,
            sum(a_1.checkin_info_4_0 + a_1.checkin_info_4_1 + a_1.checkin_info_4_2 + a_1.checkin_info_4_3 + a_1.checkin_info_4_4 + a_1.checkin_info_4_5 + a_1.checkin_info_4_6) AS sum_checkins_4,
            sum(a_1.checkin_info_5_0 + a_1.checkin_info_5_1 + a_1.checkin_info_5_2 + a_1.checkin_info_5_3 + a_1.checkin_info_5_4 + a_1.checkin_info_5_5 + a_1.checkin_info_5_6) AS sum_checkins_5,
            sum(a_1.checkin_info_6_0 + a_1.checkin_info_6_1 + a_1.checkin_info_6_2 + a_1.checkin_info_6_3 + a_1.checkin_info_6_4 + a_1.checkin_info_6_5 + a_1.checkin_info_6_6) AS sum_checkins_6,
            sum(a_1.checkin_info_7_0 + a_1.checkin_info_7_1 + a_1.checkin_info_7_2 + a_1.checkin_info_7_3 + a_1.checkin_info_7_4 + a_1.checkin_info_7_5 + a_1.checkin_info_7_6) AS sum_checkins_7,
            sum(a_1.checkin_info_8_0 + a_1.checkin_info_8_1 + a_1.checkin_info_8_2 + a_1.checkin_info_8_3 + a_1.checkin_info_8_4 + a_1.checkin_info_8_5 + a_1.checkin_info_8_6) AS sum_checkins_8,
            sum(a_1.checkin_info_9_0 + a_1.checkin_info_9_1 + a_1.checkin_info_9_2 + a_1.checkin_info_9_3 + a_1.checkin_info_9_4 + a_1.checkin_info_9_5 + a_1.checkin_info_9_6) AS sum_checkins_9,
            sum(a_1.checkin_info_10_0 + a_1.checkin_info_10_1 + a_1.checkin_info_10_2 + a_1.checkin_info_10_3 + a_1.checkin_info_10_4 + a_1.checkin_info_10_5 + a_1.checkin_info_10_6) AS sum_checkins_10,
            sum(a_1.checkin_info_11_0 + a_1.checkin_info_11_1 + a_1.checkin_info_11_2 + a_1.checkin_info_11_3 + a_1.checkin_info_11_4 + a_1.checkin_info_11_5 + a_1.checkin_info_11_6) AS sum_checkins_11,
            sum(a_1.checkin_info_12_0 + a_1.checkin_info_12_1 + a_1.checkin_info_12_2 + a_1.checkin_info_12_3 + a_1.checkin_info_12_4 + a_1.checkin_info_12_5 + a_1.checkin_info_12_6) AS sum_checkins_12,
            sum(a_1.checkin_info_13_0 + a_1.checkin_info_13_1 + a_1.checkin_info_13_2 + a_1.checkin_info_13_3 + a_1.checkin_info_13_4 + a_1.checkin_info_13_5 + a_1.checkin_info_13_6) AS sum_checkins_13,
            sum(a_1.checkin_info_14_0 + a_1.checkin_info_14_1 + a_1.checkin_info_14_2 + a_1.checkin_info_14_3 + a_1.checkin_info_14_4 + a_1.checkin_info_14_5 + a_1.checkin_info_14_6) AS sum_checkins_14,
            sum(a_1.checkin_info_15_0 + a_1.checkin_info_15_1 + a_1.checkin_info_15_2 + a_1.checkin_info_15_3 + a_1.checkin_info_15_4 + a_1.checkin_info_15_5 + a_1.checkin_info_15_6) AS sum_checkins_15,
            sum(a_1.checkin_info_16_0 + a_1.checkin_info_16_1 + a_1.checkin_info_16_2 + a_1.checkin_info_16_3 + a_1.checkin_info_16_4 + a_1.checkin_info_16_5 + a_1.checkin_info_16_6) AS sum_checkins_16,
            sum(a_1.checkin_info_17_0 + a_1.checkin_info_17_1 + a_1.checkin_info_17_2 + a_1.checkin_info_17_3 + a_1.checkin_info_17_4 + a_1.checkin_info_17_5 + a_1.checkin_info_17_6) AS sum_checkins_17,
            sum(a_1.checkin_info_18_0 + a_1.checkin_info_18_1 + a_1.checkin_info_18_2 + a_1.checkin_info_18_3 + a_1.checkin_info_18_4 + a_1.checkin_info_18_5 + a_1.checkin_info_18_6) AS sum_checkins_18,
            sum(a_1.checkin_info_19_0 + a_1.checkin_info_19_1 + a_1.checkin_info_19_2 + a_1.checkin_info_19_3 + a_1.checkin_info_19_4 + a_1.checkin_info_19_5 + a_1.checkin_info_19_6) AS sum_checkins_19,
            sum(a_1.checkin_info_20_0 + a_1.checkin_info_20_1 + a_1.checkin_info_20_2 + a_1.checkin_info_20_3 + a_1.checkin_info_20_4 + a_1.checkin_info_20_5 + a_1.checkin_info_20_6) AS sum_checkins_20,
            sum(a_1.checkin_info_21_0 + a_1.checkin_info_21_1 + a_1.checkin_info_21_2 + a_1.checkin_info_21_3 + a_1.checkin_info_21_4 + a_1.checkin_info_21_5 + a_1.checkin_info_21_6) AS sum_checkins_21,
            sum(a_1.checkin_info_22_0 + a_1.checkin_info_22_1 + a_1.checkin_info_22_2 + a_1.checkin_info_22_3 + a_1.checkin_info_22_4 + a_1.checkin_info_22_5 + a_1.checkin_info_22_6) AS sum_checkins_22,
            sum(a_1.checkin_info_23_0 + a_1.checkin_info_23_1 + a_1.checkin_info_23_2 + a_1.checkin_info_23_3 + a_1.checkin_info_23_4 + a_1.checkin_info_23_5 + a_1.checkin_info_23_6) AS sum_checkins_23
           FROM tbl_checkins a_1
             JOIN tbl_map_ids b ON a_1.business_id = b.yelp_id
          GROUP BY b.restaurant_id) a;


CREATE OR REPLACE VIEW vw_checkins_zm AS 
 SELECT a.restaurant_id,
    a.sum_checkins - avg_sq.avg_sum_checkins AS sum_checkins,
    a.sum_monday_checkins - avg_sq.avg_sum_monday_checkins AS sum_monday_checkins,
    a.sum_tuesday_checkins - avg_sq.avg_sum_tuesday_checkins AS sum_tuesday_checkins,
    a.sum_wednesday_checkins - avg_sq.avg_sum_wednesday_checkins AS sum_wednesday_checkins,
    a.sum_thursday_checkins - avg_sq.avg_sum_thursday_checkins AS sum_thursday_checkins,
    a.sum_friday_checkins - avg_sq.avg_sum_friday_checkins AS sum_friday_checkins,
    a.sum_saturday_checkins - avg_sq.avg_sum_saturday_checkins AS sum_saturday_checkins,
    a.sum_sunday_checkins - avg_sq.avg_sum_sunday_checkins AS sum_sunday_checkins,
    a.sum_checkins_0 - avg_sq.avg_sum_checkins_0 AS sum_checkins_0,
    a.sum_checkins_1 - avg_sq.avg_sum_checkins_1 AS sum_checkins_1,
    a.sum_checkins_2 - avg_sq.avg_sum_checkins_2 AS sum_checkins_2,
    a.sum_checkins_3 - avg_sq.avg_sum_checkins_3 AS sum_checkins_3,
    a.sum_checkins_4 - avg_sq.avg_sum_checkins_4 AS sum_checkins_4,
    a.sum_checkins_5 - avg_sq.avg_sum_checkins_5 AS sum_checkins_5,
    a.sum_checkins_6 - avg_sq.avg_sum_checkins_6 AS sum_checkins_6,
    a.sum_checkins_7 - avg_sq.avg_sum_checkins_7 AS sum_checkins_7,
    a.sum_checkins_8 - avg_sq.avg_sum_checkins_8 AS sum_checkins_8,
    a.sum_checkins_9 - avg_sq.avg_sum_checkins_9 AS sum_checkins_9,
    a.sum_checkins_10 - avg_sq.avg_sum_checkins_10 AS sum_checkins_10,
    a.sum_checkins_11 - avg_sq.avg_sum_checkins_11 AS sum_checkins_11,
    a.sum_checkins_12 - avg_sq.avg_sum_checkins_12 AS sum_checkins_12,
    a.sum_checkins_13 - avg_sq.avg_sum_checkins_13 AS sum_checkins_13,
    a.sum_checkins_14 - avg_sq.avg_sum_checkins_14 AS sum_checkins_14,
    a.sum_checkins_15 - avg_sq.avg_sum_checkins_15 AS sum_checkins_15,
    a.sum_checkins_16 - avg_sq.avg_sum_checkins_16 AS sum_checkins_16,
    a.sum_checkins_17 - avg_sq.avg_sum_checkins_17 AS sum_checkins_17,
    a.sum_checkins_18 - avg_sq.avg_sum_checkins_18 AS sum_checkins_18,
    a.sum_checkins_19 - avg_sq.avg_sum_checkins_19 AS sum_checkins_19,
    a.sum_checkins_20 - avg_sq.avg_sum_checkins_20 AS sum_checkins_20,
    a.sum_checkins_21 - avg_sq.avg_sum_checkins_21 AS sum_checkins_21,
    a.sum_checkins_22 - avg_sq.avg_sum_checkins_22 AS sum_checkins_22,
    a.sum_checkins_23 - avg_sq.avg_sum_checkins_23 AS sum_checkins_23,
    a.share_checkins_0 - avg_sq.avg_share_checkins_0 AS share_checkins_0,
    a.share_checkins_1 - avg_sq.avg_share_checkins_1 AS share_checkins_1,
    a.share_checkins_2 - avg_sq.avg_share_checkins_2 AS share_checkins_2,
    a.share_checkins_3 - avg_sq.avg_share_checkins_3 AS share_checkins_3,
    a.share_checkins_4 - avg_sq.avg_share_checkins_4 AS share_checkins_4,
    a.share_checkins_5 - avg_sq.avg_share_checkins_5 AS share_checkins_5,
    a.share_checkins_6 - avg_sq.avg_share_checkins_6 AS share_checkins_6,
    a.share_checkins_7 - avg_sq.avg_share_checkins_7 AS share_checkins_7,
    a.share_checkins_8 - avg_sq.avg_share_checkins_8 AS share_checkins_8,
    a.share_checkins_9 - avg_sq.avg_share_checkins_9 AS share_checkins_9,
    a.share_checkins_10 - avg_sq.avg_share_checkins_10 AS share_checkins_10,
    a.share_checkins_11 - avg_sq.avg_share_checkins_11 AS share_checkins_11,
    a.share_checkins_12 - avg_sq.avg_share_checkins_12 AS share_checkins_12,
    a.share_checkins_13 - avg_sq.avg_share_checkins_13 AS share_checkins_13,
    a.share_checkins_14 - avg_sq.avg_share_checkins_14 AS share_checkins_14,
    a.share_checkins_15 - avg_sq.avg_share_checkins_15 AS share_checkins_15,
    a.share_checkins_16 - avg_sq.avg_share_checkins_16 AS share_checkins_16,
    a.share_checkins_17 - avg_sq.avg_share_checkins_17 AS share_checkins_17,
    a.share_checkins_18 - avg_sq.avg_share_checkins_18 AS share_checkins_18,
    a.share_checkins_19 - avg_sq.avg_share_checkins_19 AS share_checkins_19,
    a.share_checkins_20 - avg_sq.avg_share_checkins_20 AS share_checkins_20,
    a.share_checkins_21 - avg_sq.avg_share_checkins_21 AS share_checkins_21,
    a.share_checkins_22 - avg_sq.avg_share_checkins_22 AS share_checkins_22,
    a.share_checkins_23 - avg_sq.avg_share_checkins_23 AS share_checkins_23,
    a.share_checkins_0_2 - avg_sq.avg_share_checkins_0_2 AS share_checkins_0_2,
    a.share_checkins_3_5 - avg_sq.avg_share_checkins_3_5 AS share_checkins_3_5,
    a.share_checkins_6_8 - avg_sq.avg_share_checkins_6_8 AS share_checkins_6_8,
    a.share_checkins_9_11 - avg_sq.avg_share_checkins_9_11 AS share_checkins_9_11,
    a.share_checkins_12_14 - avg_sq.avg_share_checkins_12_14 AS share_checkins_12_14,
    a.share_checkins_15_17 - avg_sq.avg_share_checkins_15_17 AS share_checkins_15_17,
    a.share_checkins_18_20 - avg_sq.avg_share_checkins_18_20 AS share_checkins_18_20,
    a.share_checkins_21_23 - avg_sq.avg_share_checkins_21_23 AS share_checkins_21_23,
    a.share_checkins_monday - avg_sq.avg_share_checkins_monday AS share_checkins_monday,
    a.share_checkins_tuesday - avg_sq.avg_share_checkins_tuesday AS share_checkins_tuesday,
    a.share_checkins_wednesday - avg_sq.avg_share_checkins_wednesday AS share_checkins_wednesday,
    a.share_checkins_thursday - avg_sq.avg_share_checkins_thursday AS share_checkins_thursday,
    a.share_checkins_friday - avg_sq.avg_share_checkins_friday AS share_checkins_friday,
    a.share_checkins_saturday - avg_sq.avg_share_checkins_saturday AS share_checkins_saturday,
    a.share_checkins_sunday - avg_sq.avg_share_checkins_sunday AS share_checkins_sunday,
    a.share_checkins_weekends - avg_sq.avg_share_checkins_weekends AS share_checkins_weekends
   FROM vw_checkins a
     CROSS JOIN ( SELECT avg(a_1.sum_checkins) AS avg_sum_checkins,
            avg(a_1.sum_monday_checkins) AS avg_sum_monday_checkins,
            avg(a_1.sum_tuesday_checkins) AS avg_sum_tuesday_checkins,
            avg(a_1.sum_wednesday_checkins) AS avg_sum_wednesday_checkins,
            avg(a_1.sum_thursday_checkins) AS avg_sum_thursday_checkins,
            avg(a_1.sum_friday_checkins) AS avg_sum_friday_checkins,
            avg(a_1.sum_saturday_checkins) AS avg_sum_saturday_checkins,
            avg(a_1.sum_sunday_checkins) AS avg_sum_sunday_checkins,
            avg(a_1.sum_checkins_0) AS avg_sum_checkins_0,
            avg(a_1.sum_checkins_1) AS avg_sum_checkins_1,
            avg(a_1.sum_checkins_2) AS avg_sum_checkins_2,
            avg(a_1.sum_checkins_3) AS avg_sum_checkins_3,
            avg(a_1.sum_checkins_4) AS avg_sum_checkins_4,
            avg(a_1.sum_checkins_5) AS avg_sum_checkins_5,
            avg(a_1.sum_checkins_6) AS avg_sum_checkins_6,
            avg(a_1.sum_checkins_7) AS avg_sum_checkins_7,
            avg(a_1.sum_checkins_8) AS avg_sum_checkins_8,
            avg(a_1.sum_checkins_9) AS avg_sum_checkins_9,
            avg(a_1.sum_checkins_10) AS avg_sum_checkins_10,
            avg(a_1.sum_checkins_11) AS avg_sum_checkins_11,
            avg(a_1.sum_checkins_12) AS avg_sum_checkins_12,
            avg(a_1.sum_checkins_13) AS avg_sum_checkins_13,
            avg(a_1.sum_checkins_14) AS avg_sum_checkins_14,
            avg(a_1.sum_checkins_15) AS avg_sum_checkins_15,
            avg(a_1.sum_checkins_16) AS avg_sum_checkins_16,
            avg(a_1.sum_checkins_17) AS avg_sum_checkins_17,
            avg(a_1.sum_checkins_18) AS avg_sum_checkins_18,
            avg(a_1.sum_checkins_19) AS avg_sum_checkins_19,
            avg(a_1.sum_checkins_20) AS avg_sum_checkins_20,
            avg(a_1.sum_checkins_21) AS avg_sum_checkins_21,
            avg(a_1.sum_checkins_22) AS avg_sum_checkins_22,
            avg(a_1.sum_checkins_23) AS avg_sum_checkins_23,
            avg(a_1.share_checkins_0) AS avg_share_checkins_0,
            avg(a_1.share_checkins_1) AS avg_share_checkins_1,
            avg(a_1.share_checkins_2) AS avg_share_checkins_2,
            avg(a_1.share_checkins_3) AS avg_share_checkins_3,
            avg(a_1.share_checkins_4) AS avg_share_checkins_4,
            avg(a_1.share_checkins_5) AS avg_share_checkins_5,
            avg(a_1.share_checkins_6) AS avg_share_checkins_6,
            avg(a_1.share_checkins_7) AS avg_share_checkins_7,
            avg(a_1.share_checkins_8) AS avg_share_checkins_8,
            avg(a_1.share_checkins_9) AS avg_share_checkins_9,
            avg(a_1.share_checkins_10) AS avg_share_checkins_10,
            avg(a_1.share_checkins_11) AS avg_share_checkins_11,
            avg(a_1.share_checkins_12) AS avg_share_checkins_12,
            avg(a_1.share_checkins_13) AS avg_share_checkins_13,
            avg(a_1.share_checkins_14) AS avg_share_checkins_14,
            avg(a_1.share_checkins_15) AS avg_share_checkins_15,
            avg(a_1.share_checkins_16) AS avg_share_checkins_16,
            avg(a_1.share_checkins_17) AS avg_share_checkins_17,
            avg(a_1.share_checkins_18) AS avg_share_checkins_18,
            avg(a_1.share_checkins_19) AS avg_share_checkins_19,
            avg(a_1.share_checkins_20) AS avg_share_checkins_20,
            avg(a_1.share_checkins_21) AS avg_share_checkins_21,
            avg(a_1.share_checkins_22) AS avg_share_checkins_22,
            avg(a_1.share_checkins_23) AS avg_share_checkins_23,
            avg(a_1.share_checkins_0_2) AS avg_share_checkins_0_2,
            avg(a_1.share_checkins_3_5) AS avg_share_checkins_3_5,
            avg(a_1.share_checkins_6_8) AS avg_share_checkins_6_8,
            avg(a_1.share_checkins_9_11) AS avg_share_checkins_9_11,
            avg(a_1.share_checkins_12_14) AS avg_share_checkins_12_14,
            avg(a_1.share_checkins_15_17) AS avg_share_checkins_15_17,
            avg(a_1.share_checkins_18_20) AS avg_share_checkins_18_20,
            avg(a_1.share_checkins_21_23) AS avg_share_checkins_21_23,
            avg(a_1.share_checkins_monday) AS avg_share_checkins_monday,
            avg(a_1.share_checkins_tuesday) AS avg_share_checkins_tuesday,
            avg(a_1.share_checkins_wednesday) AS avg_share_checkins_wednesday,
            avg(a_1.share_checkins_thursday) AS avg_share_checkins_thursday,
            avg(a_1.share_checkins_friday) AS avg_share_checkins_friday,
            avg(a_1.share_checkins_saturday) AS avg_share_checkins_saturday,
            avg(a_1.share_checkins_sunday) AS avg_share_checkins_sunday,
            avg(a_1.share_checkins_weekends) AS avg_share_checkins_weekends
           FROM vw_checkins a_1) avg_sq;


CREATE OR REPLACE VIEW vw_business AS 
 SELECT b.restaurant_id,
    avg(a.latitude - avg_sq.avg_latitude) AS latitude,
    avg(a.longitude - avg_sq.avg_longitude) AS longitude,
    avg(a.review_count - avg_sq.avg_review_count) AS review_count,
    avg(a.stars - avg_sq.avg_stars) AS stars,
    avg(a.neighborhoods_allston_brighton) AS neighborhoods_allston_brighton,
    avg(a.neighborhoods_back_bay) AS neighborhoods_back_bay,
    avg(a.neighborhoods_beacon_hill) AS neighborhoods_beacon_hill,
    avg(a.neighborhoods_charlestown) AS neighborhoods_charlestown,
    avg(a.neighborhoods_chinatown) AS neighborhoods_chinatown,
    avg(a.neighborhoods_dorchester) AS neighborhoods_dorchester,
    avg(a.neighborhoods_downtown) AS neighborhoods_downtown,
    avg(a.neighborhoods_dudley_square) AS neighborhoods_dudley_square,
    avg(a.neighborhoods_east_boston) AS neighborhoods_east_boston,
    avg(a.neighborhoods_fenway) AS neighborhoods_fenway,
    avg(a.neighborhoods_financial_district) AS neighborhoods_financial_district,
    avg(a.neighborhoods_hyde_park) AS neighborhoods_hyde_park,
    avg(a.neighborhoods_jamaica_plain) AS neighborhoods_jamaica_plain,
    avg(a.neighborhoods_leather_district) AS neighborhoods_leather_district,
    avg(a.neighborhoods_mattapan) AS neighborhoods_mattapan,
    avg(a.neighborhoods_mission_hill) AS neighborhoods_mission_hill,
    avg(a.neighborhoods_north_end) AS neighborhoods_north_end,
    avg(a.neighborhoods_roslindale) AS neighborhoods_roslindale,
    avg(a.neighborhoods_roslindale_village) AS neighborhoods_roslindale_village,
    avg(a.neighborhoods_south_boston) AS neighborhoods_south_boston,
    avg(a.neighborhoods_south_end) AS neighborhoods_south_end,
    avg(a.neighborhoods_waterfront) AS neighborhoods_waterfront,
    avg(a.neighborhoods_west_roxbury) AS neighborhoods_west_roxbury,
    avg(a.neighborhoods_west_roxbury_center) AS neighborhoods_west_roxbury_center,
    avg(a.neighborhoods_sum) AS neighborhoods_sum,
    avg(a.categories_american_new_) AS categories_american_new_,
    avg(a.categories_american_traditional_) AS categories_american_traditional_,
    avg(a.categories_arts__entertainment) AS categories_arts__entertainment,
    avg(a.categories_asian_fusion) AS categories_asian_fusion,
    avg(a.categories_bagels) AS categories_bagels,
    avg(a.categories_bakeries) AS categories_bakeries,
    avg(a.categories_barbeque) AS categories_barbeque,
    avg(a.categories_bars) AS categories_bars,
    avg(a.categories_brazilian) AS categories_brazilian,
    avg(a.categories_breakfast__brunch) AS categories_breakfast__brunch,
    avg(a.categories_burgers) AS categories_burgers,
    avg(a.categories_cafes) AS categories_cafes,
    avg(a.categories_caribbean) AS categories_caribbean,
    avg(a.categories_caterers) AS categories_caterers,
    avg(a.categories_chicken_wings) AS categories_chicken_wings,
    avg(a.categories_chinese) AS categories_chinese,
    avg(a.categories_coffee__tea) AS categories_coffee__tea,
    avg(a.categories_dance_clubs) AS categories_dance_clubs,
    avg(a.categories_delis) AS categories_delis,
    avg(a.categories_desserts) AS categories_desserts,
    avg(a.categories_dim_sum) AS categories_dim_sum,
    avg(a.categories_diners) AS categories_diners,
    avg(a.categories_dive_bars) AS categories_dive_bars,
    avg(a.categories_donuts) AS categories_donuts,
    avg(a.categories_event_planning__services) AS categories_event_planning__services,
    avg(a.categories_fast_food) AS categories_fast_food,
    avg(a.categories_food) AS categories_food,
    avg(a.categories_food_stands) AS categories_food_stands,
    avg(a.categories_french) AS categories_french,
    avg(a.categories_gay_bars) AS categories_gay_bars,
    avg(a.categories_gluten_free) AS categories_gluten_free,
    avg(a.categories_greek) AS categories_greek,
    avg(a.categories_grocery) AS categories_grocery,
    avg(a.categories_halal) AS categories_halal,
    avg(a.categories_hot_dogs) AS categories_hot_dogs,
    avg(a.categories_hotels) AS categories_hotels,
    avg(a.categories_hotels__travel) AS categories_hotels__travel,
    avg(a.categories_ice_cream__frozen_yogurt) AS categories_ice_cream__frozen_yogurt,
    avg(a.categories_indian) AS categories_indian,
    avg(a.categories_irish) AS categories_irish,
    avg(a.categories_italian) AS categories_italian,
    avg(a.categories_japanese) AS categories_japanese,
    avg(a.categories_jazz__blues) AS categories_jazz__blues,
    avg(a.categories_juice_bars__smoothies) AS categories_juice_bars__smoothies,
    avg(a.categories_korean) AS categories_korean,
    avg(a.categories_latin_american) AS categories_latin_american,
    avg(a.categories_lounges) AS categories_lounges,
    avg(a.categories_mediterranean) AS categories_mediterranean,
    avg(a.categories_mexican) AS categories_mexican,
    avg(a.categories_middle_eastern) AS categories_middle_eastern,
    avg(a.categories_music_venues) AS categories_music_venues,
    avg(a.categories_nightlife) AS categories_nightlife,
    avg(a.categories_pizza) AS categories_pizza,
    avg(a.categories_pubs) AS categories_pubs,
    avg(a.categories_restaurants) AS categories_restaurants,
    avg(a.categories_salad) AS categories_salad,
    avg(a.categories_sandwiches) AS categories_sandwiches,
    avg(a.categories_seafood) AS categories_seafood,
    avg(a.categories_shopping) AS categories_shopping,
    avg(a.categories_soul_food) AS categories_soul_food,
    avg(a.categories_soup) AS categories_soup,
    avg(a.categories_southern) AS categories_southern,
    avg(a.categories_spanish) AS categories_spanish,
    avg(a.categories_specialty_food) AS categories_specialty_food,
    avg(a.categories_sports_bars) AS categories_sports_bars,
    avg(a.categories_steakhouses) AS categories_steakhouses,
    avg(a.categories_sushi_bars) AS categories_sushi_bars,
    avg(a.categories_taiwanese) AS categories_taiwanese,
    avg(a.categories_tapas_bars) AS categories_tapas_bars,
    avg(a.categories_tex_mex) AS categories_tex_mex,
    avg(a.categories_thai) AS categories_thai,
    avg(a.categories_vegan) AS categories_vegan,
    avg(a.categories_vegetarian) AS categories_vegetarian,
    avg(a.categories_venues__event_spaces) AS categories_venues__event_spaces,
    avg(a.categories_vietnamese) AS categories_vietnamese,
    avg(a.categories_wine_bars) AS categories_wine_bars,
    avg(a.categories_sum) AS categories_sum,
    avg(a.city_allston) AS city_allston,
    avg(a.city_boston) AS city_boston,
    avg(a.city_brighton) AS city_brighton,
    avg(a.city_charlestown) AS city_charlestown,
    avg(a.city_dorchester) AS city_dorchester,
    avg(a.city_dorchester_center) AS city_dorchester_center,
    avg(a.city_east_boston) AS city_east_boston,
    avg(a.city_hyde_park) AS city_hyde_park,
    avg(a.city_jamaica_plain) AS city_jamaica_plain,
    avg(a.city_roslindale) AS city_roslindale,
    avg(a.city_roxbury) AS city_roxbury,
    avg(a.city_roxbury_crossing) AS city_roxbury_crossing,
    avg(a.city_south_boston) AS city_south_boston,
    avg(a.city_west_roxbury) AS city_west_roxbury,
    avg(a.city_sum) AS city_sum,
    avg(a.open_true) AS open_true,
    avg(a.accepts_credit_cards) AS accepts_credit_cards,
    avg(a.ambience_casual) AS ambience_casual,
    avg(a.ambience_classy) AS ambience_classy,
    avg(a.ambience_divey) AS ambience_divey,
    avg(a.ambience_hipster) AS ambience_hipster,
    avg(a.ambience_intimate) AS ambience_intimate,
    avg(a.ambience_romantic) AS ambience_romantic,
    avg(a.ambience_touristy) AS ambience_touristy,
    avg(a.ambience_trendy) AS ambience_trendy,
    avg(a.ambience_upscale) AS ambience_upscale,
    avg(a.byob) AS byob,
    avg(a.caters) AS caters,
    avg(a.coat_check) AS coat_check,
    avg(a.corkage) AS corkage,
    avg(a.delivery) AS delivery,
    avg(a.dietary_restrictions_vegan) AS dietary_restrictions_vegan,
    avg(a.dietary_restrictions_vegetarian) AS dietary_restrictions_vegetarian,
    avg(a.dogs_allowed) AS dogs_allowed,
    avg(a.drive_thr) AS drive_thr,
    avg(a.good_for_breakfast) AS good_for_breakfast,
    avg(a.good_for_brunch) AS good_for_brunch,
    avg(a.good_for_dancing) AS good_for_dancing,
    avg(a.good_for_dessert) AS good_for_dessert,
    avg(a.good_for_dinner) AS good_for_dinner,
    avg(a.good_for_groups) AS good_for_groups,
    avg(a.good_for_kids) AS good_for_kids,
    avg(a.good_for_latenight) AS good_for_latenight,
    avg(a.good_for_lunch) AS good_for_lunch,
    avg(a.happy_hour) AS happy_hour,
    avg(a.has_tv) AS has_tv,
    avg(a.music_accepts_credit_cards) AS music_accepts_credit_cards,
    avg(a.music_background_music) AS music_background_music,
    avg(a.music_caters) AS music_caters,
    avg(a.music_corkage) AS music_corkage,
    avg(a.music_dj) AS music_dj,
    avg(a.music_good_for_groups) AS music_good_for_groups,
    avg(a.music_good_for_kids) AS music_good_for_kids,
    avg(a.music_happy_hour) AS music_happy_hour,
    avg(a.music_has_tv) AS music_has_tv,
    avg(a.music_jukebox) AS music_jukebox,
    avg(a.music_live) AS music_live,
    avg(a.music_outdoor_seating) AS music_outdoor_seating,
    avg(a.music_take_out) AS music_take_out,
    avg(a.music_takes_reservations) AS music_takes_reservations,
    avg(a.music_video) AS music_video,
    avg(a.music_waiter_service) AS music_waiter_service,
    avg(a.music_wheelchair_accessible) AS music_wheelchair_accessible,
    avg(a.order_at_counter) AS order_at_counter,
    avg(a.outdoor_seating) AS outdoor_seating,
    avg(a.parking_garage) AS parking_garage,
    avg(a.parking_lot) AS parking_lot,
    avg(a.parking_street) AS parking_street,
    avg(a.parking_valet) AS parking_valet,
    avg(a.parking_validated) AS parking_validated,
    avg(a.payment_types_amex) AS payment_types_amex,
    avg(a.payment_types_discover) AS payment_types_discover,
    avg(a.payment_types_mastercard) AS payment_types_mastercard,
    avg(a.payment_types_visa) AS payment_types_visa,
    avg(a.take_out) AS take_out,
    avg(a.takes_reservations) AS takes_reservations,
    avg(a.waiter_service) AS waiter_service,
    avg(a.wheelchair_accessible) AS wheelchair_accessible,
    avg(a.ages_allowed_21plus) AS ages_allowed_21plus,
    avg(a.alcohol_beer_and_wine) AS alcohol_beer_and_wine,
    avg(a.alcohol_full_bar) AS alcohol_full_bar,
    avg(a.alcohol_none) AS alcohol_none,
    avg(a.attire_casual) AS attire_casual,
    avg(a.attire_dressy) AS attire_dressy,
    avg(a.byob_corkage_no) AS byob_corkage_no,
    avg(a.byob_corkage_yes_corkage) AS byob_corkage_yes_corkage,
    avg(a.byob_corkage_yes_free) AS byob_corkage_yes_free,
    avg(a.music_attire_casual) AS music_attire_casual,
    avg(a.music_byob_corkage_no) AS music_byob_corkage_no,
    avg(a.music_price_range_2) AS music_price_range_2,
    avg(a.music_smoking_no) AS music_smoking_no,
    avg(a.music_wi_fi_free) AS music_wi_fi_free,
    avg(a.music_wi_fi_no) AS music_wi_fi_no,
    avg(a.noise_level_average) AS noise_level_average,
    avg(a.noise_level_loud) AS noise_level_loud,
    avg(a.noise_level_quiet) AS noise_level_quiet,
    avg(a.noise_level_very_loud) AS noise_level_very_loud,
    avg(a.price_range_1) AS price_range_1,
    avg(a.price_range_2) AS price_range_2,
    avg(a.price_range_3) AS price_range_3,
    avg(a.price_range_4) AS price_range_4,
    avg(a.smoking_no) AS smoking_no,
    avg(a.smoking_outdoor) AS smoking_outdoor,
    avg(a.smoking_yes) AS smoking_yes,
    avg(a.wi_fi_free) AS wi_fi_free,
    avg(a.wi_fi_no) AS wi_fi_no,
    avg(a.wi_fi_paid) AS wi_fi_paid
   FROM tbl_business a
     JOIN tbl_map_ids b ON a.business_id = b.yelp_id
     CROSS JOIN ( SELECT avg(tbl_business.latitude) AS avg_latitude,
            avg(tbl_business.longitude) AS avg_longitude,
            avg(tbl_business.review_count) AS avg_review_count,
            avg(tbl_business.stars) AS avg_stars
           FROM tbl_business) avg_sq
  GROUP BY b.restaurant_id;


CREATE OR REPLACE VIEW vw_num_yelp_ids AS 
 SELECT tbl_map_ids.restaurant_id,
    count(1) AS num_yelp_ids
   FROM tbl_map_ids
  GROUP BY tbl_map_ids.restaurant_id;


CREATE OR REPLACE VIEW vw_reviews AS 
 SELECT b.restaurant_id,
    a.date,
    a.stars,
    a.user_id,
    a.votes_cool AS votes_cool_review,
    a.votes_funny AS votes_funny_review,
    a.votes_useful AS votes_useful_review,
    a.review_len
   FROM tbl_reviews a
     JOIN tbl_map_ids b ON a.business_id = b.yelp_id;


CREATE OR REPLACE VIEW vw_review_stars_votes_1 AS 
 SELECT a.restaurant_id,
    a.date,
    avg(b.stars) AS avg_stars_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.stars
            ELSE NULL::integer
        END) AS avg_stars_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.stars
            ELSE NULL::integer
        END) AS avg_stars_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.stars
            ELSE NULL::integer
        END) AS avg_stars_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.stars
            ELSE NULL::integer
        END) AS avg_stars_365_days_before,
    avg(b.votes_cool_review) AS avg_votes_cool_review_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.votes_cool_review
            ELSE NULL::double precision
        END) AS avg_votes_cool_review_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.votes_cool_review
            ELSE NULL::double precision
        END) AS avg_votes_cool_review_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.votes_cool_review
            ELSE NULL::double precision
        END) AS avg_votes_cool_review_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.votes_cool_review
            ELSE NULL::double precision
        END) AS avg_votes_cool_review_365_days_before,
    avg(b.votes_funny_review) AS avg_votes_funny_review_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.votes_funny_review
            ELSE NULL::double precision
        END) AS avg_votes_funny_review_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.votes_funny_review
            ELSE NULL::double precision
        END) AS avg_votes_funny_review_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.votes_funny_review
            ELSE NULL::double precision
        END) AS avg_votes_funny_review_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.votes_funny_review
            ELSE NULL::double precision
        END) AS avg_votes_funny_review_365_days_before,
    avg(b.votes_useful_review) AS avg_votes_useful_review_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.votes_useful_review
            ELSE NULL::double precision
        END) AS avg_votes_useful_review_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.votes_useful_review
            ELSE NULL::double precision
        END) AS avg_votes_useful_review_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.votes_useful_review
            ELSE NULL::double precision
        END) AS avg_votes_useful_review_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.votes_useful_review
            ELSE NULL::double precision
        END) AS avg_votes_useful_review_365_days_before,
    avg(b.review_len) AS avg_review_len_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.review_len
            ELSE NULL::double precision
        END) AS avg_review_len_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.review_len
            ELSE NULL::double precision
        END) AS avg_review_len_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.review_len
            ELSE NULL::double precision
        END) AS avg_review_len_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.review_len
            ELSE NULL::double precision
        END) AS avg_review_len_365_days_before
   FROM tbl_all_cases a
     JOIN vw_reviews b ON a.restaurant_id = b.restaurant_id
  WHERE b.date <= a.date
  GROUP BY a.restaurant_id, a.date;


CREATE OR REPLACE VIEW vw_review_stars_votes_zm AS 
 SELECT a.restaurant_id,
    a.date,
    a.avg_stars_before - avg_sq.avg_avg_stars_before AS avg_stars_before,
    a.avg_stars_56_days_before - avg_sq.avg_avg_stars_56_days_before AS avg_stars_56_days_before,
    a.avg_stars_91_days_before - avg_sq.avg_avg_stars_91_days_before AS avg_stars_91_days_before,
    a.avg_stars_183_days_before - avg_sq.avg_avg_stars_183_days_before AS avg_stars_183_days_before,
    a.avg_stars_365_days_before - avg_sq.avg_avg_stars_365_days_before AS avg_stars_365_days_before,
    a.avg_votes_cool_review_before - avg_sq.avg_avg_votes_cool_review_before AS avg_votes_cool_review_before,
    a.avg_votes_cool_review_56_days_before - avg_sq.avg_avg_votes_cool_review_56_days_before AS avg_votes_cool_review_56_days_before,
    a.avg_votes_cool_review_91_days_before - avg_sq.avg_avg_votes_cool_review_91_days_before AS avg_votes_cool_review_91_days_before,
    a.avg_votes_cool_review_183_days_before - avg_sq.avg_avg_votes_cool_review_183_days_before AS avg_votes_cool_review_183_days_before,
    a.avg_votes_cool_review_365_days_before - avg_sq.avg_avg_votes_cool_review_365_days_before AS avg_votes_cool_review_365_days_before,
    a.avg_votes_funny_review_before - avg_sq.avg_avg_votes_funny_review_before AS avg_votes_funny_review_before,
    a.avg_votes_funny_review_56_days_before - avg_sq.avg_avg_votes_funny_review_56_days_before AS avg_votes_funny_review_56_days_before,
    a.avg_votes_funny_review_91_days_before - avg_sq.avg_avg_votes_funny_review_91_days_before AS avg_votes_funny_review_91_days_before,
    a.avg_votes_funny_review_183_days_before - avg_sq.avg_avg_votes_funny_review_183_days_before AS avg_votes_funny_review_183_days_before,
    a.avg_votes_funny_review_365_days_before - avg_sq.avg_avg_votes_funny_review_365_days_before AS avg_votes_funny_review_365_days_before,
    a.avg_votes_useful_review_before - avg_sq.avg_avg_votes_useful_review_before AS avg_votes_useful_review_before,
    a.avg_votes_useful_review_56_days_before - avg_sq.avg_avg_votes_useful_review_56_days_before AS avg_votes_useful_review_56_days_before,
    a.avg_votes_useful_review_91_days_before - avg_sq.avg_avg_votes_useful_review_91_days_before AS avg_votes_useful_review_91_days_before,
    a.avg_votes_useful_review_183_days_before - avg_sq.avg_avg_votes_useful_review_183_days_before AS avg_votes_useful_review_183_days_before,
    a.avg_votes_useful_review_365_days_before - avg_sq.avg_avg_votes_useful_review_365_days_before AS avg_votes_useful_review_365_days_before,
    a.avg_review_len_before - avg_sq.avg_avg_review_len_before AS avg_review_len_before,
    a.avg_review_len_56_days_before - avg_sq.avg_avg_review_len_56_days_before AS avg_review_len_56_days_before,
    a.avg_review_len_91_days_before - avg_sq.avg_avg_review_len_91_days_before AS avg_review_len_91_days_before,
    a.avg_review_len_183_days_before - avg_sq.avg_avg_review_len_183_days_before AS avg_review_len_183_days_before,
    a.avg_review_len_365_days_before - avg_sq.avg_avg_review_len_365_days_before AS avg_review_len_365_days_before
   FROM vw_review_stars_votes_1 a
     CROSS JOIN ( SELECT avg(vw_review_stars_votes_1.avg_stars_before) AS avg_avg_stars_before,
            avg(vw_review_stars_votes_1.avg_stars_56_days_before) AS avg_avg_stars_56_days_before,
            avg(vw_review_stars_votes_1.avg_stars_91_days_before) AS avg_avg_stars_91_days_before,
            avg(vw_review_stars_votes_1.avg_stars_183_days_before) AS avg_avg_stars_183_days_before,
            avg(vw_review_stars_votes_1.avg_stars_365_days_before) AS avg_avg_stars_365_days_before,
            avg(vw_review_stars_votes_1.avg_votes_cool_review_before) AS avg_avg_votes_cool_review_before,
            avg(vw_review_stars_votes_1.avg_votes_cool_review_56_days_before) AS avg_avg_votes_cool_review_56_days_before,
            avg(vw_review_stars_votes_1.avg_votes_cool_review_91_days_before) AS avg_avg_votes_cool_review_91_days_before,
            avg(vw_review_stars_votes_1.avg_votes_cool_review_183_days_before) AS avg_avg_votes_cool_review_183_days_before,
            avg(vw_review_stars_votes_1.avg_votes_cool_review_365_days_before) AS avg_avg_votes_cool_review_365_days_before,
            avg(vw_review_stars_votes_1.avg_votes_funny_review_before) AS avg_avg_votes_funny_review_before,
            avg(vw_review_stars_votes_1.avg_votes_funny_review_56_days_before) AS avg_avg_votes_funny_review_56_days_before,
            avg(vw_review_stars_votes_1.avg_votes_funny_review_91_days_before) AS avg_avg_votes_funny_review_91_days_before,
            avg(vw_review_stars_votes_1.avg_votes_funny_review_183_days_before) AS avg_avg_votes_funny_review_183_days_before,
            avg(vw_review_stars_votes_1.avg_votes_funny_review_365_days_before) AS avg_avg_votes_funny_review_365_days_before,
            avg(vw_review_stars_votes_1.avg_votes_useful_review_before) AS avg_avg_votes_useful_review_before,
            avg(vw_review_stars_votes_1.avg_votes_useful_review_56_days_before) AS avg_avg_votes_useful_review_56_days_before,
            avg(vw_review_stars_votes_1.avg_votes_useful_review_91_days_before) AS avg_avg_votes_useful_review_91_days_before,
            avg(vw_review_stars_votes_1.avg_votes_useful_review_183_days_before) AS avg_avg_votes_useful_review_183_days_before,
            avg(vw_review_stars_votes_1.avg_votes_useful_review_365_days_before) AS avg_avg_votes_useful_review_365_days_before,
            avg(vw_review_stars_votes_1.avg_review_len_before) AS avg_avg_review_len_before,
            avg(vw_review_stars_votes_1.avg_review_len_56_days_before) AS avg_avg_review_len_56_days_before,
            avg(vw_review_stars_votes_1.avg_review_len_91_days_before) AS avg_avg_review_len_91_days_before,
            avg(vw_review_stars_votes_1.avg_review_len_183_days_before) AS avg_avg_review_len_183_days_before,
            avg(vw_review_stars_votes_1.avg_review_len_365_days_before) AS avg_avg_review_len_365_days_before
           FROM vw_review_stars_votes_1) avg_sq;


CREATE OR REPLACE VIEW vw_tips AS 
 SELECT b.restaurant_id,
    a.date,
    a.user_id,
    a.likes
   FROM tbl_tips a
     JOIN tbl_map_ids b ON a.business_id = b.yelp_id;


CREATE OR REPLACE VIEW vw_prev_tips AS 
 SELECT lbl1.restaurant_id,
    lbl1.date,
    count(1) AS sum_tips_before,
    sum(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 57 THEN 1
            ELSE NULL::integer
        END)::numeric AS sum_tips_last_56_day,
    sum(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN 1
            ELSE NULL::integer
        END)::numeric AS sum_tips_last_91_day,
    sum(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN 1
            ELSE NULL::integer
        END)::numeric AS sum_tips_last_183_day,
    sum(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN 1
            ELSE NULL::integer
        END)::numeric AS sum_tips_last_365_day
   FROM tbl_all_cases lbl1
     LEFT JOIN vw_tips lbl2 ON lbl1.restaurant_id = lbl2.restaurant_id AND lbl1.date > lbl2.date
  GROUP BY lbl1.restaurant_id, lbl1.date;


CREATE OR REPLACE VIEW vw_freq_insp AS 
 SELECT a.restaurant_id,
    a.date,
    sum(
        CASE
            WHEN (a.date - b.date) <= 42 THEN 1
            ELSE 0
        END)::numeric AS num_insp_42_days_before,
    sum(
        CASE
            WHEN (a.date - b.date) <= 56 THEN 1
            ELSE 0
        END)::numeric AS num_insp_56_days_before,
    sum(
        CASE
            WHEN (a.date - b.date) <= 91 THEN 1
            ELSE 0
        END)::numeric AS num_insp_91_days_before,
    sum(
        CASE
            WHEN (a.date - b.date) <= 186 THEN 1
            ELSE 0
        END)::numeric AS num_insp_183_days_before,
    sum(
        CASE
            WHEN (a.date - b.date) <= 365 THEN 1
            ELSE 0
        END)::numeric AS num_insp_365_days_before
   FROM tbl_all_cases a
     JOIN tbl_labelled_cases b ON a.restaurant_id = b.restaurant_id
  WHERE b.date <= a.date
  GROUP BY a.restaurant_id, a.date;


CREATE OR REPLACE VIEW vw_prev_label_values_1 AS 
 SELECT lbl1.restaurant_id,
    lbl1.date,
    avg(lbl2.one_star) AS avg_one_star_before,
    avg(lbl2.three_star) AS avg_three_star_before,
    avg(lbl2.two_star) AS avg_two_star_before,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS avg_one_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS avg_one_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS avg_one_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS avg_two_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS avg_two_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS avg_two_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS avg_three_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS avg_three_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS avg_three_star_last_365_day,
    max(lbl2.one_star) AS max_one_star_before,
    max(lbl2.two_star) AS max_two_star_before,
    max(lbl2.three_star) AS max_three_star_before,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS max_one_star_last_91_day,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS max_one_star_last_186_day,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS max_one_star_last_365_day,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS max_two_star_last_91_day,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS max_two_star_last_186_day,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS max_two_star_last_365_day,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS max_three_star_last_91_day,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS max_three_star_last_186_day,
    max(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS max_three_star_last_365_day,
    stddev_samp(lbl2.one_star) AS stdev_one_star_before,
    stddev_samp(lbl2.two_star) AS stdev_two_star_before,
    stddev_samp(lbl2.three_star) AS stdev_three_star_before,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS stdev_one_star_last_91_day,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS stdev_one_star_last_186_day,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.one_star
            ELSE NULL::integer
        END) AS stdev_one_star_last_365_day,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS stdev_two_star_last_91_day,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS stdev_two_star_last_186_day,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.two_star
            ELSE NULL::integer
        END) AS stdev_two_star_last_365_day,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS stdev_three_star_last_91_day,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS stdev_three_star_last_186_day,
    stddev_samp(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.three_star
            ELSE NULL::integer
        END) AS stdev_three_star_last_365_day,
    min(lbl2.one_star)::numeric AS min_one_star_before,
    min(lbl2.two_star)::numeric AS min_two_star_before,
    min(lbl2.three_star)::numeric AS min_three_star_before,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.one_star
            ELSE NULL::integer
        END)::numeric AS min_one_star_last_91_day,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.one_star
            ELSE NULL::integer
        END)::numeric AS min_one_star_last_186_day,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.one_star
            ELSE NULL::integer
        END)::numeric AS min_one_star_last_365_day,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.two_star
            ELSE NULL::integer
        END)::numeric AS min_two_star_last_91_day,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.two_star
            ELSE NULL::integer
        END)::numeric AS min_two_star_last_186_day,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.two_star
            ELSE NULL::integer
        END)::numeric AS min_two_star_last_365_day,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 THEN lbl2.three_star
            ELSE NULL::integer
        END)::numeric AS min_three_star_last_91_day,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 THEN lbl2.three_star
            ELSE NULL::integer
        END)::numeric AS min_three_star_last_186_day,
    min(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 THEN lbl2.three_star
            ELSE NULL::integer
        END)::numeric AS min_three_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.one_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_one_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.one_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_one_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.one_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_one_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.two_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_two_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.two_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_two_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.two_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_two_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.three_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_three_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.three_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_three_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.three_star = 0 THEN 1
            ELSE 0
        END) AS avg_clean_insp_three_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.one_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_one_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.one_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_one_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.one_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_one_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.two_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_two_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.two_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_two_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.two_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_two_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.three_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_three_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.three_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_three_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.three_star > 0 THEN 1
            ELSE 0
        END) AS avg_insp_three_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.one_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_one_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.one_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_one_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.one_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_one_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.two_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_two_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.two_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_two_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.two_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_two_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.three_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_three_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.three_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_three_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.three_star > 1 THEN 1
            ELSE 0
        END) AS avg_insp_2_three_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.one_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_one_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.one_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_one_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.one_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_one_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.two_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_two_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.two_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_two_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.two_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_two_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.three_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_three_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.three_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_three_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.three_star > 2 THEN 1
            ELSE 0
        END) AS avg_insp_3_three_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.one_star > 4 THEN 1
            ELSE 0
        END) AS avg_insp_5_one_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.one_star > 4 THEN 1
            ELSE 0
        END) AS avg_insp_5_one_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.one_star > 4 THEN 1
            ELSE 0
        END) AS avg_insp_5_one_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.three_star > 4 THEN 1
            ELSE 0
        END) AS avg_insp_5_three_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.three_star > 4 THEN 1
            ELSE 0
        END) AS avg_insp_5_three_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.three_star > 4 THEN 1
            ELSE 0
        END) AS avg_insp_5_three_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.one_star > 7 THEN 1
            ELSE 0
        END) AS avg_insp_8_one_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.one_star > 7 THEN 1
            ELSE 0
        END) AS avg_insp_8_one_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.one_star > 7 THEN 1
            ELSE 0
        END) AS avg_insp_8_one_star_last_365_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 91 AND lbl2.three_star > 7 THEN 1
            ELSE 0
        END) AS avg_insp_8_three_star_last_91_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 183 AND lbl2.three_star > 7 THEN 1
            ELSE 0
        END) AS avg_insp_8_three_star_last_186_day,
    avg(
        CASE
            WHEN (lbl1.date - lbl2.date) <= 365 AND lbl2.three_star > 7 THEN 1
            ELSE 0
        END) AS avg_insp_8_three_star_last_365_day
   FROM tbl_all_cases lbl1
     LEFT JOIN tbl_labelled_cases lbl2 ON lbl1.restaurant_id = lbl2.restaurant_id AND lbl1.date > lbl2.date
  GROUP BY lbl1.restaurant_id, lbl1.date;


CREATE OR REPLACE VIEW vw_prev_label_values_zm AS 
 SELECT a.restaurant_id,
    a.date,
    a.avg_one_star_before - avg_sq.avg_avg_one_star_before AS avg_one_star_before,
    a.avg_two_star_before - avg_sq.avg_avg_two_star_before AS avg_two_star_before,
    a.avg_three_star_before - avg_sq.avg_avg_three_star_before AS avg_three_star_before,
    a.avg_one_star_last_91_day - avg_sq.avg_avg_one_star_last_91_day AS avg_one_star_last_91_day,
    a.avg_one_star_last_186_day - avg_sq.avg_avg_one_star_last_186_day AS avg_one_star_last_186_day,
    a.avg_one_star_last_365_day - avg_sq.avg_avg_one_star_last_365_day AS avg_one_star_last_365_day,
    a.avg_two_star_last_91_day - avg_sq.avg_avg_two_star_last_91_day AS avg_two_star_last_91_day,
    a.avg_two_star_last_186_day - avg_sq.avg_avg_two_star_last_186_day AS avg_two_star_last_186_day,
    a.avg_two_star_last_365_day - avg_sq.avg_avg_two_star_last_365_day AS avg_two_star_last_365_day,
    a.avg_three_star_last_91_day - avg_sq.avg_avg_three_star_last_91_day AS avg_three_star_last_91_day,
    a.avg_three_star_last_186_day - avg_sq.avg_avg_three_star_last_186_day AS avg_three_star_last_186_day,
    a.avg_three_star_last_365_day - avg_sq.avg_avg_three_star_last_365_day AS avg_three_star_last_365_day,
    a.max_one_star_before::numeric - avg_sq.avg_max_one_star_before AS max_one_star_before,
    a.max_two_star_before::numeric - avg_sq.avg_max_two_star_before AS max_two_star_before,
    a.max_three_star_before::numeric - avg_sq.avg_max_three_star_before AS max_three_star_before,
    a.max_one_star_last_91_day::numeric - avg_sq.avg_max_one_star_last_91_day AS max_one_star_last_91_day,
    a.max_one_star_last_186_day::numeric - avg_sq.avg_max_one_star_last_186_day AS max_one_star_last_186_day,
    a.max_one_star_last_365_day::numeric - avg_sq.avg_max_one_star_last_365_day AS max_one_star_last_365_day,
    a.max_two_star_last_91_day::numeric - avg_sq.avg_max_two_star_last_91_day AS max_two_star_last_91_day,
    a.max_two_star_last_186_day::numeric - avg_sq.avg_max_two_star_last_186_day AS max_two_star_last_186_day,
    a.max_two_star_last_365_day::numeric - avg_sq.avg_max_two_star_last_365_day AS max_two_star_last_365_day,
    a.max_three_star_last_91_day::numeric - avg_sq.avg_max_three_star_last_91_day AS max_three_star_last_91_day,
    a.max_three_star_last_186_day::numeric - avg_sq.avg_max_three_star_last_186_day AS max_three_star_last_186_day,
    a.max_three_star_last_365_day::numeric - avg_sq.avg_max_three_star_last_365_day AS max_three_star_last_365_day,
    a.stdev_one_star_before - avg_sq.avg_stdev_one_star_before AS stdev_one_star_before,
    a.stdev_two_star_before - avg_sq.avg_stdev_two_star_before AS stdev_two_star_before,
    a.stdev_three_star_before - avg_sq.avg_stdev_three_star_before AS stdev_three_star_before,
    a.stdev_one_star_last_91_day - avg_sq.avg_stdev_one_star_last_91_day AS stdev_one_star_last_91_day,
    a.stdev_one_star_last_186_day - avg_sq.avg_stdev_one_star_last_186_day AS stdev_one_star_last_186_day,
    a.stdev_one_star_last_365_day - avg_sq.avg_stdev_one_star_last_365_day AS stdev_one_star_last_365_day,
    a.stdev_two_star_last_91_day - avg_sq.avg_stdev_two_star_last_91_day AS stdev_two_star_last_91_day,
    a.stdev_two_star_last_186_day - avg_sq.avg_stdev_two_star_last_186_day AS stdev_two_star_last_186_day,
    a.stdev_two_star_last_365_day - avg_sq.avg_stdev_two_star_last_365_day AS stdev_two_star_last_365_day,
    a.stdev_three_star_last_91_day - avg_sq.avg_stdev_three_star_last_91_day AS stdev_three_star_last_91_day,
    a.stdev_three_star_last_186_day - avg_sq.avg_stdev_three_star_last_186_day AS stdev_three_star_last_186_day,
    a.stdev_three_star_last_365_day - avg_sq.avg_stdev_three_star_last_365_day AS stdev_three_star_last_365_day,
    a.min_one_star_before - avg_sq.avg_min_one_star_before AS min_one_star_before,
    a.min_two_star_before - avg_sq.avg_min_two_star_before AS min_two_star_before,
    a.min_three_star_before - avg_sq.avg_min_three_star_before AS min_three_star_before,
    a.min_one_star_last_91_day - avg_sq.avg_min_one_star_last_91_day AS min_one_star_last_91_day,
    a.min_one_star_last_186_day - avg_sq.avg_min_one_star_last_186_day AS min_one_star_last_186_day,
    a.min_one_star_last_365_day - avg_sq.avg_min_one_star_last_365_day AS min_one_star_last_365_day,
    a.min_two_star_last_91_day - avg_sq.avg_min_two_star_last_91_day AS min_two_star_last_91_day,
    a.min_two_star_last_186_day - avg_sq.avg_min_two_star_last_186_day AS min_two_star_last_186_day,
    a.min_two_star_last_365_day - avg_sq.avg_min_two_star_last_365_day AS min_two_star_last_365_day,
    a.min_three_star_last_91_day - avg_sq.avg_min_three_star_last_91_day AS min_three_star_last_91_day,
    a.min_three_star_last_186_day - avg_sq.avg_min_three_star_last_186_day AS min_three_star_last_186_day,
    a.min_three_star_last_365_day - avg_sq.avg_min_three_star_last_365_day AS min_three_star_last_365_day,
    a.avg_clean_insp_one_star_last_91_day - avg_sq.avg_avg_clean_insp_one_star_last_91_day AS avg_clean_insp_one_star_last_91_day,
    a.avg_clean_insp_one_star_last_186_day - avg_sq.avg_avg_clean_insp_one_star_last_186_day AS avg_clean_insp_one_star_last_186_day,
    a.avg_clean_insp_one_star_last_365_day - avg_sq.avg_avg_clean_insp_one_star_last_365_day AS avg_clean_insp_one_star_last_365_day,
    a.avg_clean_insp_two_star_last_91_day - avg_sq.avg_avg_clean_insp_two_star_last_91_day AS avg_clean_insp_two_star_last_91_day,
    a.avg_clean_insp_two_star_last_186_day - avg_sq.avg_avg_clean_insp_two_star_last_186_day AS avg_clean_insp_two_star_last_186_day,
    a.avg_clean_insp_two_star_last_365_day - avg_sq.avg_avg_clean_insp_two_star_last_365_day AS avg_clean_insp_two_star_last_365_day,
    a.avg_clean_insp_three_star_last_91_day - avg_sq.avg_avg_clean_insp_three_star_last_91_day AS avg_clean_insp_three_star_last_91_day,
    a.avg_clean_insp_three_star_last_186_day - avg_sq.avg_avg_clean_insp_three_star_last_186_day AS avg_clean_insp_three_star_last_186_day,
    a.avg_clean_insp_three_star_last_365_day - avg_sq.avg_avg_clean_insp_three_star_last_365_day AS avg_clean_insp_three_star_last_365_day,
    a.avg_insp_one_star_last_91_day - avg_sq.avg_avg_insp_one_star_last_91_day AS avg_insp_one_star_last_91_day,
    a.avg_insp_one_star_last_186_day - avg_sq.avg_avg_insp_one_star_last_186_day AS avg_insp_one_star_last_186_day,
    a.avg_insp_one_star_last_365_day - avg_sq.avg_avg_insp_one_star_last_365_day AS avg_insp_one_star_last_365_day,
    a.avg_insp_two_star_last_91_day - avg_sq.avg_avg_insp_two_star_last_91_day AS avg_insp_two_star_last_91_day,
    a.avg_insp_two_star_last_186_day - avg_sq.avg_avg_insp_two_star_last_186_day AS avg_insp_two_star_last_186_day,
    a.avg_insp_two_star_last_365_day - avg_sq.avg_avg_insp_two_star_last_365_day AS avg_insp_two_star_last_365_day,
    a.avg_insp_three_star_last_91_day - avg_sq.avg_avg_insp_three_star_last_91_day AS avg_insp_three_star_last_91_day,
    a.avg_insp_three_star_last_186_day - avg_sq.avg_avg_insp_three_star_last_186_day AS avg_insp_three_star_last_186_day,
    a.avg_insp_three_star_last_365_day - avg_sq.avg_avg_insp_three_star_last_365_day AS avg_insp_three_star_last_365_day,
    a.avg_insp_2_one_star_last_91_day - avg_sq.avg_avg_insp_2_one_star_last_91_day AS avg_insp_2_one_star_last_91_day,
    a.avg_insp_2_one_star_last_186_day - avg_sq.avg_avg_insp_2_one_star_last_186_day AS avg_insp_2_one_star_last_186_day,
    a.avg_insp_2_one_star_last_365_day - avg_sq.avg_avg_insp_2_one_star_last_365_day AS avg_insp_2_one_star_last_365_day,
    a.avg_insp_2_two_star_last_91_day - avg_sq.avg_avg_insp_2_two_star_last_91_day AS avg_insp_2_two_star_last_91_day,
    a.avg_insp_2_two_star_last_186_day - avg_sq.avg_avg_insp_2_two_star_last_186_day AS avg_insp_2_two_star_last_186_day,
    a.avg_insp_2_two_star_last_365_day - avg_sq.avg_avg_insp_2_two_star_last_365_day AS avg_insp_2_two_star_last_365_day,
    a.avg_insp_2_three_star_last_91_day - avg_sq.avg_avg_insp_2_three_star_last_91_day AS avg_insp_2_three_star_last_91_day,
    a.avg_insp_2_three_star_last_186_day - avg_sq.avg_avg_insp_2_three_star_last_186_day AS avg_insp_2_three_star_last_186_day,
    a.avg_insp_2_three_star_last_365_day - avg_sq.avg_avg_insp_2_three_star_last_365_day AS avg_insp_2_three_star_last_365_day,
    a.avg_insp_3_one_star_last_91_day - avg_sq.avg_avg_insp_3_one_star_last_91_day AS avg_insp_3_one_star_last_91_day,
    a.avg_insp_3_one_star_last_186_day - avg_sq.avg_avg_insp_3_one_star_last_186_day AS avg_insp_3_one_star_last_186_day,
    a.avg_insp_3_one_star_last_365_day - avg_sq.avg_avg_insp_3_one_star_last_365_day AS avg_insp_3_one_star_last_365_day,
    a.avg_insp_3_two_star_last_91_day - avg_sq.avg_avg_insp_3_two_star_last_91_day AS avg_insp_3_two_star_last_91_day,
    a.avg_insp_3_two_star_last_186_day - avg_sq.avg_avg_insp_3_two_star_last_186_day AS avg_insp_3_two_star_last_186_day,
    a.avg_insp_3_two_star_last_365_day - avg_sq.avg_avg_insp_3_two_star_last_365_day AS avg_insp_3_two_star_last_365_day,
    a.avg_insp_3_three_star_last_91_day - avg_sq.avg_avg_insp_3_three_star_last_91_day AS avg_insp_3_three_star_last_91_day,
    a.avg_insp_3_three_star_last_186_day - avg_sq.avg_avg_insp_3_three_star_last_186_day AS avg_insp_3_three_star_last_186_day,
    a.avg_insp_3_three_star_last_365_day - avg_sq.avg_avg_insp_3_three_star_last_365_day AS avg_insp_3_three_star_last_365_day,
    a.avg_insp_5_one_star_last_91_day - avg_sq.avg_avg_insp_5_one_star_last_91_day AS avg_insp_5_one_star_last_91_day,
    a.avg_insp_5_one_star_last_186_day - avg_sq.avg_avg_insp_5_one_star_last_186_day AS avg_insp_5_one_star_last_186_day,
    a.avg_insp_5_one_star_last_365_day - avg_sq.avg_avg_insp_5_one_star_last_365_day AS avg_insp_5_one_star_last_365_day,
    a.avg_insp_5_three_star_last_91_day - avg_sq.avg_avg_insp_5_three_star_last_91_day AS avg_insp_5_three_star_last_91_day,
    a.avg_insp_5_three_star_last_186_day - avg_sq.avg_avg_insp_5_three_star_last_186_day AS avg_insp_5_three_star_last_186_day,
    a.avg_insp_5_three_star_last_365_day - avg_sq.avg_avg_insp_5_three_star_last_365_day AS avg_insp_5_three_star_last_365_day,
    a.avg_insp_8_one_star_last_91_day - avg_sq.avg_avg_insp_8_one_star_last_91_day AS avg_insp_8_one_star_last_91_day,
    a.avg_insp_8_one_star_last_186_day - avg_sq.avg_avg_insp_8_one_star_last_186_day AS avg_insp_8_one_star_last_186_day,
    a.avg_insp_8_one_star_last_365_day - avg_sq.avg_avg_insp_8_one_star_last_365_day AS avg_insp_8_one_star_last_365_day,
    a.avg_insp_8_three_star_last_91_day - avg_sq.avg_avg_insp_8_three_star_last_91_day AS avg_insp_8_three_star_last_91_day,
    a.avg_insp_8_three_star_last_186_day - avg_sq.avg_avg_insp_8_three_star_last_186_day AS avg_insp_8_three_star_last_186_day,
    a.avg_insp_8_three_star_last_365_day - avg_sq.avg_avg_insp_8_three_star_last_365_day AS avg_insp_8_three_star_last_365_day
   FROM vw_prev_label_values_1 a
     CROSS JOIN ( SELECT avg(vw_prev_label_values_1.avg_one_star_before) AS avg_avg_one_star_before,
            avg(vw_prev_label_values_1.avg_two_star_before) AS avg_avg_two_star_before,
            avg(vw_prev_label_values_1.avg_three_star_before) AS avg_avg_three_star_before,
            avg(vw_prev_label_values_1.avg_one_star_last_91_day) AS avg_avg_one_star_last_91_day,
            avg(vw_prev_label_values_1.avg_one_star_last_186_day) AS avg_avg_one_star_last_186_day,
            avg(vw_prev_label_values_1.avg_one_star_last_365_day) AS avg_avg_one_star_last_365_day,
            avg(vw_prev_label_values_1.avg_two_star_last_91_day) AS avg_avg_two_star_last_91_day,
            avg(vw_prev_label_values_1.avg_two_star_last_186_day) AS avg_avg_two_star_last_186_day,
            avg(vw_prev_label_values_1.avg_two_star_last_365_day) AS avg_avg_two_star_last_365_day,
            avg(vw_prev_label_values_1.avg_three_star_last_91_day) AS avg_avg_three_star_last_91_day,
            avg(vw_prev_label_values_1.avg_three_star_last_186_day) AS avg_avg_three_star_last_186_day,
            avg(vw_prev_label_values_1.avg_three_star_last_365_day) AS avg_avg_three_star_last_365_day,
            avg(vw_prev_label_values_1.max_one_star_before) AS avg_max_one_star_before,
            avg(vw_prev_label_values_1.max_two_star_before) AS avg_max_two_star_before,
            avg(vw_prev_label_values_1.max_three_star_before) AS avg_max_three_star_before,
            avg(vw_prev_label_values_1.max_one_star_last_91_day) AS avg_max_one_star_last_91_day,
            avg(vw_prev_label_values_1.max_one_star_last_186_day) AS avg_max_one_star_last_186_day,
            avg(vw_prev_label_values_1.max_one_star_last_365_day) AS avg_max_one_star_last_365_day,
            avg(vw_prev_label_values_1.max_two_star_last_91_day) AS avg_max_two_star_last_91_day,
            avg(vw_prev_label_values_1.max_two_star_last_186_day) AS avg_max_two_star_last_186_day,
            avg(vw_prev_label_values_1.max_two_star_last_365_day) AS avg_max_two_star_last_365_day,
            avg(vw_prev_label_values_1.max_three_star_last_91_day) AS avg_max_three_star_last_91_day,
            avg(vw_prev_label_values_1.max_three_star_last_186_day) AS avg_max_three_star_last_186_day,
            avg(vw_prev_label_values_1.max_three_star_last_365_day) AS avg_max_three_star_last_365_day,
            avg(vw_prev_label_values_1.stdev_one_star_before) AS avg_stdev_one_star_before,
            avg(vw_prev_label_values_1.stdev_two_star_before) AS avg_stdev_two_star_before,
            avg(vw_prev_label_values_1.stdev_three_star_before) AS avg_stdev_three_star_before,
            avg(vw_prev_label_values_1.stdev_one_star_last_91_day) AS avg_stdev_one_star_last_91_day,
            avg(vw_prev_label_values_1.stdev_one_star_last_186_day) AS avg_stdev_one_star_last_186_day,
            avg(vw_prev_label_values_1.stdev_one_star_last_365_day) AS avg_stdev_one_star_last_365_day,
            avg(vw_prev_label_values_1.stdev_two_star_last_91_day) AS avg_stdev_two_star_last_91_day,
            avg(vw_prev_label_values_1.stdev_two_star_last_186_day) AS avg_stdev_two_star_last_186_day,
            avg(vw_prev_label_values_1.stdev_two_star_last_365_day) AS avg_stdev_two_star_last_365_day,
            avg(vw_prev_label_values_1.stdev_three_star_last_91_day) AS avg_stdev_three_star_last_91_day,
            avg(vw_prev_label_values_1.stdev_three_star_last_186_day) AS avg_stdev_three_star_last_186_day,
            avg(vw_prev_label_values_1.stdev_three_star_last_365_day) AS avg_stdev_three_star_last_365_day,
            avg(vw_prev_label_values_1.min_one_star_before) AS avg_min_one_star_before,
            avg(vw_prev_label_values_1.min_two_star_before) AS avg_min_two_star_before,
            avg(vw_prev_label_values_1.min_three_star_before) AS avg_min_three_star_before,
            avg(vw_prev_label_values_1.min_one_star_last_91_day) AS avg_min_one_star_last_91_day,
            avg(vw_prev_label_values_1.min_one_star_last_186_day) AS avg_min_one_star_last_186_day,
            avg(vw_prev_label_values_1.min_one_star_last_365_day) AS avg_min_one_star_last_365_day,
            avg(vw_prev_label_values_1.min_two_star_last_91_day) AS avg_min_two_star_last_91_day,
            avg(vw_prev_label_values_1.min_two_star_last_186_day) AS avg_min_two_star_last_186_day,
            avg(vw_prev_label_values_1.min_two_star_last_365_day) AS avg_min_two_star_last_365_day,
            avg(vw_prev_label_values_1.min_three_star_last_91_day) AS avg_min_three_star_last_91_day,
            avg(vw_prev_label_values_1.min_three_star_last_186_day) AS avg_min_three_star_last_186_day,
            avg(vw_prev_label_values_1.min_three_star_last_365_day) AS avg_min_three_star_last_365_day,
            avg(vw_prev_label_values_1.avg_clean_insp_one_star_last_91_day) AS avg_avg_clean_insp_one_star_last_91_day,
            avg(vw_prev_label_values_1.avg_clean_insp_one_star_last_186_day) AS avg_avg_clean_insp_one_star_last_186_day,
            avg(vw_prev_label_values_1.avg_clean_insp_one_star_last_365_day) AS avg_avg_clean_insp_one_star_last_365_day,
            avg(vw_prev_label_values_1.avg_clean_insp_two_star_last_91_day) AS avg_avg_clean_insp_two_star_last_91_day,
            avg(vw_prev_label_values_1.avg_clean_insp_two_star_last_186_day) AS avg_avg_clean_insp_two_star_last_186_day,
            avg(vw_prev_label_values_1.avg_clean_insp_two_star_last_365_day) AS avg_avg_clean_insp_two_star_last_365_day,
            avg(vw_prev_label_values_1.avg_clean_insp_three_star_last_91_day) AS avg_avg_clean_insp_three_star_last_91_day,
            avg(vw_prev_label_values_1.avg_clean_insp_three_star_last_186_day) AS avg_avg_clean_insp_three_star_last_186_day,
            avg(vw_prev_label_values_1.avg_clean_insp_three_star_last_365_day) AS avg_avg_clean_insp_three_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_one_star_last_91_day) AS avg_avg_insp_one_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_one_star_last_186_day) AS avg_avg_insp_one_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_one_star_last_365_day) AS avg_avg_insp_one_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_two_star_last_91_day) AS avg_avg_insp_two_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_two_star_last_186_day) AS avg_avg_insp_two_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_two_star_last_365_day) AS avg_avg_insp_two_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_three_star_last_91_day) AS avg_avg_insp_three_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_three_star_last_186_day) AS avg_avg_insp_three_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_three_star_last_365_day) AS avg_avg_insp_three_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_2_one_star_last_91_day) AS avg_avg_insp_2_one_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_2_one_star_last_186_day) AS avg_avg_insp_2_one_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_2_one_star_last_365_day) AS avg_avg_insp_2_one_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_2_two_star_last_91_day) AS avg_avg_insp_2_two_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_2_two_star_last_186_day) AS avg_avg_insp_2_two_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_2_two_star_last_365_day) AS avg_avg_insp_2_two_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_2_three_star_last_91_day) AS avg_avg_insp_2_three_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_2_three_star_last_186_day) AS avg_avg_insp_2_three_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_2_three_star_last_365_day) AS avg_avg_insp_2_three_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_3_one_star_last_91_day) AS avg_avg_insp_3_one_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_3_one_star_last_186_day) AS avg_avg_insp_3_one_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_3_one_star_last_365_day) AS avg_avg_insp_3_one_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_3_two_star_last_91_day) AS avg_avg_insp_3_two_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_3_two_star_last_186_day) AS avg_avg_insp_3_two_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_3_two_star_last_365_day) AS avg_avg_insp_3_two_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_3_three_star_last_91_day) AS avg_avg_insp_3_three_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_3_three_star_last_186_day) AS avg_avg_insp_3_three_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_3_three_star_last_365_day) AS avg_avg_insp_3_three_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_5_one_star_last_91_day) AS avg_avg_insp_5_one_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_5_one_star_last_186_day) AS avg_avg_insp_5_one_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_5_one_star_last_365_day) AS avg_avg_insp_5_one_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_5_three_star_last_91_day) AS avg_avg_insp_5_three_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_5_three_star_last_186_day) AS avg_avg_insp_5_three_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_5_three_star_last_365_day) AS avg_avg_insp_5_three_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_8_one_star_last_91_day) AS avg_avg_insp_8_one_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_8_one_star_last_186_day) AS avg_avg_insp_8_one_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_8_one_star_last_365_day) AS avg_avg_insp_8_one_star_last_365_day,
            avg(vw_prev_label_values_1.avg_insp_8_three_star_last_91_day) AS avg_avg_insp_8_three_star_last_91_day,
            avg(vw_prev_label_values_1.avg_insp_8_three_star_last_186_day) AS avg_avg_insp_8_three_star_last_186_day,
            avg(vw_prev_label_values_1.avg_insp_8_three_star_last_365_day) AS avg_avg_insp_8_three_star_last_365_day
           FROM vw_prev_label_values_1) avg_sq;


CREATE OR REPLACE VIEW vw_reviews_users AS 
 SELECT b.restaurant_id,
    a.date,
    a.stars,
    a.user_id,
    a.votes_cool AS votes_cool_review,
    a.votes_funny AS votes_funny_review,
    a.votes_useful AS votes_useful_review,
    a.review_len,
    usr.review_count,
    usr.fans,
    usr.yelping_since,
        CASE
            WHEN usr.average_stars < 1::double precision THEN 1::double precision
            ELSE usr.average_stars
        END AS average_stars,
    usr.num_friends,
    usr.votes_cool AS votes_cool_user,
    usr.votes_funny AS votes_funny_user,
    usr.votes_useful AS votes_useful_users,
    usr.sum_years_elite
   FROM tbl_reviews a
     JOIN tbl_map_ids b ON a.business_id = b.yelp_id
     JOIN tbl_users usr ON a.user_id = usr.user_id;


CREATE OR REPLACE VIEW vw_review_users_stars_votes_1 AS 
 SELECT a.restaurant_id,
    a.date,
    avg(b.fans) AS avg_fans_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 THEN b.fans
            ELSE NULL::integer
        END) AS avg_fans_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.fans
            ELSE NULL::integer
        END) AS avg_fans_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.fans
            ELSE NULL::integer
        END) AS avg_fans_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.fans
            ELSE NULL::integer
        END) AS avg_fans_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.fans
            ELSE NULL::integer
        END) AS avg_fans_365_days_before,
    avg(b.review_count) AS avg_review_count_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 THEN b.review_count
            ELSE NULL::integer
        END) AS avg_review_count_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.review_count
            ELSE NULL::integer
        END) AS avg_review_count_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.review_count
            ELSE NULL::integer
        END) AS avg_review_count_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.review_count
            ELSE NULL::integer
        END) AS avg_review_count_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.review_count
            ELSE NULL::integer
        END) AS avg_review_count_365_days_before,
    avg(b.num_friends) AS avg_num_friends_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 THEN b.num_friends
            ELSE NULL::integer::double precision
        END) AS avg_num_friends_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.num_friends
            ELSE NULL::integer::double precision
        END) AS avg_num_friends_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.num_friends
            ELSE NULL::integer::double precision
        END) AS avg_num_friends_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.num_friends
            ELSE NULL::integer::double precision
        END) AS avg_num_friends_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.num_friends
            ELSE NULL::integer::double precision
        END) AS avg_num_friends_365_days_before,
    avg(b.stars::double precision / b.average_stars) AS avg_vs_usr_avg_stars_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 THEN b.stars::double precision / b.average_stars
            ELSE NULL::double precision
        END) AS avg_vs_usr_avg_stars_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.stars::double precision / b.average_stars
            ELSE NULL::double precision
        END) AS avg_vs_usr_avg_stars_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.stars::double precision / b.average_stars
            ELSE NULL::double precision
        END) AS avg_vs_usr_avg_stars_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.stars::double precision / b.average_stars
            ELSE NULL::double precision
        END) AS avg_vs_usr_avg_stars_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.stars::double precision / b.average_stars
            ELSE NULL::double precision
        END) AS avg_vs_usr_avg_stars_365_days_before
   FROM tbl_all_cases a
     JOIN vw_reviews_users b ON a.restaurant_id = b.restaurant_id
  WHERE b.date <= a.date
  GROUP BY a.restaurant_id, a.date;


CREATE OR REPLACE VIEW vw_review_users_stars_votes_zm AS 
 SELECT a.restaurant_id,
    a.date,
    a.avg_fans_before - avg_sq.avg_avg_fans_before AS avg_fans_before,
    a.avg_fans_42_days_before - avg_sq.avg_avg_fans_42_days_before AS avg_fans_42_days_before,
    a.avg_fans_56_days_before - avg_sq.avg_avg_fans_56_days_before AS avg_fans_56_days_before,
    a.avg_fans_91_days_before - avg_sq.avg_avg_fans_91_days_before AS avg_fans_91_days_before,
    a.avg_fans_183_days_before - avg_sq.avg_avg_fans_183_days_before AS avg_fans_183_days_before,
    a.avg_fans_365_days_before - avg_sq.avg_avg_fans_365_days_before AS avg_fans_365_days_before,
    a.avg_review_count_before - avg_sq.avg_avg_review_count_before AS avg_review_count_before,
    a.avg_review_count_42_days_before - avg_sq.avg_avg_review_count_42_days_before AS avg_review_count_42_days_before,
    a.avg_review_count_56_days_before - avg_sq.avg_avg_review_count_56_days_before AS avg_review_count_56_days_before,
    a.avg_review_count_91_days_before - avg_sq.avg_avg_review_count_91_days_before AS avg_review_count_91_days_before,
    a.avg_review_count_183_days_before - avg_sq.avg_avg_review_count_183_days_before AS avg_review_count_183_days_before,
    a.avg_review_count_365_days_before - avg_sq.avg_avg_review_count_365_days_before AS avg_review_count_365_days_before,
    a.avg_num_friends_before - avg_sq.avg_avg_num_friends_before AS avg_num_friends_before,
    a.avg_num_friends_42_days_before - avg_sq.avg_avg_num_friends_42_days_before AS avg_num_friends_42_days_before,
    a.avg_num_friends_56_days_before - avg_sq.avg_avg_num_friends_56_days_before AS avg_num_friends_56_days_before,
    a.avg_num_friends_91_days_before - avg_sq.avg_avg_num_friends_91_days_before AS avg_num_friends_91_days_before,
    a.avg_num_friends_183_days_before - avg_sq.avg_avg_num_friends_183_days_before AS avg_num_friends_183_days_before,
    a.avg_num_friends_365_days_before - avg_sq.avg_avg_num_friends_365_days_before AS avg_num_friends_365_days_before,
    a.avg_vs_usr_avg_stars_before - avg_sq.avg_avg_vs_usr_avg_stars_before AS avg_vs_usr_avg_stars_before,
    a.avg_vs_usr_avg_stars_42_days_before - avg_sq.avg_avg_vs_usr_avg_stars_42_days_before AS avg_vs_usr_avg_stars_42_days_before,
    a.avg_vs_usr_avg_stars_56_days_before - avg_sq.avg_avg_vs_usr_avg_stars_56_days_before AS avg_vs_usr_avg_stars_56_days_before,
    a.avg_vs_usr_avg_stars_91_days_before - avg_sq.avg_avg_vs_usr_avg_stars_91_days_before AS avg_vs_usr_avg_stars_91_days_before,
    a.avg_vs_usr_avg_stars_183_days_before - avg_sq.avg_avg_vs_usr_avg_stars_183_days_before AS avg_vs_usr_avg_stars_183_days_before,
    a.avg_vs_usr_avg_stars_365_days_before - avg_sq.avg_avg_vs_usr_avg_stars_365_days_before AS avg_vs_usr_avg_stars_365_days_before
   FROM vw_review_users_stars_votes_1 a
     CROSS JOIN ( SELECT avg(vw_review_users_stars_votes_1.avg_fans_before) AS avg_avg_fans_before,
            avg(vw_review_users_stars_votes_1.avg_fans_42_days_before) AS avg_avg_fans_42_days_before,
            avg(vw_review_users_stars_votes_1.avg_fans_56_days_before) AS avg_avg_fans_56_days_before,
            avg(vw_review_users_stars_votes_1.avg_fans_91_days_before) AS avg_avg_fans_91_days_before,
            avg(vw_review_users_stars_votes_1.avg_fans_183_days_before) AS avg_avg_fans_183_days_before,
            avg(vw_review_users_stars_votes_1.avg_fans_365_days_before) AS avg_avg_fans_365_days_before,
            avg(vw_review_users_stars_votes_1.avg_review_count_before) AS avg_avg_review_count_before,
            avg(vw_review_users_stars_votes_1.avg_review_count_42_days_before) AS avg_avg_review_count_42_days_before,
            avg(vw_review_users_stars_votes_1.avg_review_count_56_days_before) AS avg_avg_review_count_56_days_before,
            avg(vw_review_users_stars_votes_1.avg_review_count_91_days_before) AS avg_avg_review_count_91_days_before,
            avg(vw_review_users_stars_votes_1.avg_review_count_183_days_before) AS avg_avg_review_count_183_days_before,
            avg(vw_review_users_stars_votes_1.avg_review_count_365_days_before) AS avg_avg_review_count_365_days_before,
            avg(vw_review_users_stars_votes_1.avg_num_friends_before) AS avg_avg_num_friends_before,
            avg(vw_review_users_stars_votes_1.avg_num_friends_42_days_before) AS avg_avg_num_friends_42_days_before,
            avg(vw_review_users_stars_votes_1.avg_num_friends_56_days_before) AS avg_avg_num_friends_56_days_before,
            avg(vw_review_users_stars_votes_1.avg_num_friends_91_days_before) AS avg_avg_num_friends_91_days_before,
            avg(vw_review_users_stars_votes_1.avg_num_friends_183_days_before) AS avg_avg_num_friends_183_days_before,
            avg(vw_review_users_stars_votes_1.avg_num_friends_365_days_before) AS avg_avg_num_friends_365_days_before,
            avg(vw_review_users_stars_votes_1.avg_vs_usr_avg_stars_before) AS avg_avg_vs_usr_avg_stars_before,
            avg(vw_review_users_stars_votes_1.avg_vs_usr_avg_stars_42_days_before) AS avg_avg_vs_usr_avg_stars_42_days_before,
            avg(vw_review_users_stars_votes_1.avg_vs_usr_avg_stars_56_days_before) AS avg_avg_vs_usr_avg_stars_56_days_before,
            avg(vw_review_users_stars_votes_1.avg_vs_usr_avg_stars_91_days_before) AS avg_avg_vs_usr_avg_stars_91_days_before,
            avg(vw_review_users_stars_votes_1.avg_vs_usr_avg_stars_183_days_before) AS avg_avg_vs_usr_avg_stars_183_days_before,
            avg(vw_review_users_stars_votes_1.avg_vs_usr_avg_stars_365_days_before) AS avg_avg_vs_usr_avg_stars_365_days_before
           FROM vw_review_users_stars_votes_1) avg_sq;


CREATE OR REPLACE VIEW vw_time_between_inspections_1 AS 
 SELECT a.restaurant_id,
    a.date,
        CASE
            WHEN b.earlier_date IS NULL THEN NULL::integer
            ELSE a.date - b.earlier_date
        END AS days_since_last_inspection,
        CASE
            WHEN c.earlier_date IS NULL THEN NULL::integer
            ELSE a.date - c.earlier_date
        END AS days_since_second_last_inspection,
        CASE
            WHEN d.earlier_date IS NULL THEN NULL::integer
            ELSE a.date - d.earlier_date
        END AS days_since_third_last_inspection,
        CASE
            WHEN e.earlier_date IS NULL THEN NULL::integer
            ELSE a.date - e.earlier_date
        END AS days_since_fourth_last_inspection,
        CASE
            WHEN f.earlier_date IS NULL THEN NULL::integer
            ELSE a.date - f.earlier_date
        END AS days_since_fifth_last_inspection,
        CASE
            WHEN b.earlier_date IS NULL THEN 1
            ELSE 0
        END AS first_inspection,
        CASE
            WHEN c.earlier_date IS NULL THEN 1
            ELSE 0
        END AS second_inspection,
        CASE
            WHEN d.earlier_date IS NULL THEN 1
            ELSE 0
        END AS third_inspection,
        CASE
            WHEN e.earlier_date IS NULL THEN 1
            ELSE 0
        END AS fourth_inspection,
        CASE
            WHEN f.earlier_date IS NULL THEN 1
            ELSE 0
        END AS fifth_inspection
   FROM vw_all_ordered_cases a
     LEFT JOIN ( SELECT a_1.restaurant_id,
            a_1.date AS earlier_date,
            rank() OVER (PARTITION BY a_1.restaurant_id ORDER BY a_1.date) AS training_case_label
           FROM vw_all_ordered_cases a_1) b ON a.restaurant_id = b.restaurant_id AND a.training_case_label = (b.training_case_label + 1)
     LEFT JOIN ( SELECT a_1.restaurant_id,
            a_1.date AS earlier_date,
            rank() OVER (PARTITION BY a_1.restaurant_id ORDER BY a_1.date) AS training_case_label
           FROM vw_all_ordered_cases a_1) c ON a.restaurant_id = c.restaurant_id AND a.training_case_label = (c.training_case_label + 2)
     LEFT JOIN ( SELECT a_1.restaurant_id,
            a_1.date AS earlier_date,
            rank() OVER (PARTITION BY a_1.restaurant_id ORDER BY a_1.date) AS training_case_label
           FROM vw_all_ordered_cases a_1) d ON a.restaurant_id = d.restaurant_id AND a.training_case_label = (d.training_case_label + 3)
     LEFT JOIN ( SELECT a_1.restaurant_id,
            a_1.date AS earlier_date,
            rank() OVER (PARTITION BY a_1.restaurant_id ORDER BY a_1.date) AS training_case_label
           FROM vw_all_ordered_cases a_1) e ON a.restaurant_id = e.restaurant_id AND a.training_case_label = (e.training_case_label + 4)
     LEFT JOIN ( SELECT a_1.restaurant_id,
            a_1.date AS earlier_date,
            rank() OVER (PARTITION BY a_1.restaurant_id ORDER BY a_1.date) AS training_case_label
           FROM vw_all_ordered_cases a_1) f ON a.restaurant_id = f.restaurant_id AND a.training_case_label = (f.training_case_label + 5);


CREATE OR REPLACE VIEW vw_time_between_inspections_zm AS 
 SELECT a.restaurant_id,
    a.date,
    a.days_since_last_inspection::numeric - avg_sq.avg_days_since_last_inspection AS days_since_last_inspection,
    a.days_since_second_last_inspection::numeric - avg_sq.avg_days_since_second_last_inspection AS days_since_second_last_inspection,
    a.days_since_third_last_inspection::numeric - avg_sq.avg_days_since_third_last_inspection AS days_since_third_last_inspection,
    a.days_since_fourth_last_inspection::numeric - avg_sq.avg_days_since_fourth_last_inspection AS days_since_fourth_last_inspection,
    a.days_since_fifth_last_inspection::numeric - avg_sq.avg_days_since_fifth_last_inspection AS days_since_fifth_last_inspection,
    a.first_inspection,
    a.second_inspection,
    a.third_inspection,
    a.fourth_inspection,
    a.fifth_inspection
   FROM vw_time_between_inspections_1 a
     CROSS JOIN ( SELECT avg(vw_time_between_inspections_1.days_since_last_inspection) AS avg_days_since_last_inspection,
            avg(vw_time_between_inspections_1.days_since_last_inspection) AS avg_days_since_second_last_inspection,
            avg(vw_time_between_inspections_1.days_since_last_inspection) AS avg_days_since_third_last_inspection,
            avg(vw_time_between_inspections_1.days_since_last_inspection) AS avg_days_since_fourth_last_inspection,
            avg(vw_time_between_inspections_1.days_since_last_inspection) AS avg_days_since_fifth_last_inspection
           FROM vw_time_between_inspections_1) avg_sq;


CREATE OR REPLACE VIEW vw_review_stars_dist_1 AS 
 SELECT a.restaurant_id,
    a.date,
    avg(
        CASE
            WHEN b.stars = 1 THEN 1
            ELSE 0
        END) AS share_1_star_before,
    avg(
        CASE
            WHEN b.stars = 2 THEN 1
            ELSE 0
        END) AS share_2_star_before,
    avg(
        CASE
            WHEN b.stars = 3 THEN 1
            ELSE 0
        END) AS share_3_star_before,
    avg(
        CASE
            WHEN b.stars = 4 THEN 1
            ELSE 0
        END) AS share_4_star_before,
    avg(
        CASE
            WHEN b.stars = 5 THEN 1
            ELSE 0
        END) AS share_5_star_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 AND b.stars = 1 THEN 1
            ELSE 0
        END) AS share_1_star_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 AND b.stars = 2 THEN 1
            ELSE 0
        END) AS share_2_star_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 AND b.stars = 3 THEN 1
            ELSE 0
        END) AS share_3_star_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 AND b.stars = 4 THEN 1
            ELSE 0
        END) AS share_4_star_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 42 AND b.stars = 5 THEN 1
            ELSE 0
        END) AS share_5_star_42_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 AND b.stars = 1 THEN 1
            ELSE 0
        END) AS share_1_star_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 AND b.stars = 2 THEN 1
            ELSE 0
        END) AS share_2_star_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 AND b.stars = 3 THEN 1
            ELSE 0
        END) AS share_3_star_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 AND b.stars = 4 THEN 1
            ELSE 0
        END) AS share_4_star_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 56 AND b.stars = 5 THEN 1
            ELSE 0
        END) AS share_5_star_56_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 AND b.stars = 1 THEN 1
            ELSE 0
        END) AS share_1_star_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 AND b.stars = 2 THEN 1
            ELSE 0
        END) AS share_2_star_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 AND b.stars = 3 THEN 1
            ELSE 0
        END) AS share_3_star_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 AND b.stars = 4 THEN 1
            ELSE 0
        END) AS share_4_star_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 91 AND b.stars = 5 THEN 1
            ELSE 0
        END) AS share_5_star_91_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 AND b.stars = 1 THEN 1
            ELSE 0
        END) AS share_1_star_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 AND b.stars = 2 THEN 1
            ELSE 0
        END) AS share_2_star_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 AND b.stars = 3 THEN 1
            ELSE 0
        END) AS share_3_star_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 AND b.stars = 4 THEN 1
            ELSE 0
        END) AS share_4_star_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 183 AND b.stars = 5 THEN 1
            ELSE 0
        END) AS share_5_star_183_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 AND b.stars = 1 THEN 1
            ELSE 0
        END) AS share_1_star_365_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 AND b.stars = 2 THEN 1
            ELSE 0
        END) AS share_2_star_365_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 AND b.stars = 3 THEN 1
            ELSE 0
        END) AS share_3_star_365_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 AND b.stars = 4 THEN 1
            ELSE 0
        END) AS share_4_star_365_days_before,
    avg(
        CASE
            WHEN (a.date - b.date) <= 365 AND b.stars = 5 THEN 1
            ELSE 0
        END) AS share_5_star_365_days_before,
    stddev_samp(b.stars) AS std_review_stars_before,
    stddev_samp(
        CASE
            WHEN (a.date - b.date) <= 42 THEN b.stars
            ELSE NULL::integer
        END) AS std_review_stars_42_days_before,
    stddev_samp(
        CASE
            WHEN (a.date - b.date) <= 56 THEN b.stars
            ELSE NULL::integer
        END) AS std_review_stars_56_days_before,
    stddev_samp(
        CASE
            WHEN (a.date - b.date) <= 91 THEN b.stars
            ELSE NULL::integer
        END) AS std_review_stars_91_days_before,
    stddev_samp(
        CASE
            WHEN (a.date - b.date) <= 183 THEN b.stars
            ELSE NULL::integer
        END) AS std_review_stars_183_days_before,
    stddev_samp(
        CASE
            WHEN (a.date - b.date) <= 365 THEN b.stars
            ELSE NULL::integer
        END) AS std_review_stars_365_days_before
   FROM tbl_all_cases a
     JOIN vw_reviews b ON a.restaurant_id = b.restaurant_id
  WHERE b.date <= a.date
  GROUP BY a.restaurant_id, a.date;


CREATE OR REPLACE VIEW vw_review_stars_dist_zm AS 
 SELECT a.restaurant_id,
    a.date,
    a.share_1_star_before - avg_sq.avg_share_1_star_before AS share_1_star_before,
    a.share_2_star_before - avg_sq.avg_share_2_star_before AS share_2_star_before,
    a.share_3_star_before - avg_sq.avg_share_3_star_before AS share_3_star_before,
    a.share_4_star_before - avg_sq.avg_share_4_star_before AS share_4_star_before,
    a.share_5_star_before - avg_sq.avg_share_5_star_before AS share_5_star_before,
    a.share_1_star_42_days_before - avg_sq.avg_share_1_star_42_days_before AS share_1_star_42_days_before,
    a.share_2_star_42_days_before - avg_sq.avg_share_2_star_42_days_before AS share_2_star_42_days_before,
    a.share_3_star_42_days_before - avg_sq.avg_share_3_star_42_days_before AS share_3_star_42_days_before,
    a.share_4_star_42_days_before - avg_sq.avg_share_4_star_42_days_before AS share_4_star_42_days_before,
    a.share_5_star_42_days_before - avg_sq.avg_share_5_star_42_days_before AS share_5_star_42_days_before,
    a.share_1_star_56_days_before - avg_sq.avg_share_1_star_56_days_before AS share_1_star_56_days_before,
    a.share_2_star_56_days_before - avg_sq.avg_share_2_star_56_days_before AS share_2_star_56_days_before,
    a.share_3_star_56_days_before - avg_sq.avg_share_3_star_56_days_before AS share_3_star_56_days_before,
    a.share_4_star_56_days_before - avg_sq.avg_share_4_star_56_days_before AS share_4_star_56_days_before,
    a.share_5_star_56_days_before - avg_sq.avg_share_5_star_56_days_before AS share_5_star_56_days_before,
    a.share_1_star_91_days_before - avg_sq.avg_share_1_star_91_days_before AS share_1_star_91_days_before,
    a.share_2_star_91_days_before - avg_sq.avg_share_2_star_91_days_before AS share_2_star_91_days_before,
    a.share_3_star_91_days_before - avg_sq.avg_share_3_star_91_days_before AS share_3_star_91_days_before,
    a.share_4_star_91_days_before - avg_sq.avg_share_4_star_91_days_before AS share_4_star_91_days_before,
    a.share_5_star_91_days_before - avg_sq.avg_share_5_star_91_days_before AS share_5_star_91_days_before,
    a.share_1_star_183_days_before - avg_sq.avg_share_1_star_183_days_before AS share_1_star_183_days_before,
    a.share_2_star_183_days_before - avg_sq.avg_share_2_star_183_days_before AS share_2_star_183_days_before,
    a.share_3_star_183_days_before - avg_sq.avg_share_3_star_183_days_before AS share_3_star_183_days_before,
    a.share_4_star_183_days_before - avg_sq.avg_share_4_star_183_days_before AS share_4_star_183_days_before,
    a.share_5_star_183_days_before - avg_sq.avg_share_5_star_183_days_before AS share_5_star_183_days_before,
    a.share_1_star_365_days_before - avg_sq.avg_share_1_star_365_days_before AS share_1_star_365_days_before,
    a.share_2_star_365_days_before - avg_sq.avg_share_2_star_365_days_before AS share_2_star_365_days_before,
    a.share_3_star_365_days_before - avg_sq.avg_share_3_star_365_days_before AS share_3_star_365_days_before,
    a.share_4_star_365_days_before - avg_sq.avg_share_4_star_365_days_before AS share_4_star_365_days_before,
    a.share_5_star_365_days_before - avg_sq.avg_share_5_star_365_days_before AS share_5_star_365_days_before,
    a.std_review_stars_before - avg_sq.avg_std_review_stars_before AS std_review_stars_before,
    a.std_review_stars_42_days_before - avg_sq.avg_std_review_stars_42_days_before AS std_review_stars_42_days_before,
    a.std_review_stars_56_days_before - avg_sq.avg_std_review_stars_56_days_before AS std_review_stars_56_days_before,
    a.std_review_stars_91_days_before - avg_sq.avg_std_review_stars_91_days_before AS std_review_stars_91_days_before,
    a.std_review_stars_183_days_before - avg_sq.avg_std_review_stars_183_days_before AS std_review_stars_183_days_before,
    a.std_review_stars_365_days_before - avg_sq.avg_std_review_stars_365_days_before AS std_review_stars_365_days_before
   FROM vw_review_stars_dist_1 a
     CROSS JOIN ( SELECT avg(a_1.share_1_star_before) AS avg_share_1_star_before,
            avg(a_1.share_2_star_before) AS avg_share_2_star_before,
            avg(a_1.share_3_star_before) AS avg_share_3_star_before,
            avg(a_1.share_4_star_before) AS avg_share_4_star_before,
            avg(a_1.share_5_star_before) AS avg_share_5_star_before,
            avg(a_1.share_1_star_42_days_before) AS avg_share_1_star_42_days_before,
            avg(a_1.share_2_star_42_days_before) AS avg_share_2_star_42_days_before,
            avg(a_1.share_3_star_42_days_before) AS avg_share_3_star_42_days_before,
            avg(a_1.share_4_star_42_days_before) AS avg_share_4_star_42_days_before,
            avg(a_1.share_5_star_42_days_before) AS avg_share_5_star_42_days_before,
            avg(a_1.share_1_star_56_days_before) AS avg_share_1_star_56_days_before,
            avg(a_1.share_2_star_56_days_before) AS avg_share_2_star_56_days_before,
            avg(a_1.share_3_star_56_days_before) AS avg_share_3_star_56_days_before,
            avg(a_1.share_4_star_56_days_before) AS avg_share_4_star_56_days_before,
            avg(a_1.share_5_star_56_days_before) AS avg_share_5_star_56_days_before,
            avg(a_1.share_1_star_91_days_before) AS avg_share_1_star_91_days_before,
            avg(a_1.share_2_star_91_days_before) AS avg_share_2_star_91_days_before,
            avg(a_1.share_3_star_91_days_before) AS avg_share_3_star_91_days_before,
            avg(a_1.share_4_star_91_days_before) AS avg_share_4_star_91_days_before,
            avg(a_1.share_5_star_91_days_before) AS avg_share_5_star_91_days_before,
            avg(a_1.share_1_star_183_days_before) AS avg_share_1_star_183_days_before,
            avg(a_1.share_2_star_183_days_before) AS avg_share_2_star_183_days_before,
            avg(a_1.share_3_star_183_days_before) AS avg_share_3_star_183_days_before,
            avg(a_1.share_4_star_183_days_before) AS avg_share_4_star_183_days_before,
            avg(a_1.share_5_star_183_days_before) AS avg_share_5_star_183_days_before,
            avg(a_1.share_1_star_365_days_before) AS avg_share_1_star_365_days_before,
            avg(a_1.share_2_star_365_days_before) AS avg_share_2_star_365_days_before,
            avg(a_1.share_3_star_365_days_before) AS avg_share_3_star_365_days_before,
            avg(a_1.share_4_star_365_days_before) AS avg_share_4_star_365_days_before,
            avg(a_1.share_5_star_365_days_before) AS avg_share_5_star_365_days_before,
            avg(a_1.std_review_stars_before) AS avg_std_review_stars_before,
            avg(a_1.std_review_stars_42_days_before) AS avg_std_review_stars_42_days_before,
            avg(a_1.std_review_stars_56_days_before) AS avg_std_review_stars_56_days_before,
            avg(a_1.std_review_stars_91_days_before) AS avg_std_review_stars_91_days_before,
            avg(a_1.std_review_stars_183_days_before) AS avg_std_review_stars_183_days_before,
            avg(a_1.std_review_stars_365_days_before) AS avg_std_review_stars_365_days_before
           FROM vw_review_stars_dist_1 a_1) avg_sq;


CREATE OR REPLACE VIEW vw_prev_insp_values_1 AS 
 SELECT aaa.restaurant_id,
    aaa.date,
    aaa.one_prev_missing,
    aaa.one_one_star,
    aaa.one_two_star,
    aaa.one_three_star,
    aaa.two_prev_missing,
    aaa.two_one_star,
    aaa.two_two_star,
    aaa.two_three_star,
    aaa.three_prev_missing,
    aaa.three_one_star,
    aaa.three_two_star,
    aaa.three_three_star,
    aaa.four_prev_missing,
    aaa.four_one_star,
    aaa.four_two_star,
    aaa.four_three_star,
    aaa.five_prev_missing,
    aaa.five_one_star,
    aaa.five_two_star,
    aaa.five_three_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing) = 2 THEN 0::numeric
            ELSE (aaa.one_one_star + aaa.two_one_star)::numeric * 1.00 / (2 - aaa.one_prev_missing + aaa.two_prev_missing)::numeric
        END AS avg_last_two_one_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing) = 3 THEN 0::numeric
            ELSE (aaa.one_one_star + aaa.two_one_star + aaa.three_one_star)::numeric * 1.00 / (3 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing)::numeric
        END AS avg_last_three_one_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing) = 4 THEN 0::numeric
            ELSE (aaa.one_one_star + aaa.two_one_star + aaa.three_one_star + aaa.four_one_star)::numeric * 1.00 / (4 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing)::numeric
        END AS avg_last_four_one_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing + aaa.five_prev_missing) = 5 THEN 0::numeric
            ELSE (aaa.one_one_star + aaa.two_one_star + aaa.three_one_star + aaa.four_one_star + aaa.five_one_star)::numeric * 1.00 / (5 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing + aaa.five_prev_missing)::numeric
        END AS avg_last_five_one_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing) = 2 THEN 0::numeric
            ELSE (aaa.one_two_star + aaa.two_two_star)::numeric * 1.00 / (2 - aaa.one_prev_missing + aaa.two_prev_missing)::numeric
        END AS avg_last_two_two_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing) = 3 THEN 0::numeric
            ELSE (aaa.one_two_star + aaa.two_two_star + aaa.three_two_star)::numeric * 1.00 / (3 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing)::numeric
        END AS avg_last_three_two_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing) = 4 THEN 0::numeric
            ELSE (aaa.one_two_star + aaa.two_two_star + aaa.three_two_star + aaa.four_two_star)::numeric * 1.00 / (4 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing)::numeric
        END AS avg_last_four_two_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing + aaa.five_prev_missing) = 5 THEN 0::numeric
            ELSE (aaa.one_two_star + aaa.two_two_star + aaa.three_two_star + aaa.four_two_star + aaa.five_two_star)::numeric * 1.00 / (5 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing + aaa.five_prev_missing)::numeric
        END AS avg_last_five_two_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing) = 2 THEN 0::numeric
            ELSE (aaa.one_three_star + aaa.two_three_star)::numeric * 1.00 / (2 - aaa.one_prev_missing + aaa.two_prev_missing)::numeric
        END AS avg_last_two_three_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing) = 3 THEN 0::numeric
            ELSE (aaa.one_three_star + aaa.two_three_star + aaa.three_three_star)::numeric * 1.00 / (3 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing)::numeric
        END AS avg_last_three_three_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing) = 4 THEN 0::numeric
            ELSE (aaa.one_three_star + aaa.two_three_star + aaa.three_three_star + aaa.four_three_star)::numeric * 1.00 / (4 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing)::numeric
        END AS avg_last_four_three_star,
        CASE
            WHEN (aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing + aaa.five_prev_missing) = 5 THEN 0::numeric
            ELSE (aaa.one_three_star + aaa.two_three_star + aaa.three_three_star + aaa.four_three_star + aaa.five_three_star)::numeric * 1.00 / (5 - aaa.one_prev_missing + aaa.two_prev_missing + aaa.three_prev_missing + aaa.four_prev_missing + aaa.five_prev_missing)::numeric
        END AS avg_last_five_three_star,
    GREATEST(aaa.one_one_star, aaa.two_one_star) AS greatest_last_two_one_star,
    GREATEST(aaa.one_one_star, aaa.two_one_star, aaa.three_one_star) AS greatest_last_three_one_star,
    GREATEST(aaa.one_one_star, aaa.two_one_star, aaa.three_one_star, aaa.four_one_star) AS greatest_last_four_one_star,
    GREATEST(aaa.one_one_star, aaa.two_one_star, aaa.three_one_star, aaa.four_one_star, aaa.five_one_star) AS greatest_last_five_one_star,
    GREATEST(aaa.one_two_star, aaa.two_two_star) AS greatest_last_two_two_star,
    GREATEST(aaa.one_two_star, aaa.two_two_star, aaa.three_two_star) AS greatest_last_three_two_star,
    GREATEST(aaa.one_two_star, aaa.two_two_star, aaa.three_two_star, aaa.four_two_star) AS greatest_last_four_two_star,
    GREATEST(aaa.one_two_star, aaa.two_two_star, aaa.three_two_star, aaa.four_two_star, aaa.five_two_star) AS greatest_last_five_two_star,
    GREATEST(aaa.one_three_star, aaa.two_three_star) AS greatest_last_two_three_star,
    GREATEST(aaa.one_three_star, aaa.two_three_star, aaa.three_three_star) AS greatest_last_three_three_star,
    GREATEST(aaa.one_three_star, aaa.two_three_star, aaa.three_three_star, aaa.four_three_star) AS greatest_last_four_three_star,
    GREATEST(aaa.one_three_star, aaa.two_three_star, aaa.three_three_star, aaa.four_three_star, aaa.five_three_star) AS greatest_last_five_three_star,
    LEAST(aaa.one_one_star, aaa.two_one_star) AS least_last_two_one_star,
    LEAST(aaa.one_one_star, aaa.two_one_star, aaa.three_one_star) AS least_last_three_one_star,
    LEAST(aaa.one_one_star, aaa.two_one_star, aaa.three_one_star, aaa.four_one_star) AS least_last_four_one_star,
    LEAST(aaa.one_one_star, aaa.two_one_star, aaa.three_one_star, aaa.four_one_star, aaa.five_one_star) AS least_last_five_one_star,
    LEAST(aaa.one_two_star, aaa.two_two_star) AS least_last_two_two_star,
    LEAST(aaa.one_two_star, aaa.two_two_star, aaa.three_two_star) AS least_last_three_two_star,
    LEAST(aaa.one_two_star, aaa.two_two_star, aaa.three_two_star, aaa.four_two_star) AS least_last_four_two_star,
    LEAST(aaa.one_two_star, aaa.two_two_star, aaa.three_two_star, aaa.four_two_star, aaa.five_two_star) AS least_last_five_two_star,
    LEAST(aaa.one_three_star, aaa.two_three_star) AS least_last_two_three_star,
    LEAST(aaa.one_three_star, aaa.two_three_star, aaa.three_three_star) AS least_last_three_three_star,
    LEAST(aaa.one_three_star, aaa.two_three_star, aaa.three_three_star, aaa.four_three_star) AS least_last_four_three_star,
    LEAST(aaa.one_three_star, aaa.two_three_star, aaa.three_three_star, aaa.four_three_star, aaa.five_three_star) AS least_last_five_three_star
   FROM ( SELECT dims.restaurant_id,
            dims.date,
                CASE
                    WHEN one.one_star IS NULL THEN 1
                    ELSE 0
                END AS one_prev_missing,
                CASE
                    WHEN one.one_star IS NULL THEN NULL::integer
                    ELSE one.one_star
                END AS one_one_star,
                CASE
                    WHEN one.two_star IS NULL THEN NULL::integer
                    ELSE one.two_star
                END AS one_two_star,
                CASE
                    WHEN one.three_star IS NULL THEN NULL::integer
                    ELSE one.three_star
                END AS one_three_star,
                CASE
                    WHEN two.one_star IS NULL THEN 1
                    ELSE 0
                END AS two_prev_missing,
                CASE
                    WHEN two.one_star IS NULL THEN NULL::integer
                    ELSE two.one_star
                END AS two_one_star,
                CASE
                    WHEN two.one_star IS NULL THEN NULL::integer
                    ELSE two.two_star
                END AS two_two_star,
                CASE
                    WHEN two.one_star IS NULL THEN NULL::integer
                    ELSE two.three_star
                END AS two_three_star,
                CASE
                    WHEN three.one_star IS NULL THEN 1
                    ELSE 0
                END AS three_prev_missing,
                CASE
                    WHEN three.one_star IS NULL THEN NULL::integer
                    ELSE three.one_star
                END AS three_one_star,
                CASE
                    WHEN three.one_star IS NULL THEN NULL::integer
                    ELSE three.two_star
                END AS three_two_star,
                CASE
                    WHEN three.one_star IS NULL THEN NULL::integer
                    ELSE three.three_star
                END AS three_three_star,
                CASE
                    WHEN four.one_star IS NULL THEN 1
                    ELSE 0
                END AS four_prev_missing,
                CASE
                    WHEN four.one_star IS NULL THEN NULL::integer
                    ELSE four.one_star
                END AS four_one_star,
                CASE
                    WHEN four.one_star IS NULL THEN NULL::integer
                    ELSE four.two_star
                END AS four_two_star,
                CASE
                    WHEN four.one_star IS NULL THEN NULL::integer
                    ELSE four.three_star
                END AS four_three_star,
                CASE
                    WHEN five.one_star IS NULL THEN 1
                    ELSE 0
                END AS five_prev_missing,
                CASE
                    WHEN five.one_star IS NULL THEN NULL::integer
                    ELSE five.one_star
                END AS five_one_star,
                CASE
                    WHEN five.one_star IS NULL THEN NULL::integer
                    ELSE five.two_star
                END AS five_two_star,
                CASE
                    WHEN five.one_star IS NULL THEN NULL::integer
                    ELSE five.three_star
                END AS five_three_star
           FROM tbl_all_cases dims
             LEFT JOIN ( SELECT a.restaurant_id,
                    a.date AS later_date,
                    a.dataset,
                    b.date AS earlier_date,
                    a.date - b.date AS days_since,
                    b.one_star,
                    b.two_star,
                    b.three_star,
                    rank() OVER (PARTITION BY a.restaurant_id, a.date ORDER BY b.date DESC) AS rank_before
                   FROM tbl_all_cases a
                     JOIN tbl_labelled_cases b ON a.restaurant_id = b.restaurant_id AND a.date > b.date AND (b.date <> ALL (ARRAY['2012-12-30'::date, '2013-12-30'::date]))) one ON dims.restaurant_id = one.restaurant_id AND dims.date = one.later_date AND one.rank_before = 1
             LEFT JOIN ( SELECT a.restaurant_id,
                    a.date AS later_date,
                    a.dataset,
                    b.date AS earlier_date,
                    b.one_star,
                    b.two_star,
                    b.three_star,
                    rank() OVER (PARTITION BY a.restaurant_id, a.date ORDER BY b.date DESC) AS rank_before
                   FROM tbl_all_cases a
                     JOIN tbl_labelled_cases b ON a.restaurant_id = b.restaurant_id AND a.date > b.date AND (b.date <> ALL (ARRAY['2012-12-30'::date, '2013-12-30'::date]))) two ON dims.restaurant_id = two.restaurant_id AND dims.date = two.later_date AND two.rank_before = 2
             LEFT JOIN ( SELECT a.restaurant_id,
                    a.date AS later_date,
                    a.dataset,
                    b.date AS earlier_date,
                    b.one_star,
                    b.two_star,
                    b.three_star,
                    rank() OVER (PARTITION BY a.restaurant_id, a.date ORDER BY b.date DESC) AS rank_before
                   FROM tbl_all_cases a
                     JOIN tbl_labelled_cases b ON a.restaurant_id = b.restaurant_id AND a.date > b.date AND (b.date <> ALL (ARRAY['2012-12-30'::date, '2013-12-30'::date]))) three ON dims.restaurant_id = three.restaurant_id AND dims.date = three.later_date AND three.rank_before = 3
             LEFT JOIN ( SELECT a.restaurant_id,
                    a.date AS later_date,
                    a.dataset,
                    b.date AS earlier_date,
                    b.one_star,
                    b.two_star,
                    b.three_star,
                    rank() OVER (PARTITION BY a.restaurant_id, a.date ORDER BY b.date DESC) AS rank_before
                   FROM tbl_all_cases a
                     JOIN tbl_labelled_cases b ON a.restaurant_id = b.restaurant_id AND a.date > b.date AND (b.date <> ALL (ARRAY['2012-12-30'::date, '2013-12-30'::date]))) four ON dims.restaurant_id = four.restaurant_id AND dims.date = four.later_date AND four.rank_before = 4
             LEFT JOIN ( SELECT a.restaurant_id,
                    a.date AS later_date,
                    a.dataset,
                    b.date AS earlier_date,
                    b.one_star,
                    b.two_star,
                    b.three_star,
                    rank() OVER (PARTITION BY a.restaurant_id, a.date ORDER BY b.date DESC) AS rank_before
                   FROM tbl_all_cases a
                     JOIN tbl_labelled_cases b ON a.restaurant_id = b.restaurant_id AND a.date > b.date AND (b.date <> ALL (ARRAY['2012-12-30'::date, '2013-12-30'::date]))) five ON dims.restaurant_id = five.restaurant_id AND dims.date = five.later_date AND five.rank_before = 5) aaa;


CREATE OR REPLACE VIEW vw_prev_insp_values_zm AS 
 SELECT a.restaurant_id,
    a.date,
    a.one_prev_missing::numeric - avg_sq.avg_one_prev_missing AS one_prev_missing,
    a.one_one_star::numeric - avg_sq.avg_one_one_star AS one_one_star,
    a.one_two_star::numeric - avg_sq.avg_one_two_star AS one_two_star,
    a.one_three_star::numeric - avg_sq.avg_one_three_star AS one_three_star,
    a.two_prev_missing::numeric - avg_sq.avg_two_prev_missing AS two_prev_missing,
    a.two_one_star::numeric - avg_sq.avg_two_one_star AS two_one_star,
    a.two_two_star::numeric - avg_sq.avg_two_two_star AS two_two_star,
    a.two_three_star::numeric - avg_sq.avg_two_three_star AS two_three_star,
    a.three_prev_missing::numeric - avg_sq.avg_three_prev_missing AS three_prev_missing,
    a.three_one_star::numeric - avg_sq.avg_three_one_star AS three_one_star,
    a.three_two_star::numeric - avg_sq.avg_three_two_star AS three_two_star,
    a.three_three_star::numeric - avg_sq.avg_three_three_star AS three_three_star,
    a.four_prev_missing::numeric - avg_sq.avg_four_prev_missing AS four_prev_missing,
    a.four_one_star::numeric - avg_sq.avg_four_one_star AS four_one_star,
    a.four_two_star::numeric - avg_sq.avg_four_two_star AS four_two_star,
    a.four_three_star::numeric - avg_sq.avg_four_three_star AS four_three_star,
    a.five_prev_missing::numeric - avg_sq.avg_five_prev_missing AS five_prev_missing,
    a.five_one_star::numeric - avg_sq.avg_five_one_star AS five_one_star,
    a.five_two_star::numeric - avg_sq.avg_five_two_star AS five_two_star,
    a.five_three_star::numeric - avg_sq.avg_five_three_star AS five_three_star,
    a.avg_last_two_one_star - avg_sq.avg_avg_last_two_one_star AS avg_last_two_one_star,
    a.avg_last_three_one_star - avg_sq.avg_avg_last_three_one_star AS avg_last_three_one_star,
    a.avg_last_four_one_star - avg_sq.avg_avg_last_four_one_star AS avg_last_four_one_star,
    a.avg_last_five_one_star - avg_sq.avg_avg_last_five_one_star AS avg_last_five_one_star,
    a.avg_last_two_two_star - avg_sq.avg_avg_last_two_two_star AS avg_last_two_two_star,
    a.avg_last_three_two_star - avg_sq.avg_avg_last_three_two_star AS avg_last_three_two_star,
    a.avg_last_four_two_star - avg_sq.avg_avg_last_four_two_star AS avg_last_four_two_star,
    a.avg_last_five_two_star - avg_sq.avg_avg_last_five_two_star AS avg_last_five_two_star,
    a.avg_last_two_three_star - avg_sq.avg_avg_last_two_three_star AS avg_last_two_three_star,
    a.avg_last_three_three_star - avg_sq.avg_avg_last_three_three_star AS avg_last_three_three_star,
    a.avg_last_four_three_star - avg_sq.avg_avg_last_four_three_star AS avg_last_four_three_star,
    a.avg_last_five_three_star - avg_sq.avg_avg_last_five_three_star AS avg_last_five_three_star,
    a.greatest_last_two_one_star::numeric - avg_sq.avg_greatest_last_two_one_star AS greatest_last_two_one_star,
    a.greatest_last_three_one_star::numeric - avg_sq.avg_greatest_last_three_one_star AS greatest_last_three_one_star,
    a.greatest_last_four_one_star::numeric - avg_sq.avg_greatest_last_four_one_star AS greatest_last_four_one_star,
    a.greatest_last_five_one_star::numeric - avg_sq.avg_greatest_last_five_one_star AS greatest_last_five_one_star,
    a.greatest_last_two_two_star::numeric - avg_sq.avg_greatest_last_two_two_star AS greatest_last_two_two_star,
    a.greatest_last_three_two_star::numeric - avg_sq.avg_greatest_last_three_two_star AS greatest_last_three_two_star,
    a.greatest_last_four_two_star::numeric - avg_sq.avg_greatest_last_four_two_star AS greatest_last_four_two_star,
    a.greatest_last_five_two_star::numeric - avg_sq.avg_greatest_last_five_two_star AS greatest_last_five_two_star,
    a.greatest_last_two_three_star::numeric - avg_sq.avg_greatest_last_two_three_star AS greatest_last_two_three_star,
    a.greatest_last_three_three_star::numeric - avg_sq.avg_greatest_last_three_three_star AS greatest_last_three_three_star,
    a.greatest_last_four_three_star::numeric - avg_sq.avg_greatest_last_four_three_star AS greatest_last_four_three_star,
    a.greatest_last_five_three_star::numeric - avg_sq.avg_greatest_last_five_three_star AS greatest_last_five_three_star,
    a.least_last_two_one_star::numeric - avg_sq.avg_least_last_two_one_star AS least_last_two_one_star,
    a.least_last_three_one_star::numeric - avg_sq.avg_least_last_three_one_star AS least_last_three_one_star,
    a.least_last_four_one_star::numeric - avg_sq.avg_least_last_four_one_star AS least_last_four_one_star,
    a.least_last_five_one_star::numeric - avg_sq.avg_least_last_five_one_star AS least_last_five_one_star,
    a.least_last_two_two_star::numeric - avg_sq.avg_least_last_two_two_star AS least_last_two_two_star,
    a.least_last_three_two_star::numeric - avg_sq.avg_least_last_three_two_star AS least_last_three_two_star,
    a.least_last_four_two_star::numeric - avg_sq.avg_least_last_four_two_star AS least_last_four_two_star,
    a.least_last_five_two_star::numeric - avg_sq.avg_least_last_five_two_star AS least_last_five_two_star,
    a.least_last_two_three_star::numeric - avg_sq.avg_least_last_two_three_star AS least_last_two_three_star,
    a.least_last_three_three_star::numeric - avg_sq.avg_least_last_three_three_star AS least_last_three_three_star,
    a.least_last_four_three_star::numeric - avg_sq.avg_least_last_four_three_star AS least_last_four_three_star,
    a.least_last_five_three_star::numeric - avg_sq.avg_least_last_five_three_star AS least_last_five_three_star
   FROM vw_prev_insp_values_1 a
     CROSS JOIN ( SELECT avg(a_1.one_prev_missing) AS avg_one_prev_missing,
            avg(a_1.one_one_star) AS avg_one_one_star,
            avg(a_1.one_two_star) AS avg_one_two_star,
            avg(a_1.one_three_star) AS avg_one_three_star,
            avg(a_1.two_prev_missing) AS avg_two_prev_missing,
            avg(a_1.two_one_star) AS avg_two_one_star,
            avg(a_1.two_two_star) AS avg_two_two_star,
            avg(a_1.two_three_star) AS avg_two_three_star,
            avg(a_1.three_prev_missing) AS avg_three_prev_missing,
            avg(a_1.three_one_star) AS avg_three_one_star,
            avg(a_1.three_two_star) AS avg_three_two_star,
            avg(a_1.three_three_star) AS avg_three_three_star,
            avg(a_1.four_prev_missing) AS avg_four_prev_missing,
            avg(a_1.four_one_star) AS avg_four_one_star,
            avg(a_1.four_two_star) AS avg_four_two_star,
            avg(a_1.four_three_star) AS avg_four_three_star,
            avg(a_1.five_prev_missing) AS avg_five_prev_missing,
            avg(a_1.five_one_star) AS avg_five_one_star,
            avg(a_1.five_two_star) AS avg_five_two_star,
            avg(a_1.five_three_star) AS avg_five_three_star,
            avg(a_1.avg_last_two_one_star) AS avg_avg_last_two_one_star,
            avg(a_1.avg_last_three_one_star) AS avg_avg_last_three_one_star,
            avg(a_1.avg_last_four_one_star) AS avg_avg_last_four_one_star,
            avg(a_1.avg_last_five_one_star) AS avg_avg_last_five_one_star,
            avg(a_1.avg_last_two_two_star) AS avg_avg_last_two_two_star,
            avg(a_1.avg_last_three_two_star) AS avg_avg_last_three_two_star,
            avg(a_1.avg_last_four_two_star) AS avg_avg_last_four_two_star,
            avg(a_1.avg_last_five_two_star) AS avg_avg_last_five_two_star,
            avg(a_1.avg_last_two_three_star) AS avg_avg_last_two_three_star,
            avg(a_1.avg_last_three_three_star) AS avg_avg_last_three_three_star,
            avg(a_1.avg_last_four_three_star) AS avg_avg_last_four_three_star,
            avg(a_1.avg_last_five_three_star) AS avg_avg_last_five_three_star,
            avg(a_1.greatest_last_two_one_star) AS avg_greatest_last_two_one_star,
            avg(a_1.greatest_last_three_one_star) AS avg_greatest_last_three_one_star,
            avg(a_1.greatest_last_four_one_star) AS avg_greatest_last_four_one_star,
            avg(a_1.greatest_last_five_one_star) AS avg_greatest_last_five_one_star,
            avg(a_1.greatest_last_two_two_star) AS avg_greatest_last_two_two_star,
            avg(a_1.greatest_last_three_two_star) AS avg_greatest_last_three_two_star,
            avg(a_1.greatest_last_four_two_star) AS avg_greatest_last_four_two_star,
            avg(a_1.greatest_last_five_two_star) AS avg_greatest_last_five_two_star,
            avg(a_1.greatest_last_two_three_star) AS avg_greatest_last_two_three_star,
            avg(a_1.greatest_last_three_three_star) AS avg_greatest_last_three_three_star,
            avg(a_1.greatest_last_four_three_star) AS avg_greatest_last_four_three_star,
            avg(a_1.greatest_last_five_three_star) AS avg_greatest_last_five_three_star,
            avg(a_1.least_last_two_one_star) AS avg_least_last_two_one_star,
            avg(a_1.least_last_three_one_star) AS avg_least_last_three_one_star,
            avg(a_1.least_last_four_one_star) AS avg_least_last_four_one_star,
            avg(a_1.least_last_five_one_star) AS avg_least_last_five_one_star,
            avg(a_1.least_last_two_two_star) AS avg_least_last_two_two_star,
            avg(a_1.least_last_three_two_star) AS avg_least_last_three_two_star,
            avg(a_1.least_last_four_two_star) AS avg_least_last_four_two_star,
            avg(a_1.least_last_five_two_star) AS avg_least_last_five_two_star,
            avg(a_1.least_last_two_three_star) AS avg_least_last_two_three_star,
            avg(a_1.least_last_three_three_star) AS avg_least_last_three_three_star,
            avg(a_1.least_last_four_three_star) AS avg_least_last_four_three_star,
            avg(a_1.least_last_five_three_star) AS avg_least_last_five_three_star
           FROM vw_prev_insp_values_1 a_1) avg_sq;


CREATE OR REPLACE VIEW vw_amt_20150702_v02 AS 
 SELECT a.restaurant_id,
    a.id,
    a.date,
    a.one_star,
    a.two_star,
    a.three_star,
    a.dataset,
        CASE
            WHEN date_part('dow'::text, a.date) = 0::double precision THEN 1
            ELSE 0
        END AS day_of_week_0_dummy,
        CASE
            WHEN date_part('dow'::text, a.date) = 1::double precision THEN 1
            ELSE 0
        END AS day_of_week_1_dummy,
        CASE
            WHEN date_part('dow'::text, a.date) = 2::double precision THEN 1
            ELSE 0
        END AS day_of_week_2_dummy,
        CASE
            WHEN date_part('dow'::text, a.date) = 3::double precision THEN 1
            ELSE 0
        END AS day_of_week_3_dummy,
        CASE
            WHEN date_part('dow'::text, a.date) = 4::double precision THEN 1
            ELSE 0
        END AS day_of_week_4_dummy,
        CASE
            WHEN date_part('dow'::text, a.date) = 5::double precision THEN 1
            ELSE 0
        END AS day_of_week_5_dummy,
        CASE
            WHEN date_part('dow'::text, a.date) = 6::double precision THEN 1
            ELSE 0
        END AS day_of_week_6_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 1::double precision THEN 1
            ELSE 0
        END AS month_1_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 2::double precision THEN 1
            ELSE 0
        END AS month_2_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 3::double precision THEN 1
            ELSE 0
        END AS month_3_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 4::double precision THEN 1
            ELSE 0
        END AS month_4_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 5::double precision THEN 1
            ELSE 0
        END AS month_5_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 6::double precision THEN 1
            ELSE 0
        END AS month_6_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 7::double precision THEN 1
            ELSE 0
        END AS month_7_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 8::double precision THEN 1
            ELSE 0
        END AS month_8_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 9::double precision THEN 1
            ELSE 0
        END AS month_9_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 10::double precision THEN 1
            ELSE 0
        END AS month_10_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 11::double precision THEN 1
            ELSE 0
        END AS month_11_dummy,
        CASE
            WHEN date_part('month'::text, a.date) = 12::double precision THEN 1
            ELSE 0
        END AS month_12_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 1::double precision THEN 1
            ELSE 0
        END AS week_1_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 2::double precision THEN 1
            ELSE 0
        END AS week_2_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 3::double precision THEN 1
            ELSE 0
        END AS week_3_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 4::double precision THEN 1
            ELSE 0
        END AS week_4_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 5::double precision THEN 1
            ELSE 0
        END AS week_5_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 6::double precision THEN 1
            ELSE 0
        END AS week_6_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 7::double precision THEN 1
            ELSE 0
        END AS week_7_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 8::double precision THEN 1
            ELSE 0
        END AS week_8_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 9::double precision THEN 1
            ELSE 0
        END AS week_9_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 10::double precision THEN 1
            ELSE 0
        END AS week_10_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 11::double precision THEN 1
            ELSE 0
        END AS week_11_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 12::double precision THEN 1
            ELSE 0
        END AS week_12_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 13::double precision THEN 1
            ELSE 0
        END AS week_13_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 14::double precision THEN 1
            ELSE 0
        END AS week_14_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 15::double precision THEN 1
            ELSE 0
        END AS week_15_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 16::double precision THEN 1
            ELSE 0
        END AS week_16_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 17::double precision THEN 1
            ELSE 0
        END AS week_17_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 18::double precision THEN 1
            ELSE 0
        END AS week_18_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 19::double precision THEN 1
            ELSE 0
        END AS week_19_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 20::double precision THEN 1
            ELSE 0
        END AS week_20_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 21::double precision THEN 1
            ELSE 0
        END AS week_21_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 22::double precision THEN 1
            ELSE 0
        END AS week_22_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 23::double precision THEN 1
            ELSE 0
        END AS week_23_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 24::double precision THEN 1
            ELSE 0
        END AS week_24_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 25::double precision THEN 1
            ELSE 0
        END AS week_25_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 26::double precision THEN 1
            ELSE 0
        END AS week_26_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 27::double precision THEN 1
            ELSE 0
        END AS week_27_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 28::double precision THEN 1
            ELSE 0
        END AS week_28_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 29::double precision THEN 1
            ELSE 0
        END AS week_29_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 30::double precision THEN 1
            ELSE 0
        END AS week_30_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 31::double precision THEN 1
            ELSE 0
        END AS week_31_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 32::double precision THEN 1
            ELSE 0
        END AS week_32_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 33::double precision THEN 1
            ELSE 0
        END AS week_33_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 34::double precision THEN 1
            ELSE 0
        END AS week_34_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 35::double precision THEN 1
            ELSE 0
        END AS week_35_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 36::double precision THEN 1
            ELSE 0
        END AS week_36_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 37::double precision THEN 1
            ELSE 0
        END AS week_37_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 38::double precision THEN 1
            ELSE 0
        END AS week_38_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 39::double precision THEN 1
            ELSE 0
        END AS week_39_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 40::double precision THEN 1
            ELSE 0
        END AS week_40_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 41::double precision THEN 1
            ELSE 0
        END AS week_41_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 42::double precision THEN 1
            ELSE 0
        END AS week_42_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 43::double precision THEN 1
            ELSE 0
        END AS week_43_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 44::double precision THEN 1
            ELSE 0
        END AS week_44_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 45::double precision THEN 1
            ELSE 0
        END AS week_45_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 46::double precision THEN 1
            ELSE 0
        END AS week_46_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 47::double precision THEN 1
            ELSE 0
        END AS week_47_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 48::double precision THEN 1
            ELSE 0
        END AS week_48_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 49::double precision THEN 1
            ELSE 0
        END AS week_49_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 50::double precision THEN 1
            ELSE 0
        END AS week_50_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 51::double precision THEN 1
            ELSE 0
        END AS week_51_dummy,
        CASE
            WHEN date_part('week'::text, a.date) = 52::double precision THEN 1
            ELSE 0
        END AS week_52_dummy,
        CASE
            WHEN date_part('year'::text, a.date) = 2006::double precision THEN 1
            ELSE 0
        END AS year_2006,
        CASE
            WHEN date_part('year'::text, a.date) = 2007::double precision THEN 1
            ELSE 0
        END AS year_2007,
        CASE
            WHEN date_part('year'::text, a.date) = 2008::double precision THEN 1
            ELSE 0
        END AS year_2008,
        CASE
            WHEN date_part('year'::text, a.date) = 2009::double precision THEN 1
            ELSE 0
        END AS year_2009,
        CASE
            WHEN date_part('year'::text, a.date) = 2010::double precision THEN 1
            ELSE 0
        END AS year_2010,
        CASE
            WHEN date_part('year'::text, a.date) = 2011::double precision THEN 1
            ELSE 0
        END AS year_2011,
        CASE
            WHEN date_part('year'::text, a.date) = 2012::double precision THEN 1
            ELSE 0
        END AS year_2012,
        CASE
            WHEN date_part('year'::text, a.date) = 2013::double precision THEN 1
            ELSE 0
        END AS year_2013,
        CASE
            WHEN date_part('year'::text, a.date) = 2014::double precision THEN 1
            ELSE 0
        END AS year_2014,
        CASE
            WHEN date_part('year'::text, a.date) = 2015::double precision THEN 1
            ELSE 0
        END AS year_2015,
        CASE
            WHEN date_part('days'::text, a.date) = 1::double precision THEN 1
            ELSE 0
        END AS day_of_month_1_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 2::double precision THEN 1
            ELSE 0
        END AS day_of_month_2_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 3::double precision THEN 1
            ELSE 0
        END AS day_of_month_3_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 4::double precision THEN 1
            ELSE 0
        END AS day_of_month_4_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 5::double precision THEN 1
            ELSE 0
        END AS day_of_month_5_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 6::double precision THEN 1
            ELSE 0
        END AS day_of_month_6_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 7::double precision THEN 1
            ELSE 0
        END AS day_of_month_7_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 8::double precision THEN 1
            ELSE 0
        END AS day_of_month_8_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 9::double precision THEN 1
            ELSE 0
        END AS day_of_month_9_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 10::double precision THEN 1
            ELSE 0
        END AS day_of_month_10_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 11::double precision THEN 1
            ELSE 0
        END AS day_of_month_11_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 12::double precision THEN 1
            ELSE 0
        END AS day_of_month_12_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 13::double precision THEN 1
            ELSE 0
        END AS day_of_month_13_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 14::double precision THEN 1
            ELSE 0
        END AS day_of_month_14_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 15::double precision THEN 1
            ELSE 0
        END AS day_of_month_15_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 16::double precision THEN 1
            ELSE 0
        END AS day_of_month_16_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 17::double precision THEN 1
            ELSE 0
        END AS day_of_month_17_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 18::double precision THEN 1
            ELSE 0
        END AS day_of_month_18_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 19::double precision THEN 1
            ELSE 0
        END AS day_of_month_19_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 20::double precision THEN 1
            ELSE 0
        END AS day_of_month_20_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 21::double precision THEN 1
            ELSE 0
        END AS day_of_month_21_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 22::double precision THEN 1
            ELSE 0
        END AS day_of_month_22_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 23::double precision THEN 1
            ELSE 0
        END AS day_of_month_23_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 24::double precision THEN 1
            ELSE 0
        END AS day_of_month_24_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 25::double precision THEN 1
            ELSE 0
        END AS day_of_month_25_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 26::double precision THEN 1
            ELSE 0
        END AS day_of_month_26_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 27::double precision THEN 1
            ELSE 0
        END AS day_of_month_27_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 28::double precision THEN 1
            ELSE 0
        END AS day_of_month_28_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 29::double precision THEN 1
            ELSE 0
        END AS day_of_month_29_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 30::double precision THEN 1
            ELSE 0
        END AS day_of_month_30_dummy,
        CASE
            WHEN date_part('days'::text, a.date) = 31::double precision THEN 1
            ELSE 0
        END AS day_of_month_31_dummy,
        CASE
            WHEN a.date = '2012-12-30'::date THEN 1
            ELSE 0
        END AS dummy_2012_12_30_dummy,
        CASE
            WHEN a.date = '2013-12-30'::date THEN 1
            ELSE 0
        END AS dummy_2013_12_30_dummy,
    COALESCE(map_ids.num_yelp_ids, 0::bigint) AS num_yelp_ids,
    COALESCE(vc.sum_checkins, 0::double precision) AS sum_checkins,
    COALESCE(vc.sum_monday_checkins, 0::double precision) AS sum_monday_checkins,
    COALESCE(vc.sum_tuesday_checkins, 0::double precision) AS sum_tuesday_checkins,
    COALESCE(vc.sum_wednesday_checkins, 0::double precision) AS sum_wednesday_checkins,
    COALESCE(vc.sum_thursday_checkins, 0::double precision) AS sum_thursday_checkins,
    COALESCE(vc.sum_friday_checkins, 0::double precision) AS sum_friday_checkins,
    COALESCE(vc.sum_saturday_checkins, 0::double precision) AS sum_saturday_checkins,
    COALESCE(vc.sum_sunday_checkins, 0::double precision) AS sum_sunday_checkins,
    COALESCE(vc.sum_checkins_0, 0::double precision) AS sum_checkins_0,
    COALESCE(vc.sum_checkins_1, 0::double precision) AS sum_checkins_1,
    COALESCE(vc.sum_checkins_2, 0::double precision) AS sum_checkins_2,
    COALESCE(vc.sum_checkins_3, 0::double precision) AS sum_checkins_3,
    COALESCE(vc.sum_checkins_4, 0::double precision) AS sum_checkins_4,
    COALESCE(vc.sum_checkins_5, 0::double precision) AS sum_checkins_5,
    COALESCE(vc.sum_checkins_6, 0::double precision) AS sum_checkins_6,
    COALESCE(vc.sum_checkins_7, 0::double precision) AS sum_checkins_7,
    COALESCE(vc.sum_checkins_8, 0::double precision) AS sum_checkins_8,
    COALESCE(vc.sum_checkins_9, 0::double precision) AS sum_checkins_9,
    COALESCE(vc.sum_checkins_10, 0::double precision) AS sum_checkins_10,
    COALESCE(vc.sum_checkins_11, 0::double precision) AS sum_checkins_11,
    COALESCE(vc.sum_checkins_12, 0::double precision) AS sum_checkins_12,
    COALESCE(vc.sum_checkins_13, 0::double precision) AS sum_checkins_13,
    COALESCE(vc.sum_checkins_14, 0::double precision) AS sum_checkins_14,
    COALESCE(vc.sum_checkins_15, 0::double precision) AS sum_checkins_15,
    COALESCE(vc.sum_checkins_16, 0::double precision) AS sum_checkins_16,
    COALESCE(vc.sum_checkins_17, 0::double precision) AS sum_checkins_17,
    COALESCE(vc.sum_checkins_18, 0::double precision) AS sum_checkins_18,
    COALESCE(vc.sum_checkins_19, 0::double precision) AS sum_checkins_19,
    COALESCE(vc.sum_checkins_20, 0::double precision) AS sum_checkins_20,
    COALESCE(vc.sum_checkins_21, 0::double precision) AS sum_checkins_21,
    COALESCE(vc.sum_checkins_22, 0::double precision) AS sum_checkins_22,
    COALESCE(vc.sum_checkins_23, 0::double precision) AS sum_checkins_23,
    COALESCE(vc.share_checkins_0, 0::double precision) AS share_checkins_0,
    COALESCE(vc.share_checkins_1, 0::double precision) AS share_checkins_1,
    COALESCE(vc.share_checkins_2, 0::double precision) AS share_checkins_2,
    COALESCE(vc.share_checkins_3, 0::double precision) AS share_checkins_3,
    COALESCE(vc.share_checkins_4, 0::double precision) AS share_checkins_4,
    COALESCE(vc.share_checkins_5, 0::double precision) AS share_checkins_5,
    COALESCE(vc.share_checkins_6, 0::double precision) AS share_checkins_6,
    COALESCE(vc.share_checkins_7, 0::double precision) AS share_checkins_7,
    COALESCE(vc.share_checkins_8, 0::double precision) AS share_checkins_8,
    COALESCE(vc.share_checkins_9, 0::double precision) AS share_checkins_9,
    COALESCE(vc.share_checkins_10, 0::double precision) AS share_checkins_10,
    COALESCE(vc.share_checkins_11, 0::double precision) AS share_checkins_11,
    COALESCE(vc.share_checkins_12, 0::double precision) AS share_checkins_12,
    COALESCE(vc.share_checkins_13, 0::double precision) AS share_checkins_13,
    COALESCE(vc.share_checkins_14, 0::double precision) AS share_checkins_14,
    COALESCE(vc.share_checkins_15, 0::double precision) AS share_checkins_15,
    COALESCE(vc.share_checkins_16, 0::double precision) AS share_checkins_16,
    COALESCE(vc.share_checkins_17, 0::double precision) AS share_checkins_17,
    COALESCE(vc.share_checkins_18, 0::double precision) AS share_checkins_18,
    COALESCE(vc.share_checkins_19, 0::double precision) AS share_checkins_19,
    COALESCE(vc.share_checkins_20, 0::double precision) AS share_checkins_20,
    COALESCE(vc.share_checkins_21, 0::double precision) AS share_checkins_21,
    COALESCE(vc.share_checkins_22, 0::double precision) AS share_checkins_22,
    COALESCE(vc.share_checkins_23, 0::double precision) AS share_checkins_23,
    COALESCE(vc.share_checkins_0_2, 0::double precision) AS share_checkins_0_2,
    COALESCE(vc.share_checkins_3_5, 0::double precision) AS share_checkins_3_5,
    COALESCE(vc.share_checkins_6_8, 0::double precision) AS share_checkins_6_8,
    COALESCE(vc.share_checkins_9_11, 0::double precision) AS share_checkins_9_11,
    COALESCE(vc.share_checkins_12_14, 0::double precision) AS share_checkins_12_14,
    COALESCE(vc.share_checkins_15_17, 0::double precision) AS share_checkins_15_17,
    COALESCE(vc.share_checkins_18_20, 0::double precision) AS share_checkins_18_20,
    COALESCE(vc.share_checkins_21_23, 0::double precision) AS share_checkins_21_23,
    COALESCE(vc.share_checkins_monday, 0::double precision) AS share_checkins_monday,
    COALESCE(vc.share_checkins_tuesday, 0::double precision) AS share_checkins_tuesday,
    COALESCE(vc.share_checkins_wednesday, 0::double precision) AS share_checkins_wednesday,
    COALESCE(vc.share_checkins_thursday, 0::double precision) AS share_checkins_thursday,
    COALESCE(vc.share_checkins_friday, 0::double precision) AS share_checkins_friday,
    COALESCE(vc.share_checkins_saturday, 0::double precision) AS share_checkins_saturday,
    COALESCE(vc.share_checkins_sunday, 0::double precision) AS share_checkins_sunday,
    COALESCE(vc.share_checkins_weekends, 0::double precision) AS share_checkins_weekends,
        CASE
            WHEN vc.sum_checkins IS NULL THEN 1
            ELSE 0
        END AS n_checkins,
    COALESCE(vb.latitude, 0::double precision) AS latitude,
    COALESCE(vb.longitude, 0::double precision) AS longitude,
    COALESCE(vb.review_count, 0::double precision) AS review_count,
    COALESCE(vb.stars, 0::double precision) AS stars,
    COALESCE(vb.neighborhoods_allston_brighton, 0::double precision) AS neighborhoods_allston_brighton,
    COALESCE(vb.neighborhoods_back_bay, 0::double precision) AS neighborhoods_back_bay,
    COALESCE(vb.neighborhoods_beacon_hill, 0::double precision) AS neighborhoods_beacon_hill,
    COALESCE(vb.neighborhoods_charlestown, 0::double precision) AS neighborhoods_charlestown,
    COALESCE(vb.neighborhoods_chinatown, 0::double precision) AS neighborhoods_chinatown,
    COALESCE(vb.neighborhoods_dorchester, 0::double precision) AS neighborhoods_dorchester,
    COALESCE(vb.neighborhoods_downtown, 0::double precision) AS neighborhoods_downtown,
    COALESCE(vb.neighborhoods_dudley_square, 0::double precision) AS neighborhoods_dudley_square,
    COALESCE(vb.neighborhoods_east_boston, 0::double precision) AS neighborhoods_east_boston,
    COALESCE(vb.neighborhoods_fenway, 0::double precision) AS neighborhoods_fenway,
    COALESCE(vb.neighborhoods_financial_district, 0::double precision) AS neighborhoods_financial_district,
    COALESCE(vb.neighborhoods_hyde_park, 0::double precision) AS neighborhoods_hyde_park,
    COALESCE(vb.neighborhoods_jamaica_plain, 0::double precision) AS neighborhoods_jamaica_plain,
    COALESCE(vb.neighborhoods_leather_district, 0::double precision) AS neighborhoods_leather_district,
    COALESCE(vb.neighborhoods_mattapan, 0::double precision) AS neighborhoods_mattapan,
    COALESCE(vb.neighborhoods_mission_hill, 0::double precision) AS neighborhoods_mission_hill,
    COALESCE(vb.neighborhoods_north_end, 0::double precision) AS neighborhoods_north_end,
    COALESCE(vb.neighborhoods_roslindale, 0::double precision) AS neighborhoods_roslindale,
    COALESCE(vb.neighborhoods_roslindale_village, 0::double precision) AS neighborhoods_roslindale_village,
    COALESCE(vb.neighborhoods_south_boston, 0::double precision) AS neighborhoods_south_boston,
    COALESCE(vb.neighborhoods_south_end, 0::double precision) AS neighborhoods_south_end,
    COALESCE(vb.neighborhoods_waterfront, 0::double precision) AS neighborhoods_waterfront,
    COALESCE(vb.neighborhoods_west_roxbury, 0::double precision) AS neighborhoods_west_roxbury,
    COALESCE(vb.neighborhoods_west_roxbury_center, 0::double precision) AS neighborhoods_west_roxbury_center,
    COALESCE(vb.neighborhoods_sum, 0::double precision) AS neighborhoods_sum,
    COALESCE(vb.categories_american_new_, 0::double precision) AS categories_american_new_,
    COALESCE(vb.categories_american_traditional_, 0::double precision) AS categories_american_traditional_,
    COALESCE(vb.categories_arts__entertainment, 0::double precision) AS categories_arts__entertainment,
    COALESCE(vb.categories_asian_fusion, 0::double precision) AS categories_asian_fusion,
    COALESCE(vb.categories_bagels, 0::double precision) AS categories_bagels,
    COALESCE(vb.categories_bakeries, 0::double precision) AS categories_bakeries,
    COALESCE(vb.categories_barbeque, 0::double precision) AS categories_barbeque,
    COALESCE(vb.categories_bars, 0::double precision) AS categories_bars,
    COALESCE(vb.categories_brazilian, 0::double precision) AS categories_brazilian,
    COALESCE(vb.categories_breakfast__brunch, 0::double precision) AS categories_breakfast__brunch,
    COALESCE(vb.categories_burgers, 0::double precision) AS categories_burgers,
    COALESCE(vb.categories_cafes, 0::double precision) AS categories_cafes,
    COALESCE(vb.categories_caribbean, 0::double precision) AS categories_caribbean,
    COALESCE(vb.categories_caterers, 0::double precision) AS categories_caterers,
    COALESCE(vb.categories_chicken_wings, 0::double precision) AS categories_chicken_wings,
    COALESCE(vb.categories_chinese, 0::double precision) AS categories_chinese,
    COALESCE(vb.categories_coffee__tea, 0::double precision) AS categories_coffee__tea,
    COALESCE(vb.categories_dance_clubs, 0::double precision) AS categories_dance_clubs,
    COALESCE(vb.categories_delis, 0::double precision) AS categories_delis,
    COALESCE(vb.categories_desserts, 0::double precision) AS categories_desserts,
    COALESCE(vb.categories_dim_sum, 0::double precision) AS categories_dim_sum,
    COALESCE(vb.categories_diners, 0::double precision) AS categories_diners,
    COALESCE(vb.categories_dive_bars, 0::double precision) AS categories_dive_bars,
    COALESCE(vb.categories_donuts, 0::double precision) AS categories_donuts,
    COALESCE(vb.categories_event_planning__services, 0::double precision) AS categories_event_planning__services,
    COALESCE(vb.categories_fast_food, 0::double precision) AS categories_fast_food,
    COALESCE(vb.categories_food, 0::double precision) AS categories_food,
    COALESCE(vb.categories_food_stands, 0::double precision) AS categories_food_stands,
    COALESCE(vb.categories_french, 0::double precision) AS categories_french,
    COALESCE(vb.categories_gay_bars, 0::double precision) AS categories_gay_bars,
    COALESCE(vb.categories_gluten_free, 0::double precision) AS categories_gluten_free,
    COALESCE(vb.categories_greek, 0::double precision) AS categories_greek,
    COALESCE(vb.categories_grocery, 0::double precision) AS categories_grocery,
    COALESCE(vb.categories_halal, 0::double precision) AS categories_halal,
    COALESCE(vb.categories_hot_dogs, 0::double precision) AS categories_hot_dogs,
    COALESCE(vb.categories_hotels, 0::double precision) AS categories_hotels,
    COALESCE(vb.categories_hotels__travel, 0::double precision) AS categories_hotels__travel,
    COALESCE(vb.categories_ice_cream__frozen_yogurt, 0::double precision) AS categories_ice_cream__frozen_yogurt,
    COALESCE(vb.categories_indian, 0::double precision) AS categories_indian,
    COALESCE(vb.categories_irish, 0::double precision) AS categories_irish,
    COALESCE(vb.categories_italian, 0::double precision) AS categories_italian,
    COALESCE(vb.categories_japanese, 0::double precision) AS categories_japanese,
    COALESCE(vb.categories_jazz__blues, 0::double precision) AS categories_jazz__blues,
    COALESCE(vb.categories_juice_bars__smoothies, 0::double precision) AS categories_juice_bars__smoothies,
    COALESCE(vb.categories_korean, 0::double precision) AS categories_korean,
    COALESCE(vb.categories_latin_american, 0::double precision) AS categories_latin_american,
    COALESCE(vb.categories_lounges, 0::double precision) AS categories_lounges,
    COALESCE(vb.categories_mediterranean, 0::double precision) AS categories_mediterranean,
    COALESCE(vb.categories_mexican, 0::double precision) AS categories_mexican,
    COALESCE(vb.categories_middle_eastern, 0::double precision) AS categories_middle_eastern,
    COALESCE(vb.categories_music_venues, 0::double precision) AS categories_music_venues,
    COALESCE(vb.categories_nightlife, 0::double precision) AS categories_nightlife,
    COALESCE(vb.categories_pizza, 0::double precision) AS categories_pizza,
    COALESCE(vb.categories_pubs, 0::double precision) AS categories_pubs,
    COALESCE(vb.categories_restaurants, 0::double precision) AS categories_restaurants,
    COALESCE(vb.categories_salad, 0::double precision) AS categories_salad,
    COALESCE(vb.categories_sandwiches, 0::double precision) AS categories_sandwiches,
    COALESCE(vb.categories_seafood, 0::double precision) AS categories_seafood,
    COALESCE(vb.categories_shopping, 0::double precision) AS categories_shopping,
    COALESCE(vb.categories_soul_food, 0::double precision) AS categories_soul_food,
    COALESCE(vb.categories_soup, 0::double precision) AS categories_soup,
    COALESCE(vb.categories_southern, 0::double precision) AS categories_southern,
    COALESCE(vb.categories_spanish, 0::double precision) AS categories_spanish,
    COALESCE(vb.categories_specialty_food, 0::double precision) AS categories_specialty_food,
    COALESCE(vb.categories_sports_bars, 0::double precision) AS categories_sports_bars,
    COALESCE(vb.categories_steakhouses, 0::double precision) AS categories_steakhouses,
    COALESCE(vb.categories_sushi_bars, 0::double precision) AS categories_sushi_bars,
    COALESCE(vb.categories_taiwanese, 0::double precision) AS categories_taiwanese,
    COALESCE(vb.categories_tapas_bars, 0::double precision) AS categories_tapas_bars,
    COALESCE(vb.categories_tex_mex, 0::double precision) AS categories_tex_mex,
    COALESCE(vb.categories_thai, 0::double precision) AS categories_thai,
    COALESCE(vb.categories_vegan, 0::double precision) AS categories_vegan,
    COALESCE(vb.categories_vegetarian, 0::double precision) AS categories_vegetarian,
    COALESCE(vb.categories_venues__event_spaces, 0::double precision) AS categories_venues__event_spaces,
    COALESCE(vb.categories_vietnamese, 0::double precision) AS categories_vietnamese,
    COALESCE(vb.categories_wine_bars, 0::double precision) AS categories_wine_bars,
    COALESCE(vb.categories_sum, 0::double precision) AS categories_sum,
    COALESCE(vb.city_allston, 0::double precision) AS city_allston,
    COALESCE(vb.city_boston, 0::double precision) AS city_boston,
    COALESCE(vb.city_brighton, 0::double precision) AS city_brighton,
    COALESCE(vb.city_charlestown, 0::double precision) AS city_charlestown,
    COALESCE(vb.city_dorchester, 0::double precision) AS city_dorchester,
    COALESCE(vb.city_dorchester_center, 0::double precision) AS city_dorchester_center,
    COALESCE(vb.city_east_boston, 0::double precision) AS city_east_boston,
    COALESCE(vb.city_hyde_park, 0::double precision) AS city_hyde_park,
    COALESCE(vb.city_jamaica_plain, 0::double precision) AS city_jamaica_plain,
    COALESCE(vb.city_roslindale, 0::double precision) AS city_roslindale,
    COALESCE(vb.city_roxbury, 0::double precision) AS city_roxbury,
    COALESCE(vb.city_roxbury_crossing, 0::double precision) AS city_roxbury_crossing,
    COALESCE(vb.city_south_boston, 0::double precision) AS city_south_boston,
    COALESCE(vb.city_west_roxbury, 0::double precision) AS city_west_roxbury,
    COALESCE(vb.city_sum, 0::double precision) AS city_sum,
    COALESCE(vb.open_true, 0::double precision) AS open_true,
    COALESCE(vb.accepts_credit_cards, 0::double precision) AS accepts_credit_cards,
    COALESCE(vb.ambience_casual, 0::double precision) AS ambience_casual,
    COALESCE(vb.ambience_classy, 0::double precision) AS ambience_classy,
    COALESCE(vb.ambience_divey, 0::double precision) AS ambience_divey,
    COALESCE(vb.ambience_hipster, 0::double precision) AS ambience_hipster,
    COALESCE(vb.ambience_intimate, 0::double precision) AS ambience_intimate,
    COALESCE(vb.ambience_romantic, 0::double precision) AS ambience_romantic,
    COALESCE(vb.ambience_touristy, 0::double precision) AS ambience_touristy,
    COALESCE(vb.ambience_trendy, 0::double precision) AS ambience_trendy,
    COALESCE(vb.ambience_upscale, 0::double precision) AS ambience_upscale,
    COALESCE(vb.byob, 0::double precision) AS byob,
    COALESCE(vb.caters, 0::double precision) AS caters,
    COALESCE(vb.coat_check, 0::double precision) AS coat_check,
    COALESCE(vb.corkage, 0::double precision) AS corkage,
    COALESCE(vb.delivery, 0::double precision) AS delivery,
    COALESCE(vb.dietary_restrictions_vegan, 0::double precision) AS dietary_restrictions_vegan,
    COALESCE(vb.dietary_restrictions_vegetarian, 0::double precision) AS dietary_restrictions_vegetarian,
    COALESCE(vb.dogs_allowed, 0::double precision) AS dogs_allowed,
    COALESCE(vb.drive_thr, 0::double precision) AS drive_thr,
    COALESCE(vb.good_for_breakfast, 0::double precision) AS good_for_breakfast,
    COALESCE(vb.good_for_brunch, 0::double precision) AS good_for_brunch,
    COALESCE(vb.good_for_dancing, 0::double precision) AS good_for_dancing,
    COALESCE(vb.good_for_dessert, 0::double precision) AS good_for_dessert,
    COALESCE(vb.good_for_dinner, 0::double precision) AS good_for_dinner,
    COALESCE(vb.good_for_groups, 0::double precision) AS good_for_groups,
    COALESCE(vb.good_for_kids, 0::double precision) AS good_for_kids,
    COALESCE(vb.good_for_latenight, 0::double precision) AS good_for_latenight,
    COALESCE(vb.good_for_lunch, 0::double precision) AS good_for_lunch,
    COALESCE(vb.happy_hour, 0::double precision) AS happy_hour,
    COALESCE(vb.has_tv, 0::double precision) AS has_tv,
    COALESCE(vb.music_accepts_credit_cards, 0::double precision) AS music_accepts_credit_cards,
    COALESCE(vb.music_background_music, 0::double precision) AS music_background_music,
    COALESCE(vb.music_caters, 0::double precision) AS music_caters,
    COALESCE(vb.music_corkage, 0::double precision) AS music_corkage,
    COALESCE(vb.music_dj, 0::double precision) AS music_dj,
    COALESCE(vb.music_good_for_groups, 0::double precision) AS music_good_for_groups,
    COALESCE(vb.music_good_for_kids, 0::double precision) AS music_good_for_kids,
    COALESCE(vb.music_happy_hour, 0::double precision) AS music_happy_hour,
    COALESCE(vb.music_has_tv, 0::double precision) AS music_has_tv,
    COALESCE(vb.music_jukebox, 0::double precision) AS music_jukebox,
    COALESCE(vb.music_live, 0::double precision) AS music_live,
    COALESCE(vb.music_outdoor_seating, 0::double precision) AS music_outdoor_seating,
    COALESCE(vb.music_take_out, 0::double precision) AS music_take_out,
    COALESCE(vb.music_takes_reservations, 0::double precision) AS music_takes_reservations,
    COALESCE(vb.music_video, 0::double precision) AS music_video,
    COALESCE(vb.music_waiter_service, 0::double precision) AS music_waiter_service,
    COALESCE(vb.music_wheelchair_accessible, 0::double precision) AS music_wheelchair_accessible,
    COALESCE(vb.order_at_counter, 0::double precision) AS order_at_counter,
    COALESCE(vb.outdoor_seating, 0::double precision) AS outdoor_seating,
    COALESCE(vb.parking_garage, 0::double precision) AS parking_garage,
    COALESCE(vb.parking_lot, 0::double precision) AS parking_lot,
    COALESCE(vb.parking_street, 0::double precision) AS parking_street,
    COALESCE(vb.parking_valet, 0::double precision) AS parking_valet,
    COALESCE(vb.parking_validated, 0::double precision) AS parking_validated,
    COALESCE(vb.payment_types_amex, 0::double precision) AS payment_types_amex,
    COALESCE(vb.payment_types_discover, 0::double precision) AS payment_types_discover,
    COALESCE(vb.payment_types_mastercard, 0::double precision) AS payment_types_mastercard,
    COALESCE(vb.payment_types_visa, 0::double precision) AS payment_types_visa,
    COALESCE(vb.take_out, 0::double precision) AS take_out,
    COALESCE(vb.takes_reservations, 0::double precision) AS takes_reservations,
    COALESCE(vb.waiter_service, 0::double precision) AS waiter_service,
    COALESCE(vb.wheelchair_accessible, 0::double precision) AS wheelchair_accessible,
    COALESCE(vb.ages_allowed_21plus, 0::double precision) AS ages_allowed_21plus,
    COALESCE(vb.alcohol_beer_and_wine, 0::double precision) AS alcohol_beer_and_wine,
    COALESCE(vb.alcohol_full_bar, 0::double precision) AS alcohol_full_bar,
    COALESCE(vb.alcohol_none, 0::double precision) AS alcohol_none,
    COALESCE(vb.attire_casual, 0::double precision) AS attire_casual,
    COALESCE(vb.attire_dressy, 0::double precision) AS attire_dressy,
    COALESCE(vb.byob_corkage_no, 0::double precision) AS byob_corkage_no,
    COALESCE(vb.byob_corkage_yes_corkage, 0::double precision) AS byob_corkage_yes_corkage,
    COALESCE(vb.byob_corkage_yes_free, 0::double precision) AS byob_corkage_yes_free,
    COALESCE(vb.music_attire_casual, 0::double precision) AS music_attire_casual,
    COALESCE(vb.music_byob_corkage_no, 0::double precision) AS music_byob_corkage_no,
    COALESCE(vb.music_price_range_2, 0::double precision) AS music_price_range_2,
    COALESCE(vb.music_smoking_no, 0::double precision) AS music_smoking_no,
    COALESCE(vb.music_wi_fi_free, 0::double precision) AS music_wi_fi_free,
    COALESCE(vb.music_wi_fi_no, 0::double precision) AS music_wi_fi_no,
    COALESCE(vb.noise_level_average, 0::double precision) AS noise_level_average,
    COALESCE(vb.noise_level_loud, 0::double precision) AS noise_level_loud,
    COALESCE(vb.noise_level_quiet, 0::double precision) AS noise_level_quiet,
    COALESCE(vb.noise_level_very_loud, 0::double precision) AS noise_level_very_loud,
    COALESCE(vb.price_range_1, 0::double precision) AS price_range_1,
    COALESCE(vb.price_range_2, 0::double precision) AS price_range_2,
    COALESCE(vb.price_range_3, 0::double precision) AS price_range_3,
    COALESCE(vb.price_range_4, 0::double precision) AS price_range_4,
    COALESCE(vb.smoking_no, 0::double precision) AS smoking_no,
    COALESCE(vb.smoking_outdoor, 0::double precision) AS smoking_outdoor,
    COALESCE(vb.smoking_yes, 0::double precision) AS smoking_yes,
    COALESCE(vb.wi_fi_free, 0::double precision) AS wi_fi_free,
    COALESCE(vb.wi_fi_no, 0::double precision) AS wi_fi_no,
    COALESCE(vb.wi_fi_paid, 0::double precision) AS wi_fi_paid,
        CASE
            WHEN vb.wi_fi_paid IS NULL THEN 1
            ELSE 0
        END AS n_business_null,
    COALESCE(vrsv.avg_stars_before, 0::numeric) AS avg_stars_before,
    COALESCE(vrsv.avg_stars_56_days_before, 0::numeric) AS avg_stars_56_days_before,
    COALESCE(vrsv.avg_stars_91_days_before, 0::numeric) AS avg_stars_91_days_before,
    COALESCE(vrsv.avg_stars_183_days_before, 0::numeric) AS avg_stars_183_days_before,
    COALESCE(vrsv.avg_stars_365_days_before, 0::numeric) AS avg_stars_365_days_before,
    COALESCE(vrsv.avg_votes_cool_review_before, 0::double precision) AS avg_votes_cool_review_before,
    COALESCE(vrsv.avg_votes_cool_review_56_days_before, 0::double precision) AS avg_votes_cool_review_56_days_before,
    COALESCE(vrsv.avg_votes_cool_review_91_days_before, 0::double precision) AS avg_votes_cool_review_91_days_before,
    COALESCE(vrsv.avg_votes_cool_review_183_days_before, 0::double precision) AS avg_votes_cool_review_183_days_before,
    COALESCE(vrsv.avg_votes_cool_review_365_days_before, 0::double precision) AS avg_votes_cool_review_365_days_before,
    COALESCE(vrsv.avg_votes_funny_review_before, 0::double precision) AS avg_votes_funny_review_before,
    COALESCE(vrsv.avg_votes_funny_review_56_days_before, 0::double precision) AS avg_votes_funny_review_56_days_before,
    COALESCE(vrsv.avg_votes_funny_review_91_days_before, 0::double precision) AS avg_votes_funny_review_91_days_before,
    COALESCE(vrsv.avg_votes_funny_review_183_days_before, 0::double precision) AS avg_votes_funny_review_183_days_before,
    COALESCE(vrsv.avg_votes_funny_review_365_days_before, 0::double precision) AS avg_votes_funny_review_365_days_before,
    COALESCE(vrsv.avg_votes_useful_review_before, 0::double precision) AS avg_votes_useful_review_before,
    COALESCE(vrsv.avg_votes_useful_review_56_days_before, 0::double precision) AS avg_votes_useful_review_56_days_before,
    COALESCE(vrsv.avg_votes_useful_review_91_days_before, 0::double precision) AS avg_votes_useful_review_91_days_before,
    COALESCE(vrsv.avg_votes_useful_review_183_days_before, 0::double precision) AS avg_votes_useful_review_183_days_before,
    COALESCE(vrsv.avg_votes_useful_review_365_days_before, 0::double precision) AS avg_votes_useful_review_365_days_before,
    COALESCE(vrsv.avg_review_len_before, 0::double precision) AS avg_review_len_before,
    COALESCE(vrsv.avg_review_len_56_days_before, 0::double precision) AS avg_review_len_56_days_before,
    COALESCE(vrsv.avg_review_len_91_days_before, 0::double precision) AS avg_review_len_91_days_before,
    COALESCE(vrsv.avg_review_len_183_days_before, 0::double precision) AS avg_review_len_183_days_before,
    COALESCE(vrsv.avg_review_len_365_days_before, 0::double precision) AS avg_review_len_365_days_before,
        CASE
            WHEN vrsv.avg_stars_before IS NULL THEN 1
            ELSE 0
        END AS n_avg_stars_before,
        CASE
            WHEN vrsv.avg_stars_56_days_before IS NULL THEN 1
            ELSE 0
        END AS n_avg_stars_56_days_before,
        CASE
            WHEN vrsv.avg_stars_91_days_before IS NULL THEN 1
            ELSE 0
        END AS n_avg_stars_91_days_before,
        CASE
            WHEN vrsv.avg_stars_183_days_before IS NULL THEN 1
            ELSE 0
        END AS n_avg_stars_183_days_before,
        CASE
            WHEN vrsv.avg_stars_365_days_before IS NULL THEN 1
            ELSE 0
        END AS n_avg_stars_365_days_before,
    COALESCE(vplv.avg_one_star_before, 0::numeric) AS avg_one_star_before,
    COALESCE(vplv.avg_two_star_before, 0::numeric) AS avg_two_star_before,
    COALESCE(vplv.avg_three_star_before, 0::numeric) AS avg_three_star_before,
    COALESCE(vplv.avg_one_star_last_91_day, 0::numeric) AS avg_one_star_last_91_day,
    COALESCE(vplv.avg_one_star_last_186_day, 0::numeric) AS avg_one_star_last_186_day,
    COALESCE(vplv.avg_one_star_last_365_day, 0::numeric) AS avg_one_star_last_365_day,
    COALESCE(vplv.avg_two_star_last_91_day, 0::numeric) AS avg_two_star_last_91_day,
    COALESCE(vplv.avg_two_star_last_186_day, 0::numeric) AS avg_two_star_last_186_day,
    COALESCE(vplv.avg_two_star_last_365_day, 0::numeric) AS avg_two_star_last_365_day,
    COALESCE(vplv.avg_three_star_last_91_day, 0::numeric) AS avg_three_star_last_91_day,
    COALESCE(vplv.avg_three_star_last_186_day, 0::numeric) AS avg_three_star_last_186_day,
    COALESCE(vplv.avg_three_star_last_365_day, 0::numeric) AS avg_three_star_last_365_day,
    COALESCE(vplv.max_one_star_before, 0::numeric) AS max_one_star_before,
    COALESCE(vplv.max_two_star_before, 0::numeric) AS max_two_star_before,
    COALESCE(vplv.max_three_star_before, 0::numeric) AS max_three_star_before,
    COALESCE(vplv.max_one_star_last_91_day, 0::numeric) AS max_one_star_last_91_day,
    COALESCE(vplv.max_one_star_last_186_day, 0::numeric) AS max_one_star_last_186_day,
    COALESCE(vplv.max_one_star_last_365_day, 0::numeric) AS max_one_star_last_365_day,
    COALESCE(vplv.max_two_star_last_91_day, 0::numeric) AS max_two_star_last_91_day,
    COALESCE(vplv.max_two_star_last_186_day, 0::numeric) AS max_two_star_last_186_day,
    COALESCE(vplv.max_two_star_last_365_day, 0::numeric) AS max_two_star_last_365_day,
    COALESCE(vplv.max_three_star_last_91_day, 0::numeric) AS max_three_star_last_91_day,
    COALESCE(vplv.max_three_star_last_186_day, 0::numeric) AS max_three_star_last_186_day,
    COALESCE(vplv.max_three_star_last_365_day, 0::numeric) AS max_three_star_last_365_day,
    COALESCE(vplv.stdev_one_star_before, 0::numeric) AS stdev_one_star_before,
    COALESCE(vplv.stdev_two_star_before, 0::numeric) AS stdev_two_star_before,
    COALESCE(vplv.stdev_three_star_before, 0::numeric) AS stdev_three_star_before,
    COALESCE(vplv.stdev_one_star_last_91_day, 0::numeric) AS stdev_one_star_last_91_day,
    COALESCE(vplv.stdev_one_star_last_186_day, 0::numeric) AS stdev_one_star_last_186_day,
    COALESCE(vplv.stdev_one_star_last_365_day, 0::numeric) AS stdev_one_star_last_365_day,
    COALESCE(vplv.stdev_two_star_last_91_day, 0::numeric) AS stdev_two_star_last_91_day,
    COALESCE(vplv.stdev_two_star_last_186_day, 0::numeric) AS stdev_two_star_last_186_day,
    COALESCE(vplv.stdev_two_star_last_365_day, 0::numeric) AS stdev_two_star_last_365_day,
    COALESCE(vplv.stdev_three_star_last_91_day, 0::numeric) AS stdev_three_star_last_91_day,
    COALESCE(vplv.stdev_three_star_last_186_day, 0::numeric) AS stdev_three_star_last_186_day,
    COALESCE(vplv.stdev_three_star_last_365_day, 0::numeric) AS stdev_three_star_last_365_day,
    COALESCE(vplv.min_one_star_before, 0::numeric) AS min_one_star_before,
    COALESCE(vplv.min_two_star_before, 0::numeric) AS min_two_star_before,
    COALESCE(vplv.min_three_star_before, 0::numeric) AS min_three_star_before,
    COALESCE(vplv.min_one_star_last_91_day, 0::numeric) AS min_one_star_last_91_day,
    COALESCE(vplv.min_one_star_last_186_day, 0::numeric) AS min_one_star_last_186_day,
    COALESCE(vplv.min_one_star_last_365_day, 0::numeric) AS min_one_star_last_365_day,
    COALESCE(vplv.min_two_star_last_91_day, 0::numeric) AS min_two_star_last_91_day,
    COALESCE(vplv.min_two_star_last_186_day, 0::numeric) AS min_two_star_last_186_day,
    COALESCE(vplv.min_two_star_last_365_day, 0::numeric) AS min_two_star_last_365_day,
    COALESCE(vplv.min_three_star_last_91_day, 0::numeric) AS min_three_star_last_91_day,
    COALESCE(vplv.min_three_star_last_186_day, 0::numeric) AS min_three_star_last_186_day,
    COALESCE(vplv.min_three_star_last_365_day, 0::numeric) AS min_three_star_last_365_day,
    COALESCE(vplv.avg_insp_one_star_last_91_day, 0::numeric) AS avg_insp_one_star_last_91_day,
    COALESCE(vplv.avg_insp_one_star_last_186_day, 0::numeric) AS avg_insp_one_star_last_186_day,
    COALESCE(vplv.avg_insp_one_star_last_365_day, 0::numeric) AS avg_insp_one_star_last_365_day,
    COALESCE(vplv.avg_insp_two_star_last_91_day, 0::numeric) AS avg_insp_two_star_last_91_day,
    COALESCE(vplv.avg_insp_two_star_last_186_day, 0::numeric) AS avg_insp_two_star_last_186_day,
    COALESCE(vplv.avg_insp_two_star_last_365_day, 0::numeric) AS avg_insp_two_star_last_365_day,
    COALESCE(vplv.avg_insp_three_star_last_91_day, 0::numeric) AS avg_insp_three_star_last_91_day,
    COALESCE(vplv.avg_insp_three_star_last_186_day, 0::numeric) AS avg_insp_three_star_last_186_day,
    COALESCE(vplv.avg_insp_three_star_last_365_day, 0::numeric) AS avg_insp_three_star_last_365_day,
    COALESCE(vplv.avg_clean_insp_one_star_last_91_day, 0::numeric) AS avg_clean_insp_one_star_last_91_day,
    COALESCE(vplv.avg_clean_insp_one_star_last_186_day, 0::numeric) AS avg_clean_insp_one_star_last_186_day,
    COALESCE(vplv.avg_clean_insp_one_star_last_365_day, 0::numeric) AS avg_clean_insp_one_star_last_365_day,
    COALESCE(vplv.avg_clean_insp_two_star_last_91_day, 0::numeric) AS avg_clean_insp_two_star_last_91_day,
    COALESCE(vplv.avg_clean_insp_two_star_last_186_day, 0::numeric) AS avg_clean_insp_two_star_last_186_day,
    COALESCE(vplv.avg_clean_insp_two_star_last_365_day, 0::numeric) AS avg_clean_insp_two_star_last_365_day,
    COALESCE(vplv.avg_clean_insp_three_star_last_91_day, 0::numeric) AS avg_clean_insp_three_star_last_91_day,
    COALESCE(vplv.avg_clean_insp_three_star_last_186_day, 0::numeric) AS avg_clean_insp_three_star_last_186_day,
    COALESCE(vplv.avg_clean_insp_three_star_last_365_day, 0::numeric) AS avg_clean_insp_three_star_last_365_day,
    COALESCE(vplv.avg_insp_2_one_star_last_91_day, 0::numeric) AS avg_insp_2_one_star_last_91_day,
    COALESCE(vplv.avg_insp_2_one_star_last_186_day, 0::numeric) AS avg_insp_2_one_star_last_186_day,
    COALESCE(vplv.avg_insp_2_one_star_last_365_day, 0::numeric) AS avg_insp_2_one_star_last_365_day,
    COALESCE(vplv.avg_insp_2_two_star_last_91_day, 0::numeric) AS avg_insp_2_two_star_last_91_day,
    COALESCE(vplv.avg_insp_2_two_star_last_186_day, 0::numeric) AS avg_insp_2_two_star_last_186_day,
    COALESCE(vplv.avg_insp_2_two_star_last_365_day, 0::numeric) AS avg_insp_2_two_star_last_365_day,
    COALESCE(vplv.avg_insp_2_three_star_last_91_day, 0::numeric) AS avg_insp_2_three_star_last_91_day,
    COALESCE(vplv.avg_insp_2_three_star_last_186_day, 0::numeric) AS avg_insp_2_three_star_last_186_day,
    COALESCE(vplv.avg_insp_2_three_star_last_365_day, 0::numeric) AS avg_insp_2_three_star_last_365_day,
    COALESCE(vplv.avg_insp_3_one_star_last_91_day, 0::numeric) AS avg_insp_3_one_star_last_91_day,
    COALESCE(vplv.avg_insp_3_one_star_last_186_day, 0::numeric) AS avg_insp_3_one_star_last_186_day,
    COALESCE(vplv.avg_insp_3_one_star_last_365_day, 0::numeric) AS avg_insp_3_one_star_last_365_day,
    COALESCE(vplv.avg_insp_3_two_star_last_91_day, 0::numeric) AS avg_insp_3_two_star_last_91_day,
    COALESCE(vplv.avg_insp_3_two_star_last_186_day, 0::numeric) AS avg_insp_3_two_star_last_186_day,
    COALESCE(vplv.avg_insp_3_two_star_last_365_day, 0::numeric) AS avg_insp_3_two_star_last_365_day,
    COALESCE(vplv.avg_insp_3_three_star_last_91_day, 0::numeric) AS avg_insp_3_three_star_last_91_day,
    COALESCE(vplv.avg_insp_3_three_star_last_186_day, 0::numeric) AS avg_insp_3_three_star_last_186_day,
    COALESCE(vplv.avg_insp_3_three_star_last_365_day, 0::numeric) AS avg_insp_3_three_star_last_365_day,
    COALESCE(vplv.avg_insp_5_one_star_last_91_day, 0::numeric) AS avg_insp_5_one_star_last_91_day,
    COALESCE(vplv.avg_insp_5_one_star_last_186_day, 0::numeric) AS avg_insp_5_one_star_last_186_day,
    COALESCE(vplv.avg_insp_5_one_star_last_365_day, 0::numeric) AS avg_insp_5_one_star_last_365_day,
    COALESCE(vplv.avg_insp_5_three_star_last_91_day, 0::numeric) AS avg_insp_5_three_star_last_91_day,
    COALESCE(vplv.avg_insp_5_three_star_last_186_day, 0::numeric) AS avg_insp_5_three_star_last_186_day,
    COALESCE(vplv.avg_insp_5_three_star_last_365_day, 0::numeric) AS avg_insp_5_three_star_last_365_day,
    COALESCE(vplv.avg_insp_8_one_star_last_91_day, 0::numeric) AS avg_insp_8_one_star_last_91_day,
    COALESCE(vplv.avg_insp_8_one_star_last_186_day, 0::numeric) AS avg_insp_8_one_star_last_186_day,
    COALESCE(vplv.avg_insp_8_one_star_last_365_day, 0::numeric) AS avg_insp_8_one_star_last_365_day,
    COALESCE(vplv.avg_insp_8_three_star_last_91_day, 0::numeric) AS avg_insp_8_three_star_last_91_day,
    COALESCE(vplv.avg_insp_8_three_star_last_186_day, 0::numeric) AS avg_insp_8_three_star_last_186_day,
    COALESCE(vplv.avg_insp_8_three_star_last_365_day, 0::numeric) AS avg_insp_8_three_star_last_365_day,
        CASE
            WHEN vplv.avg_one_star_before IS NULL THEN 1
            ELSE 0
        END AS n_vplv__before,
        CASE
            WHEN vplv.avg_one_star_last_91_day IS NULL THEN 1
            ELSE 0
        END AS n_avg_one_star_last_91_day,
        CASE
            WHEN vplv.avg_one_star_last_186_day IS NULL THEN 1
            ELSE 0
        END AS n_avg_one_star_last_186_day,
        CASE
            WHEN vplv.avg_one_star_last_365_day IS NULL THEN 1
            ELSE 0
        END AS n_avg_one_star_last_365_day,
        CASE
            WHEN vplv.stdev_one_star_last_91_day IS NULL THEN 1
            ELSE 0
        END AS n_stdev_one_star_last_91_day,
        CASE
            WHEN vplv.stdev_one_star_last_186_day IS NULL THEN 1
            ELSE 0
        END AS n_stdev_one_star_last_186_day,
        CASE
            WHEN vplv.stdev_one_star_last_365_day IS NULL THEN 1
            ELSE 0
        END AS n_stdev_one_star_last_365_day,
    COALESCE(vrusv.avg_fans_before, 0::numeric) AS avg_fans_before,
    COALESCE(vrusv.avg_fans_42_days_before, 0::numeric) AS avg_fans_42_days_before,
    COALESCE(vrusv.avg_fans_56_days_before, 0::numeric) AS avg_fans_56_days_before,
    COALESCE(vrusv.avg_fans_91_days_before, 0::numeric) AS avg_fans_91_days_before,
    COALESCE(vrusv.avg_fans_183_days_before, 0::numeric) AS avg_fans_183_days_before,
    COALESCE(vrusv.avg_fans_365_days_before, 0::numeric) AS avg_fans_365_days_before,
    COALESCE(vrusv.avg_review_count_before, 0::numeric) AS avg_review_count_before,
    COALESCE(vrusv.avg_review_count_42_days_before, 0::numeric) AS avg_review_count_42_days_before,
    COALESCE(vrusv.avg_review_count_56_days_before, 0::numeric) AS avg_review_count_56_days_before,
    COALESCE(vrusv.avg_review_count_91_days_before, 0::numeric) AS avg_review_count_91_days_before,
    COALESCE(vrusv.avg_review_count_183_days_before, 0::numeric) AS avg_review_count_183_days_before,
    COALESCE(vrusv.avg_review_count_365_days_before, 0::numeric) AS avg_review_count_365_days_before,
    COALESCE(vrusv.avg_num_friends_before, 0::numeric::double precision) AS avg_num_friends_before,
    COALESCE(vrusv.avg_num_friends_42_days_before, 0::numeric::double precision) AS avg_num_friends_42_days_before,
    COALESCE(vrusv.avg_num_friends_56_days_before, 0::numeric::double precision) AS avg_num_friends_56_days_before,
    COALESCE(vrusv.avg_num_friends_91_days_before, 0::numeric::double precision) AS avg_num_friends_91_days_before,
    COALESCE(vrusv.avg_num_friends_183_days_before, 0::numeric::double precision) AS avg_num_friends_183_days_before,
    COALESCE(vrusv.avg_num_friends_365_days_before, 0::numeric::double precision) AS avg_num_friends_365_days_before,
    COALESCE(vrusv.avg_vs_usr_avg_stars_before, 0::double precision) AS avg_vs_usr_avg_stars_before,
    COALESCE(vrusv.avg_vs_usr_avg_stars_42_days_before, 0::double precision) AS avg_vs_usr_avg_stars_42_days_before,
    COALESCE(vrusv.avg_vs_usr_avg_stars_56_days_before, 0::double precision) AS avg_vs_usr_avg_stars_56_days_before,
    COALESCE(vrusv.avg_vs_usr_avg_stars_91_days_before, 0::double precision) AS avg_vs_usr_avg_stars_91_days_before,
    COALESCE(vrusv.avg_vs_usr_avg_stars_183_days_before, 0::double precision) AS avg_vs_usr_avg_stars_183_days_before,
    COALESCE(vrusv.avg_vs_usr_avg_stars_365_days_before, 0::double precision) AS avg_vs_usr_avg_stars_365_days_before,
    COALESCE(tbi.days_since_last_inspection, 0::numeric) AS days_since_last_inspection,
    COALESCE(tbi.days_since_second_last_inspection, 0::numeric) AS days_since_second_last_inspection,
    COALESCE(tbi.days_since_third_last_inspection, 0::numeric) AS days_since_third_last_inspection,
    COALESCE(tbi.days_since_fourth_last_inspection, 0::numeric) AS days_since_fourth_last_inspection,
    COALESCE(tbi.days_since_fifth_last_inspection, 0::numeric) AS days_since_fifth_last_inspection,
    COALESCE(tbi.first_inspection, 0) AS first_inspection,
    COALESCE(tbi.second_inspection, 0) AS second_inspection,
    COALESCE(tbi.third_inspection, 0) AS third_inspection,
    COALESCE(tbi.fourth_inspection, 0) AS fourth_inspection,
    COALESCE(tbi.fifth_inspection, 0) AS fifth_inspection,
    COALESCE(vwpt.sum_tips_before::double precision, 0::double precision) AS sum_tips_before,
    COALESCE(vwpt.sum_tips_last_56_day::double precision, 0::double precision) AS sum_tips_last_56_day,
    COALESCE(vwpt.sum_tips_last_91_day::double precision, 0::double precision) AS sum_tips_last_91_day,
    COALESCE(vwpt.sum_tips_last_183_day::double precision, 0::double precision) AS sum_tips_last_183_day,
    COALESCE(vwpt.sum_tips_last_365_day::double precision, 0::double precision) AS sum_tips_last_365_day,
    COALESCE(rst.share_1_star_before::double precision, 0::double precision) AS share_1_star_before,
    COALESCE(rst.share_2_star_before::double precision, 0::double precision) AS share_2_star_before,
    COALESCE(rst.share_3_star_before::double precision, 0::double precision) AS share_3_star_before,
    COALESCE(rst.share_4_star_before::double precision, 0::double precision) AS share_4_star_before,
    COALESCE(rst.share_5_star_before::double precision, 0::double precision) AS share_5_star_before,
    COALESCE(rst.share_1_star_42_days_before::double precision, 0::double precision) AS share_1_star_42_days_before,
    COALESCE(rst.share_2_star_42_days_before::double precision, 0::double precision) AS share_2_star_42_days_before,
    COALESCE(rst.share_3_star_42_days_before::double precision, 0::double precision) AS share_3_star_42_days_before,
    COALESCE(rst.share_4_star_42_days_before::double precision, 0::double precision) AS share_4_star_42_days_before,
    COALESCE(rst.share_5_star_42_days_before::double precision, 0::double precision) AS share_5_star_42_days_before,
    COALESCE(rst.share_1_star_56_days_before::double precision, 0::double precision) AS share_1_star_56_days_before,
    COALESCE(rst.share_2_star_56_days_before::double precision, 0::double precision) AS share_2_star_56_days_before,
    COALESCE(rst.share_3_star_56_days_before::double precision, 0::double precision) AS share_3_star_56_days_before,
    COALESCE(rst.share_4_star_56_days_before::double precision, 0::double precision) AS share_4_star_56_days_before,
    COALESCE(rst.share_5_star_56_days_before::double precision, 0::double precision) AS share_5_star_56_days_before,
    COALESCE(rst.share_1_star_91_days_before::double precision, 0::double precision) AS share_1_star_91_days_before,
    COALESCE(rst.share_2_star_91_days_before::double precision, 0::double precision) AS share_2_star_91_days_before,
    COALESCE(rst.share_3_star_91_days_before::double precision, 0::double precision) AS share_3_star_91_days_before,
    COALESCE(rst.share_4_star_91_days_before::double precision, 0::double precision) AS share_4_star_91_days_before,
    COALESCE(rst.share_5_star_91_days_before::double precision, 0::double precision) AS share_5_star_91_days_before,
    COALESCE(rst.share_1_star_183_days_before::double precision, 0::double precision) AS share_1_star_183_days_before,
    COALESCE(rst.share_2_star_183_days_before::double precision, 0::double precision) AS share_2_star_183_days_before,
    COALESCE(rst.share_3_star_183_days_before::double precision, 0::double precision) AS share_3_star_183_days_before,
    COALESCE(rst.share_4_star_183_days_before::double precision, 0::double precision) AS share_4_star_183_days_before,
    COALESCE(rst.share_5_star_183_days_before::double precision, 0::double precision) AS share_5_star_183_days_before,
    COALESCE(rst.share_1_star_365_days_before::double precision, 0::double precision) AS share_1_star_365_days_before,
    COALESCE(rst.share_2_star_365_days_before::double precision, 0::double precision) AS share_2_star_365_days_before,
    COALESCE(rst.share_3_star_365_days_before::double precision, 0::double precision) AS share_3_star_365_days_before,
    COALESCE(rst.share_4_star_365_days_before::double precision, 0::double precision) AS share_4_star_365_days_before,
    COALESCE(rst.share_5_star_365_days_before::double precision, 0::double precision) AS share_5_star_365_days_before,
        CASE
            WHEN rst.std_review_stars_before IS NULL THEN 1
            ELSE 0
        END AS n_std_review_stars_before,
        CASE
            WHEN rst.std_review_stars_42_days_before IS NULL THEN 1
            ELSE 0
        END AS n_std_review_stars_42_days_before,
        CASE
            WHEN rst.std_review_stars_56_days_before IS NULL THEN 1
            ELSE 0
        END AS n_std_review_stars_56_days_before,
        CASE
            WHEN rst.std_review_stars_91_days_before IS NULL THEN 1
            ELSE 0
        END AS n_std_review_stars_91_days_before,
        CASE
            WHEN rst.std_review_stars_183_days_before IS NULL THEN 1
            ELSE 0
        END AS n_std_review_stars_183_days_before,
        CASE
            WHEN rst.std_review_stars_365_days_before IS NULL THEN 1
            ELSE 0
        END AS n_std_review_stars_365_days_before,
    COALESCE(fri.num_insp_42_days_before::double precision, 0::double precision) AS num_insp_42_days_before,
    COALESCE(fri.num_insp_56_days_before::double precision, 0::double precision) AS num_insp_56_days_before,
    COALESCE(fri.num_insp_91_days_before::double precision, 0::double precision) AS num_insp_91_days_before,
    COALESCE(fri.num_insp_183_days_before::double precision, 0::double precision) AS num_insp_183_days_before,
    COALESCE(fri.num_insp_365_days_before::double precision, 0::double precision) AS num_insp_365_days_before,
    COALESCE(plvo.one_prev_missing, 0::numeric) AS one_prev_missing,
    COALESCE(plvo.one_one_star, 0::numeric) AS one_one_star,
    COALESCE(plvo.one_two_star, 0::numeric) AS one_two_star,
    COALESCE(plvo.one_three_star, 0::numeric) AS one_three_star,
    COALESCE(plvo.two_prev_missing, 0::numeric) AS two_prev_missing,
    COALESCE(plvo.two_one_star, 0::numeric) AS two_one_star,
    COALESCE(plvo.two_two_star, 0::numeric) AS two_two_star,
    COALESCE(plvo.two_three_star, 0::numeric) AS two_three_star,
    COALESCE(plvo.three_prev_missing, 0::numeric) AS three_prev_missing,
    COALESCE(plvo.three_one_star, 0::numeric) AS three_one_star,
    COALESCE(plvo.three_two_star, 0::numeric) AS three_two_star,
    COALESCE(plvo.three_three_star, 0::numeric) AS three_three_star,
    COALESCE(plvo.four_prev_missing, 0::numeric) AS four_prev_missing,
    COALESCE(plvo.four_one_star, 0::numeric) AS four_one_star,
    COALESCE(plvo.four_two_star, 0::numeric) AS four_two_star,
    COALESCE(plvo.four_three_star, 0::numeric) AS four_three_star,
    COALESCE(plvo.five_prev_missing, 0::numeric) AS five_prev_missing,
    COALESCE(plvo.five_one_star, 0::numeric) AS five_one_star,
    COALESCE(plvo.five_two_star, 0::numeric) AS five_two_star,
    COALESCE(plvo.five_three_star, 0::numeric) AS five_three_star,
    COALESCE(plvo.avg_last_two_one_star, 0::numeric) AS avg_last_two_one_star,
    COALESCE(plvo.avg_last_three_one_star, 0::numeric) AS avg_last_three_one_star,
    COALESCE(plvo.avg_last_four_one_star, 0::numeric) AS avg_last_four_one_star,
    COALESCE(plvo.avg_last_five_one_star, 0::numeric) AS avg_last_five_one_star,
    COALESCE(plvo.avg_last_two_two_star, 0::numeric) AS avg_last_two_two_star,
    COALESCE(plvo.avg_last_three_two_star, 0::numeric) AS avg_last_three_two_star,
    COALESCE(plvo.avg_last_four_two_star, 0::numeric) AS avg_last_four_two_star,
    COALESCE(plvo.avg_last_five_two_star, 0::numeric) AS avg_last_five_two_star,
    COALESCE(plvo.avg_last_two_three_star, 0::numeric) AS avg_last_two_three_star,
    COALESCE(plvo.avg_last_three_three_star, 0::numeric) AS avg_last_three_three_star,
    COALESCE(plvo.avg_last_four_three_star, 0::numeric) AS avg_last_four_three_star,
    COALESCE(plvo.avg_last_five_three_star, 0::numeric) AS avg_last_five_three_star,
    COALESCE(plvo.greatest_last_two_one_star, 0::numeric) AS greatest_last_two_one_star,
    COALESCE(plvo.greatest_last_three_one_star, 0::numeric) AS greatest_last_three_one_star,
    COALESCE(plvo.greatest_last_four_one_star, 0::numeric) AS greatest_last_four_one_star,
    COALESCE(plvo.greatest_last_five_one_star, 0::numeric) AS greatest_last_five_one_star,
    COALESCE(plvo.greatest_last_two_two_star, 0::numeric) AS greatest_last_two_two_star,
    COALESCE(plvo.greatest_last_three_two_star, 0::numeric) AS greatest_last_three_two_star,
    COALESCE(plvo.greatest_last_four_two_star, 0::numeric) AS greatest_last_four_two_star,
    COALESCE(plvo.greatest_last_five_two_star, 0::numeric) AS greatest_last_five_two_star,
    COALESCE(plvo.greatest_last_two_three_star, 0::numeric) AS greatest_last_two_three_star,
    COALESCE(plvo.greatest_last_three_three_star, 0::numeric) AS greatest_last_three_three_star,
    COALESCE(plvo.greatest_last_four_three_star, 0::numeric) AS greatest_last_four_three_star,
    COALESCE(plvo.greatest_last_five_three_star, 0::numeric) AS greatest_last_five_three_star,
    COALESCE(plvo.least_last_two_one_star, 0::numeric) AS least_last_two_one_star,
    COALESCE(plvo.least_last_three_one_star, 0::numeric) AS least_last_three_one_star,
    COALESCE(plvo.least_last_four_one_star, 0::numeric) AS least_last_four_one_star,
    COALESCE(plvo.least_last_five_one_star, 0::numeric) AS least_last_five_one_star,
    COALESCE(plvo.least_last_two_two_star, 0::numeric) AS least_last_two_two_star,
    COALESCE(plvo.least_last_three_two_star, 0::numeric) AS least_last_three_two_star,
    COALESCE(plvo.least_last_four_two_star, 0::numeric) AS least_last_four_two_star,
    COALESCE(plvo.least_last_five_two_star, 0::numeric) AS least_last_five_two_star,
    COALESCE(plvo.least_last_two_three_star, 0::numeric) AS least_last_two_three_star,
    COALESCE(plvo.least_last_three_three_star, 0::numeric) AS least_last_three_three_star,
    COALESCE(plvo.least_last_four_three_star, 0::numeric) AS least_last_four_three_star,
    COALESCE(plvo.least_last_five_three_star, 0::numeric) AS least_last_five_three_star,
        CASE
            WHEN plvo.three_one_star IS NULL THEN 1
            ELSE 0
        END AS n_three_one_star,
        CASE
            WHEN plvo.four_one_star IS NULL THEN 1
            ELSE 0
        END AS n_four_one_star,
        CASE
            WHEN plvo.five_one_star IS NULL THEN 1
            ELSE 0
        END AS n_five_one_star,
        CASE
            WHEN plvo.avg_last_two_one_star IS NULL THEN 1
            ELSE 0
        END AS n_avg_last_two_one_star,
        CASE
            WHEN plvo.avg_last_three_one_star IS NULL THEN 1
            ELSE 0
        END AS n_avg_last_three_one_star,
        CASE
            WHEN plvo.avg_last_four_one_star IS NULL THEN 1
            ELSE 0
        END AS n_avg_last_four_one_star,
        CASE
            WHEN plvo.avg_last_five_one_star IS NULL THEN 1
            ELSE 0
        END AS n_avg_last_five_one_star,
    COALESCE(rst.std_review_stars_before, 0::numeric) AS std_review_stars_before,
    COALESCE(rst.std_review_stars_42_days_before, 0::numeric) AS std_review_stars_42_days_before,
    COALESCE(rst.std_review_stars_56_days_before, 0::numeric) AS std_review_stars_56_days_before,
    COALESCE(rst.std_review_stars_91_days_before, 0::numeric) AS std_review_stars_91_days_before,
    COALESCE(rst.std_review_stars_183_days_before, 0::numeric) AS std_review_stars_183_days_before,
    COALESCE(rst.std_review_stars_365_days_before, 0::numeric) AS std_review_stars_365_days_before
   FROM tbl_all_cases a
     LEFT JOIN vw_checkins_zm vc ON a.restaurant_id = vc.restaurant_id
     LEFT JOIN vw_business vb ON a.restaurant_id = vb.restaurant_id
     LEFT JOIN vw_review_stars_votes_zm vrsv ON a.restaurant_id = vrsv.restaurant_id AND a.date = vrsv.date
     LEFT JOIN vw_num_yelp_ids map_ids ON a.restaurant_id = map_ids.restaurant_id
     LEFT JOIN vw_prev_tips vwpt ON a.restaurant_id = vwpt.restaurant_id AND a.date = vwpt.date
     LEFT JOIN vw_freq_insp fri ON a.restaurant_id = fri.restaurant_id AND a.date = fri.date
     LEFT JOIN vw_prev_label_values_zm vplv ON a.restaurant_id = vplv.restaurant_id AND a.date = vplv.date
     LEFT JOIN vw_review_users_stars_votes_zm vrusv ON a.restaurant_id = vrusv.restaurant_id AND a.date = vrusv.date
     LEFT JOIN vw_time_between_inspections_zm tbi ON a.restaurant_id = tbi.restaurant_id AND a.date = tbi.date
     LEFT JOIN vw_review_stars_dist_zm rst ON a.restaurant_id = rst.restaurant_id AND a.date = rst.date
     LEFT JOIN vw_prev_insp_values_zm plvo ON a.restaurant_id = plvo.restaurant_id AND a.date = plvo.date;
"""

cur.execute(s_create_tables_and_views)
