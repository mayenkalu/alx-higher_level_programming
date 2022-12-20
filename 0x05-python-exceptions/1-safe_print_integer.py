#!/usr/bin/python3
def safe_print_integer(value):
    try:
        #Print the integer value using the "{:d}".format()
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        #If value is not an integer, catch the ValueError
        #and return False
        return False

