#!/usr/bin/python3

""" Reads the content of a file """

def read_file(filename=""):
    """prints the content of UTF-8 text file"""
    with open(filename, encoding="utf-8") as e:
        print(e.read(), end="")
