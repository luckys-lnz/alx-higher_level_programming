#!/usr/bin/python3

""" A function that returns a list of list of int 
    representing pascals triangle
"""
def pascal_triangle(n):

    """ Returns an empty list if n < or = 0"""
    if n <= 0:
        return []

    """ Initialize the Pascal's triangle with the first row """
    triangle = [[1]]

    for i in range(1, n):
        """ Calculate the next row based on the current row """
        current_row = [1]
        for j in range(1, len(triangle[-1])):
            current_row.append(triangle[-1][j - 1] + triangle[-1][j])
        current_row.append(1)
        
        """ Append the current row to the triangle"""
        triangle.append(current_row)

    return triangle
