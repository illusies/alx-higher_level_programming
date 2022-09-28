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
		
        super().integer_validator('size', size)
        self.__size = size

	def area(self):
        """A function that returns the area of the square"""
        return self.__size ** 2

	def __str__(self):
        """A function that prints and returns the following square description: [Square] <width>/<height>
		"""
        return f"[Square] {self.__size}/{self.__size}"
