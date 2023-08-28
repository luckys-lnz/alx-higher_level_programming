#!/usr/bin/python3
def safe_print_integer(value):
    """ try: to print value"""
    try:
        print("{:d}".format(value))
        """check value is type int using isinstance"""
        if(isinstance(value, int)):
            return True
    except:
        """return false if not type int"""
        return False
