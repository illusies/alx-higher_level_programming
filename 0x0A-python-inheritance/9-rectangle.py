#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """An instantiation
        PARAMETERS:
			self:
			width: a private positive integer
			height: a private positive integer
        """
		
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """A function that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """A function that prints and returns the following rectangle description: [Rectangle] <width>/<height>
		"""
		
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
