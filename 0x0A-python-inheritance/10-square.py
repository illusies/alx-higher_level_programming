#!/usr/bin/python3
"""A class Square that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class square using Rectangle"""

    def __init__(self, size):
        """An instantiation
        PARAMETERS:
			self:
			size: a private positive integer
        """
		
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

	def area(self):
        """A function that returns the area of the square"""
		
        return self.__width * self.__height
