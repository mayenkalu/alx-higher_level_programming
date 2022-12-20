#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    #Initialize  a counter for the number of elements to print
    count = 0
    try:
        #Print the first x elements of my_list
        for i in range(x):
            print(my_list[i], end=' ')
            count += 1
    except IndexError:
        #If x is larger than the length of my_list, catch the IndexError
        #and do nothing
        pass
    #Print a newline after the elements have been printed
    print()
    #Return the number of elements printed
    return count
