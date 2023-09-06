#!/usr/bin/python3
"""A class that defines a rectangle"""
class Rectangle:
    """ num of rectangle instances"""
    number_of_instances = 0
    print_symbol = "#"

    """this represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        Rectangle.number_of_instances +=1

    def area(self):
        """ return area of rectangle """
        return(self.__height * self.__width)
    
    def perimeter(self):
        if self.__height == 0 or self.__width ==0:
            return 0
        return ((self.width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """ show diagram of the rectangle """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        rectangle += str(self.print_symbol) * self.__width

        return rectangle
    
    """
        representation of the rectangle: 
        recreates a new instance using eval()
    """

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    
    """
        Print the message Bye rectangle... (... being 3 dots not ellipsis) 
        when an instance of Rectangle is deleted
    """
    def __del__(self):
        if (Rectangle.number_of_instances > 0):
            Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
    
    def bigger_or_equal(rect_1, rect_2):
        """
            compares two rectangles
            Args:
                rect_1: first rectangle
                rect_2: second rectangle
            return: biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        area_1 = rect_1.__width * rect_1.__height
        area_2 = rect_2.__width * rect_2.__height
        if area_1 == area_2 or area_1 > area_2:
            return rect_1
        return rect_2
