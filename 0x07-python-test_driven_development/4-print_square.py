#!/usr/bin/python3
def print_square(size):
    """
        Args:
            size - size of square

        Return: the size of square with the # character

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
            TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError ("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if not isinstance(size,float) and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print("#" * size)
