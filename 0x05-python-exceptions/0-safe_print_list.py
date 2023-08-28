#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    """variable to track num to be printerd"""
    nb_print = 0

    """loop to iterate over arr"""
    for i in range(x):

        try:
            """try: to print the current item"""

            print("{}".format(my_list[i]), end="")
            """increment items"""
            nb_print += 1

        except IndexError:
            """if IndexError occurs: break the loop"""
            break
    print()
    return (nb_print)
