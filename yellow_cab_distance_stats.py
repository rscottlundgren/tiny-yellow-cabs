"""The Yellow Cab Distance Stats Class"""

import os
from datetime import datetime
import pandas as pd
import ansi_colors as colors
import user_messages as msg

class YellowCabDistanceStats:
    """
    A class used to represent a month's worth of NYC Yellow Cab trips

    ...

    Attributes
    ----------
    year : int
        The year the NYC Yellow Cab trip data came from
    month : int
        The month the NYC Yellow Cab trip data came from
    percentile : float
        The percentile used to parse the NYC Yellow Cab trip data
    current_directory : str
        The str value representing the current directory of the program
    raw_dataframe : dataframe
        The dataframe of the raw NYC Yellow Cab trip data
    below_percentile_dataframe : dataframe
        The dataframe of NYC Yellow cab trip data whose distance is less than the percentile
    total_raw_trips : int
        The total number of raw trips in the raw NYC Yellow Cab dataframe
    total_below_percentile_trips : int
        The total number of trips whose distance is less than the percentile
    saved_file_path : str
        The str value representing the saved file path of the .parquet file
    full_saved_file_name : str
        The str value representing the full saved file name of the .parquet file
    
    Methods
    -------
    get_year()
        Returns the class' `year` attribute
    get_month()
        Returns the class' `month` attribute
    get_percentile()
        Returns the class' `percentile` attribute
    get_current_directory()
        Returns the class' `current_directory` attribute
    get_raw_dataframe()
        Returns the class' `raw_dataframe` attribute
    get_below_percentile_dataframe()
        Returns the class' `below` attribute
    get_total_raw_trips()
        Returns the class' `total_raw_trips` attribute
    get_total_below_percentile_trips()
        Returns the class' `total_below_percentile_trips` attribute
    get_saved_file_path()
        Returns the class' `saved_file_path` attribute
    get_saved_full_file_name()
        Returns the class' `saved_full_file_name` attribute
    set_raw_dataframe(year, month)
        Sets the class' `raw_dataframe` attribute value
    set_below_percentile_dataframe(percentile)
        Sets the class' `below_percentile_dataframe` attribute value
    set_total_raw_trips()
        Sets the class' `total_raw_trips` attribute value
    set_total_below_percentile_trips()
        Sets the class' `total_below_percentile_trips` attribute value
    display_file_name_and_location()
        Prints str summarizing file name and save location
    display_file_summary()
        Prints str summarizing collected data for User
    """

    def __init__(self, year, month, percentile, current_directory):
        """Constructs the instance of the YellowCabDistanceStats class

        Args:
            year (int): The year the NYC Yellow Cab trip data came from
            month (int): The month the NYC Yellow Cab trip data came from
            percentile (float): The percentile used to parse the NYC Yellow Cab trip data
        """
        self.year = year
        self.month = month
        self.percentile = percentile
        self.current_directory = current_directory
        self.raw_dataframe = self.set_raw_dataframe(self.get_year(), self.get_month())
        self.below_percentile_dataframe = self.set_below_percentile_dataframe(self.get_percentile())
        self.total_raw_trips = self.set_total_raw_trips()
        self.total_below_percentile_trips = self.set_total_below_percentile_trips()
        self.saved_file_path = self.get_current_directory() + os.sep + 'TYC_Results'
        self.saved_full_file_name = ''

    # Getters

    def get_year(self):
        """Returns the class' `year` attribute

        Returns:
            int: The year the NYC Yellow Cab trip data came from
        """
        return self.year

    def get_month(self):
        """Returns the class' `month` attribute

        Returns:
            int: The month the NYC Yellow Cab trip data came from
        """
        return self.month

    def get_percentile(self):
        """Returns the class' `percentile` attribute

        Returns:
            float: The percentile used to parse the NYC Yellow Cab trip data
        """
        return self.percentile

    def get_current_directory(self):
        """Returns the class' `current_directory` attribute

        Returns:
            str: The str value representing the current directory of the program
        """
        return self.current_directory

    def get_raw_dataframe(self):
        """Returns the class' `raw_dataframe` attribute

        Returns:
            dataframe: The dataframe of the raw NYC Yellow Cab trip data
        """
        return self.raw_dataframe

    def get_below_percentile_dataframe(self):
        """Returns the class' `below_percentile_dataframe` attribute

        Returns:
            dataframe: The total number of trips whose distance is less than the percentile
        """
        return self.below_percentile_dataframe

    def get_total_raw_trips(self):
        """Returns the class' `total_raw_trips` attribute

        Returns:
            int: The total number of raw trips in the raw NYC Yellow Cab dataframe
        """
        return self.total_raw_trips

    def get_total_below_percentile_trips(self):
        """Returns the class' `total_below_percentile_trips` attribute

        Returns:
            int: The total number of trips whose distance is less than the percentile
        """
        return self.total_below_percentile_trips
    
    def get_saved_file_path(self):
        """Returns the class' `saved_file_plath` attribute

        Returns:
            str: The str value representing the saved file path of the .parquet file
        """
        return self.saved_file_path
    
    def get_saved_full_file_name(self):
        """Returns the class' `saved_full_file_name` attribute

        Returns:
            str: The str value representing the full file name of the .parquet file
        """
        return self.saved_full_file_name

    # Setters

    def set_raw_dataframe(self, year, month):
        """Sets the class' `raw_dataframe` attribute value

        Args:
            year (int): The year the NYC Yellow Cab trip data came from
            month (int): The month the NYC Yellow Cab trip data came from

        Returns:
            dataframe: The dataframe of the raw NYC Yellow Cab trip data
        """

        # Read the dataframe into a variable
        print(msg.STATUS_READING_RAW_PARQUET_FILE_DATA_IN_PROGRESS)
        downloaded_parquet_file = pd.read_parquet(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet')
        print(msg.STATUS_READING_RAW_PARQUET_FILE_DATA_COMPLETED)

        # Return the dataframe
        return downloaded_parquet_file


    def set_below_percentile_dataframe(self, percentile):
        """Sets the class' `below_percentile_dataframe` attribute value

        Args:
            percentile (float): The percentile used to parse the NYC Yellow Cab trip data

        Returns:
            dataframe: The total number of trips whose distance is less than the percentile
        """

        # Retrieve the unparsed dataframe
        print(msg.STATUS_RETRIEVING_UNPARSED_DATA_IN_PROGRESS)
        unparsed_data = self.get_raw_dataframe()
        print(msg.STATUS_RETRIEVING_UNPARSED_DATA_COMPLETED)

        # Sort the unparsed dataframe by the 'trip_distance' column
        print(msg.STATUS_SORTING_DATAFRAME_BY_DISTANCE_IN_PROGRESS)
        sorted_data = unparsed_data.sort_values(by='trip_distance')
        print(msg.STATUS_SORTING_DATAFRAME_BY_DISTANCE_COMPLETE)

        # Reindex the sorted data in the dataframe
        print(msg.STATUS_REINDEXING_SORTED_DATAFRAME_IN_PROGRESS)
        reindexed_data = sorted_data.reset_index(drop=True)
        print(msg.STATUS_REINDEXING_SORTED_DATAFRAME_COMPLETE)

        # Calculate the slice location in dataframe
        print(msg.STATUS_CALCULATING_SLICE_LOCATION_IN_DATAFRAME_IN_PROGRESS)
        index_number = int(percentile * reindexed_data.shape[0])
        print(msg.STATUS_CALCULATING_SLICE_LOCATION_IN_DATAFRAME_COMPLETE)

        # Slice the dataframe from 0 to the 'index_number' / slice location
        print(msg.STATUS_SLICING_DATAFRAME_IN_PROGRESS)
        sorted_reindexed_data = reindexed_data.iloc[:index_number]
        print(msg.STATUS_SLICING_DATAFRAME_COMPLETED)

        # Return the sorted and reindexed dataframe
        return sorted_reindexed_data

    def set_total_raw_trips(self):
        """Sets the class' `total_raw_trips` attribute value

        Returns:
            int: The total number of raw trips in the raw NYC Yellow Cab dataframe
        """
        return self.get_raw_dataframe().shape[0]

    def set_total_below_percentile_trips(self):
        """Sets the class' `total_below_percentile_trips` attribute value

        Returns:
            int: The total number of trips whose distance is less than the percentile
        """
        return self.get_below_percentile_dataframe().shape[0]
    
    def set_saved_full_file_name(self, full_file_name):
        """Sets the class' `saved_full_file_name` attribute value

        Args:
            saved_full_file_name (str): The str value representing the full file name of the .parquet file
        """
        self.saved_full_file_name = full_file_name

    # Helper Method

    def save_total_below_percentile_dataframe_to_local_machine(self):
        """Saves the parsed parquet file to the User's local machine
        """

        # Create a directory following the standard file path:
        # EX: current/directory/of/cloned/repo/TYC_Results
        print(msg.STATUS_VALIDATING_CREATING_TYC_RESULTS_DIRECTORY_IN_PROGRESS)
        os.makedirs(self.get_saved_file_path(), exist_ok=True)
        print(msg.STATUS_VALIDATING_CREATING_TYC_RESULTS_DIRECTORY_COMPLETE)

        # Create a str representation of the timestamp when the file was created
        # EX: 2023-07-06_175359_
        print(msg.STATUS_CREATING_CUSTOM_FILE_NAME_IN_PROGRESS)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S_')

        # Create a dynamic file name accommodating class attributes year, 
        # month, and percentile
        # EX: yellow_tripdata_2023-04_sorted_by_distance_90_percentile.parquet
        file_name = f'yellow_tripdata_{self.get_year()}-{self.get_month():02d}_sorted_by_distance_{int(self.get_percentile() * 100)}_percentile.parquet'

        # Assemble the full standardized file name, save it to the class attributes
        full_file_name = timestamp + file_name
        self.set_saved_full_file_name(full_file_name)
        print(msg.STATUS_CREATING_CUSTOM_FILE_NAME_COMPLETE)

        # Assemble the full standardized file path
        file_path = self.get_saved_file_path() + os.sep + full_file_name

        # Create a parquet file using the assembled file path
        print(msg.STATUS_DOWNLOADING_EXTRACTED_PARQUET_FILE_IN_PROGRESS)
        self.get_below_percentile_dataframe().to_parquet(file_path, engine='auto')
        print(msg.STATUS_DOWNLOADING_EXTRACTED_PARQUET_FILE_COMPLETE)

    def display_file_name_and_location(self):
        """Prints str summarizing file name and save location
        """
        print('Your file has been saved at...' + colors.YELLOW_BOLD_BRIGHT + f'\n\t{self.get_saved_file_path()}' + colors.RESET + '\nwith the following file name:' + colors.YELLOW_BOLD_BRIGHT + f'\n\t{self.get_saved_full_file_name()}\n' + colors.RESET)

    def display_file_summary(self):
        """Prints str summarizing collected data for User
        """
        print(colors.WHITE_BOLD_BRIGHT + '\nQuick Summary' + colors.RESET + f'\nOf the {self.get_total_raw_trips()} total trips taken by Yellow Cab in {self.get_month():02d}/{self.get_year()},...\n\t...{self.get_total_below_percentile_trips()} of those trips were below the {self.get_percentile()} percentile for distance traveled.\n')
