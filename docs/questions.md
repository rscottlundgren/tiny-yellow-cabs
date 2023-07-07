# Questions Asked (& Answered)

A recording of the questions asked (and the answers received) has been made below for later reference, along with the scenario that inspired the creation of this repo.

## Tech Screen Scenario

> A client you are working with asks about this:
> 
> Using [NYC “Yellow Taxi” Trips Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), give me all the trips over 0.9 percentile in distance traveled for any of the parquet files you can find there.

## Case-Related Questions & Answers

These questions are specifically related to the "client" and their needs for the data, how they would like it calculated, returned to them, etc.

| Question | Answer |
| --- | --- |
| What is the purpose for identifying trips over 0.9 percentile in distance traveled? Tell me more about how this data is going to be used. Asked another way - what question are you trying to answer / hypothesis are you trying to prove / disprove with this data? | _Ideally we'd like to remove trips with a long distance because the analysis we want to run is over "short" trips. We thought 0.9 was a good number for that._ |
| Are there any specific definitions of "trip" that you're using as the basis for your original question (i.e. a "trip" is defined as any `Trip_distance` greater than .25 miles / 1 mile / 5 miles, etc.)? This will help to ensure that the data I'm returning is accurate to your needs. | _Each row in the dataset is a trip for us_ |
| Are you looking for trips within a specific time frame? If so, please share that so I can ensure you're getting only the data you're looking for. | _Data for just a month is fine, pick the one you prefer._ |
| Are you looking to do a comparison of trips over a specific period of time across the whole data set (i.e. Q1 YoY from 2009 - 2023, MoM within a specific year, between 0900 - 1700 daily, etc.)? | _No_ |
| There are several fields that I can use to filter this data beyond just returning those trips over 0.9 percentile in distance traveled. Are there any specific [fields](yellowTaxiDataDictionary.md) that you would like applied before identifying the trips by distance (`Passenger_count`, `RateCodeID`, `PULocationID`, `DOLocationID` are all potential filters that come to mind, depending on what you're trying to accomplish)? | _We'd like to just filter out trips over 0.9, in later stages we may use other columns to filter._ |
| You specify that you'd like to identify all trips over 0.9 percentile in distance traveled. Typically in the calculation of a percentile in this instance I would follow the algorithm below, but if you'd like me to make any changes to the method of calculation please share your approach so I can make these calculations according to your wishes:<br/>1. Arrange the records in ascending order according to distance traveled<br/>2. Multiply the total number of records in the dataset by 0.9<br/>3. If the value returned is a whole number, I'd move onto the next step, otherwise I would round the value up and then move onto the next step<br/>4. Identify the record with that index and count every record containing a distance value equal to the index's distance value or greater. | _Sounds good, if you think there is a better way, open to suggestions._ |
| How would you like the results to be presented? Do you want an output to appear in your terminal? A raw data file with only those records at or above the percentile recorded? What format would you like the results to be presented in? | _I think a parquet file with the same format would be good._ |

## Exercise-Related Questions & Answers

These questions are specifically related to the limitations on the exercise as requested by Tinybird.

| Question | Answer |
| --- | --- |
| Do you have a preference if I solve this in Python or another language (I'm assuming you want this done in Python but I wanted to double-check)?  | _Any language you prefer, I'd recommend you use the one you are more comfortable with._ |
| Does the "prohibition" of third-party services include the use of Pandas or similar libraries (dependent upon the language)? | _You can use any third-party library_ |
| What versions of Python, JavaScript, or Java should I use so it's easier for you to execute my solution without having to install anything additional? | _As soon as you explain how to run your example in a windows/linux/osx machine we are fine with whatever you choose._ |

[Back To README](https://github.com/rscottlundgren/tiny-yellow-cabs)
