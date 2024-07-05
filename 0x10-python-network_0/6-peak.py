def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using a modified binary search.

    A peak is defined as an element that is greater than or equal to its neighbors.

    Args:
    - list_of_integers (list): The list of integers in which to find a peak.

    Returns:
    - int or None: The peak element found in the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    # Call the recursive helper function to find the peak
    return _find_peak(list_of_integers, 0, len(list_of_integers) - 1)


def _find_peak(list_of_integers, left, right):
    """
    Recursive helper function to find a peak using binary search.

    Args:
    - list_of_integers (list): The list of integers in which to find a peak.
    - left (int): The left index of the current search range.
    - right (int): The right index of the current search range.

    Returns:
    - int: The peak element found in the list within the specified range.
    """
    # Calculate the middle index
    mid = (left + right) // 2

    # Check if mid is a peak
    if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (
        mid == len(list_of_integers) - 1
        or list_of_integers[mid + 1] <= list_of_integers[mid]
    ):
        return list_of_integers[mid]

    # If the element to the left of mid is greater, peak is likely on the left side
    if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return _find_peak(list_of_integers, left, mid - 1)
    else:
        # Otherwise, peak is likely on the right side
        return _find_peak(list_of_integers, mid + 1, right)
