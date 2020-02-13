from Helpers.DataTypeHelpers import *
from datetime import datetime

__all__ = ['inputInt',  'inputFloat',  'inputString', 'inputDate']


def inputInt(prompt="Enter an integer:",
             min_value=0, max_value=100):
    """ 
    Parse string input into int within minimum and maxmium range
    Args:
        prompt = "Enter an integer:" (string)
        min_value = 0 (int)
        max_value = 100 (int)
    Returns:
        int
    """		
    # local variable loop to keep track of True and False
    loop = True
    while loop:
        # local variable user to store user input
        user = input(prompt)
        # import isInt() to determine string can be parse into int
        if isInt(user):
            # check that the input string is within min and max
            if (min_value <= int(user) <= max_value):
                loop = False
                return int(user)
            else:
                # input string not within min and max range
                print(
                    "Value must be between {} and {}"
                    .format(min_value, max_value)
                )
                loop = True
        else:
            # input string cannot be parsed into int
            print("Enter text needs to be in the int format")
            loop = True


def inputFloat(prompt="Enter a float: ",
               min_value=0, max_value=100):
    """ 
    Parse string input into float within minimum and maxmium range
    Args:
        prompt = "Enter a float:" (string)
        min_value = 0 (int)
        max_value = 100 (int)
    Returns:
        float
    """	
    # local variable loop to keep track of True and False
    loop = True
    while loop:
        # local variable user to store user input
        user = input(prompt)
        # import isFloat() to check that the string can be parsed into float
        if isFloat(user):
            # check that the input string is within min and max range
            if (min_value <= float(user) <= max_value):
                loop = False
                return float(user)
            else:
                # input string not withing min and max range
                print(
                    "Value must be between {} and {}"
                    .format(min_value, max_value)
                )
                loop = True
        else:
            # input string cannot be parsed into float
            print("Enter text needs to be in the float format")
            loop = True


def inputString(prompt="Enter a string: ",
                min_length=0, max_length=100):
    """ 
    Output string within minimum and maxmium length
    Args:
        prompt = "Enter a string:" (string)
        min_length = 0 (int)
        max_length = 100 (int)
    Returns:
        user (string)
    """	
    # local variable loop to keep track of True and False
    loop = True
    while loop:
        # local variable user to store user input
        user = input(prompt)
        # check that the input string is within min and max length
        if (min_length <= len(user) <= max_length):
            loop = False
            return user
        else:
            # input string not within min and max length
            loop = True
            print(
                "Text must be between {} and {}"
                .format(min_length, max_length)
            )


def inputDate(prompt="Enter a date in ISO format (yyyy-mm-dd): "):
    """ 
    Parse string input into date
    Args:
        prompt = "Enter a date in ISO format (yyyy-mm-dd): " (string)
    Returns:
        string
    """	
    # local variable loop to keep track of True and False
    loop = True
    while loop:
        # local variable user to store user input
        user = input(prompt)
        # import isDate() to check that the string can be parsed into date
        if isDate(user):
            loop = False
            return datetime.strptime(user, '%Y-%m-%d')
        else:
            print("Value must be a date")
            loop = True
