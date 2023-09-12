#!/usr/bin/python3

""" function that appends to a file and returns the num added"""

def append_write(filename="", text=""):
    """ function to append to a file """
    with open(filename, "a", encoding="utf-8") as e:
        return e.write(text)
