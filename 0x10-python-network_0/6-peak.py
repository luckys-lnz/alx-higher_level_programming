#!/usr/bin/bash
"""Check the peak of integers."""


def find_peak(list_of_integers):
    """ A function that returns the peak of integers in a list. """
    if not list_of_integers:
        return None

    return _find_peak(list_of_integers, 0, len(list_of_integers) - 1)

def _find_peak(list_of_integers, left, right):
    mid = (left + right) // 2

    if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
       (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return _find_peak(list_of_integers, left, mid - 1)
    else:
        return _find_peak(list_of_integers, mid + 1, right)

