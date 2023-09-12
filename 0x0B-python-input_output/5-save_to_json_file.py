#!/usr/bin/python3

"""
    function that writes an Object to a text file, 
    using a JSON representation: 
"""
import json

def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using json representation """
    j_str = json.dumps(my_obj, indent = 4)

    with open (filename, "w") as file:
        file.write(j_str)
