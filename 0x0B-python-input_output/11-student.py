#!/usr/bin/python3
"""This module defines a class Student"""

class Student:
    """ Represent a student. """

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Gets a dictionary representation of the Student.
        If attribute is a list of strings, represents only those attributes
        included in the list
        """
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for key, value in json.items():
            setattr(self, key, value)

