#!/usr/bin/python3
"""Checks the peak in a list of numbers"""


def find_peak(list_of_integers):
    """Function that checks the peak of integers in a list"""
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            # Peak is likely on the left side
            high = mid - 1
        else:
            # Peak is likely on the right side
            low = mid + 1
    
    return None

