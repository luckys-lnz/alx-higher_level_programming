#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    first_elem = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            first_elem += 1
        except(ValueError, TypeError):
            continue
    print()
    return first_elem
