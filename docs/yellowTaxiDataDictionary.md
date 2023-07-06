# Yellow Taxi Data Dictionary

The Yellow Taxi Data Dictionary is a PDF document describing each of the fields contained in each month's Yellow Taxi Parquet file. Date of original download (used in the creation of this program), static link, link to the live document, and brief description are included below:

| Date Downloaded | Static Link | Live Link | Summary |
| :---: | --- | :---: | --- |
| 2023-07-02 | [Trip Record - Data Dictionary](./refs/data_dictionary_trip_records_yellow.pdf) | [Live](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf) | A PDF document describing the "Yellow Taxi" data gathered by TLC. |

A recreation of the Data Dictionary can be found below for easier viewing:

| Field Name | Data Type | Description | Example / Key |
| --- | --- | --- | --- |
| `VendorID` | int32 | A code indicating the TPEP[^1] provider that provided the record. | `1` = Creative Mobile Technologies, LLC <br/> `2` = VeriFone, Inc. |
| `tpep_pickup_datetime` | datetime64[ns] | The date and time when the meter was engaged. | `2023-04-03 08:28:00` |
| `tpep_dropoff_datetime` | datetime64[ns] | The date and time when the meter was disengaged. | `2023-04-03 08:28:00` |
| `passenger_count` | float64 | The number of passengers in the vehicle. <br/> **_This is a driver-entered value._** | `1.0` |
| `trip_distance` | float64 | The elapsed trip distance in miles reported by the taximeter. | `5.75` |
| `RateCodeID` | float64 | The final rate code in effect at the end of the trip. | `1` = Standard Rate <br/> `2` = JFK <br/> `3` = Newark <br/> `4` = Nassau or Westchester <br/> `5` = Negotiated Fare <br/> `6` = Group Ride |
| `store_and_fwd_flag` | TBD | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor (aka "store and forward") because the vehicle did not have a connection to the server. | `Y` = "Store and Forward" Trip <br/> `N` = Not a "Store and Forward" trip |
| `PULocationID` | int32 | TLC Taxi Zone in which the taximeter was engaged. | TBD |
| `DOLocationID` | int32 | TLC Taxi Zone in which the taximeter was disengaged. | TBD |
| `payment_type` | int64 | A numeric code signifying how the passenger paid for the trip. | `1` = Credit Card <br/> `2` = Cash <br/> `3` = No Charge <br/> `4` = Dispute <br/> `5` = Unknown <br/> `6` = Voided Trip |
| `fare_amount` | float64 | The time-and-distance fare calculated by the meter. | TBD |
| `extra` | float64 | Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1.00 rush hour and overnight charges. | TBD |
| `mta_tax` | float64 | $0.50 MTA tax that is automatically triggered based on the metered rate in use. | TBD |
| `tip_amount` | float64 | This field is automatically populated for credit card tips; cash tips are not included. | `5.56` |
| `tolls_amount` | float64 | Total amount of all tolls paid in trip. | `6.55` |
| `improvement_surcharge` | float64 | $0.30 improvement surcharge assessed trips at the flag drop[^2]. The improvement surcharge began being levied in 2015. | `1.0` |
| `total_amount` | float64 | The total amount charged to passengers; does not include cash tips. | `34.80` |
| `congestion_Surcharge` | float64 | Total amount collected in trip for NYS congestion surcharge. | `2.5` |
| `airport_fee` | float64 | Fee pick up only at LaGuardia and John F. Kennedy Airports. | `1.75` |

[Back to README]()

[^1]: TPEP stands for "Taxicab Passenger Enhancement Programs".

[^2]: Flag drop is a flat fee amount that any passenger will have to pay a taxi cab to get a ride (flag drop referenced the old taximeters which would "drop their flag" when the taxi cab was hired).