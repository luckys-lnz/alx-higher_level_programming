def add_integer(a, b=98):
    """
    Args:
        a: first arg
        b: second arg
    
    Return:
        sum of a and b

    Raises:
        TypeError: if args are neither int or float
    """
    if(not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
        """ used  isinstance to check the type of both args """
    elif(not isinstance(b, int)and (not isinstance(b, float))):
            raise TypeError("b must be an integer")
    return int (a) + int (b)
