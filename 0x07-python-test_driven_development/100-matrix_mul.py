#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
        Args:
            m_a - list matrix a
            m_b - list  matrix b

        Return: a new matrix

        Raises:
            TypeError
            ValueError
    """

    """ check if Args are list """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    
    """ check if Args are list of list """
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    
    """checks if Args are empty"""
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty or m_b can't be empty")
    
    """ Check if all elements in m_a and m_b are integers or floats """
    for row in m_a:
        if not all(isinstance(count, (int, float)) for count in row):
            raise TypeError("m_a should contain only integers or floats")
    
    for row in m_b:
        if not all(isinstance(count,(int, float)) for count in row):
            raise TypeError("m_b sgykd contain only integers or floats")
        
    """ Check if m_a and m_b are rectangles (if the rows have the same size) """
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    
    """ Check if m_a and m_b can be multiplied (columns in m_a == rows in m_b) """
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """ multiplication """

    """calc is a storage of the list"""
    calc = []

    """ loops through the rows of m_a"""
    for j in range(len(m_a)):
        row = []

        """loops throgh colum of m_b"""
        for k in range(len(m_b[0])):
            count_sum = []

            """ looop throught in dimension """
            for l in range(len(m_b)):

                """get the products"""
                count_sum =+ m_a[j][l] * m_b[l][k]

                """append accumulated sum"""
            row.append(count_sum)

            """append current row to result"""
        calc.append(row)

        return calc
