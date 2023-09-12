#!/usr/bin/python3

""" A function that creates Object from a jSON file"""
import json

def load_from_json_file(filename):
    """ creates object from JSON file"""
    with open(filename) as file:
        return json.load(file)
