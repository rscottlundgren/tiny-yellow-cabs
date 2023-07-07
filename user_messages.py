"""A list of str constants for user messaging"""

import ansi_colors as colors

ERROR_INPUT_PERCENTILE_NOT_NUMERIC = colors.RED_BOLD_BRIGHT + 'ERROR - Input Not Numeric\n' + colors.RESET + colors.RED + 'Input must be a float between 0.0 and 1.0 (inclusive).\n' + colors.RESET
ERROR_INPUT_PERCENTILE_NOT_IN_RANGE = colors.RED_BOLD_BRIGHT + 'ERROR - Input Not In Range\n' + colors.RESET + colors.RED + 'Input must be a float between 0.0 and 1.0 (inclusive).\n' + colors.RESET
ERROR_INPUT_YEAR_NOT_IN_RANGE = colors.RED_BOLD_BRIGHT + 'ERROR - Input Not In Range\n' + colors.RESET + colors.RED + 'Input must be between 2009 and the current year.\n' + colors.RESET
ERROR_INPUT_YEAR_NOT_NUMERIC = colors.RED_BOLD_BRIGHT + 'ERROR - Input Not Numeric\n' + colors.RESET + colors.RED + 'Please enter a year between 2009 and this year (inclusive).\n' + colors.RESET
ERROR_INVALID_INPUT_YEAR_LENGTH = colors.RED_BOLD_BRIGHT + 'ERROR - Invalid Input Length\n' + colors.RESET + colors.RED + 'Please enter a four digit year (YYYY) between 2009 and this year (inclusive).\n' + colors.RESET
ERROR_INVALID_MONTH = colors.RED_BOLD_BRIGHT + 'ERROR - Invalid Input\n' + colors.RESET + colors.RED + 'Please enter either the full name (i.e. January) or the first three letters (i.e. Jan) of the month you are looking for.\n' + colors.RESET
ERROR_RECORD_NOT_AVAILABLE = colors.RED_BOLD_BRIGHT + 'ERROR - Record Not Available\n' + colors.RESET + colors.RED + 'Record for selected month unavailable; please enter a month greater than 91 days in the past.\n' + colors.RESET

NOTIFICATION_PROCESSING_REQUEST = colors.GREEN_BOLD_BRIGHT + '\nPlease Hold: Processing Your Request...\n' + colors.RESET
NOTIFICATION_INTRO = '\nThank you for using \'Tiny Yellow Cabs\'.\n\nThis application will allow you to parse NYC "Yellow Taxi" trip data for a particular month and year that you select under a percentile that you provide.\nYou have access to data as far back as January 2009 up to two (2) months ago (i.e. if it is July right now, the latest month you can access is April of the current year).\nOnce you have provided those three pieces of information (a valid year, month, and percentile), a .parquet file will be downloaded onto your local machine and a location on where to find it will be shown in the terminal.\n'
NOTIFICATION_GOODBYE = '\nGoodbye!\n'

PROMPT_USER_TO_INPUT_MONTH_OR_QUIT = 'Please enter the month name / abbreviation or \'q\' to quit: '
PROMPT_USER_TO_INPUT_PERCENTILE_OR_QUIT = 'Please enter the percentile value (between 0.0 & 1.0) or \'q\' to quit: '
PROMPT_USER_TO_INPUT_YEAR_OR_QUIT = 'Please enter a year in YYYY format or \'q\' to quit: '

STATUS_READING_RAW_PARQUET_FILE_DATA_COMPLETED = colors.GREEN + 'Reading complete!' + colors.RESET
STATUS_READING_RAW_PARQUET_FILE_DATA_IN_PROGRESS = 'Reading raw .parquet file data into dataframe...'
STATUS_RETRIEVING_UNPARSED_DATA_COMPLETED = colors.GREEN + 'Retrieval complete!' + colors.RESET
STATUS_RETRIEVING_UNPARSED_DATA_IN_PROGRESS = 'Retrieving raw data dataframe...'
STATUS_SORTING_DATAFRAME_BY_DISTANCE_COMPLETE = colors.GREEN + 'Sorting complete!' + colors.RESET
STATUS_SORTING_DATAFRAME_BY_DISTANCE_IN_PROGRESS = 'Sorting dataframe by `trip_distance`...'
STATUS_REINDEXING_SORTED_DATAFRAME_COMPLETE = colors.GREEN + 'Reindexing complete!' + colors.RESET
STATUS_REINDEXING_SORTED_DATAFRAME_IN_PROGRESS = 'Reindexing sorted dataframe...'
STATUS_CALCULATING_SLICE_LOCATION_IN_DATAFRAME_COMPLETE = colors.GREEN + 'Calculation complete!' + colors.RESET
STATUS_CALCULATING_SLICE_LOCATION_IN_DATAFRAME_IN_PROGRESS = 'Calculating slice location in sorted dataframe...'
STATUS_SLICING_DATAFRAME_IN_PROGRESS = 'Slicing sorted dataframe at percentile marker...'
STATUS_SLICING_DATAFRAME_COMPLETED = colors.GREEN + 'Slicing complete!' + colors.RESET
STATUS_VALIDATING_CREATING_TYC_RESULTS_DIRECTORY_IN_PROGRESS = 'Validating presence of \'TYC_Results\' directory; creating directory if it does not exist...'
STATUS_VALIDATING_CREATING_TYC_RESULTS_DIRECTORY_COMPLETE = colors.GREEN + 'Directory validation / creation complete!' + colors.RESET
STATUS_CREATING_CUSTOM_FILE_NAME_IN_PROGRESS = 'Creating custom file name for extracted data...'
STATUS_CREATING_CUSTOM_FILE_NAME_COMPLETE = colors.GREEN + 'Creation complete!' + colors.RESET
STATUS_DOWNLOADING_EXTRACTED_PARQUET_FILE_IN_PROGRESS = 'Downloading extracted dataframe as a .parquet file to your local machine...'
STATUS_DOWNLOADING_EXTRACTED_PARQUET_FILE_COMPLETE = colors.GREEN + 'Download complete!' + colors.RESET