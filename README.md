A repo with all the code you used and a readme (in english) explaining your approach, the steps to reproduce your test and everything you feel is important.

# Tiny Yellow Cab Data

## Table of Contents

- [Using The Program]()
- [Approach]()
  - [Prep Work]()
- [Dataset Considerations]()
- [Helpful Resources / Links]()

## Using The Program
### Cloning The Repo
This program was built using Python 3.11. If you do not have Python 3.11 installed, I highly recommend that you do so prior to attempting to run this program. Instructions on downloading Python 3.11 can be found on the [Python language website](https://www.python.org/downloads/).

Once you have a working version of Python 3.11 on your local machine, clone this repo (if you're unsure how to do that, GitHub has some [really great documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) that will walk you through the process). When you have successfully cloned this repo to your local machine, you can move onto the section "Running The Program".

### Running The Program

1. If you haven't already done so, open a Terminal window.
2. `cd` into the filepath where you cloned this repo.
3. Enter the following command into your terminal and hit "Enter".
   ```
   python3 tycd.py
   ```
4. The program will then walk you through three questions in the terminal:

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

## Dataset Considerations

To start, while the TLC yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts, the website makes it very clear:

> **Warning**
> The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP).



- This is where we include some of the excellent information gleaned from the materials, including links to the reference material that was captured at time of design

Yellow and green 

## Links

| Description | Static | Live |
| --- | ------ | ---- |
| **TLC Trip Record Data - Site Screen Capture** | [Static](./docs/refs/www.nyc.gov_site_tlc_about_tlc-trip-record-data.page.png) | [Live](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |
| **TLC Trip Record Data - User Guide** | [Static](./docs/refs/trip_record_user_guide.pdf) | [Live](https://www.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf) |
| **TLC Trip Record Data - Yellow Trips Data Dictionary** | [Static](./docs/yellowTaxiDataDictionary.md) | [Live](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf) |

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
