#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # Initialize a counter for the number of integers printed
    count = 0
    try:
        # Print the first x elements of my_list that are integers
        for i in range(x):
            # Use "{:d}".format() to print the integer value
            print("{:d}".format(my_list[i]), end=' ')
            count += 1
    except (ValueError, IndexError):
        # If an element is not an integer or if x is larger than the length of my_list,
        # catch the ValueError or IndexError and do nothing
        pass
    # Print a newline after the integers have been printed
    print()
    # Return the number of integers printed
    return count
