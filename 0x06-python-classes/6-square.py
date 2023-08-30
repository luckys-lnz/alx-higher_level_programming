#!/usr/bin/python3
"""Square class definintion """


class Square:
    """ Square class defined
        Attributes:
            size (int): Size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes
        Args:
            size (int): size
            postion(tuple): postion
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """
        set area
        Return:
            area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter of size
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, num):
        """
        Setter of size
        Args:
            num (int): size
        Raises
            TypeError: if size is not int
            numError: size less than 0
        Returns:
            None
        """
        if type(num) is not int:
            raise TypeError("size must be an integer")
        elif num < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = num

    def my_print(self):
        """
        print a square
        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

    @property
    def position(self):
        """
        get postion attribute
        """
        return self.__position

    @position.setter
    def position(self, num):
        """
            setter of position
        Args:
            num (tuple): position of the square in 2D space
        Returns:
            None
        """
        if len(num) != 2 or type(num) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(num[0]) != int or num[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(num[1]) != int or num[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = num
