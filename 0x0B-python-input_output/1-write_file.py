#!/usr/bin/python3

""" function that writes to a file and returns the char written"""

def write_file(filename="", text=""):
    """function to write to a file"""
    with open(filename, "w", encoding="utf-8") as e:
        return e.write(text)
