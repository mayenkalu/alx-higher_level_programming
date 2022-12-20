#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        # Perform the division and store the result in a variable
        result = a / b
    except ZeroDivisionError:
        # If b is zero, catch the ZeroDivisionError and return None
        return None
    finally:
        # Print the result using "{}".format()
        print("Inside result: {}".format(result))
    # Return the result
    return result
