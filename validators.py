from datetime import date
from datetime import datetime
from calendar import month_name
from calendar import month_abbr
import user_messages as msg

def does_user_want_to_quit(user_input):
    """Determines if the User has decided they wish to quit the program

    Args:
        user_input (str): str representation of the User's input in the terminal

    Returns:
        bool: value indicating if the user entered a 'q' / 'Q' to quit the program
    """
    return user_input == 'q' or user_input == 'Q'

def reformat_user_month_input(user_month_input):
    """Reformats the User's input to potentially match against one of two enums

    Args:
        user_month_input (str): str representation of the User's input in the terminal

    Returns:
        str: reformatted str to potentially match against one of two enums
    """

    reformatted_input = user_month_input.lower().capitalize()
    return reformatted_input

def collect_desired_year(user_input):
    """Collects the validated desired year from the User

    Args:
        user_input (str): str value representing the User's input into the terminal

    Returns:
        int: int value representing the User's validated year
    """

    # State
    user_entered_valid_year = False
    validated_input = 0

    # Behavior
    # While the User has not entered a valid year...
    while user_entered_valid_year is False:

        # If the User wants to quit, break out of the while loop
        if does_user_want_to_quit(user_input):
            validated_input = -1
            break

        # If the User's input is numeric and the length is 4...
        if user_input.isnumeric() and len(user_input) == 4:

            # If the User's input is not between 2008 and the current year (inclusive), print an error message to the terminal and request another input
            if int(user_input) <= 2008 or int(user_input) > date.today().year:
                print(msg.ERROR_INPUT_YEAR_NOT_IN_RANGE)
                user_input = input(msg.PROMPT_USER_TO_INPUT_YEAR_OR_QUIT)

            # Otherwise, the User's input is within the accepted range, change the trigger to indicate that the User has entered a valid year and assign that validated value to the returned variable
            else:
                user_entered_valid_year = True
                validated_input = user_input
        
        # Or, if the User's input is numeric and the length does not equal 4, print an error message to the terminal and request another input
        elif user_input.isnumeric() and len(user_input) != 4:
            print(msg.ERROR_INVALID_INPUT_YEAR_LENGTH)
            user_input = input(msg.PROMPT_USER_TO_INPUT_YEAR_OR_QUIT)
        
        # Otherwise, print an error message to the terminal and request another input
        else:
            print(msg.ERROR_INPUT_YEAR_NOT_NUMERIC)
            user_input = input(msg.PROMPT_USER_TO_INPUT_YEAR_OR_QUIT)

    # Return the validated (or "validated", if the User quit) value
    return int(validated_input)

def collect_desired_month(user_input, validated_year):
    """Collect the validated desired month from the User

    Args:
        user_input (str): str value representing the User's input into the terminal
        validated_year (int): int value representing the User's validated desired year

    Returns:
        int: int value representing the User's validated month
    """

    # State
    user_entered_valid_month = False
    validated_input = ''

    # Behavior
    # While the User has not entered a valid month...
    while user_entered_valid_month is False:

        # If the User wants to quit, break out of the while loop
        if does_user_want_to_quit(user_input):
            break

        # Reformat the User input to help facilitate accurate matching against one of two enums
        reformatted_user_input = reformat_user_month_input(user_input)

        # If the reformatted user input is in the `month_name` enum...
        if reformatted_user_input in month_name:

            # Convert reformatted user input into corresponding integer value representing the month
            potential_month = datetime.strptime(reformatted_user_input, '%B').month

            # Convert the year and the month into a date object (first of that month and year) for testing to see if the provided month and year combination were a valid pairing based on today's date
            potential_date = date(validated_year, potential_month, 1)

            # Calculate the difference in days between today's date and the `potential_date` object previously created
            difference_in_days = (date.today() - potential_date).days

            # If The Difference Is Greater Than Or Equal To 91...
            if difference_in_days >= 91:

                # Change the trigger to represent that a valid month has been found and assign that month's value to the returned variable
                user_entered_valid_month = True
                validated_input = potential_month

            # Otherwise...
            else:

                # Print an error message to the terminal and request another input
                print(msg.ERROR_RECORD_NOT_AVAILABLE)
                user_input = input(msg.PROMPT_USER_TO_INPUT_MONTH_OR_QUIT)

        # Otherwise, if the reformatted user input is in the `month_abbr` enum...
        elif reformatted_user_input in month_abbr:

            # Convert reformatted user input into corresponding integer value representing the month
            potential_month = datetime.strptime(reformatted_user_input, '%b').month

            # Convert the year and the month into a date object (first of that month and year) for testing to see if the provided month and year combination were a valid pairing based on today's date
            potential_date = date(int(validated_year), potential_month, 1)

            # Calculate the difference in days between today's date and the `potential_date` object previously created
            difference_in_days = (date.today() - potential_date).days

            # If The Difference Is Greater Than Or Equal To 91...
            if difference_in_days >= 91:

                # Change the trigger to represent that a valid month has been found and assign that month's value to the returned variable
                user_entered_valid_month = True
                validated_input = potential_month

            # Otherwise...
            else:
                # Print an error message to the terminal and request another input
                print(msg.ERROR_RECORD_NOT_AVAILABLE)
                user_input = input(msg.PROMPT_USER_TO_INPUT_MONTH_OR_QUIT)

        # Otherwise...
        else:

            # Print an error message to the terminal and request another input
            print(msg.ERROR_INVALID_MONTH)
            user_input = input(msg.PROMPT_USER_TO_INPUT_MONTH_OR_QUIT)

    # Return the validated (or "validated", if the User quit) value
    return validated_input

def collect_desired_percentile(user_input):
    """Collect the validated desired percentile from the User

    Args:
        user_input (str): str value representing the User's input into the terminal

    Returns:
        float: float value representing the User's validated desired percentile
    """

    # State
    user_entered_valid_percentile = False
    validated_input = -0.1

    # Behavior
    # While the User has not entered a valid percentile...
    while user_entered_valid_percentile is False:

        # If the User wants to quit, break out of the while loop
        if does_user_want_to_quit(user_input):
            break

        # Try to convert the User's input into a float - if the conversion is not possible, print an error message to the terminal and request another input
        try:
            converted_user_input = float(user_input)
            # If the converted input is less than 0 or greater than 1...
            if converted_user_input < 0.0 or converted_user_input > 1.0:

                # Print an error message to the terminal and request another input
                print(msg.ERROR_INPUT_PERCENTILE_NOT_IN_RANGE)
                user_input = input(msg.PROMPT_USER_TO_INPUT_PERCENTILE_OR_QUIT)
        
            # Otherwise...
            else:

                # Change the trigger to represent that a valid percentile has been found and assign that percentile's value to the returned variable
                validated_input = converted_user_input
                user_entered_valid_percentile = True

        except ValueError:
            print(msg.ERROR_INPUT_PERCENTILE_NOT_NUMERIC)
            user_input = input(msg.PROMPT_USER_TO_INPUT_PERCENTILE_OR_QUIT)

    # Return the validated (or "validated", if the User quit) value
    return validated_input