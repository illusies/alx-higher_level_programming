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
		
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
