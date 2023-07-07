A repo with all the code you used and a readme (in english) explaining your approach, the steps to reproduce your test and everything you feel is important.

# Tiny Yellow Cab Data

## Table of Contents

- [Using The Program](https://github.com/rscottlundgren/tiny-yellow-cabs#using-the-program)
  - [Download Python 3.11]()
  - [Cloning The Repo](https://github.com/rscottlundgren/tiny-yellow-cabs#cloning-the-repo)
  - [Running The Program](https://github.com/rscottlundgren/tiny-yellow-cabs#running-the-program)
- [Approach](https://github.com/rscottlundgren/tiny-yellow-cabs#approach)
  - [Prep Work](https://github.com/rscottlundgren/tiny-yellow-cabs#prep-work)
- [Dataset Considerations](https://github.com/rscottlundgren/tiny-yellow-cabs#dataset-considerations)
- [Helpful Resources / Links](https://github.com/rscottlundgren/tiny-yellow-cabs#links)

## Using The Program
### Download Python 3.11
This program was built using Python 3.11. If you do not have Python 3.11 installed, instructions on downloading Python 3.11 can be found on the [Python language website](https://www.python.org/downloads/). To confirm you've installed it, run the following command and you should receive the following result:
```
$ python3 --version
Python 3.11.4
```

### Cloning The Repo
Once you have a working version of Python 3.11 on your local machine...
1. Clone this repo and `cd` (`c`hange `d`irectory) into that folder by running the following commands: 
    ```
    git clone https://github.com/rscottlundgren/tiny-yellow-cabs.git
    cd tiny-yellow-cabs
    ```

### Running The Program
1. To start the program, enter the following command into your terminal and hit "Enter":
   ```
   python3 tiny-yellow-cabs.py
   ```
2. The program will then prompt you with its first question - asking you to enter a year (that year should be between 2009 and the current year). Enter your selected year and hit "Enter".
3. The program will then prompt you with its second question - asking you to enter a month (that month should be entered as either a full name (i.e. January) or a three-letter abbreviation (i.e. Jan) and should be a month that occurred 2 months prior to the present month or earlier). Enter your selected month and hit "Enter". If you're looking for further examples the below might help:

   1. If today is March 15, 2023 and you entered 2023 as your year, the latest month you can enter is January / Jan
   2. If today is February 28, 2024 and you entered 2023 as your year, the latest month you can enter is November / Nov
   3. If today is July 4, 2023 and you entered 2020 as your year, the latest month you can enter is December / Dec

4. The program will then prompt you with its third (and final) question - asking you to enter a percentile (that percentile should be a decimal (aka a float) between 0.0 and 1.0, inclusive). Enter your desired percentile and hit "Enter".
5. After the questions have been answered, the program will run through a series of actions, documenting each action to the Terminal. At the end of the program you'll receive a quick summary of the data that was parsed and details as to where the results file (`.parquet` extension) is stored, then the program will shut down.

[Back To Top](https://github.com/rscottlundgren/tiny-yellow-cabs)

## Approach

### Prep Work

- Provide scenario
- investigated website
  - Just yellow taxi information
  - reviewed documentation including:
    - Data Dictionary for Yellow Cabs: https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
    - TLC Trip Record Data Page: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
    - TLC Trip Record Users Guide: https://www.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf
- Formulated first round questions for Tinybird
- reference questions that you asked
- Features that would be nice
  - The ability to reference a specific month's data set, rather than be stuck with a specific month that you may not want
    - Additionally, have the platform check to see if the data is available and not have that information be hardcoded
  - The ability to select the percentile before running the data transformation (optional)
  - Some level of testing
  - Actions logged in the terminal for the User
  - Return a data snapshot (5 number summary) - including total number of records - along with the returned requested raw data
- 

[Back To Top](https://github.com/rscottlundgren/tiny-yellow-cabs)

## Dataset Considerations

To start, while the TLC yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts, the website makes it very clear:

> **Warning**
> The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP).



- This is where we include some of the excellent information gleaned from the materials, including links to the reference material that was captured at time of design

Yellow and green 

[Back To Top](https://github.com/rscottlundgren/tiny-yellow-cabs)

## Links

| Description | Static | Live |
| --- | ------ | ---- |
| **TLC Trip Record Data - Site Screen Capture** | [Static](./docs/refs/www.nyc.gov_site_tlc_about_tlc-trip-record-data.page.png) | [Live](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |
| **TLC Trip Record Data - User Guide** | [Static](./docs/refs/trip_record_user_guide.pdf) | [Live](https://www.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf) |
| **TLC Trip Record Data - Yellow Trips Data Dictionary** | [Static](./docs/yellowTaxiDataDictionary.md) | [Live](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf) |

[Back To Top](https://github.com/rscottlundgren/tiny-yellow-cabs)

## Extra Data To Potentially Include

**Website**
- All files will be stored in the PARQUET format.
- Trip data will be published monthly (with two months delay) instead of bi-annually
- Yellow trip data will now include 1 additional column (`airport_fee`, please see Yellow Trips Dictionary for details); The additioinal column will be added to the old files as well; The earliest date to inclue the additional column: January 2011
- TPEP and LPEP trip data PARQUETs from Janauary through June 2015 have been updated to include a new field - `improvement_surcharge` - which lists the itemized portion of the fare covering the Taxicab Improvement Surcharge or Street Hail Livery Improvement Surcharge; This is a $0.30 surcharge on all trips to help fund accessibility in taxis and SHLs, which began on January 1, 2015; All TPEP and LPEP trip data files uploaded moving forward will also include this new field

**User Guide**
- Created in 1971, the New York City Taxi and Limousine Commission (TLC) is the agency responsible for licensing and regulating New York City's medallion (yellow) taxis, street hail livery (green) taxis, for-hire vehicles (FHVs), commuter vans, and paratransit vehicles
- The TLC collects trip record information for each taxi and for-hire vehicle trip completed by their licensed drivers and vehicles
- They receive taxi trip data from the technology service providers (TSPs) that provide electronic metering in each cab, and FHV trip data from the app, community livery, black car, or luxury limousine company, or base, who dispatched the trip
- In each trip record dataset, one row represents a single trip made by a TLC-licensed vehicle

**User Guide - Taxi Data - Yellow**
- Trips made by the New York City's iconic yellow taxis have been recorded and provided to the TLC since 2009
- Yellow taxis are traditionally hailed by signaling to a driver who is on duty and seeking a passenger (street hail), but now they may also be hailed using an e-hail app like Curb or Arro
- Yellow Taxis are the only vehicles permitted to respond to a street hail from a passenger in all five boroughs
- Records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts
- The records were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology service providers
- The trip data was no created by the TLC, and TLC cannot guarantee their accuracy

**User Guide - PULocationID & DOLocationID**
- Each of the trip records contains a field corresponding to the location of the pickup or dropoff of the trip (or in FHV records before 2017, just the pickup), populated by numbers 1 - 263
- These numbers correspond to taxi zones, which may be downloaded as a table or map / shapefile and matched to the trip records using a join
- Note that the Taxi Zones are roughly based on NYC Department of City Planning's Neighborhood Tabulation Areas (NTAs) and are meant to approximate neighborhoods, so you can see which neighborhood a passenger was picked up in, and which neighborhood they were dropped off in

**NYC Open Data**
- NYC Open Data is a citywide platform where all agencies share data for free, with everyone, to increase transparency and foster civic innovation
- The TLC publishes numerous datasets through the NYC Open Data portal, with about 60 currently available online
- The portal allows users to customize the data they'd like to download before they download it and to download it in the format that works best for them
- Each dataset on open data has linked metadata available including when the dataset was last updated, what it contains, and (often) a link to a data dictionary
- The portal: https://opendata.cityofnewyork.us/
- The API: https://dev.socrata.com/foundry/data.cityofnewyork.us/pqfs-mqru
