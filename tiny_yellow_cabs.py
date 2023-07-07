"""Tiny Yellow Cabs"""
import os
import validators as validator
import user_messages as msg
from yellow_cab_distance_stats import YellowCabDistanceStats as ycds

def run_program():
    """Runs the program to collect and save a parquet file from a percentile subset of the User's target data the NYC Yellow Cab records
    """

    # State
    current_directory = os.getcwd()
    valid_month = ''
    valid_year = -1
    valid_percentile = -0.1

    # Behavior
    # Prompt the User for a year
    user_input = input(msg.PROMPT_USER_TO_INPUT_YEAR_OR_QUIT)

    # If the User does not want to quit...
    if validator.does_user_want_to_quit(user_input) is False:

        # Collect and save the User's validated desired year
        valid_year = validator.collect_desired_year(user_input)

    # If the valid year does not equal -1 (a sentinel value)...
    if valid_year != -1:

        # Prompt the User for a month
        user_input = input(msg.PROMPT_USER_TO_INPUT_MONTH_OR_QUIT)

        # Collect and save the User's validated desired month
        valid_month = validator.collect_desired_month(user_input, valid_year)

    # If the valid month does not equal an empty str (a sentinel value)...
    if valid_month != '':

        # Prompt the User for a percentile
        user_input = input(msg.PROMPT_USER_TO_INPUT_PERCENTILE_OR_QUIT)

        # Collect and save the User's validated desired percentile
        valid_percentile = validator.collect_desired_percentile(user_input)

    # If the valid percentile does not equal -0.1 (a sentinel value)...
    if valid_percentile != -0.1:

        # Notify the User that the program is beginning to process the request for data
        print(msg.NOTIFICATION_PROCESSING_REQUEST)

        # Instantiate a new instance of the YellowCabDistanceStats class
        requested_data = ycds(valid_year, valid_month, valid_percentile, current_directory)

        # Save a copy of the data, lower than the percentile, from the dataframe to the User's local machine as a parquet file
        requested_data.save_total_below_percentile_dataframe_to_local_machine()

        # Display a brief summary of the tabulated requested data to the terminal for the User
        requested_data.display_file_summary()

        # Display the location and file name of the saved parquet file for the User's reference
        requested_data.display_file_name_and_location()

run_program()
