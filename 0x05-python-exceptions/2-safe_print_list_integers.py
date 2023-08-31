#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """variable to store the x element"""
    first_elem = 0

    """iterate over the x element to collect the fiestElem"""
    for i in range(x):

        """print all integers on the same line,skip other values"""
        try:

            """using try to format integers to be printed from my_list"""
            print("{:d}".format(my_list[i]), end="")

            """incrementing first_elem, to get next Val"""
            first_elem +=1

            """throw an exception if x > my_list"""
        except (ValueError, TypeError):

            """skip other values not integers"""
            pass

        """print new line"""
    print("")

    """return elements x"""
    return (first_elem)
