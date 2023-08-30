#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, num):
        if not isinstance(num, int):
            raise TypeError("size must be an integer")
        elif num < 0:
            raise ValueError("size must be >= 0")
        self.__size = num

    @property
    def position(self):
        """Get and set the current position of square."""
        return (self.__position)

    @position.setter
    def position(self, num):
        if (not isinstance(num, tuple) or
                len(num) != 2 or
                not all(isinstance(num, int) for num in num) or
                not all(num >= 0 for num in num)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = num

    def area(self):

        """Return the current area of square."""
        return (self.__size * self.__size)

    def my_print(self):

        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):

        """Define the print representation of Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
