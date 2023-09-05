#!/usr/bin/python3
def say_my_name(first_name, last_name=""):

    """
        Args:
            first_name: must be of type string
            last_name: must be of type stirng

        Returns: First name and last name

        Raises:
            TypeError: if first_name is not a string
            TypeError: if Last_name is not a string
    """

    """check if first and last name are string"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name,last_name))
