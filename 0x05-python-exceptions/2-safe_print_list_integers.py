#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    first_elem = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            first_elem += 1
        except (ValueError, TypeError):
            pass
    print("")
    return (first_elem)
