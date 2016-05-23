# DinersChoiceInChicago

Centers for Disease Control estimates that each year roughly 1 in 6 Americans get sick from food. Of those, 75% are associated with food prepared in restaurants, delis or caterers. So where to eat tasty and safety food?

Chicago has thousands of restaurants failed health inspection every year according to City of Chicago data. From 2010 up to now, there have been about 20K total inspections each year, about 19% failed. Majority of failed inspection exposes customers to little risk and may be corrected immediately while critical violations create a health hazard carrying a high risk of food-borne illness.

Chicago department of public health conduct inspections routinely as well as complaint-baed inspections. each year, CDPH receives 4,000 complaints against food establishments. About 17% of total inspections is in response to complaints. Particularly, 0.6% of total inspections is related to food poisoning.

![InspectionType](https://github.com/m-yu/DinersChoiceInChicago/blob/master/InspectionType.png "InspectionType")
![Complaints](https://github.com/m-yu/DinersChoiceInChicago/blob/master/complaints.png "Complaints")

Yelp has a new feature since Oct. 2015 for city of San Francisco that each restaurant is given a health inspection score with past inspections and violations listed and any restaurants residing in bottom 5 percent of food safety rating will be overlaid with a pop-up warning message. This feature is expected to be expanded nationwide.

According to the Economic Journal, an extra half star rating on Yelp boosts business by 19%. Restaurant business in San Francisco would be regularized by the feature of health inspection score. While in Chicago, do restaurants that receive inspections due to complaints and fail have lower rating on yelp?

I here combine food inspection data from City of Chicago data portal with yelp data through Yelp API to understand the correlation between city food inspection and yelp review score. 

##Dine in yelp best rated chinese restaurants...
###Are you interested in a restaurant with 1250 reviews and 4.0 score? What about if you are told that it failed 9 times of total 28 inspections since 2012?
![BestRatedChinese](https://github.com/m-yu/DinersChoiceInChicago/blob/master/BestRatedChinese.png "Yelp best rated Chinese restaurant at Chicago Chinatown with food inspection results")
![BestRatedChinese](https://github.com/m-yu/DinersChoiceInChicago/blob/master/BestRatedChineseInspections.png "Yelp best rated Chinese restaurant at Chicago Chinatown with food inspection results")

Overall, 3 restaurants with score 4.5-5 passed all inspections since 2015. Some restaurants with score 4 received frequent inspections and failed many times. Generally speaking, restaurants with score 4 do not perform better in food inspections comparing to those with score 3.5.

Among 20 best rated chinese restaurant in chinatown area, MINGHIN CUISINE is most reviewed at yelp with an average 4.0 score. It is also the most frequently inspected, totally 28 inspections in the last five years, half of them were due to complaints. 3 out of 9 overall failed inspections were conducted since 2015. Followings are two failed inspections and part of their violations.  

- Canvass inspection 1621342 on 01/29/2016, 
  - SERIOUS CITATION ISSUED: 7-38-020: "OBSERVED 30 PLUS DROPPINGS ON AND UNDER THE SHELVING NEAR THE WASHER AND DRYER IN THE UPSTAIRS UTENSIL WASHING AREA AND ON THE FLOOR. INSTRUCTED TO ELIMINATE RODENT ACTIVITY AND CLEAN ALL AFFECTED AREAS."
  - SERIOUS CITATION ISSUED: 7-38-005(A): "OBSERVED A MOLD-LIKE SUBSTANCE ON THE DROP PLATE OF ICE MACHINE IN THE UPSTAIRS DISHWASHING AREA."
  
- Inspection 1583335 due to complaint on 10/22/2015, 
  - SERIOUS CITATION ISSUED 7-38-020: "INADEQUATE PEST CONTROL, FOUND OVER 40 MOUSE DROPPINGS ALONG WALL BASE IN 2ND FLOOR KITCHEN, ABOUT 30 LIVE FRUIT FLIES IN 1ST FLOOR KITCHEN." 
  - CRITICAL CITATION ISSUED 7-38-005(A): "POTENTIALLY HAZARDOUS FOODS STORED AT IMPROPER TEMPERATURE. FOUND 7LBS OF RAW FISH AT 51.4F, 5 LBS OF RAW CHICKEN AT 52.6F 6 LBS OF RAW BEEF AT 51.5F. ITEMS STORED IN SAID COOLER. INSTRUCTED MGR TO KEEP ALL COLD POTENTIALLY HAZARDOUS FOODS STORED AT 40F OR LOWER."

Good news for MINGHIN CUISINE's diners: they have corrected above issues, and passed the most recent inspection on 02/05/2016.
