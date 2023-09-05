#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
        Args:
            matrix: a list of integers or floats
            div: int or float for dividing the list matrix

        Return: A new matrix

        Raises:
            TypeError: matrix must be a matrix (list of lists) of integers/floats
            TypeError: div must be a number(int/float)
            ZeroDivisionError: trying to divide by zero
    """

    """check if the matrix is a list of list of int / float"""

    if not all(isinstance(row, list) and all(isinstance(count, (int,float))for count in row)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """ Checks if each row of the matrix has the same size. """
    size = len(matrix[0])
    if any(len(row) != size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    """ Checks if div is a number (integer or float) """
    if(not isinstance(div,(int, float))):
        raise TypeError("div must be a number")
    
    """ Checks if div is not equal to zero. """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    """ Divides all elements of the matrix by div and rounds the result to two decimal places. """
    new_list = [[round(count / div, 2) for count in row] for row in matrix]
    
    """ returns a new matrix """
    return new_list
