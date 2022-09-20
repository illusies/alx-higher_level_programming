#!/usr/bin/python3
""" A class Rectangle that defines a rectangle by: (based on 2-rectangle.py)"""

class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
		PARAMETERS
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
		
        self.width = width
        self.height = height

    @property
    def width(self):
        """Function that gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Function that gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Function that returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Function that prints the rectangle using (#)"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
