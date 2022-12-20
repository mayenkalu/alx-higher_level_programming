#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a counter for the number of elements printed
    count = 0
    try:
        # Print the first x elements of my_list
        for i in my_list:
            if count < x:
                print("{}".format(my_list[count]), end='')
                count += 1

        print()
    except IndexError:
        # If x is larger than the length of my_list, catch the IndexError
        # and do nothing
        pass
    finally:
        # Return the number of elements printed
        return count
